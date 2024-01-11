import importlib
from pathlib import Path
from pkgutil import iter_modules

def fetch_criterion(name):
    try:
        criterion_module = importlib.import_module(f"src.criteria.criteria_{name}")
        return criterion_module.evaluate
    except ImportError as fetch_error:
        raise ImportError(f"No criterion module found for '{name}'. Error: {fetch_error}")

def fetch_criteria():
    criteria_directory = Path(__file__).parent / "criteria"
    criteria = {}

    for _, name, _ in iter_modules([str(criteria_directory)]):

        if name.startswith("criteria_"):

            criterion_module = importlib.import_module(f"src.criteria.{name}")

            criteria[name] = {
                "evaluate": criterion_module.evaluate,
                "required_fields": getattr(criterion_module, "required_fields", {})
            }

    return criteria
