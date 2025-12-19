**Project Overview**

This project is a Tier-2 web application that allows users to generate and download QR codes for text, URLs, or custom input. It consists of a lightweight frontend website, a Python-based backend API for QR generation, and a fully automated CI/CD pipeline that builds, containerizes, and deploys the application to AWS.

The system is designed to be cost-optimized, modular, and easy to extend. Each component is Dockerized, and deployments are handled through Amazon ECS, with images stored in Amazon ECR. The CI/CD pipeline is implemented using Jenkins and intelligently rebuilds and deploys only the components that have changed.

Features:

* Generate QR codes for text, URLs, or custom input

* Download generated QR codes as images

* Simple and responsive frontend website

* Backend API for QR generation

* Dockerized application components

* Automated CI/CD pipeline using Jenkins

* Optimized AWS infrastructure using ECS + ECR

Tech Stack:

* Backend: Python

* Frontend: HTML, JavaScript

* CI/CD: Jenkins

* Containerization: Docker, Amazon ECR

* Deployment: Amazon ECS

      CI/CD Pipeline Flow
      
      Developer Commit
              ↓
      GitHub Webhook
              ↓
      Jenkins
              ↓
      Detect Changed Component(s)
              ↓
      Build & Test Only Changed Folder(s)
              ↓
      Docker Image Build
              ↓
      Push Image to Amazon ECR
              ↓
      Deploy Updated Image to Amazon ECS
              ↓
      Live Website

**Execution Steps:**

* Clone the Repository

      git clone https://github.com/Harshit10j2004/CICD-pipeline_for_containerized_app.git
      cd CICD-pipeline_for_containerized_app
* Backend Setup (Local)

      cd backend
      pip install -r requirements.txt
      python app.py
  
* Docker Build
  
        docker build -t backend .
  
* Frontend setup (Local)

      cd frontend

* Docker Build

      docker build -t frontend .

* Docker compose for testing locally

      cd ..
      docker compose up

After testing all things

* Jenkins setup

  Verify Jenkins Is Running
  
      sudo systemctl status jenkins


  If not running:

      sudo systemctl start jenkins
      sudo systemctl enable jenkins


  Open in browser:

      http://<EC2-PUBLIC-IP>:8080

  Install Required Jenkins Plugins

  Go to:

      Manage Jenkins → Plugins → Available


  Install:

    * Git

    * GitHub

    * Pipeline

    * Docker Pipeline
 
    * AWS

  Restart Jenkins if prompted.

  Install Docker on EC2 (Required for Builds)

  Jenkins runs on host, but Docker must exist.

      sudo apt update
      sudo apt install -y docker.io
      sudo systemctl start docker
      sudo systemctl enable docker

  Add Credentials in Jenkins
    * GitHub Credentials
      
      Manage Jenkins → Credentials → System → Global → Add Credentials


          Kind: Username with password
          
          Username: GitHub username
          
          Password: GitHub personal access token
          
          ID: github-creds

    * AWS Credentials

      Manage Jenkins → Credentials → System → Global → Add Credentials


          Kind: AWS Credentials
          
          Access Key ID
          
          Secret Access Key
          
          ID: aws-creds

    * Create Pipeline Job

      Jenkins Dashboard → New Item
      
      Name: qr-app-pipeline
      
      Type: Pipeline
      
      Click OK

    * Configure Pipeline Job
      General:
      
      GitHub project
      
          https://github.com/<username>/<repo>
      
      Build Triggers
      
          GitHub hook trigger for GITScm polling
          
           Do NOT enable polling

      Pipeline
      
        Definition: Pipeline script from SCM
      
      SCM: Git

      Repository URL:
      
          https://github.com/<username>/<repo>.git
      
      
      Credentials: github-creds
      
            Branch:
            
            */main
            
      
      Script Path:
      
          Jenkinsfile


      Save.



  * Configure GitHub Webhook

    GitHub repo → Settings → Webhooks → Add Webhook

    Payload URL:

        http://<EC2-PUBLIC-IP>:8080/github-webhook/


    Content type: application/json
    
    Secret: empty
    
    Events: Just push

    Active: 
    
    Save.

* Verify Webhook Delivery

    GitHub → Webhooks → Click webhook → Recent Deliveries
    
    You must see:
    
    200 OK


    If not:
    
    Port 8080 blocked in EC2 Security Group
    
    Jenkins not running
    
    Wrong URL

* End-to-End Test
  
      git commit -am "webhook test"
      git push origin main


Expected:

Jenkins job auto-triggers

Console log prints:

Webhook triggered Jenkins successfully



**See my Blog for information and journey**: 

https://harshithere.hashnode.dev/beyond-manual 

