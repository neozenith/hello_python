"""
    @author: Josh Peak
    @description: Task definition file to simpliufy and automate this repository
"""
from invoke import task

# TODO: Implement Watch tasks
# https://github.com/gorakhargosh/watchdog

@task
def lint(context):
    """
        This task is available from CLI but normal development should leverage lint in VS Code.
        See More https://code.visualstudio.com/docs/python/linting
    """
    context.run("pylint greeting")

@task
def test(context):
    """
        Run pytest tooling
    """
    context.run("pytest")

@task
def cov(context):
    """see also: coverage"""
    coverage(context)

@task
def coverage(context):
    """
        Run code coverage tooling with pytest tests as stimulants
    """
    context.run("pytest --cov")
    
