# Python Starter Template

Start your python projects off right!  Use this template.

## Basic Usage
Create a new project on Github and use this repo as a template.

Clone the newly made repo.
```
git clone <ssh_repo_url>
```

### Create a Virtual Environment
Once cloned, create a virtual environment.  You made nead to download additional packages if this is your first time creating a virtual environment.

```
python3 -m venv ./venv
```

### Activate your virtual environment
```
// Unix
source ./venv/bin/activate

// Windows
source ./venv/Scripts/activate
```
You'll know you're in the virtual environment as your terminal will now be prefixed with `(venv) user@pc`.

### Update PIP
Its a good idea to update pip.
```
python.exe -m pip install --upgrade pip
```

## Starting Development Environment
Make sure your virtual environment is activated, and then install the application locally
```
pip install -e .'[dev]'
```
This will install all necessary packages for production AND development.

## Uploading to PyPi
```
python -m twine upload --repository <repo_url> dist/\*
```

# References
[Python Packaging](https://packaging.python.org/en/latest/tutorials/packaging-projects/
)

# TODO
1. Create python convenience script for adding the project name to the necessary files.
2. Way to use both `pyproject.toml` and `setup.py`?  Keeping both up to date is cumbersome.


