# CertGen - Django Project to build an App that Generates and Manage an Issue of Certificates 

[![Build Status](https://travis-ci.org/Riverfount/pypro.svg?branch=master)](https://travis-ci.org/Riverfount/pypro)
[![codecov](https://codecov.io/gh/Riverfount/pypro/branch/master/graph/badge.svg)](https://codecov.io/gh/Riverfount/pypro)
[![Updates](https://pyup.io/repos/github/Riverfount/pypro/shield.svg)](https://pyup.io/repos/github/Riverfount/pypro/)
[![Python 3](https://pyup.io/repos/github/Riverfount/pypro/python-3-shield.svg)](https://pyup.io/repos/github/Riverfount/pypro/)
[![License: AGPL v3](https://img.shields.io/badge/License-AGPL%20v3-blue.svg?style=flat-square)](https://www.gnu.org/licenses/agpl-3.0)
[![PyPI - Python Version](https://img.shields.io/badge/Python%20Version-3.6.5-blue.svg?style=flat-square)](https://github.com/Riverfount/pypro)
[![PyPI - Django Version](https://img.shields.io/badge/Django%20Version-2.0.6-blue.svg?style=flat-square)](https://github.com/Riverfount/pypro)

##If you want to contribute you need to do:

Make sure that the Python >= 3.6.5 was installed.

1. Fork this project
2. Clone your fork to your computer
3. Add this repo as an upstream remote repo
4. Change to the directory of the project 
5. Create a virtualenv with Python >= 3.6.5
6. Active the virtualenv
7. Install the dependencies of the project
8. Make sure that the code agrees with the PEP8 recommendations
9. Make sure that the test will pass with codecov coverage

###These steps as a code:

```console
git clone [address to your remote fork repo]
git remote add upsream git@github.com:vmdesenvolvimento/certgen.git
cd certgen 
python -m venv .venv
source .venv/bin/activatte
pip install -r requirements-dev.txt
flake8 .
pytest --cov .
```

## Feature Branch

The workflow that we follow is the _Feature Branch_. In this process, you need to create a new branch with the number of
the Issue existing in the main repository. After you finish the code of this branch you make the `git push` to your
repository and make a Pull Request (PR) to the main repo, and mark at least one of the other members of the team to do
the code review and if all are ok this member of the team make rebase of the PR.   




