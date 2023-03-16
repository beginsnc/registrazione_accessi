from datetime import datetime
from distutils.core import setup  # Need this to handle modules

import py2exe
import PySimpleGUI

from module.accessi import Accesso

setup(windows=["new_gui.py"])
