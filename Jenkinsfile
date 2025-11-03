pipeline {
    agent any
    environment {
        VENV = "${WORKSPACE}\\venv"
    }
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Setup') {
    steps {
        bat 'python -m venv %VENV%'
        bat '%VENV%\\Scripts\\python.exe -m pip install --upgrade pip'
        bat '%VENV%\\Scripts\\python.exe -m pip install -r requirements.txt'
    }
}

        stage('Lint') {
            steps {
                bat '%VENV%\\Scripts\\pip install flake8'
                bat '%VENV%\\Scripts\\flake8 .'
            }
        }
        stage('Test') {
            steps {
                bat '%VENV%\\Scripts\\python manage.py test'
            }
        }
        stage('Build Docker Image') {
            when {
                branch 'main'
            }
            steps {
                bat 'docker build -t your_django_image:%BUILD_NUMBER% .'
            }
        }
    }
    post {
        always {
            cleanWs()
        }
    }
}
