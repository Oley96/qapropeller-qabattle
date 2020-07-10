node {

    stage("Checkout repository") {
        git branch: 'master',
        url: 'https://github.com/Oley96/qapropeller-qabattle.git'
    }

    stage("Install deps") {
        sh 'python3 -m venv venv'
        sh 'venv/bin/pip install -r requirements.txt'

    }

    stage("Run test") {
            catchError(buildResult: 'SUCCESS', stageResult: 'FAILURE') {
                sh 'venv/bin/pytest --reruns 2 --remote=True --browser_ver=83.0 --alluredir=allure-results ./tests'
            }
    }

    stage("Create report") {
        script {
            allure([
                    includeProperties: false,
                    jdk: '',
                    properties: [],
                    reportBuildPolicy: 'ALWAYS',
                    results: [[path: 'allure-results']]
            ])
    }
    }

}