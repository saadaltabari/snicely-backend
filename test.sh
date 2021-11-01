
docker-compose -f docker-compose.test.yml up -d --build

docker-compose -f docker-compose.test.yml run web-server pytest

#source envs/test.env
#docker-compose -f docker-compose.test.yml run mongodb mongo --username=$MONGO_DB_USER --password=$MONGO_DB_PASSWORD --authenticationDatabase=$MONGO_DB_AUTH_SOURCE test --eval "printjson(db.dropDatabase())"

docker-compose -f docker-compose.test.yml down
