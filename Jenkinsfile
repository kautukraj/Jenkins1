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
                sh "python3 Prog11.py"
            }
        }
     stage('Test 1') {
            steps {
                sh "chmod u+x Test1.py"
                sh "python3 Test1.py"
            }
        }
        
     stage('Test 2') {
            steps {
                sh "chmod u+x Test2.py"
                sh "python3 Test2.py"
            }
        }

    }
}
