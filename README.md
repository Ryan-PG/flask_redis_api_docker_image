# flask_redis_api_docker_image


A dockerized flask_redis api. This is a flask_redis simple api that have routes to set(POST) and get(GET) routes.




# Compose
Fist of all compose this container using this command:  
`sudo docker compose -f flask_redis_compose_file.yaml up`  

# SET

To set a key-value pair using `curl` command, you can use the following syntax:  
`curl -X POST -H "Content-Type: application/json" -d '{"key": "name", "value": "Ryan"}' localhost:80/set`  



# GET

To retrieve the value of a key using `curl` command, you can use the following syntax:  
`curl localhost:80/get?key=name`  
