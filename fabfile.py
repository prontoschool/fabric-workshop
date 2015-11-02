# Simple Tasks

def hello():
    print 'Hello ThaiPy!'


def hi(name='Kan'):
    print 'Hi ' + name


# Local Commands

from fabric.api import local, lcd


def deploy_fizzbuzz():
    with lcd('fizzbuzz'):
        local('python fizzbuzz_test.py')
        local('git add fizzbuzz.py fizzbuzz_test.py')
        local('git commit')
        local('git push origin master')
