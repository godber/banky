#!/usr/bin/env python
'''
Generates an HTML question from the provided YAML question file.
'''
from pathlib import Path
from random import sample

import click
import yaml
from yattag import Doc, indent


@click.command()
@click.argument('file_name')
def gen(file_name):
    # Read and parse the YAML file containing the question
    try:
        f = open(file_name)
        question = yaml.safe_load(f)
        f.close()
    except Exception as e:
        raise e

    # print(question)

    # Create a list of tuples like (choice, True or False)
    choice_list = [
        (choice_value, truth_value)
        for truth_value in question['choices']
        for choice_value in question['choices'][truth_value]
    ]

    doc, tag, text = Doc().tagtext()

    doc.asis('<!DOCTYPE html>')
    with tag('html'):
        with tag('body'):
            with tag('h1'):
                text('Question')
            with tag('div'):
                text(question['label'])
            if 'figures' in question.keys():
                with tag('div', id='photo-container'):
                    for fig in question['figures']:
                        doc.stag('img', src=fig, klass="photo", height='80px')
            with tag('div', klass='choices'):
                with tag('ol'):
                    for (choice_text, truthiness) in sample(choice_list, k=len(choice_list)):
                        with tag('li', klass='foo'):
                            text(choice_text)



    print(indent(doc.getvalue()))




if __name__ == '__main__':
    gen()
