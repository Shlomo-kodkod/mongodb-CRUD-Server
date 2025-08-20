# Data server project 
- A service for CRUD operations in MongoDB server.


## Project Features
- Mongodb database using OpenShift.
- Access layer to DB.
- FastAPI server - Accesses mongodb and operate CRUD operations to a dedicated endpoint.

## Project structure
```
data-loader/
├── services/
│ └── data_loader/ # Data loading service
├── scripts/ #  OS scripts
├── infrastructure/
│ └── k8s/ # Kubernetes manifests (YAMLs)
├── Dockerfile
├── requirements.txt
└── README.md
```