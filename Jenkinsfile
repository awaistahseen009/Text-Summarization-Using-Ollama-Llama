pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "llama-text-summarizer-awais:latest"
        REGISTRY = "your-dockerhub-username/llama-text-summarizer"
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Build') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Test') {
            steps {
                sh 'pytest tests/'
            }
        }
        stage('Deploy') {
            steps {
                script {
                    sh 'docker build -t $DOCKER_IMAGE .'
                    // Uncomment and configure the following lines to push to Docker Hub
                    // withCredentials([usernamePassword(credentialsId: 'dockerhub', usernameVariable: 'DOCKERHUB_USER', passwordVariable: 'DOCKERHUB_PASS')]) {
                    //     sh "echo $DOCKERHUB_PASS | docker login -u $DOCKERHUB_USER --password-stdin"
                    //     sh "docker tag $DOCKER_IMAGE $REGISTRY"
                    //     sh "docker push $REGISTRY"
                    // }
                }
            }
        }
    }
} 