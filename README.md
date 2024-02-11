# serverless-lambda-function-name-enum-python

[![PyPI version](https://badge.fury.io/py/ptmpdy.svg)](https://badge.fury.io/py/ptmpdy)
[![Workflow on new release published](https://github.com/hayata-yamamoto/ptmpdy/actions/workflows/pypi-publish.yml/badge.svg)](https://github.com/hayata-yamamoto/ptmpdy/actions/workflows/pypi-publish.yml)

## Overview

This CLI tools provide code generation experience.

If you have a [serverless.yml](tests/test_data/serverless.yml) to host your lambda application, ptmpdy provides Python Enum objects like

```python
from enum import Enum


class LambdaHandlers(str, Enum):
    sample_handler = "sample-service-sample-handler"
    sample_handler2 = "sample-service-sample-handler2"

```

## Usage

Please see [usage.md](docs/usage.md).

## Project Scope

Serverless Framework

- [x] Adding to Python code generation from `serverless.yml`
- [ ] Adding serverless plugin

## Development

```bash
poetry install
```

## Contributions

This project is welcome to contribute. When you want to contribute this project, please follow contribute guides.

**Guides**

1. Vote issues
2. Create a PR to main branch in assigning to @hayata-yamamoto as a reviewer
