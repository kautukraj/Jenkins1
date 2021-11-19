pipeline {
agent any
    stages {
        stage('Clone Git') {
            steps {
                git 'https://github.com/kautukraj/Jenkins1.git'
            }
        }
        stage('Build Code') {
            steps {
                sh "chmod u+x HelloWorld.py"
                sh "./HelloWorld.py"
            }
        }
    }
}
