# Password Generator 

Test framework for [Password Generator](https://www.security.org/password-generator/) feature


## Requirements

- [Python](https://www.python.org/downloads/) ~= 3.12
- [Chrome](https://www.google.com/chrome/) browser ~= 130.0.6723.92
- [Firefox](https://www.mozilla.org/en-US/firefox/) browser ~= 132.0.1


## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install dependencies.

```commandline
pip install -r requirements.txt
```


## Usage

Run tests.

By default, all tests run in single thread with Chrome browser.
```commandline
pytest
```

Generate report.html and store it in /reports dir. 

By default, report disabled.
```commandline
pytest --html=reports/report.html --self-contained-html
```

Choose another browser to run tests. 

By default, used Chrome browser. Available option is Firefox.
```commandline
pytest --browser Firefox
```

Enable headless mode. 

By default, disabled.
```commandline
pytest --headless True
```

Run tests in parallel. 

By default disabled. Recommended value 'auto' - distributing tests across all available CPUs. Could be passed a fixed number of parallel threads. 
```commandline
pytest -n auto
```
