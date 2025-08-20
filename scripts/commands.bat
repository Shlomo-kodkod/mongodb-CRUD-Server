docker build -t kodkod1docker/mongo-crud-server:v5 .
docker push kodkod1docker/mongo-crud-server:v5


cd infrastructure\k8s 

oc apply -f mongodb-secret.yaml
oc apply -f mongo-pvc.yaml
oc apply -f mongodb-deployment.yaml
oc apply -f mongo-service.yaml


oc apply -f fastapi-deployment.yaml
oc apply -f fastapi-service.yaml

oc expose service fastapi-server --port=8083 --target-port=8083 --name=fastapi-server
