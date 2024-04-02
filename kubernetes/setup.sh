#!/bin/bash

echo "Starting cluster setup ..."

# setup cluster
kind create cluster --config=cluster.yaml

# wait for cluster to be ready
kubectl wait --for=condition=Ready nodes --all

echo "Deploying metrics ..."

# deploy metrics server
kubectl apply -f https://github.com/kubernetes-sigs/metrics-server/releases/latest/download/components.yaml
kubectl patch deployment metrics-server -n kube-system --type='json' -p='[{"op": "add", "path": "/spec/template/spec/containers/0/args/-", "value": "--kubelet-insecure-tls"}]'
kubectl rollout status deployment/metrics-server -n kube-system --timeout=60s

echo "Deploying objects ..."

# deploy webapp
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
kubectl apply -f hpa.yaml

# deploy alpine
kubectl apply -f alpine.yaml

echo "done."