pipeline {
    agent none
    stages{
        stage('Install requirements'){
            agent{
                docker{
                    image 'joyzoursky/python-chromedriver'
                }
            }
            steps{
                withEnv(["HOME=${env.WORKSPACE}"]){
                    sh 'python -m pip install django==2.1.15'
                    sh 'python -m pip install --upgrade pip'
                    sh 'python -m pip install -r requirements.txt'
                }
            }
        }
        stage('Compile'){
            agent{
                docker{
                    image 'joyzoursky/python-chromedriver'
                }
            }
            steps{
                withEnv(["HOME=${env.WORKSPACE}"]){
		            sh 'python -m compileall PM2022_TEAM_27//'//manage.py'
                    sh 'pip install django_jenkins'
		            sh 'pip install requests'
		            sh 'pip install selenium'
		            sh 'pip install chromedriver_py'
			    sh 'pip install coverage'
                    sh 'pip install mysql'
                }
            }
        }
        stage('Tests'){
            agent{
                docker{
                     image 'joyzoursky/python-chromedriver'
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
