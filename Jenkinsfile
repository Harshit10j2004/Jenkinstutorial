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
        DOCKER_USER = "harshit1001"

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

        stage('Cleanup') 
        {
            steps 
            {
                bat 'docker image prune -a -f'
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
        stage('Image creation ')
        {
            steps{

               
                echo 'image creation'

                bat 'docker build -t %ECR_REGISTRY%/%ECR_REPO%:%IMAGE_TAG% ./app'


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
