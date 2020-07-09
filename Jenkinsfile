node {

    stage("Checkout repository") {
        git branch: 'master',
        url: 'https://github.com/Oley96/qapropeller-qabattle.git'
    }

    stage("Install deps") {
        sh 'pip install -r requirements.txt'
    }

    stage("Run test and create allure report") {
        sh 'chmod +x run.sh'
        sh 'bash run.sh'
    }

}