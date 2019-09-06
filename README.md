# hello-py-k8s-envoy-example

```
$ eval $(minikube docker-env)
$ kubectl create configmap envoy-config --from-file envoy-config
$ kubectl apply -f hello-py.yaml
$ minikube service hello-py-service
```
