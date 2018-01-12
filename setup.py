"""
 コンソールから
 python setup.py build
 で実行すること
"""
import os
import sys
from cx_Freeze import setup, Executable

os.environ['TCL_LIBRARY'] = "C:\\Users\\利武\\AppData\Local\\Programs\\Python\\Python36\\tcl\\tcl8.6"
os.environ['TK_LIBRARY'] = "C:\\Users\\利武\\AppData\Local\\Programs\\Python\\Python36\\tcl\\tk8.6"

base = None
executables = [
    Executable('main.py', base=base)
]
build_exe_options = {'packages': ['os', 'sys', 'json', 'twitter'],
                     'excludes': [],
                     'includes': ['tkinter']
}
options = {'build_exe': build_exe_options
}

# GUI=有効, CUI=無効 にする
if sys.platform == 'win32':
    base = 'Win32GUI'
elif sys.platform == 'win64':
    base = 'Win64GUI'

# セットアップ
setup(name='SimpleTweet',
      version="1.0",
      description="My application!",
      options=options,
      executables=executables
      )
