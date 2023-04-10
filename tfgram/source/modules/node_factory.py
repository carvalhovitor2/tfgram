from source.modules.terraform import TerraformParser

class NodeFactory:
    def __init__(self, files):
        if not isinstance(files, list):
            files = [files]

        self.files = files

    def _calculate_dependencies(self):
        terraform = TerraformParser(self.files)
        terraform_components = terraform.parse()

        nodes = self._filter_supported_components(terraform_components)
        print(nodes)

    def _filter_supported_components(self, terraform_components):
        components = {
            'modules': []
        }
        print(terraform_components)
        for k, v in terraform_components.items():
            if k == 'module':
                for module in v.values():
                    source = module['source']
                    components['modules'].append(source)
            elif isinstance(v, dict) and bool(v):
                nested_components = self._filter_supported_components(v)
                for component_type, component_value in nested_components.items():
                    if component_type not in components:
                        components[component_type] = []
                    components[component_type].extend(component_value)
        return components
    
