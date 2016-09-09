from fabric.api import *
from fabric.contrib import django


env.hosts = ['root@138.68.6.219']


# echo remote env variables
def env():
    run('env')


# checkout remote project to be develop status
def develop():
    django.settings_module('datamole.settings')


# checkout remote project to be product status
def product():
    django.settings_module('datamole.settings.production')
    # restart()


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
