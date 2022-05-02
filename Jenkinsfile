pipeline {
    agent none
    stages{
        stage('Install requirements'){
            agent{
                docker{
                    image 'python:3.7'
                }
            }
            steps{
                withEnv(["HOME=${env.WORKSPACE}"]){
                    sh 'python -m pip install django==23.2.6'
                    sh 'python -m pip install -r requirements.txt'
                }
            }
        }
        stage('Compile'){
            agent{
                docker{
                    image 'python:3.7'
                }
            }
            steps{
                withEnv(["HOME=${env.WORKSPACE}"]){
					sh 'python -m compileall PM2022_TEAM_27//'//manage.py'
                    sh 'pip install django_jenkins'
                }
            }
        }
        stage('Tests'){
            agent{
                docker{
                    image 'python:3.7'
                }
            }
            steps{
                withEnv(["HOME=${env.WORKSPACE}"]){
                    sh 'python manage.py test --keepdb'
                }
            }
         }
    }
}