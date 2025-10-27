pipeline {
    agent any
    environment {
        PYTHON = 'C:\\Users\\HP\\AppData\\Local\\Programs\\Python\\Python313\\python.exe'
        APP_TOKEN = credentials("APP_TOKEN")
    }
    stages {
        stage('Checkout Code') {
            steps {
                git url:'https://github.com/sibeshpatel9490/jenkinsdemo3.git', branch:'main'
            }
        }
        stage('Install Dependencies') {
            steps {
                bat "%PYTHON% -m pip install -r requirements.txt"
            }
        }
        stage('Extract Data') {
            steps {
                bat """
                SET TOKEN=${env.APP_TOKEN}
                ${env.PYTHON} extract_data.py
                """
            }
        }
    }
}