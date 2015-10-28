import sys
from cx_Freeze import setup, Executable

setup(
    name = "Keyboard Challenge",
    version = "0.1",
    description = "Keyboard Challenge Keagsn Smith",
    executables = [Executable("keyboard_app.py", base = "Win32GUI")])