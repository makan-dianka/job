#!/bin/bash

set -e

eval "$(ssh-agent -s)"
ssh-add ~/.ssh/gitlab_key

git pull git@gitlab.com:dmakan/job.git master 
docker-compose --env-file .env up -d