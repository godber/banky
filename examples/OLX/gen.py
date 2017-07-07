#!/usr/bin/env python
'''
Generates an EdX style XML question from the provided YAML question file.
'''
from pathlib import Path
from random import sample

import click
import yaml
from lxml import etree


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

    problem = etree.Element('problem')
    multiplechoiceresponse = etree.Element('multiplechoiceresponse')
    problem.append(multiplechoiceresponse)

    # Adding the label to multiplechoiceresponse
    label = etree.Element('label')
    label.text = question['label']
    multiplechoiceresponse.append(label)

    # Adding the choicegroup to multiplechoiceresponse
    choicegroup = etree.Element('choicegroup', type='MultipleChoice')
    multiplechoiceresponse.append(choicegroup)  # FIXME: Do I have to move this down?

    # Create a list of tuples like (choice, True or False)
    choice_list = [
        (choice_value, truth_value)
        for truth_value in question['choices']
        for choice_value in question['choices'][truth_value]
    ]
    # Randomize the choice_list using `random.sample` then create the choice
    # elements and add them to choicegroup.  Note that since the truthiness
    # values are boolean True or False, the correct value will be True or False
    # (with first character capitalized), unlike the example EdX XML
    for (choice_text, truthiness) in sample(choice_list, k=len(choice_list)):
        choice = etree.Element("choice", correct=str(truthiness))
        choice.text = choice_text
        choicegroup.append(choice)

    outfile = Path(Path(file_name).stem + '.xml')
    if outfile.exists():
        print('WARNING: File exists, overwriting %s.' % outfile)

    # Write out the XML to a file.
    et = etree.ElementTree(problem)
    et.write(str(outfile), pretty_print=True)



if __name__ == '__main__':
    gen()
