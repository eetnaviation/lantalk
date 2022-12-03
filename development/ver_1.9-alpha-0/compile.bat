@echo off
pyinstaller --onefile client_1.9-alpha-0.py
pyinstaller --onefile server_1.9-alpha-0.py
del client_1.9-alpha-0.spec
del server_1.9-alpha-0.spec
rmdir /s /q build