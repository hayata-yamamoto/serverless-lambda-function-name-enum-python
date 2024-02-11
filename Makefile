default: | help

SRC_DIR=sls_enum

format: ## format codes
	poetry run autoflake -ri --remove-all-unused-imports --ignore-init-module-imports --remove-unused-variables ${SRC_DIR} && \
	poetry run isort ${SRC_DIR} && \
	poetry run black ${SRC_DIR}

check: ## check codes
	poetry run mypy ${SRC_DIR}

help:  ## Show all of tasks
	@grep -E '^[a-zA-Z0-9\_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "; OFS="\t"}; {sub("Makefile:","")}; {printf "\033[36m%-30s\033[0m%s\n", $$1, $$2}'