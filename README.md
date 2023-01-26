# How to run tests

```sh
$ git clone https://github.com/mtshrmn/234124-ex5-tests ex5test
$ cd ex5test
$ cp /path/to/ex5.py .
$ python -m pytest
```

## Running the tests on csl3

```sh
$ git clone https://github.com/mtshrmn/234124-ex5-tests ex5test
$ cd ex5test
$ sh ./install_pytest.sh
$ cp /path/to/ex5.py .
$ python3 -m pytest
```
### Disclaimer
Those tests were randomly generated


### Troubleshooting

- Pytest isn't installed
```sh
$ python -m pytest
/usr/bin/python: No module named pytest

```
Install pytest using pip (**make sure pip is installed**)
```sh
$ python -m pip install pytest
```
