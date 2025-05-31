# Template Repository for Python Development

This repository serves as a template for developing new functionality for the [`djangomatic-python-backend`](https://github.com/yourorganization/djangomatic-python-backend) Django application. It replicates the environment of the main project to help developers create and test new features outside the main repository.

## Table of Contents

- [Getting Started](#getting-started)
- [Development Workflow](#development-workflow)
- [Integration with djangomatic-python-backend](#integration-with-djangomatic-python-backend)
- [Version Control](#version-control)
- [Resources](#resources)
- [Using the Makefile](#using-the-makefile)
- [Testing](#testing)
- [Repository Structure](#repository-structure)
- [Prototyping & Development](#prototyping-&-development)

## Getting Started

### Prerequisites

- Python 3.12
- [Git](https://git-scm.com/) for version control
- One of the following for managing virtual environments:
  - [Pyenv](https://github.com/pyenv/pyenv) (preferred)
  - [Conda](https://docs.conda.io/en/latest/)
  - [Poetry](https://python-poetry.org/) installed globally

### Clone the Repository

```bash
git clone https://github.com/td-automation-team/template-repo-python.git
cd template-repo-python
```

### Create and Activate the Virtual Environment

Choose one of the following methods to create a `.venv` virtual environment:

#### Option 1: Using Pyenv (Preferred)

**On macOS:**

Install `pyenv` and `pyenv-virtualenv`:

```bash
brew update
brew install pyenv pyenv-virtualenv
```

Configure your shell environment (optional):

```bash
echo 'eval "$(pyenv init -)"' >> ~/.bash_profile
echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.bash_profile
source ~/.bash_profile
```

Create and activate the virtual environment:

```bash
pyenv install 3.12
pyenv virtualenv 3.12 .venv
pyenv local .venv
pyenv activate .venv
```

or

```bash
pyenv install 3.12
pyenv global 3.12
python -m venv .venv
pyenv global system
source .venv/bin/activate
```

**On Windows (Using WSL):**

Install `pyenv` and follow similar steps as on macOS.

#### Option 2: Using Conda

Create and activate the virtual environment:

```bash
conda create -n .venv python=3.12
conda activate .venv
```

#### Option 3: Using Globally Installed Poetry

If Poetry is installed globally:

```bash
poetry config virtualenvs.in-project true
poetry install
poetry shell
```

### Install Dependencies

If not already installed (Options 1 and 2), install the project dependencies:

```bash
poetry install
```

### Create a `.env` File (If Required)

If the project requires environment variables, create a `.env` file in the root directory. Ensure sensitive information is managed securely.

### Set Up Pre-Commit Hooks

Install the pre-commit hooks defined in [`.pre-commit-config.yaml`](./.pre-commit-config.yaml):

```bash
pre-commit install
```

## Development Workflow

### Using the Template Notebook

A starter notebook is available in the `src` directory:

```bash
src/dev_template.ipynb
```

- Rename it with a descriptive name for your feature.
- Develop and test new functionality within this notebook.
- Document your code and explanations using markdown cells.

### Organizing Input Data

- Place input data files in the `_input_data` directory.
- Organize data appropriately for the project.
- Avoid committing large files to the repository.

### Best Practices

- Follow Python coding standards (PEP 8).
- Use type hints where appropriate.
- Write tests for new features.
- Comment code to improve readability.
- Commit changes frequently with meaningful messages.

## Integration with `djangomatic-python-backend`

After testing:

- Integrate new functionality into the `djangomatic-python-backend` project.
- Adhere to the project's guidelines for adding features.
- Ensure all tests pass before committing changes.

## Version Control

- Use Git for version control.
- Create branches for new features.
- Rebase or merge regularly to stay up-to-date.
- Push changes to a remote repository for collaboration.

## Resources

- [Pyenv Documentation](https://github.com/pyenv/pyenv)
- [Conda Documentation](https://docs.conda.io/)
- [Poetry Documentation](https://python-poetry.org/docs/)
- [Pre-Commit Hooks](https://pre-commit.com/)
- [PEP 8 Style Guide](https://www.python.org/dev/peps/pep-0008/)

## Using the Makefile

The project includes a Makefile to simplify common development tasks:

```bash
make <target>
```

Common targets include:

- `make install`: Install dependencies.
- `make lint`: Run linters.
- `make test`: Run tests.
- `make clean`: Clean up temporary files.

## Testing

### Directory Structure

Organize your tests in a `tests` directory at the root of your project. Use subdirectories to group related tests.

```
template-repo-python/
│
├── tests/
│   ├── __init__.py
│   ├── test_module1.py
│   ├── test_module2.py
│   └── ...
│
├── src/
│   ├── module1.py
│   ├── module2.py
│   └── ...
│
└── ...
```

### Writing Tests

Use the `unittest` module or `pytest` for writing tests. Here is an example using `pytest`:

```python
# tests/test_module1.py

import pytest
from src.module1 import function_to_test

def test_function_to_test():
    result = function_to_test()
    assert result == expected_value
```

### Running Tests

To run tests, use the following command:

```bash
make test
```

Or, if you are using `pytest` directly:

```bash
pytest
```

### Best Practices

- Write tests for all new features and bug fixes.
- Use descriptive names for test functions.
- Group related tests in classes or modules.
- Use fixtures for setup and teardown.
- Aim for high test coverage but prioritize meaningful tests over coverage percentage.
- Run tests frequently during development to catch issues early.

> For reference, this template includes sample tests under the `tests` directory. They can be adapted to fit your needs.

Ensure all tests pass before committing changes.

## Repository Structure

Below is a simplified layout of the project:

```
template-repo-python/
├── _input_data/                # dir for input datasets
├── .pre-commit-config.yaml     # config for linting & code formatting
├── .gitignore                  # files Git should ignore
├── Makefile                    # commands for managing the project
├── README.md                   # project documentation & setup instructions
├── pyproject.toml              # deps management & build configuration
├── src/                        # source code dir
│   ├── __init__.py             # makes it a Python package
│   ├── dev_template.ipynb      # template notebook for dev
│   ├── usage_example.py        # example module showcasing usage patterns
│   └── ...
├── tests/                      # test dir
│   ├── __init__.py             # makes it a Python package
│   ├── test_usage_example.py   # tests for the example module
│   └── ...
└── ...
```

The repository follows a clean, modular structure where:

- Source code lives in `src/`
- Tests mirror the source structure in `tests/`
- Configuration files are in the root
- Development tools are configured via dot files
- Input data is segregated in `_input_data/`

This showcases where notebooks, modules, tests, and configurations reside.

## Prototyping & Development

- Use notebooks in `src/dev_*.ipynb` for exploration, rapid prototyping, or quick data experiments.
- After prototyping, transpose stable code into Python modules under `src/`, ensuring each addition is tested in the `tests/` directory.
- Consistent testing and module structure simplifies integration into downstream Django projects.
- Adhere to the existing Python style guidelines and project conventions.
