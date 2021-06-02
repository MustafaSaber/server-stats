![Main Workflow](https://github.com/MustafaSaber/server-stats/actions/workflows/mainwf.yml/badge.svg)
# Server Stats

A simple project to get server statistics (RAM/CPU/DISK) of CentOS machine over time

## Requirements

* ansible
* pip3
* precommit
* docker (Optional)

Install python packages requirements via `pip3 install -r requiements.txt` you can go an extra mile and make virtual env for your project.

## Deploying To Host

Using this [script](./scripts/deploy_server.sh) will deploy to the specific [hosts](./ansible/hosts), change in hosts file and add your specifc machine. To access the current machine reach out for the repo administrator.

Dockerizing application and push to DockerHub via this [script](./scripts/publish_dockerhub.sh), it will use `.docker-secret` in application root folder. You can run `cp .docker-secret-sample .docker-secret` and change in it's values.
