#!/usr/bin/bash

set -e

eval "$(ssh-agent -s)"
ssh-add ~/.ssh/gitlab_key

git pull git@gitlab.com:dmakan/job.git
docker stop job && docker rm job
docker image rm job_app:latest
docker-compose --env-file .env up -d