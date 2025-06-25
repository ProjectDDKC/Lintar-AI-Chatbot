@echo off

call venv\Scripts\activate
set PYTHONPYCACHEPREFIX=.pycacheglobal
start "" pythonw run.py
