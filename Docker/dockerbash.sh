#root commands (sudo or sudo su)

docker ps
docker ps -a #show images and running images

docker run --name myimagename -p localport:distantport -dockertype
#example
docker run --name mymongo -p 27027:27017 - mongo 


docker run --name truckapi --link mymongo mongo -d json-api