#!/usr/bin/env python3
# PYTHON_ARGCOMPLETE_OK

import os
import sys
import argparse
import argcomplete
from argcomplete.completers import EnvironCompleter

import lib.config
from lib.log import log, err, info

CONF_PATH = os.path.join(os.path.dirname(os.path.realpath(__file__)), './config')

# FXME: hack to avoid making optional positional arguments
if '--completions' in sys.argv:
  info('install argcomplete:')
  print('pip install argcomplete')
  info('run or add this to your ~/.bashrc file:')
  print('eval \"$(register-python-argcomplete %s)\"' % 'dp.py')
  info('or if you you are using pyenv:')
  os.system('echo "eval "\'\"$(\'"$(which register-python-argcomplete) dp.py)"\'"\'')
  exit(0)

def comp_envs(prefix, parsed_args, **kwargs):
  conf_tree = lib.config.init_tree(CONF_PATH)
  return conf_tree.keys()

def task_envs(prefix, parsed_args, **kwargs):
  conf_tree = lib.config.init_tree(CONF_PATH)
  return ('deploy', 'update', 'sync', 'log')

parser = argparse.ArgumentParser(description='Deploy tasks runner')
parser.add_argument('env', metavar='<env>',
                    help='deploy environment').completer = comp_envs
parser.add_argument('task', metavar='<task>',
                    help='deploy task').completer = task_envs
parser.add_argument("-v", "--verbosity", action="store_true",
                    help="increase output verbosity")
parser.add_argument("--completions", action="store_true",
                    help="show commands to enable bash completions")
parser.add_argument("--test", choices=('http', 'http:s', 'ssh', 'rsync', 'wss'))


argcomplete.autocomplete(parser)

args = parser.parse_args()

# log(lib.config.conf_tree)
log(lib.config.conf_tree[args.env])
