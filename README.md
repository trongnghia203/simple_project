## Simple project exercise

Simple project to test packaging. Try to implement all the point in section Tasks. There are also Additional tasks if you are in mood.
All the code is python 3.6 or higher.


### Preparations
- create virtualenv with python 3.6 or higher
- install the only dependency `pyyaml` using pip
- test application code can be executed
```
cd simple_project
python -m simple_code.simple
```


### Tasks
- execute application without `-m` parameter and compare `import path` list
- configure packaging using setuptools with setup.cfg and setup.py
  - make sure that data file(s) are part of package
  - make sure application dependencies are defined
  - make sure application entry point is defined
- create second virtualenv
- install application to the second virtualenv:
  1. create sdist package and try to install it using pip
  2. install the whole project by pip directly - `pip install [-e] <project_dir>`
- verify application can be executed from virtualenv after installation


### Additional tasks
- try to setup packaging with setup.py file only
- try to identify where the application files were moved during `pip install`
- try to setup packaging with [Flit](https://flit.readthedocs.io/en/latest/) or [Poetry](https://python-poetry.org/docs/)
- try to use [cookiecutter](https://cookiecutter.readthedocs.io/en/1.7.2/index.html) to generate project


### References
- https://setuptools.readthedocs.io/en/latest/userguide/quickstart.html
- https://setuptools.readthedocs.io/en/latest/userguide/commands.html
- https://packaging.python.org/guides/distributing-packages-using-setuptools/#initial-files


### Example of packaging
https://github.com/pytest-dev/pytest

