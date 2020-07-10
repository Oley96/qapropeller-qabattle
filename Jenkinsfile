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
        sh 'venv/bin/pytest --remote=True --browser_ver=83.0 ./tests'
    }

    stage("Create report") {
        script {
            allure([
                    includeProperties: false,
                    jdk: '',
                    properties: [],
                    reportBuildPolicy: 'ALWAYS',
                    results: [[path: 'target/allure-results']]
            ])
    }
    }

}