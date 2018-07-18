# CertGen - Django Project to build an App that Generates and Manage an Issue of Certificates 

[![Build Status](https://travis-ci.org/vmdesenvolvimento/certgen.svg?branch=master)](https://travis-ci.org/vmdesenvolvimento/certgen)
[![codecov](https://codecov.io/gh/vmdesenvolvimento/certgen/branch/master/graph/badge.svg)](https://codecov.io/gh/vmdesenvolvimento/certgen)
[![Updates](https://pyup.io/repos/github/vmdesenvolvimento/certgen/shield.svg)](https://pyup.io/repos/github/vmdesenvolvimento/certgen/)
[![Python 3](https://pyup.io/repos/github/vmdesenvolvimento/certgen/python-3-shield.svg)](https://pyup.io/repos/github/vmdesenvolvimento/certgen/)
[![License: AGPL v3](https://img.shields.io/badge/License-AGPL%20v3-blue.svg?style=flat-square)](https://www.gnu.org/licenses/agpl-3.0)
[![PyPI - Python Version](https://img.shields.io/badge/Python%20Version-3.6.5-blue.svg?style=flat-square)](https://github.com/vmdesenvolvimento/certgen)
[![PyPI - Django Version](https://img.shields.io/badge/Django%20Version-2.0.6-blue.svg?style=flat-square)](https://github.com/vmdesenvolvimento/certgen)

## If you want to contribute you need to do:

Make sure that the Python >= 3.6.5 was installed.

1. Fork this project
2. Clone your fork to your computer
3. Add this repo as an upstream remote repo
4. Change to the directory of the project 
5. Create a virtualenv with Python >= 3.6.5
6. Active the virtualenv
7. Install the dependencies of the project
8. Create a .env with a copy of contrib/env-sample
9. Make sure that the code agrees with the PEP8 recommendations
10. Make sure that the test will pass with codecov coverage

### These steps as a code:

```console
git clone [address to your remote fork repo]
git remote add upstream git@github.com:vmdesenvolvimento/certgen.git
cd certgen 
python -m venv .venv
source .venv/bin/activate
pip install -r requirements-dev.txt
cp contrib/env-sample .env
isort -rc --atomic .
flake8 .
pytest --cov .
```

## Feature Branch

_Feature Branch_ is the workflow in place. In this process, you need to create a new branch with the number of the Issue
existing in the main repository. Feature is described on a issue tracker which generates a number for it. This number is
used as branch's name. Then you create a PR with finished code and refer the issue's number to automatically close it
which will map requisite to code changes. Thus you assign at least a team mate as reviwer and code is rebased after 
discussion.

### How to implement Feature Branch on the project?

1. Go to the project directory
2. Activate the virtualenv
3. Make the fetch and rebase of upstream repository - branch master
4. Create a new branch with the number of the Issue
5. You should work to implement the task of the Issue
6. Add the files changed to the stage of local repository
7. Make a commit with a expressive message about what you do
8. Make the push to your repository fork
9. Make the Pull Request to the main repository
10. Mark at least teammate to review your code
11. Wait that your PR will be reviewed and merged on to the master of the main repository

### Some of the before steps expressed in code:

```console
~/$ cd certgen
~/certgen (master)/$ source .venv/bin/activate
(.venv) ~/certegen (master)/$ git pull --rebase upstream master
(.venv) ~/certegen (master)/$ git checkout -b [issue's number]
```
... now work to implement the task of the issue ...

```console
(.venv) ~/certegen (master)/$ git add .
(.venv) ~/certegen (master)/$ git commit -m 'A message that expose what do you do'
(.venv) ~/certegen (master)/$ git push origin master
```

The steps 10 - 12 must do on Github.
