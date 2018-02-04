from distutils.core import setup
from py2exe.build_exe import py2exe

setup(
    version = "0.1",
    description = "Buscador de libros a partir de bd local",
    author = "Rolando Morales Perez",
    license = "GNU General Public License (GPL)",
    windows = [{"script": "Index.py"}],
    options = {
        "py2exe": {
            "includes": ["PyQt4.QtCore", "PyQt4.QtGui", "sip", "sqlite3", "urllib"],
            "dll_excludes": ["MSVCP90.dll"]
        }
    }
)