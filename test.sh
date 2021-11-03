
docker-compose -f docker-compose.test.yml up -d --build

docker-compose -f docker-compose.test.yml run web-server pytest

docker-compose -f docker-compose.test.yml down
