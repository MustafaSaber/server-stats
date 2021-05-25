#!/bin/bash
# If you don't have .docker-secret with right creds this script won't work

if [ -z "$1" ]
  then
    echo "No argument supplied, You must supply the tag value, (ex: mustafasaber/image:1.0) ."
    exit 1
fi

docker logout

set -e

current_path=$(pwd)
echo "Repo path is ${current_path}"
source "${current_path}"/.docker-secret

echo "$DOCKER_HUB_PASSWORD" | docker login -u "$DOCKER_USERNAME" --password-stdin
TAG=$1

docker build -t "${TAG}" .
docker push "${TAG}"

set +e