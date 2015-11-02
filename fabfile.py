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
    'vagrant@192.168.66.77:22',
]
env.passwords = {
    'vagrant@192.168.66.77:22': 'vagrant'
}


def create_empty_file(name='test'):
    env.forward_agent = True
    run('touch ' + name)
    run('ls -al')


# ssh-add ~/.ssh/thaipy-demo.pem since accessing EC2 requires a key pair
def my_ec2():
    env.hosts = [
        'ubuntu@54.251.184.112:22',
    ]


def deploy_page():
    run('rm -rf fabric-workshop')
    run('git clone https://github.com/zkan/fabric-workshop.git')
    run('sudo cp fabric-workshop/index.html /usr/share/nginx/html')
    run('sudo service nginx restart')
