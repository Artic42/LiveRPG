# Stop and remove already running images adn containers
sudo docker stop LSBAPITEST
sudo docker rm LSBAPITEST
sudo docker rmi lsb_api_test

# Build API server
sudo docker build -t lsb_api_test database

sudo docker run -itd -p 7012:8000 --name LSBAPITEST lsb_api_test