cat web/js/login.js > web/login.js
echo "sessionStorage.setItem('apiServer', 'http://localhost:8000');" >> web/login.js

# Stop and remove already running images adn containers
sudo docker stop LSBAPI
sudo docker rm LSBAPI

sudo docker stop LSBWEB
sudo docker rm LSBWEB

# Build API server
sudo docker build -t lsb_api database

# Build Webserver
sudo docker build -t lsb_web web

# Run servers in doker
sudo docker run -itd -p 80:80 --name LSBWEB lsb_web
sudo docker run -itd -p 8000:8000 --name LSBAPI lsb_api

rm web/login.js
