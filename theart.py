#!/usr/bin/env python

import sys
import re

from lib import parse, Node, build, quit


def main(fpath):
    root = parse(fpath)


if __name__ == '__main__':
    if not len(sys.argv) == 2:
        quit('One and only one parameter -> scenario path')

    main(sys.argv[1])
