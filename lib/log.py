import sys

class Colors:
  BLUE = '\033[94m'
  GREEN = '\033[92m'
  YELLOW = '\033[93m'
  RED = '\033[91m'
  RESET = '\033[0m'
  BOLD = '\033[1m'
  UNDERLINE = '\033[4m'

def cprint(*args, color='', prefix='> '):
  largs = list(args)
  largs[0] = color + prefix + str(largs[0])
  largs[-1] = str(largs[-1]) + Colors.RESET

  print(*largs)

def log(*args):
  cprint(*args, color=Colors.BOLD)

def info(*args):
  cprint(*args, color=Colors.GREEN)

def warn(*args):
  cprint(*args, color=Colors.YELLOW)

def err(*args):
  cprint(*args, color=Colors.RED, prefix='ERR: ')
  exit(1)
