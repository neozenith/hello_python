"""
    @author: Josh Peak
    @description: Task definition file to simpliufy and automate this repository
"""
from invoke import task


@task
def lint(context):
    """
        This task is available from CLI but normal development should leverage lint in VS Code.
        See More https://code.visualstudio.com/docs/python/linting
    """
    context.run(" ".join([
        "autopep8",
        "--recursive",
        "--jobs 0",
        "--in-place",
        "--aggressive",
        "-v",
        "greeting",
        "tests"
    ]))
    context.run("pylint greeting")


@task
def test(context):
    """
        Run pytest tooling
    """
    context.run("python -m pytest")


@task
def cov(context):
    """see also: coverage"""
    coverage(context)


@task
def coverage(context):
    """
        Run code coverage tooling with pytest tests as stimulants
        NOTE: must use form python -m pytest to include SRC_ROOT in
        sys.path so local module resolves for testing and not site-packages
    """
    context.run(" ".join([
        "python -m pytest",
        "--cov=greeting",
        "--cov-report html",
        "--cov-branch",
        "--cov-fail-under=75"
    ]))


@task
def covwatch(context):
    """
        Run code coverage tooling in watch mode
        NOTE: must use form python -m pytest to include SRC_ROOT in
        sys.path so local module resolves for testing and not site-packages
    """
    # TODO: Implement Watch tasks
    # https://github.com/gorakhargosh/watchdog
    context.run(" ".join([
        "python -m pytest",
        "--cov=greeting",
        "--cov-report html",
        "--cov-branch",
        "--cov-fail-under=75"
    ]))
