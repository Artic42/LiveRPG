docker exec -it casinoRoyale rm -rf /usr/share/nginx
docker cp web casinoRoyale:/usr/share/nginx
docker exec -it casinoRoyale nginx -s reload