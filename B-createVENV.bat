@echo off

python -m pip install virtualenv
python -m virtualenv venv

call venv\Scripts\activate
pip install -r requirements.txt





