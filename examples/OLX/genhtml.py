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
def cli(file_name):
    print(gen(file_name))


def gen(file_name):
    """Read and parse the YAML file containing the question"""
    try:
        f = open(file_name)
        question = yaml.safe_load(f)
        f.close()
    except Exception as e:
        raise e

    p = Path(file_name)

    # Create a list of tuples like (choice, True or False)
    choice_list = [
        (choice_value, truth_value)
        for truth_value in question['choices']
        for choice_value in question['choices'][truth_value]
    ]

    doc, tag, text = Doc().tagtext()

    with tag('h1'):
        text('Question - %s' % file_name)
    with tag('div'):
        text(question['label'])
    if question['figures']:
        with tag('div', id='photo-container'):
            for fig in question['figures']:
                # FIXME: It's a bad hack to just use the source path
                # for the figures, the html and figures should be
                # copied into an output directory
                figure_path = p.parent.joinpath(fig)
                doc.stag('img', src=str(figure_path), klass='photo', height='400px')
    with tag('div', klass='choices'):
        with tag('ol'):
            for (choice_text, truthiness) in sample(choice_list, k=len(choice_list)):
                with tag('li'):
                    if truthiness:
                        text(str(choice_text) + " - (CORRECT CHOICE)")
                    else:
                        text(str(choice_text))

    return indent(doc.getvalue())


if __name__ == '__main__':
    cli()
