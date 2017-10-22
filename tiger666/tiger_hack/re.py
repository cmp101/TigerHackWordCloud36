#!/usr/bin/env python
# coding=utf-8

import re
import os
import sys


p = re.compile(r' ')

for line in sys.stdin:
    for i in range(15*int(p.split(line)[0])):
        print p.split(line)[1],
