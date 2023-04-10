from source.modules.argparser import parse_arguments
from source.modules.node_factory import NodeFactory

def main():
    args = parse_arguments()
    nodes = NodeFactory(args.files)
    terraform_resources = nodes._calculate_dependencies()

if __name__ == "__main__":
    main()
