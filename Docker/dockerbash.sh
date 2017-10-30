#root commands (sudo or sudo su)

#docker run images while dockerfile create an image
docker build -t friendlyname .
docker build [option] PATH | URL #-t tag an image


docker run --name myimagename -p localport:distantport -dockertype
#example
docker run --name mymongo -p 27027:27017 - mongo 

docker run --name truckapi --link mymongo mongo -d json-api


docker ps
docker ps -a #show images and running images


docker rmi $(docker images -q) # remove all images

docker rm $(docker ps -a -q) # remove all container