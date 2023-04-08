import os
import hcl

class TerraformParser:
    def __init__(self, files):
        if not isinstance(files, list):
            files = [files]
        
        self.files = files

    def validate(self):
        for file in self.files:
            if not os.path.exists(file):
                raise FileNotFoundError(f"File not found: {file}")

            if not file.endswith('.tf'):
                raise ValueError(f"Not a Terraform file: {file}")

            with open(file, 'r') as f:
                try:
                    hcl.load(f)
                except ValueError as e:
                    raise ValueError(f"Invalid Terraform file ({file}): {e}")

