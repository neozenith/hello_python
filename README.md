# Hello Python

## Getting Started

This repository is following the follwoing Python Packaging structure:

https://pytest.readthedocs.io/en/reorganize-docs/new-docs/user/directory_structure.html

```
├─ packagename
│  ├─ __init__.py
│  └─ ...
├─ tests
│  └─ ...
├─ tasks.py
└─ setup.py
```

```bash
pip install -r requirements.txt
```

Using the [invoke](https://www.pyinvoke.org/) framework to manage `tasks.py`

```bash
# Discover tasks
inv --list
```