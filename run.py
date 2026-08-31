import os
from app import create_app

app = create_app(os.getenv('FLASK_ENV', 'development'))

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    host = os.getenv('HOST', '127.0.0.1')
    debug = os.getenv('FLASK_DEBUG', '1') == '1'
    print(f'Starting NetWatch AI Platform on http://{host}:{port}')
    app.run(host=host, port=port, debug=debug)
