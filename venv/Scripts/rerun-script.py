#!C:\Users\1\PycharmProjects\new_fg\venv\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'rerun==1.0.30','console_scripts','rerun'
__requires__ = 'rerun==1.0.30'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('rerun==1.0.30', 'console_scripts', 'rerun')()
    )
