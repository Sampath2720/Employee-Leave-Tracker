pipeline {
    agent any

    stages {

        stage('Clone Repository') {
            steps {
                git branch: 'main', url: 'https://github.com/Sampath2720/Employee-Leave-Tracker.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t employee-leave:latest .'
            }
        }

        stage('Deploy Container') {
            steps {
                sh '''
                docker stop employee-leave-ci || true
                docker rm employee-leave-ci || true

                docker run -d \
                --name employee-leave-ci \
                -p 7004:5000 \
                employee-leave:latest
                '''
            }
        }
    }
}
