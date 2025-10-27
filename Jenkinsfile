pipeline {
    agent any
    environment {
        PYTHON = 'C:\\Users\\HP\\AppData\\Local\\Programs\\Python\\Python313\\python.exe'
        APP_TOKEN = credentials("APP_TOKEN")
    }
    stages {
        stage('Checkout Code') {
            steps {
                checkout scm
            }
        }
        stage('Install Dependencies') {
            steps {
                bat " ${env.PYTHON} -m pip install -r requirements.txt"
            }
        }
        stage('Extract Data') {
            steps {
                bat """
                SET TOKEN=%APP_TOKEN%
                %PYTHON% extract_data.py
                """
            }
        }
    }
}