#!/usr/bin/env python

"""Finds all question.yml files and generate a single HTML document for review

./review.py GFAquestions/W1B/ > out.html
"""

import os
from pathlib import Path

import click

from genhtml import gen


@click.command()
@click.argument('dir')
def main(dir):
    for root_dir, dirs, files in os.walk(dir):
        for file in files:
            if file == 'question.yml':
                print(gen(root_dir + "/" + file))


if __name__ == '__main__':
    main()
