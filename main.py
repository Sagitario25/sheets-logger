import sheets
import os
import time
import getpass

if os.path.exists ("doc.txt"):
	key = open ("doc.txt", "r").readline ()
else:
	key = ""

if key == "":
	s = sheets.Sheet ()
else:
	s = sheets.Sheet (key)

s.addLine (time = time.ctime (), username = getpass.getuser ())