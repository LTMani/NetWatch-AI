"""NetWatch AI Enterprise Platform - Main CLI Entrypoint."""
import sys
import os
from app import create_app

app = create_app(os.getenv('FLASK_ENV', 'development'))

def main():
    port = int(os.getenv('PORT', 5000))
    print(f"Starting NetWatch AI Enterprise Platform on http://127.0.0.1:{port}")
    app.run(host='0.0.0.0', port=port, debug=True)

if __name__ == '__main__':
    main()
