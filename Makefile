install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python3 -m pytest -vv --cov=main test_*.py
	py.test --nbval-lax *.ipynb


format:	
	black *.py 

lint:
	pylint --disable=R,C,locally-disabled --ignore-patterns=test_.*?py *.py
	ruff check *.py	
# container-lint:
# 	docker run --rm -i hadolint/hadolint < Dockerfile

# refactor: format lint

# deploy:
# 	#deploy goes here
		
all: install lint test format deploy
