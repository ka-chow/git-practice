pipeline {
    agent any

    triggers {
        issueCommentTrigger('.*/docs.*')
    }

    stages {
        stage('Checkout') {
            steps {
                echo 'Code checked out from Git'
            }
        }
        stage('Set up Python') {
            steps {
                bat 'python --version'
                bat 'pip install -r requirements.txt'
            }
        }
        stage('Run Tests') {
            steps {
                bat 'python -m pytest test_utils.py -v'
            }
        }
        stage('Generate pydoc HTML') {
            steps {
                echo 'Generating HTML documentation with pydoc...'
                bat 'python -m pydoc -w utils'
                publishHTML(target: [
                    allowMissing: false,
                    alwaysLinkToLastBuild: true,
                    keepAll: true,
                    reportDir: '.',
                    reportFiles: 'utils.html',
                    reportName: 'pydoc HTML Report'
                ])
            }
        }
    }

    post {
        always {
            echo 'CI pipeline finished.'
        }
        success {
            echo 'All tests passed!'
        }
        failure {
            echo 'Some tests failed.'
        }
    }
}