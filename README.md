# Erlang term library implemented in pure Python [![Build Status](https://travis-ci.org/machinezone/python_etf.svg?branch=master)](https://travis-ci.org/machinezone/python_etf)

to use:

```python
from erl_terms import decode

result = decode("[{1, 2}, {3, 4}].")
```

to run tests:

```bash
python setup.py test
```