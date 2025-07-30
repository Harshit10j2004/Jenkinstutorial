pipeline
{
    agent any
    tools
    {

        git 'main-git'
    }

    environment 
    {
        
        ECR_REPO = "harshit1001"
        ECR_REGISTRY = "869935091377.dkr.ecr.ap-south-1.amazonaws.com"
        ECR_REPO2 = "frontend-repo"
        APP_REGISTRY = " "
        IMAGE_TAG = "latest"
        DOCKER_USER = "harshit1001"
        cluster = "harshitclusterforqr"
        service1 = "backend"
        service2 = "frontend"



    }
    stages
    {
        stage("checkout")
        {

            steps
            {
                echo "started to checkout"
                checkout scm
            }
        }

        stage("download dependencies")
        {
            
            steps
            {

                echo "started downloading"

                bat 'pip install -r requirements.txt'
            }
        }


        stage("checking which code changes"){

            steps{

                script{

                    echo 'checking which image is changed'

                    def changedFiles = bat(
                        script: 'git diff --name-only HEAD~1', 
                        returnStdout: true
                    ).trim()

                    echo 'changed file is \n${changedFiles}'

                    env.backend_changed = changedFiles.contains('app/') ? 'true' : 'false'
                    env.frontend_changed = changedFiles.contains('frontend/') ? 'true' : 'false'
                }
            }
        }

        
        stage("tests")
        {

            steps
            {
                script{

                    if (env.backend_changed == 'true'){

                        echo "start backend testing"
                        bat 'python -m pytest tests/ --maxfail=1 --disable-warnings --tb=short'

                    }
                    
                    else{

                        echo 'skipping backend testing'
                    }

                    if(env.frontend_changed == 'true'){

                        echo "start frontend testing"
                    }

                    else{

                        echo 'skipping frontend testing'
                    }

                }
                
            }
        }
        stage('Image creation ')
        {
            steps{

                script{

                    if(env.backend_changed){

                        echo 'backend image creation'

                        bat 'docker build --no-cache -t %ECR_REGISTRY%/%ECR_REPO%:%IMAGE_TAG% ./app'

                    }
                    else{

                        echo 'skipping the backend'
                    }

                    if(env.frontend_changed){

                        echo 'creating frontend image'

                        bat 'docker build --no-cache -t %ECR_REGISTRY%/%ECR_REPO2%:%IMAGE_TAG% ./frontend'


                    }
                    else{

                        echo 'skipping the frontend'
                    }
                }

               
                

                }
           
            
        }

        stage('login to ecr')
        {

            steps
            {

                withAWS(credentials: 'AWS' , region: 'ap-south-1'){

                    echo 'login into ecr'

                    bat 'aws ecr get-login-password --region ap-south-1 | docker login --username AWS --password-stdin 869935091377.dkr.ecr.ap-south-1.amazonaws.com'
                }

            }
        }

        stage('push to ecr')
        {

            steps
            {
                withAWS(credentials: 'AWS', region: 'ap-south-1')
                {
                    script{

                        if(env.backend_changed == 'true'){

                            echo 'pushing backend image'
                            bat 'docker push %ECR_REGISTRY%/%ECR_REPO%:%IMAGE_TAG%'

                        }
                        else{
                            echo 'skipping pushing to ecr'
                        }

                        if(env.frontend_changed == 'true'){

                            echo 'pushing frontend image'
                            bat 'docker push %ECR_REGISTRY%/%ECR_REPO2%:%IMAGE_TAG%'

                        }
                        else{

                            echo 'skipping frontend'
                        }
                    }

                   
                    
                }
                
            }
        }

        stage('deploying into ecr'){

            steps{

                withAWS(credentials: 'AWS' , region: 'ap-south-1'){

                    script{

                        if(env.backend_changed == 'true'){

                            echo 'deploying the backend'

                            bat 'aws ecs update-service --cluster ${cluster} --service ${service1} --force-new-deployment'

                        }
                        else{

                            echo 'backend doesnt need to update'
                        }

                        if(env.frontend_changed == 'true'){

                            echo 'deploying the frontend'

                            bat 'aws ecs update-service --cluster ${cluster} --service ${service2} --force-new-deployment'
                        }
                    }
                }
            }
        }


    }

    post{

        success{
            echo 'sucess and mail is send'
            mail to: "hg079567@gmail.com",
                subject: "deployed"
                body: "the app is updated and deployed"
        }

        failure{
            echo "failure see logs and mail is send"
            mail to: "hg079567@gmail.com",
                subject: "error"
                body: "the app cant deploy there is error see logs"
        }
    }


}
