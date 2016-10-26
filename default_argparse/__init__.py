import sys
from argparse import ArgumentParser, FileType

parser = ArgumentParser()
parser.add_argument('-l', '--log-file', default = sys.stdout, type = FileType('w'), help = 'Log file')
parser.add_argument('-L', '--log-level', default = 'INFO', choices = ['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'], help = 'Logging level')
parser.add_argument('-F', '--log-format', default = '[%(asctime)s] %(name)s.%(levelname)s: %(message)s', help = 'The logging format')
