# 🧩 JSON Parser

A simple JSON parser written in Python.

## 🎯 About

This is to help me learn more about the tokenization and parsing processes. So, I implement a simple JSON parser in Python because it is a more simple language.

## 🛝 Example

```py
import src.json import parse

json = '{"foo": "bar", "bool": false}'

data = parse(json)

print(data)

"""
Output:

{'foo': 'bar', 'bool': False}
"""
```

## 🧸 Testing

```sh
python -m unittest discover -s ./tests -p "*_test.py"
```
