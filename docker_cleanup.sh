#!/bin/bash

# Stop all running Docker containers
docker stop $(docker ps -q)

# Prune stopped containers
docker container prune -f

# Prune all volumes (including unused)
docker volume prune -f
