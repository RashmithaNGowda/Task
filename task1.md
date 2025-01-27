1.Reads and Parses YAML Files:
The dev.yaml and demo.yaml files are loaded into dev_data and demo_data, respectively.

2.Processes Each Service:
Loops through all services in dev.yaml.
Skips the ui service.
If the service exists in demo.yaml, updates the specified fields (fields_to_update) in demo.yaml using values from dev.yaml.

3.Saves Updates:
Writes the modified demo.yaml data back to disk.

4.Reports Success:
Outputs a message confirming the fields have been updated, excluding the ui service.

prerequisites to install before running: pip install ruamel.yaml