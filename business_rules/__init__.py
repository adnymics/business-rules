# Version is set in project.json
# TODO: read project.json and set __version__ accordingly?
#__version__ = '1.0.5'

from .engine import run_all
from .utils import export_rule_data

# Appease pyflakes by "using" these exports
assert run_all
assert export_rule_data
