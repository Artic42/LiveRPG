
# Install python dependencies
poetry add /routers
poetry add /databaseManager
poetry install --no-root

# Keep it running
poetry run python API.py

# Start NGINX
nginx -g 'daemon off;'