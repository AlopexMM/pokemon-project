#!/bin/bash

pokemonContainer=`docker ps | grep pokemon-creator`

if [[ $pokemonContainer != "" ]] then
    docker stop pokemon-creator
    docker rm pokemon-creator
    docker rmi $(docker images | grep pokemon-creator | awk '{print $3}')
fi