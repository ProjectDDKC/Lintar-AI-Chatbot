@echo off

call venv\Scripts\activate
set PYTHONPYCACHEPREFIX=.pycacheglobal
python run.py

pause
