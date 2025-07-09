pipeline{
    agent any
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

                sh 'pip install -r requirements.txt'
            }
        }
        stage("tests"){

            steps{

                echo "start testing"
                sh 'pytest tests/ --maxfail=1 --disable-warnings --tb=short'
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
