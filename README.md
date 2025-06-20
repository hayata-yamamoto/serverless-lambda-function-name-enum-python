# sls_enum

[![PyPI version](https://badge.fury.io/py/sls-enum.svg)](https://badge.fury.io/py/sls-enum)

## Overview

A CLI tool that generates Python Enum classes from Serverless Framework configuration files. This tool parses your `serverless.yml` file and creates type-safe Enum objects for Lambda function names, making it easier to reference your functions in Python code.

## Features

- Generate Python Enum classes from `serverless.yml` files
- Support for stage-specific function naming
- Type-safe Lambda function name references
- Dry-run mode for previewing generated code
- Easy integration with existing Python projects

## Installation

```bash
pip install sls_enum
```

Or using Poetry:

```bash
poetry add sls_enum
```

## Usage

### Basic Usage

Generate an Enum class from your serverless.yml:

```bash
sls_enum serverless.yml output.py
```

### With Stage

Include stage in function names:

```bash
sls_enum serverless.yml output.py --stage dev
```

### Dry Run

Preview the generated code without writing to file:

```bash
sls_enum serverless.yml output.py --dry-run
```

### Example Output

Given a `serverless.yml` with functions like:

```yaml
service: my-service
functions:
  sample-handler:
    handler: handler.sample
  another-handler:
    handler: handler.another
```

The tool generates:

```python
from enum import Enum


class LambdaHandlers(str, Enum):
    sample_handler = "my-service-sample-handler"
    another_handler = "my-service-another-handler"
```

## Command Line Options

- `FP`: Path to serverless.yml file (required)
- `OUTPUT`: Output Python file path (required)
- `--stage TEXT`: Stage name to include in function names
- `--dry-run`: Preview generated code without writing to file
- `--help`: Show help message

## Development

### Setup

```bash
poetry install
```

### Running Tests

```bash
poetry run pytest
```

### Code Formatting

```bash
poetry run black .
poetry run isort .
```

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Run tests and ensure code formatting
6. Create a pull request targeting the main branch
7. Assign @hayata-yamamoto as a reviewer

## License

See [LICENSE](LICENCE) file for details.
