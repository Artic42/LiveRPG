
# Install python dependencies
poetry install --no-root

# Keep it running
poetry run python /API/API.py

# Start NGINX
ngins -g 'daemon off;'