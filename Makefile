.PHONY: manage
manage:
	poetry run python src/manage.py ${CMD}

.PHONY: dev
dev:
	@make manage CMD="runserver"
