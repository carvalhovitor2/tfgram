from terraform import TerraformParser

class NodeFactory:
    def __init__(self, files):
        if not isinstance(files, list):
            files = [files]

        self.files = files

    def _calculate_dependencies(self):
        


