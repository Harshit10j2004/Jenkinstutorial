pipeline{
    agent any
    tools{

        git 'main-git'
    }
    stages{
        stage("checkout"){

            steps{
                echo "started to checkout"
                checkout scm
            }
        }

        stage("download dependencies"){
            
            steps{

                echo "started downloading"

                bat 'pip install -r requirements.txt'
            }
        }
        stage("tests"){

            steps{

                echo "start testing"
                bat 'python -m pytest tests/ --maxfail=1 --disable-warnings --tb=short'
            }
        }
        stage('Image creation and pushing'){
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
