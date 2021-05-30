FROM centos:7

WORKDIR /opt/task

RUN yum -y update && yum -y install java-11-openjdk-devel python3-devel libselinux-python gcc epel-repo ansible

COPY . .

RUN pip3 install -r requirements.txt
