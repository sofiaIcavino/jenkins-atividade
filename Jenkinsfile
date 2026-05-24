pipeline {
    agent any

    triggers {
        cron('0 * * * *')
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Instalar dependencias') {
            steps {
                sh 'pip install pytest pytest-cov --break-system-packages'
            }
        }

        stage('Build') {
            steps {
                sh 'python3 -m py_compile conversor.py'
            }
        }

        stage('Testes') {
            steps {
                catchError(buildResult: 'UNSTABLE', stageResult: 'UNSTABLE') {
                    sh 'python3 -m pytest test_conversor.py -v --junitxml=resultado_testes.xml'
                }
            }
            post {
                always {
                    junit 'resultado_testes.xml'
                }
            }
        }

        stage('Cobertura de Codigo') {
            steps {
                sh 'python3 -m pytest --cov=conversor --cov-report=xml --cov-report=term test_conversor.py'
            }
            post {
                always {
                    recordCoverage(tools: [[parser: 'COBERTURA', pattern: 'coverage.xml']])
                }
            }
        }
    }
}
