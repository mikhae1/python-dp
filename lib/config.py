import os
import yaml
import glob
import logging

join = os.path.join
from lib.log import log, err, info

conf_tree = {}

def init_tree(conf_path):
  global conf_tree

  for fpath in glob.glob(join(conf_path, '**/*.yml'), recursive=True):
    f = open(fpath, 'r')
    branch = yaml.load(f)
    for key in branch.keys():
      if key in conf_tree:
        err('Error loading "%s": env "%s" is already loaded' %
          (fpath, key))

    conf_tree = {**conf_tree, **branch}

  return conf_tree


