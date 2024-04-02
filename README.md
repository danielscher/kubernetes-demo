# Kubernetes Horizontal Pod Autoscaler (HPA) Demo
This repository contains a demonstration of the Horizontal Pod Autoscaler (HPA) object in Kubernetes. 
The demo showcases how to set up a multi-node cluster using Kind (Kubernetes in Docker) on a single machine, 
deploy a Flask web server, and then simulate heavy traffic to the web server using a traffic generator.

# Prerequisites
* Docker
* Kind
* kubectl

# Setup
1. clone repository.
2. cd to kubernetes folder and execute `./setup.sh` to setup all required Kubernetes objects.

# Monitoring
open to side-by-side terminals 
1. execute `kubectl get hpa -w` to monitor hpa in one terminal.
2. execute `white (1) {kubectl top pods -l app=my-app; sleep 4}` to monitor pods in the other.  
*sometimes metrics server requires more time to get going so in case `top` does not work wait 1-2 minutes.

# Simulate traffic
to simulate traffic we'll use wrk.
1. run `kubectl exec -it alpine --bin/sh` to open a terminal in the alpine container
2. install wrk with `apk install wrk` and run `wrk -t 2 -c 10 -d 300 http://my-app-service/`

Web app will start to use up resources and the hpa will attempt to scale the application to meet the specified resource utilization.

# License
This project is licensed under the [MIT License](https://opensource.org/licenses/MIT). Feel free to use, modify, and distribute this code for educational and non-commercial purposes.
