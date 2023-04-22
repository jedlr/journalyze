# Journalyze

A Python library to facilitate the journinaling experience.

![GitHub](https://img.shields.io/badge/license-MIT-ff69b4)
[![](https://img.shields.io/github/issues/jedlr/journalyze?color=ff69b4)](https://github.com/jedlr/journalyze/issues)

[![Build Status](https://github.com/jedlr/journalyze/workflows/Build%20Status/badge.svg?branch=main)](https://github.com/jedlr/journalyze/actions?query=workflow%3A%22Build+Status%22)
[![codecov](https://codecov.io/gh/jedlr/journalyze/branch/main/graph/badge.svg)](https://codecov.io/gh/jedlr/journalyze)
[![PyPI](https://img.shields.io/pypi/v/journalyze)](https://pypi.org/project/journalyze/)

## Overview
Journalyze:
* Fetches journaling prompts 

## Installation
```
pip install journalyze
```
## How to Use
After installing the library, there are currently 3 functions available for use.

Simply `import * from journalyze`, and then call any of the following functions:

**get_prompt()**

`getPrompt()` randomly selects a prompt from the list of prompts in csv file

**add_prompt()**

`add_prompt()` adds a new prompt to the list of prompts in csv file

**remove_prompt()**

`remove_prompt()` removes a prompt from the list of prompts in csv file

## Example
Running the following code
```python
import journalyze as dp

dp = DailyPrompt('journalyze/prompts.csv')
prompt = dp.get_prompt()
print(prompt)
```
Outputs something like this to the console
```
Describe yourself using the first 10 words that come to mind. Then list 10 words that you’d like to use to describe yourself. List a few ways to transform those descriptions into reality.
```


## Details
This project is a pure python project using modern tooling. It uses a `Makefile` as a command registry, with the following commands:
- `make`: list available commands
- `make develop`: install and build this library and its dependencies using `pip`
- `make build`: build the library using `setuptools`
- `make lint`: perform static analysis of this library with `flake8` and `black`
- `make format`: autoformat this library using `black`
- `make annotate`: run type checking using `mypy`
- `make test`: run automated tests with `pytest`
- `make coverage`: run automated tests with `pytest` and collect coverage information
- `make dist`: package library for distribution
