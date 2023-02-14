# Installation

A very easy process, following [https://dev.to/ndrohith/deploy-a-containerised-fast-api-application-in-digital-ocean-25](this repo)

docker build -t fast-ocean-droplet .
OR
docker build . -t fast-ocean-droplet

The period means to build what's in this folder, the -t is an optional tag to name the built image.

 docker run -d -p 8000:8000 fast-ocean-droplet
 the -d flag is detached, to run in the background.

For some reason adding a firewall in DO GUI to accept connections on 22 and 80 seemed to enable connections on 8000.

This doesn't make any sense to me.

## Docker Compose

On remote, git pull, then docker compose up -d

## Context
docker context create dev --docker "host=ssh://root@167.71.191.239"

docker-compose --context dev up -d
