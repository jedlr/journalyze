# Welcome to journalyze's documentation!

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

**get_affirmation()**

`get_affirmation()` randomly selects a positive affirmation from the list of affirmations in csv file
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

```eval_rst
.. toctree::
   :maxdepth: 2
   :caption: Contents:
```