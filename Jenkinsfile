pipeline {
    agent any
    stages {
        stage('Test') {
            steps {
                retry(3) {
                    echo 'This is testing for pipline'
                }

                timeout(time: 3, unit: 'MINUTES') {
                    echo 'This is testing for pipline'
                }
            }
        }
    }
}
