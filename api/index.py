import sys
import os

# Vercel b�ndelt in _vendor/ eine Python-2-uuid.py, die die stdlib �berschattet.
# Wir schieben stdlib-Pfade vor _vendor, damit uuid aus der Standardbibliothek geladen wird.
stdlib = os.path.dirname(os.__file__)
if stdlib in sys.path:
    sys.path.remove(stdlib)
sys.path.insert(0, stdlib)

import uuid
uuid  # suppress unused warning

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import app
