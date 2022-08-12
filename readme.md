<h2>WINC Backend Continous Deployment</h2>

[![Run tests and deploy if succesfull](https://github.com/Mark-NB/winc-cd/actions/workflows/run-tests.yml/badge.svg)](https://github.com/Mark-NB/winc-cd/actions/workflows/run-tests.yml)

<h3>Report</h3>
<h4>Three components of the solution</h4>
<h5>SSH server acces</h5>
<p>I have set-up a SSH key which allows github actions to acces the server at digital ocean which is required to execute the git pull command on the server. The SSH key has been addes to github's "secrets" so that it can be used inside github actions without comprimising the key's contents</p>
<h5>Github action</h5>
<p>I have created a github action by adding a YAML file to my repository. This YAML file provides github actions with the information it needs to execute the desired actions. In my case the action is triggered everytime a new commit is pushed to the repository. The action is divided into 2 jobs. "run-tests" and "deploy". The run-tests job tells github to setup a envireoment </p>