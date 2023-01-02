from typing import Optional

import yaml
from jinja2 import Template
from rich import print
from typer import Argument, Exit, Option, Typer

app = Typer()

TEMPLATE = """from enum import Enum
    

class LambdaHandlers(str, Enum):
    {% for key, value in handlers.items() %}
    {{- key }} = \"{{ value }}\"
    {% endfor %}
"""


@app.command()
def generate(
    fp: str = Argument(...),
    output: str = Argument(...),
    stage: Optional[str] = Option(default=None),
    dry_run: bool = Option(default=False),
) -> None:
    with open(fp) as f:
        data = yaml.safe_load(f)

    if not data.get("service"):
        print("service is not declared")
        Exit(1)

    if not data.get("functions"):
        print("functions are not declared")
        Exit(1)

    service = data["service"]
    handlers = {}
    for handler_suffix, meta in data["functions"].items():
        if meta.get("events"):
            continue

        if stage:
            handler_name = f"{service}-{stage}-{handler_suffix}"
        else:
            handler_name = f"{service}-{handler_suffix}"

        handlers.update({handler_suffix.replace("-", "_"): handler_name})

    template: Template = Template(source=TEMPLATE)
    out = template.render(handlers=handlers)

    if dry_run:
        print(out)
    else:
        with open(output, "w") as f:
            f.write(out)
