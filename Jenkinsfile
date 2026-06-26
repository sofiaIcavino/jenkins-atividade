pipeline {
    agent none

    triggers {
        cron('12 03 * * *')
    }

    stages {
        stage('Build') {
            agent {
                docker {
                    image 'python:3.12-slim'
                    args '--user root'
                }
            }
            steps {
                sh 'python3 -m py_compile conversor.py'
                sh 'echo "Build concluído com sucesso no container de build!"'
            }
        }

        stage('Testes') {
            agent {
                docker {
                    image 'python:3.12-slim'
                    args '--user root'
                }
            }
            steps {
                sh 'pip install pytest --quiet'
                catchError(buildResult: 'UNSTABLE', stageResult: 'UNSTABLE') {
                    sh 'python3 -m pytest test_conversor.py -v --junitxml=resultado_testes.xml'
                }
            }
            post {
                always {
                    junit allowEmptyResults: true, testResults: 'resultado_testes.xml'
                }
            }
        }
    }

    post {
        success  { echo 'Pipeline finalizado com sucesso!' }
        unstable { echo 'Build ok, mas testes falhando — instável!' }
        failure  { echo 'Falha no pipeline!' }
    }
}