# Kubernetes-multiingress-deployment
Below are the steps followed to achive the output.

minikube start
minikube addons enable ingress
kubectl get pods -n kube-system
kubectl create namespace development1
kubectl create namespace development2
  helm install stable/nginx-ingress --set controller.ingressClass=first --namespace development1 --set controller.replicaCount=1 --set rbac.create=false
  helm install stable/nginx-ingress --set controller.ingressClass=second --namespace development2 --set controller.replicaCount=1 --set rbac.create=false
kubectl apply -f deployment1.yaml -n development1 
kubectl apply -f deployment2.yaml -n development2
kubectl apply -f service1.yaml
kubectl apply -f service2.yaml
kubectl apply -f ingress1.yaml
kubectl get ingress
kubectl apply -f ingress2.yaml
kubectl get ingress 
curl localhost:30080
curl localhost:30081
kubectl autoscale deployment web1 --cpu-percent=50 --min=1 --max=10
will scale from 1 to 10  replicas of the Pods
kubectl get hpa
When increased the load on box using the following command.
    kubectl run -i --tty load-generator --rm --image=busybox --restart=Never -- /bin/sh -c "while sleep 0.01; do wget -q -O- http:google.com; done"
kubectl get hpa
NAME         REFERENCE                     TARGET      MINPODS   MAXPODS   REPLICAS   AGE
web1   Deployment/web1/scale                328% / 50%  1         10        1          6m
kubectl get deployment
NAME         READY   UP-TO-DATE   AVAILABLE   AGE
web1   7/7      7           7           19m
Stop the load using CTRL+C
kubectl get hpa
   NAME         REFERENCE                     TARGET       MINPODS   MAXPODS   REPLICAS   AGE
    web1   Deployment/web1/scale              0% / 50%     1         10        1          15m
kubectl get deployment web1
NAME         READY   UP-TO-DATE   AVAILABLE   AGE
web1   1/1     1            1           27m
    

