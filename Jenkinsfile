node {
  stage('SCM') {
    checkout scm
  }
  stage('SonarQube Analysis') {
    def scannerHome = tool 'sonarqube';
    withSonarQubeEnv() {
      sh "$(scannerHome)/bin/sonar-scanner"
    }
  }
}
