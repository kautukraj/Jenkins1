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
                sh "chmod u+x Prog11.py"
                sh "./Prog11.py"
            }
        }
     stage('Test Code') {
            steps {
                sh "chmod u+x Test1.py"
                sh "./Test1.py"
            }
        }
    }
}