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
        APP_REGISTRY = " "
        IMAGE_TAG = "latest"

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
        stage("tests")
        {

            steps
            {

                echo "start testing"
                bat 'python -m pytest tests/ --maxfail=1 --disable-warnings --tb=short'
            }
        }
        stage('Image creation and pushing to dockerhub')
        {
            steps{

                withCredentials([
                    usernamePassword
                    (
                        credentialsId: 'dockerhub-creds',
                        usernameVariable: 'DOCKER_USER',
                        passwordVariable: 'DOCKER_PASS'
                    )
                         ]) 
                {
                    
                    echo "login"

                    bat 'docker login -u %DOCKER_USER% -p %DOCKER_PASS%'

                    echo 'image creation'

                    bat 'docker image build -t %DOCKER_USER%/qr:latest ./app'

                    echo 'pushing'

                    bat 'docker push  %DOCKER_USER%/qr:latest'


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
                    echo 'tagging image'
                    bat 'docker tag qr:%IMAGE_TAG% %ECR_REGISTRY%/%ECR_REPO%:%IMAGE_TAG%'

                    echo 'pushing image'
                    bat 'docker push %ECR_REGISTRY%/%ECR_REPO%:%IMAGE_TAG%'
                }
                
            }
        }


    }

    post{

        success{
            echo "all good"
        }

        failure{
            echo "see logs"
        }
    }


}
