docker-compose -f docker-compose.prod.yml down -v
docker-compose -f docker-compose.prod.yml up -d --build
docker-compose -f docker-compose.prod.yml exec -T api python manage.py migrate --noinput
docker-compose -f docker-compose.prod.yml exec -T api python manage.py loaddata common/fixtures/accounts.json
docker-compose -f docker-compose.prod.yml exec -T api python manage.py collectstatic --no-input --clear 
