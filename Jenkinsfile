pipeline {
    agent { 
        node {
            label 'docker-agent-python2'
            }
      }
    triggers {
        pollSCM 'H/5 * * * *'
    }
    stages {
        stage('Build') {
            steps {
                echo "Building.."
                sh '''
                cd myapp
                
                echo "Creating virtual environment..."
                python3 -m venv /home/jenkins/venv
                . /home/jenkins/venv/bin/activate
                echo "Installing fire package..."
                pip install -r requirements.txt
                '''
            }
        }
        stage('Test') {
            steps {
                echo "Testing.."
                sh '''
                echo "Entering venv"
                . /home/jenkins/venv/bin/activate
                cd myapp
                python3 hello.py
                python3 hello.py --name=Kai
                '''
            }
        }
        stage('Deliver') {
            steps {
                echo 'Deliver....'
                sh '''
                echo "doing delivery stuff.."
                '''
            }
        }
    }
}