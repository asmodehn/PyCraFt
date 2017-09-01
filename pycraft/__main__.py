
import yaml
import argparse
import pprint


def parse(filename):

    with open(filename, 'r') as f:
        ast = yaml.safe_load(f)

    pprint.pprint(ast)


if __name__ == '__main__':
    parse("interpreter/type.yaml")
    parse("interpreter/intr.yaml")

