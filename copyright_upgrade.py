import os
import re #regular expressions
def f(args, dn, fnl):
    if dn.startswith(r".\.git"):
        return
    for i in fnl:
        if len(fnl) > 1: 
           l.append(os.path.join(dn, i))

l=[]
os.path.walk(os.path.curdir, f, None)

for i in l:
    try:
        fi = file(i, "r+")
        s = fi.read(1024*110)
        ns=re.sub(r"Riemer, 2016", "Riemer, 2016\r", s)
        fi.seek(0)
        fi.write(ns)
    except IOError as e:
        pass
print "Done " + str(len(l)) + " file(s)"

