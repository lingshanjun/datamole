from fabric.api import *
from fabric.contrib import django

env.hosts = ['root@138.68.6.219']


# checkout remote project to be develop status
def develop_r():
    with cd('/home/django/datamole/datamole/settings/'):
        run('echo "debug = True" > debug_conf.py ')
        restart()


# checkout remote project to be product status
def product_r():
    with cd('/home/django/datamole/datamole/settings/'):
        run('echo "debug = False" > debug_conf.py ')
        restart()


# update code from git repo and restart server
def update():
    with cd('/home/django/datamole'):
        run('git pull')
        run('service gunicorn restart')


# just update code from git repo
def pull():
    with cd('/home/django/datamole'):
        run('git pull')


# just restart server
def restart():
    with cd('/home/django/datamole'):
        run('service gunicorn restart')


# checkout local project to be develop status
def develop_l():
    with lcd('/Users/lwj/mysite/datamole/datamole/settings/'):
        local('echo "debug = True" > debug_conf.py ')


# checkout local project to be product status
def product_l():
     with lcd('/Users/lwj/mysite/datamole/datamole/settings/'):
        local('echo "debug = False" > debug_conf.py ')
    # restart()