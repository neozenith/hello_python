# Hello Python

## Getting Started

This repository is following the follwoing Python Packaging structure:

https://blog.ionelmc.ro/2014/05/25/python-packaging/#the-structure


```
├─ src
│  └─ packagename
│     ├─ __init__.py
│     └─ ...
├─ tests
│  └─ ...
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