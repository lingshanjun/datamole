from fabric.api import *


env.hosts = ['root@138.68.6.219']

# echo remote env variables
def env():
    run('env')


# checkout remote project to be develop status
def develop():
    run('echo "export DJANGO_SETTINGS_MODULE=datamole.settings" > /etc/profile')
    run('source /etc/profile')
    run('env')


# checkout remote project to be product status
def product():
    run('echo "export DJANGO_SETTINGS_MODULE=datamole.settings.production" > /etc/profile')
    run('source /etc/profile')
    run('env')


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
