import os
import traceback

from importlib import util

#from .scanner.main import *
#from .scanner.options import *
#from .scanner.ScanInformation import *
#from .scanner.target import *
#from .scanner.nmap import *

class ModulesClass:
    plugins = []

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        cls.plugins.append(cls)

def load_module(path):
    name = os.path.split(path)[-1]
    spec = util.spec_from_file_location(name, path)
    module = util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

path = os.path.abspath(__file__)
dirpath = os.path.dirname(path)

for fname in os.listdir(dirpath):
    if not fname.startswith(".") and \
        not fname.startswith("__") and fname.endswith(".py"):
        try:
            load_module(os.path.join(dirpath, fname))
        except Exception:
            traceback.print_exc()