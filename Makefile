buildAndRun:
	docker compose up --build

down:
	docker compose  down --rmi all --volumes --remove-orphans

prune:
	docker system prune --volumes

execBash:
	docker compose exec web bash

tests:
	docker compose run web python manage.py test

migrations:
	docker compose run web python manage.py migrate