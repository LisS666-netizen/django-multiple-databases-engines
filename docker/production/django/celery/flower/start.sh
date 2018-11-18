#!/usr/bin/env bash

set -o errexit
set -o nounset

celery flower \
    --app=beyond_campus.taskapp \
    --broker="${CELERY_BROKER_URL}" \
    --basic_auth="${CELERY_FLOWER_USER}:${CELERY_FLOWER_PASSWORD}"
