#!/bin/bash

echo "Starting cleanup ..."

echo "Deleting Kubernetes objects ..."

# delete web app related objects
kubectl delete deployment my-deployment
kubectl delete service my-service
kubectl delete hpa auto-scaler

# remove alpine machine
kubectl delete pod alpine

echo "Deleting Kind Cluster ..."

# remove cluster
kind delete cluster

echo "cleanup done."