docker stop casinoRoyale
docker rm casinoRoyale
docker rmi casino_royale
docker build -t casino_royale .
docker run -t -p 8000:8000 -p 80:80 --name casinoRoyale casino_royale
