# 🐍 Hello Python

## Getting Started

This project uses [VS Code](https://code.visualstudio.com/download) and the [Python Extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python) which you can setup using their [Python Setup Tutorial](https://code.visualstudio.com/docs/languages/python)

This repository is following the below Python Packaging structure:

https://pytest.readthedocs.io/en/reorganize-docs/new-docs/user/directory_structure.html

```
├─ packagename
│  ├─ __init__.py
│  └─ ...
├─ tests
│  └─ ...
├─ Pipfile
└─ tasks.py
```

This repository also uses [`pipenv`](https://github.com/pypa/pipenv) (which combines `pip` and `virtualenv`) to manage dependencies just like `npm`, `bundler`, `cargo`, `yarn`, etc. 
Have a read about it with this [pipenv guide](https://realpython.com/pipenv-guide/).

So to pull down dependencies run:

```bash
# Install dependencies
pipenv install
# Drop down to virtual environment
pipenv shell
```

We are using the [invoke](https://www.pyinvoke.org/) framework to manage `tasks.py`

```bash
# Discover tasks
$ inv --list
# Or if not in a pipenv shell use this for one off tasks:
$ pipenv run inv --list
Available tasks:

  cov        see also: coverage
  coverage   Run code coverage tooling with pytest tests as stimulants
  covwatch   Run code coverage tooling in watch mode
  lint       This task is available from CLI but normal development should leverage lint in VS Code.
  test       Run pytest tooling

```

# TODO

 - Docker files and kubernetes tooling
 - Cython optimisation of performance critical code
    - https://docs.python-guide.org/scenarios/speed/
 - Profiling tooling

# Resources

 - https://docs.python-guide.org/
    - https://docs.python-guide.org/intro/learning/
 - http://howtopython.org/en/latest/
 - https://github.com/kennethreitz (Author of `requests` module)