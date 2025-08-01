

This project is a Tier-2 Web Application that allows users to generate and download QR codes. It includes a simple frontend website, backend API for QR generation, and an automated CI/CD pipeline for deployment to AWS.

**Features**:

1) Generate QR codes for text, URLs, or custom input

2) Download QR codes as images

3) Responsive frontend website for easy usage

4) CI/CD pipeline with Jenkins

5) Dockerized deployment to AWS (ECR + ECS)

6) cost-optimized infrastructure

**Tech Stack**:

1) Backend: Python

2) Frontend: HTML, JavaScript

3) CI/CD: Jenkins

4) Containerization: Docker, Amazon ECR

5) Deployment: Amazon ECS

**Flow of pipeline**:

[Developer Commit] -->|GitHub Webhook| [Jenkins]
[Determine Changed Component(s)]
[Build & Test only for changed folder(s)]
[Docker Image(s) for those component(s)]
[Upload the image to ECR]
[ECS Deployment]
[Live Website]

**See my Blog for all information**: 

https://harshithere.hashnode.dev/beyond-manual 

