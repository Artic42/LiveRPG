car js/login.js > login.js
echo "sessionStorage.setItem('apiServer', localhost:8000);" >> login.js

# Stop and remove already running images adn containers
docker stop LSBAPI
docker rm LSBAPI
docker rmi lsb_api

docker stop LSBWEB
docker rm LSBWEB
docker rmi lsb_web

# Build API server
docker build -t lsb_api database

# Build Webserver
docker build -t lsb_web web

# Run servers in doker
docker run -itd -p 80:80 --name LSBWEB lsb_web
docker run -itd -p 8000:8000 --name LSBAPI lsb_api
