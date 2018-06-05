# CertGen - Django Project to build an App that Generates and Manage an Issue of Certificates 

[![Build Status](https://travis-ci.org/vmdesenvolvimento/certgen.svg?branch=master)](https://travis-ci.org/vmdesenvolvimento/certgen)
[![codecov](https://codecov.io/gh/vmdesenvolvimento/certgen/branch/master/graph/badge.svg)](https://codecov.io/gh/vmdesenvolvimento/certgen)
[![Updates](https://pyup.io/repos/github/vmdesenvolvimento/certgen/shield.svg)](https://pyup.io/repos/github/vmdesenvolvimento/certgen/)
[![Python 3](https://pyup.io/repos/github/vmdesenvolvimento/certgen/python-3-shield.svg)](https://pyup.io/repos/github/vmdesenvolvimento/certgen/)
[![License: AGPL v3](https://img.shields.io/badge/License-AGPL%20v3-blue.svg?style=flat-square)](https://www.gnu.org/licenses/agpl-3.0)
[![PyPI - Python Version](https://img.shields.io/badge/Python%20Version-3.6.5-blue.svg?style=flat-square)](https://github.com/Riverfount/pypro)
[![PyPI - Django Version](https://img.shields.io/badge/Django%20Version-2.0.6-blue.svg?style=flat-square)](https://github.com/Riverfount/pypro)
[![Waffle.io - Columns and their card count](https://badge.waffle.io/vmdesenvolvimento/certgen.png?columns=all)](https://waffle.io/vmdesenvolvimento/certgen?utm_source=badge)

## If you want to contribute you need to do:

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

### These steps as a code:

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

_Feature Branch_ is the workflow in place. In this process, you need to create a new branch with the number of the Issue existing in the main repository. Feature is described on a issue tracker which generates a number for it. This number is used as branch's name. Then you create a PR with finished code and refer the issue's number to automatically close it which will map requisite to code changes. Thus you assign at least a team mate as reviwer and code is rebased after discussion.
