pipeline {
    agent any
    environment {
        VENV = "${WORKSPACE}/venv"
    }
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Setup') {
            steps {
                sh 'python3 -m venv $VENV'
                sh '$VENV/bin/pip install --upgrade pip'
                sh '$VENV/bin/pip install -r requirements.txt'
            }
        }
        stage('Lint') {
            steps {
                sh '$VENV/bin/pip install flake8'
                sh '$VENV/bin/flake8 .'
            }
        }
        stage('Test') {
            steps {
                sh '$VENV/bin/python manage.py test'
            }
        }
        stage('Build Docker Image') {
            when {
                branch 'main'
            }
            steps {
                sh 'docker build -t your_django_image:$BUILD_NUMBER .'
            }
        }
    }
    post {
        always {
            cleanWs()
        }
    }
}
