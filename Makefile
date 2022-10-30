.PHONY: manage
manage:
	poetry run python src/manage.py ${CMD}

.PHONY: dev
dev:
	@make manage CMD="runserver"

.PHONY: lint
lint:
	poetry run flake8 .
	poetry run black . --check
	poetry run isort . --check-only

.PHONY: fix
fix:
	poetry run black .
	poetry run isort .
