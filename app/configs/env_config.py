import pathlib

from starlette.config import Config

ROOT = pathlib.Path(__file__).resolve().parent.parent  # app/
BASE_DIR = ROOT.parent  # ./

config_get_env = Config(BASE_DIR / ".env")


