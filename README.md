# Demo Project
Using Python 3.6 pytest and requests, this solution aims at providing an easy to scale API test framework.

# Pre-requisites

The following steps are required to address the package dependencies. You may optionally run this within a virtual environment. 
```
python setup.py install
pip install .
```

# Running tests locally

From the root directory of this repository
```
export OWM_API_KEY=<your API key>
pytest
```

# Running tests on Travis-CI

This repository comes pre-configured with a `.travis.yml` file.

However, you will need to add the following Environment Variable(s) in the build settings.

| Environment variable | Description |
|---|---|
| `OWM_API_KEY` | openeweathermaps API key, keep hidden |