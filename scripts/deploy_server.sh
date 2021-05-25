#!/bin/sh

PRIV_KEY=${1:-private_key.pem}

echo $PRIV_KEY

ansible-playbook ./ansible/playbook.yml -i ./ansible/hosts --private-key=$PRIV_KEY