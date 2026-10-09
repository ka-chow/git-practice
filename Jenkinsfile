pipeline {
    agent any

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
        stage('Generate Docs') {
            steps {
                bat 'if not exist docs mkdir docs'
                bat 'copy README.md docs\\index.md'
                echo 'Documentation generated in docs/index.md'
            }
        }
        stage('Generate Doxygen HTML') {
            when {
                triggeredBy 'GitHubPullRequestCommentCause'
            }
            steps {
                echo 'Generating HTML documentation with Doxygen...'
                bat 'doxygen Doxyfile'
                publishHTML(target: [
                    allowMissing: false,
                    alwaysLinkToLastBuild: true,
                    keepAll: true,
                    reportDir: 'docs/html',
                    reportFiles: 'index.html',
                    reportName: 'Doxygen HTML Report'
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