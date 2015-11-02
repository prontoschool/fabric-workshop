VAGRANT_IP = '192.168.66.77'
EC2_IP = '54.179.183.245'


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


# Remote Commands

from fabric.api import cd, env, run


env.hosts = [
    'vagrant@' + VAGRANT_IP + ':22',
]
env.passwords = {
    'vagrant@' + VAGRANT_IP + ':22': 'vagrant'
}


def create_empty_file(name='test'):
    env.forward_agent = True
    run('touch ' + name)
    run('ls -al')


# ssh-add ~/.ssh/thaipy-demo.pem since accessing EC2 requires a key pair
def my_ec2():
    env.hosts = [
        'ubuntu@' + EC2_IP + ':22',
    ]


def deploy_page():
    run('rm -rf fabric-workshop')
    run('git clone https://github.com/zkan/fabric-workshop.git')
    run('sudo cp fabric-workshop/index.html /usr/share/nginx/html')
    run('sudo service nginx restart')


# Parallel Execution

from fabric.api import parallel


def my_servers():
    env.hosts = [
        'vagrant@' + VAGRANT_IP + ':22',
        'ubuntu@' + EC2_IP + ':22',
    ]


@parallel
def run_in_parallel():
    run('whoami')
