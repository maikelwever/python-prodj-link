#!/usr/bin/env python3

from setuptools import setup, find_packages
import os

def get_requirements():
  this_folder = os.path.dirname(os.path.abspath(__name__))
  with open(os.path.join(this_folder, 'requirements.txt')) as f:
    return [line.strip() for line in f.readlines() if line.strip()]

setup(
  name="prodj",
  version="0.1.0",
  packages=find_packages(),
  install_requires=get_requirements(),
  entry_points={
    'console_scripts': [
      'midiclock = prodj.bin.midiclock:main',
      'monitor-curses = prodj.bin.monitor_curses:main',
      'monitor-qt = prodj.bin.monitor_qt:main',
      'monitor-simple = prodj.bin.monitor_simple:main',
    ],
  },
  description="Python ProDJ Link scripts",
  license="Apache-2.0",
)
