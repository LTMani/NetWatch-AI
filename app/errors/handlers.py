from flask import jsonify, render_template, request
from app.errors.exceptions import NetWatchException

def register_error_handlers(app):
    @app.errorhandler(NetWatchException)
    def handle_netwatch_exception(error):
        if request.path.startswith('/api/') or request.is_json:
            response = jsonify(error.to_dict())
            response.status_code = error.status_code
            return response
        return render_template(
            'errors/400.html',
            error_code=error.error_code,
            status_code=error.status_code,
            message=error.message,
            title=f'Error {error.status_code}'
        ), error.status_code

    @app.errorhandler(400)
    def handle_bad_request(e):
        if request.path.startswith('/api/') or request.is_json:
            return jsonify({
                'status': 'error',
                'error_code': 'BAD_REQUEST',
                'message': getattr(e, 'description', 'The request could not be parsed by the server.')
            }), 400
        return render_template('errors/400.html', message=getattr(e, 'description', 'Invalid request')), 400

    @app.errorhandler(401)
    def handle_unauthorized(e):
        if request.path.startswith('/api/') or request.is_json:
            return jsonify({
                'status': 'error',
                'error_code': 'UNAUTHORIZED',
                'message': 'Authentication required to access this resource.'
            }), 401
        return render_template('errors/403.html', message='Please sign in to proceed.'), 401

    @app.errorhandler(403)
    def handle_forbidden(e):
        if request.path.startswith('/api/') or request.is_json:
            return jsonify({
                'status': 'error',
                'error_code': 'FORBIDDEN',
                'message': 'You do not have administrative permission for this resource.'
            }), 403
        return render_template('errors/403.html', message='Access denied by security policy.'), 403

    @app.errorhandler(404)
    def handle_not_found(e):
        if request.path.startswith('/api/') or request.is_json:
            return jsonify({
                'status': 'error',
                'error_code': 'NOT_FOUND',
                'message': 'Requested endpoint or network resource does not exist.'
            }), 404
        return render_template('errors/404.html', message='Resource not found.'), 404

    @app.errorhandler(429)
    def handle_too_many_requests(e):
        if request.path.startswith('/api/') or request.is_json:
            return jsonify({
                'status': 'error',
                'error_code': 'RATE_LIMIT_EXCEEDED',
                'message': 'Too many requests. Please throttle your queries.'
            }), 429
        return render_template('errors/400.html', message='Rate limit exceeded.'), 429

    @app.errorhandler(500)
    def handle_internal_server_error(e):
        app.logger.error(f'Unhandled server error: {e}', exc_info=True)
        if request.path.startswith('/api/') or request.is_json:
            return jsonify({
                'status': 'error',
                'error_code': 'INTERNAL_SERVER_ERROR',
                'message': 'An unexpected server error occurred. Telemetry recorded for review.'
            }), 500
        return render_template('errors/500.html', message='Internal system error occurred.'), 500
