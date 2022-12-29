# ptmpdy 

ptmpdy project is aiming to reduce troubles in serverless stack operations. 

"ptmpdy" is "Please Tell Me Path Declaration in Yaml"

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

Please see [usage.md](usage.md).

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
