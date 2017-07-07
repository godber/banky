#!/usr/bin/env python
'''
Validates a YAML Question File
'''
from sys import exit

import click
import yaml

# All of the required top level keys are listed here
REQUIRED_KEYS = ['label', 'choices']

# The required keys under the choice key, note that these are python boolean
# types.  If the yaml file just contains the bare key true: ... it will be
# parsed as a Boolean.  If the key were in quotes, like 'true': then it would
# be a string and you could use the commented out version
REQUIRED_CHOICE_KEYS = [True, False]
# REQUIRED_CHOICE_KEYS = ['true', 'false']


@click.command()
@click.argument('file_name')
def validate(file_name):
    # Read and parse the YAML file containing the question
    try:
        f = open(file_name)
        question = yaml.safe_load(f)
        f.close()
    except Exception as e:
        raise e

    # The label and choices keys are required
    for key in REQUIRED_KEYS:
        if key not in question.keys():
            print('ERROR: %s is missing the key: %s' % (file_name, key))

    if 'choices' in question.keys():
        # Make sure the question has both true and false choices
        for key in REQUIRED_CHOICE_KEYS:
            if key not in question['choices'].keys():
                print('ERROR: %s is missing %s choices.' % (file_name, key))

        if True in question['choices'].keys():
            if len(question['choices'][True]) != 1:
                print('ERROR: %s must have exactly one true choice.' % file_name)

        if False in question['choices'].keys():
            if len(question['choices'][False]) < 2:
                print('ERROR: %s must have more than one false choice.' % file_name)


if __name__ == '__main__':
    validate()
