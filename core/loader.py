import importlib
import inspect
import pkgutil

from core.plugin import Plugin
import tools


def load_plugins():
    plugins = []

    for module_info in pkgutil.iter_modules(tools.__path__):
        module = importlib.import_module(f"tools.{module_info.name}")

        for _, obj in inspect.getmembers(module, inspect.isclass):
            if issubclass(obj, Plugin) and obj is not Plugin:
                plugins.append(obj())

    return plugins