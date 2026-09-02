# ---------------------------------------------------------
# Load environment variables.
# ---------------------------------------------------------

.DEFAULT_GOAL := build

# Set the Docker compose profile to all if an argument is not provided.
DOCKER_COMPOSE_PROFILE ?= all

# Set the specified environment file if an argument is not provided. 
ENV_FILE ?= .env
include $(ENV_FILE)

# ---------------------------------------------------------
# Init
# ---------------------------------------------------------

.SILENT: init
.PHONY: init

init:
	cat /dev/urandom | tr -dc 'a-zA-Z0-9' | fold -w 16 | head -n 1 > db-password.txt &&\
	echo DB_NAME=\"$(DB_NAME)\" >> backend/mission-clock/settings/dev/.env &&\
	echo DB_USER=\"$(DB_USER)\" >> backend/mission-clock/settings/dev/.env &&\
	echo DB_PASS=\"$(shell cat db-password.txt)\" >> backend/mission-clock/settings/dev/.env &&\
	echo DB_HOST=\"$(DB_HOST)\" >> backend/mission-clock/settings/dev/.env &&\
	echo DB_PORT=\"$(DB_PORT)\" >> backend/mission-clock/settings/dev/.env 

# ---------------------------------------------------------
# Build the container images.
# ---------------------------------------------------------

.SILENT: build
.PHONY: build

build: 
	docker compose --env-file $(ENV_FILE) --profile $(DOCKER_COMPOSE_PROFILE) build

# ---------------------------------------------------------
# Start the containers.
# ---------------------------------------------------------

.SILENT: start
.PHONY: start

start: 
	docker compose --env-file $(ENV_FILE) --profile $(DOCKER_COMPOSE_PROFILE) up -d

# ---------------------------------------------------------
# Stop the containers.
# ---------------------------------------------------------

.SILENT: stop
.PHONY: stop

stop: 
	docker compose --env-file $(ENV_FILE) --profile $(DOCKER_COMPOSE_PROFILE) down
