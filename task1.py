from ruamel.yaml import YAML

def load_yaml(file_path):
    yaml = YAML()
    with open(file_path, 'r') as file:
        return yaml.load(file)

def save_yaml(data, file_path):
    yaml = YAML()
    with open(file_path, 'w') as file:
        yaml.dump(data, file)

dev_file = 'dev.yaml'
demo_file = 'demo.yaml'

dev_data = load_yaml(dev_file)
demo_data = load_yaml(demo_file)

fields_to_update = [
    "chart_name",
    "chart_branch",
    "branch",
    "commit",
    "registry",
    "repository",
    "image_tag",
    "image_digest",
]

# Update fields for all services except 'ui'
for service, config in dev_data.get('services', {}).items():
    if service != "ui":
        if service in demo_data['services']:
            for field in fields_to_update:
                if field in config:
                    demo_data['services'][service][field] = config[field]

save_yaml(demo_data, demo_file)

print(f"Updated specific fields in {demo_file} from {dev_file}, excluding 'ui'.")
