from ptmpdy.main import app
from contextlib import contextmanager
from typer.testing import CliRunner
from pathlib import Path


DATA_DIR = Path(__file__).resolve().parent / 'test_data'

runner = CliRunner()
config_path = DATA_DIR / "serverless.yml"
export_path = DATA_DIR / 'export.py'


@contextmanager
def remove_test_file() -> None:
    export_path.unlink(missing_ok=True)

    yield

    export_path.unlink(missing_ok=True)


def test_can_generate_python_code() -> None:
    with remove_test_file():
        ret = runner.invoke(app, [str(config_path), str(export_path)])
        assert ret.exit_code == 0
        assert export_path.exists()


def test_can_show_python_code_will_be_generated_when_pass_dry_run() -> None:
    with remove_test_file():
        ret = runner.invoke(app, [str(config_path), str(export_path), "--dry-run"])
        assert ret.exit_code == 0
        assert not export_path.exists()
