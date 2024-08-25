#!/bin/bash

if [[ $(docker ps | grep pokemon-creator) != "" ]]
then
    docker stop pokemon-creator
    docker rm pokemon-creator
    docker rmi $(docker images | grep pokemon-creator | awk '{print $3}')
else
exit 0
fi