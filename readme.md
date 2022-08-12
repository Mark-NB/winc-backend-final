<h2>WINC Backend Continous Deployment</h2>

[![Run tests and deploy if succesfull](https://github.com/Mark-NB/winc-cd/actions/workflows/run-tests.yml/badge.svg)](https://github.com/Mark-NB/winc-cd/actions/workflows/run-tests.yml)

<h3>Report</h3>

<h4>Short overview</h4>
<p>This assigenment has asked me to setup a CD (continous deployment) pipeline. In a nutshell, a developer writes some new code on his/her/their local machine, pushes this new code to the repository on github, github then uses a action to automatically test the code, and(if these tests are succesfull) upload the new code to the server which is running the application</p>

<h4>Three components of the solution</h4>
<h5>SSH server acces</h5>
<p>I have set-up a SSH key which allows github actions to acces the server at digital ocean which is required to execute the neccesary scripts on the server. The SSH key has been addes to github's "secrets" so that it can be used inside github actions without comprimising the key's contents</p>
<h5>Github action</h5>
<p>I have created a github action by adding a YAML file to my repository. This YAML file provides github actions with the information it needs to execute the desired actions. In my case the action is triggered everytime a new commit is pushed to the repository. The action is divided into 2 jobs, "run-tests" and "deploy". The run-tests job tells github to setup a enviroment with python and the neccesary dependencies(found in the requirements.txt file), and then runs the tests using pytest. If all tests are succesfull the deploy job starts. This job uses the appleboy/ssh-action to connect to the VPS using the SSH-key found inside the github secrets. It then runs a few lines of script on the server which i will explain below</p>
<h5>SSH github access</h5>
<p>I have setup a second SSH key which allows the VPS to connect to the github repository. This SSH key has been stored in the repo's deploy key section. When the github action is being ran, as explained above, the server uses this SSH key to connect to the github repo and do it's git pull, updating the files on the server to the new version found in the repository.</p>

<h4>Three problems i encountered</h4>
<h5>Jinja dependency in testing</h5>
<p>When i first setup the test part of the github action i ran into a error concerning the loading of jinja as a dependency. I found out rather quickly that, as jinja is already included with flask, i did not need to name it seperately in my requirements.txt file. Removing jinja from the requirements.txt file immediately solved this problem.</p>
<h5>SSH agent persistency for server to github access</h5>
<p>When using the github action to make the server perform the pull request i ran into a authentication problem. Github could access the VPS withou issues and run scripts localy, but running the git pull to update the local repository gave back a authentication error (err: git@github.com: Permission denied (publickey)). Yet when i ran the same command whilst being logged in to the server directly (using bash for example) the git pull worked just fine. I first switched the local repo to use HTTPS instead of SSH, which did work fine, both localy and through a github action. This told me that the problem was the SSH acces to github. I found out, after some help from Ate, and some futher google work, that the SSH-agent on the server is'nt persistent so a new login or system reboot would cause the SSH agent and the key to dissapear. I fixxed this issue by having the github action run some additional script on the server to startup the SSH agent, and load the SSH key, prior to doing the git pull.</p>
<h5>It was very warm</h5>
<p>I felt like a joke couldn't hurt here, and to be honest it was really hot yesterday and today. On the serious note though, the above problems where the only "serious" problems I encountered during this assignment. I might have made a few typo's here or there but nothing that really halted my progress other than the above. I felt that the subject matter was well explained in the course material beforehand and it all seemed to make sense to me so i didn't struggle much with this assignment.</p>