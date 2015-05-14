"""
Some commands based around
https://hynek.me/articles/sharing-your-labor-of-love-pypi-quick-and-dirty/

"""

from fabric.api import env, local, task
import os

# Local path configuration (can be absolute or relative to fabfile)
env.deploy_path = 'dist'


@task
def clean():
    """Delete any built output."""
    if os.path.isdir(env.deploy_path):
        local('rm -rf {deploy_path}'.format(**env))


@task
def build():
    """Build the packages."""
    local('python setup.py sdist')
    local('python setup.py bdist_wheel')


@task
def rebuild():
    """Clean, then build."""
    clean()
    build()


@task
def register(repository='test'):
    """Register on pypi."""
    local('python setup.py register -r %s' % repository)


@task
def bumpversion(part='patch'):
    """Bump the version."""
    local('bumpversion %s setup.py' % part)


@task
def upload(repository='test'):
    """Upload to test pypi."""
    local('python setup.py sdist upload -r %s' % repository)
    local('python setup.py bdist_wheel upload -r %s' % repository)


@task
def test():
    local('python -m unittest discover tests')
