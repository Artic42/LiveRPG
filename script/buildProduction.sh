cat web/js/login.js > web/login.js
echo "sessionStorage.setItem('apiServer', 'https://lsbapi.artic42.com');" >> web/login.js

# Stop and remove already running images adn containers
sudo docker stop LSBAPI
sudo docker rm LSBAPI
sudo docker rmi lsb_api

sudo docker stop LSBWEB
sudo docker rm LSBWEB
sudo docker rmi lsb_web

# Build API server
sudo docker build -t lsb_api database

# Build Webserver
sudo docker build -t lsb_web web

# Run servers in doker
sudo docker run -itd -p 7001:80 --name LSBWEB lsb_web
sudo docker run -itd -p 7002:8000 --name LSBAPI lsb_api

rm web/login.js