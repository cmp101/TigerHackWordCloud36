#!/usr/bin/env python
# coding=utf-8

import os
import sys
import commands

for line in sys.stdin:
    (s,o) = commands.getstatusoutput('echo ' + line + '\n' + './fasttext nn ../model/fil9.bin')
    print o


