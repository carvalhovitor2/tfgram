import argparse

def parse_arguments():
    parser = argparse.ArgumentParser(description="Generate diagrams from Terraform files")

    parser.add_argument("-f", "--files", metavar="FILE", nargs="+", help="Terraform files to process")

    args = parser.parse_args()
    return args
