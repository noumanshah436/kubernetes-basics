# FastNext Local (FastAPI + Next.js + Celery) - Minikube / Local Setup

This project is prepared for **local development** using Docker Compose and for **local Kubernetes (Minikube/kind)** testing.

## Contents
- backend/            -> FastAPI app + Celery worker
- frontend/           -> Next.js app
- docker-compose.yml  -> Local dev orchestration (postgres, redis, backend, worker, frontend)
- k8s/                -> Kubernetes manifests (Namespace, ConfigMap, Secrets, Deployments, StatefulSet, Ingress)

## Quick local (docker-compose) run
1. Build & bring up services:
   ```bash
   docker compose up --build
   ```
2. Backend: http://localhost:8000
   Frontend: http://localhost:3000

## Quick Minikube steps (local images)
1. Start minikube and enable ingress (example):
   ```bash
   minikube start --driver=docker
   minikube addons enable ingress
   ```
2. Build docker images into minikube's docker daemon (so you can use local images):
   ```bash
   eval $(minikube -p minikube docker-env)
   docker build -t backend:local ./backend
   docker build -t frontend:local ./frontend
   ```
3. Apply k8s manifests:
   ```bash
   kubectl apply -f k8s/namespace.yaml
   kubectl apply -f k8s/configmap.yaml -n fastnext
   kubectl apply -f k8s/secrets.yaml -n fastnext
   kubectl apply -f k8s/postgres-statefulset.yaml -n fastnext
   kubectl apply -f k8s/redis-deployment.yaml -n fastnext
   kubectl apply -f k8s/backend-deployment.yaml -n fastnext
   kubectl apply -f k8s/frontend-deployment.yaml -n fastnext
   kubectl apply -f k8s/celery-deployment.yaml -n fastnext
   kubectl apply -f k8s/ingress.yaml -n fastnext
   ```
4. Add host entry to access via `myapp.local` (or use `minikube tunnel`/LoadBalancer):
   - Edit `/etc/hosts` and add:
     ```
     127.0.0.1 myapp.local
     ```
   - Or run `minikube tunnel` (requires admin).

## Notes
- DB migrations are not included (Alembic is present in requirements). For production, add proper migrations and secrets handling.
- This setup uses simple env/config for demo. Do not use in production without hardening.
- For local Kubernetes we use images `backend:local` and `frontend:local` built into Minikube's docker daemon.