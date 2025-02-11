#!/usr/bin/python3

import importlib.util

PKGS = [
    'os', 'sys', 'configparser', 'argparse', 'struct', 'multiprocessing',
    'socket', 'time', 'logging', 'redis', 'numpy', 'fnmatch', 're',
    'signal', 'simplejson'
]

for p in PKGS:
    m_repr = f"'{p}'"
    m_repr = m_repr.ljust(20, ".")
    print(f"Module {m_repr}", end=" ")

    try:
        spec = importlib.util.find_spec(p)
        if spec is None:
            raise ImportError
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        print("OK")
    except ImportError:
        print("FAIL")
