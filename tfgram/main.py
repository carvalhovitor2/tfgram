from source.modules.argparser import parse_arguments
from source.modules.terraform import TerraformParser

def main():
    args = parse_arguments()
    terraform_parser = TerraformParser(args.files)
    terraform_parser.validate()

if __name__ == "__main__":
    main()
