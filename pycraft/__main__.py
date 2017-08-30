
import yaml
import argparse


def parse(filename):

    with open(filename, 'r') as f:
        ast = yaml.safe_load(f)

    print(ast)


if __name__ == '__main__':
    parse("examples/intr.yaml")

