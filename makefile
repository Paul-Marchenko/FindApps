SELENOID_UI_URL=http://localhost:8080

start:
	docker-compose up -d
	bash -c "open -a /Applications/Google\ Chrome.app ${SELENOID_UI_URL}"
stop:
	docker-compose stop
	docker-compose down --rmi local
test:
	pytest -qs tests/
test_lf:
	pytest -q --lf tests/
clear:
	find . -name __pycache__ | xargs rm -rf
	find . -name '*.pyc' | xargs rm -rf
	rm -f video/*
	rm -rf `find . -name __pycache__`