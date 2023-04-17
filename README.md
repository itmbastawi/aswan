# Aswan project
Django REST API 
- webapi project
- mainapp
    - content 
        * View, model, serializers, testing

## structure
1. Django project
1. requirements.txt
1. env
1. make
1. Dockerfile
1. docker-compose


## Getting start
1. Clone git repository
1. Edit .env file
1. Stop tracking env file
```
git update-index --assume-unchanged .env

```
### Makefile
1. build and start docker compose 
``` 
make up
```
2. stop docker compose
```
make down
```
3. build docker image
```
make build
```