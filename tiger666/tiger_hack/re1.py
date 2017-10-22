#!/usr/bin/env python
# coding=utf-8

import re
import os
import sys


p = re.compile(r' ')

for line in sys.stdin:
    print p.split(line)[1],
