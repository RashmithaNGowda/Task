# YAML File Update Script

## Overview
This script reads and parses YAML files (`dev.yaml` and `demo.yaml`), updates specific fields in `demo.yaml` based on `dev.yaml`, and saves the changes while skipping the `ui` service.

## Functionality
```markdown
1. Reads and Parses YAML Files:
   - The `dev.yaml` and `demo.yaml` files are loaded into `dev_data` and `demo_data`, respectively.

2. Processes Each Service:
   - Loops through all services in `dev.yaml`.
   - Skips the `ui` service.
   - If the service exists in `demo.yaml`, updates the specified fields (`fields_to_update`) in `demo.yaml` using values from `dev.yaml`.

3. Saves Updates:
   - Writes the modified `demo.yaml` data back to disk.

4. Reports Success:
   - Outputs a message confirming the fields have been updated, excluding the `ui` service.
```

## Prerequisites
Before running the script, install the required package:
```sh
pip install ruamel.yaml
```

## Usage
Run the script using Python:
```sh
python update_yaml.py
```

