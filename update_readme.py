# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 19:58:33 2020

@author: qtckp
"""


import os
from os import listdir
from os.path import isfile, join, dirname


screen_shots_dir = join(dirname(__file__), 'screenshots')


onlyfiles = [f for f in listdir(screen_shots_dir) if isfile(join(screen_shots_dir, f))]


with open('README.md', 'r', encoding = 'utf8') as f:
    lines = [line for line in f if not line.startswith('!')]


onlyfiles = [f'![1](https://github.com/PasaOpasen/my_FarmTogether_farm/blob/master/screenshots/{file})' for file in onlyfiles]


with open('README.md', 'w', encoding = 'utf8') as f:
    f.write('\n'.join(lines + onlyfiles)+'\n')












