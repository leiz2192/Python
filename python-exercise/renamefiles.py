#!/usr/bin/env python3
# -*- -*- coding:utf-8 -*-

from datetime import datetime

import os

print("OS Name: " + os.name)
print("OS Environ: " + os.environ.get('PATH'))

print("Current path: " + os.path.abspath('.'))

baseDir='F:\迅雷下载'

for f in os.listdir(baseDir):
    print(f.find("exe"))
    print("FileName: %s" % (f))
    fnpos=f.find("exe")
    if fnpos > 0:
        newFileName = os.path.join(baseDir, f)
        print("FileName: %s" % (newFileName))
        # os.rename(os.path.join(baseDir,f), newFileName)
#    f = os.path.join(baseDir, f)
#    fsize = os.path.getsize(f)
#    mtime = datetime.fromtimestamp(os.path.getmtime(f)).strftime('%Y-%m-%d %H:%M')
#    flag = '\\' if os.path.isdir(f) else ''
#    print('%10d  %s  %s%s' % (fsize, mtime, f, flag))
