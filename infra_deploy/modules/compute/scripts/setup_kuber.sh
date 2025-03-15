#!/bin/bash

yc managed-kubernetes cluster get-credentials catg7gju3svbo6eaa60g --external

yc managed-kubernetes cluster start catg7gju3svbo6eaa60g

kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
