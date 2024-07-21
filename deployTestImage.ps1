docker stop testImageLiveRPG
docker rm testImageLiveRPG
docker rmi test_image_live_rpg
docker build -t test_image_live_rpg .
docker run -d -p 8001:8000 -p 80:80 --name testImageLiveRPG test_image_live_rpg
