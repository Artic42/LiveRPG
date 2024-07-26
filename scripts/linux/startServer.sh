# Start Nginx
nginx

# Install python dependencies
poetry install --no-root

# Keep it running
poetry run python API.py

# Start NGINX
nginx -g 'daemon off;'