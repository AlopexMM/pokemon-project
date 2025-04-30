#!/bin/bash

if [[ $(docker ps | grep pokemon-creator) != "" ]]
then
    docker stop pokemon-creator
    docker rm pokemon-creator
    docker rmi $(docker images | grep pokemon-creator | awk '{print $3}')
    echo "Deleted container and image"
else
echo "Nothing to delete"
exit 0
fi