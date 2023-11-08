# Project Name

[![Build Status](https://your-ci-badge-url-here)](https://your-ci-project-link-here)

## Description

This Python package provides a collection of string manipulation functions, including grouping 
anagrams, checking string inclusions, decoding strings, and finding the length of the longest 
substring without repeating characters.

## Installation

To install this package, run the following command in your terminal:

```bash
pip install your-package-name
```

## Usage

Here's how to use the functions provided in this package:

### Group Anagrams

```python
from your_package_name import groupAnagrams
print(groupAnagrams(["string1", "string2", "string3"]))
```

### Check Inclusion

```python
from your_package_name import checkInclusion
print(checkInclusion("string1", "string2"))
```

### Length of Longest Substring

```python
from your_package_name import lengthOfLongestSubstring
print(lengthOfLongestSubstring("string1"))
```

### Decode String

```python
from your_package_name import decodeString
print(decodeString("string1"))
```

For complete examples, refer to the [example Python program](#).

## Contributing

To contribute to this project, please follow these steps:

1. Clone the repository:
   ```bash
   git clone 
https://github.com/software-students-fall2023/3-python-package-exercise-team-dominators-1.git
   ```
2. Set up a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  
   ```
3. Install dependencies using `Pipfile`:
   ```bash
   pip install pipenv
   pipenv install
   ```
4. Build and test the package:
   ```bash
   python setup.py sdist bdist_wheel
   python -m unittest discover
   ```

## Team

- [Steve Hai](https://github.com/Hyteve)
- [Ashley Luo](https://github.com/luoashley)
- [Ethan Sha](https://github.com/EthanSha111)
- [Merry Cui](https://github.com/merrylearninggithub)

## PyPI

This package is also available on PyPI:

[Your package on PyPI](https://pypi.org/project/stringmanipulate/0.0.2/)