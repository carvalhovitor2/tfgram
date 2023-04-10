import os
import hcl2

class TerraformParser:
    def __init__(self, files):
        if not isinstance(files, list):
            files = [files]
        
        self.files = files

    def _validate(self):
        for file in self.files:
            if not os.path.exists(file):
                raise FileNotFoundError(f"File not found: {file}")

            if not file.endswith('.tf'):
                raise ValueError(f"Not a Terraform file: {file}")

            with open(file, 'r') as f:
                try:
                    hcl2.load(f)
                except ValueError as e:
                    raise ValueError(f"Invalid Terraform file ({file}): {e}")

    def parse(self):
        self._validate()
        parsed_files = {}
        for file in self.files:
            with open(file, 'r') as f:
                parsed_file = hcl2.load(f)
            parsed_files[file] = parsed_file
        return parsed_files
