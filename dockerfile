FROM nginx:alpine

# Install python3, pip3 and poetry
RUN apk add --no-cache python3
RUN apk add --no-cache py3-pip
RUN apk add --no-cache poetry

# Copy necessary files
COPY pyproject.toml ./
COPY databaseManager ./databaseManager
COPY API.py ./API.py
COPY routers ./routers 
COPY nginx.conf /etc/nginx/nginx.conf
COPY web /usr/share/nginx
COPY scripts/linux/startServer.sh /startServer.sh
COPY database/EmptyDatabase.db ./Database.db
COPY database/EmptyDatabase.db ./ProductionDatabase.db
COPY database/TestDatabase.db ./TestDatabase.db

# Open ports
EXPOSE 80
EXPOSE 8000

# Start command
CMD ["/startServer.sh"]

