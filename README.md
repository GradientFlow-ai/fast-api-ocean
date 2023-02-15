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

But docker-compose up -d will rebuild and restart.

## Context
I want to be able to restart the remote server easily and quickly.

The below does not work with docker-compose due to SSH issues, so currently I will just use Terraform and recreate every time

docker context update dev --docker "host=ssh://root@165.227.185.65"
or create
docker context update dev --docker "host=ssh://root@167.71.191.239:/root/fast_api_ocean"

docker-compose --context dev up -d

docker-compose -H "ssh://root@167.71.191.239" up -d

I had to SSH into the DO droplet and run:
ufw delete limit 22/tcp
ufw reload

[see](https://stackoverflow.com/questions/66734233/docker-compose-with-remote-context-gives-ssh-error-connection-refused)


## Terraform
terraform plan \
  -var "do_token=${DO_PAT}" \
  -var "pvt_key=$HOME/.ssh/id_rsa"


terraform apply \
  -var "do_token=${DO_PAT}" \
  -var "pvt_key=$HOME/.ssh/id_rsa"

terraform state list

May need sometime: https://registry.terraform.io/providers/integrations/github/latest/docs/resources/repository_deploy_key

## Github Actions

Might try this at some point.

## More Docker
docker-compose up -d --build Will force build

docker exec -it <container_id> bash, will ssh into the container. But changes to my own filesystem are not reflected.


## Curl
 curl -H 'Content-Type: application/json' \
      -d '{ "title":"foo","body":"bar", "id": 1}' \
      -X POST \
      http://localhost:3000/tsne
