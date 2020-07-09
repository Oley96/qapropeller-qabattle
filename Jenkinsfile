node {

    stage("Checkout repository") {
        git branch: 'master',
        url: 'https://github.com/Oley96/qapropeller-qabattle.git'
    }

    stage("Install deps") {
        sh 'python3 -m venv venv'
        sh 'source venv/bin/activate'
        sh 'pip3 install -r requirements.txt'
    }

    stage("Run test") {
        sh 'chmod +x run.sh'
        sh 'bash run.sh'
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