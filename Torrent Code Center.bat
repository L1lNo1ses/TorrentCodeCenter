cd env\Scripts\
call activate.bat
cd .. 
cd ..
python.exe -m pip install --upgrade pip
pip install pyperclip --upgrade
pip install pillow --upgrade
python main.py
pip uninstall pyperclip -y
pip uninstall pillow -y
exit