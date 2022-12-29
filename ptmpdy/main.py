import yaml
from jinja2 import Template
from rich import print
from typer import Exit, Typer

app = Typer()

TEMPLATE = """from enum import Enum
    

class LambdaHandlers(str, Enum):
    {% for key, value in handlers.items() %}
    {{- key }} = \"{{ value }}\"
    {% endfor %}
"""


@app.command()
def generate(fp: str, output: str, dry_run: bool = False) -> None:
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

        handlers.update(
            {handler_suffix.replace("-", "_"): f"{service}-{handler_suffix}"}
        )

    template: Template = Template(source=TEMPLATE)
    out = template.render(handlers=handlers)

    if dry_run:
        print(out)
    else:
        with open(output, "w") as f:
            f.write(out)
