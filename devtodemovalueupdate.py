import yaml

def update_service_values(source_file, target_file):
    try:
        # Load data from the source YAML file
        with open(source_file, 'r') as src:
            source_data = yaml.safe_load(src)

        # Load data from the target YAML file
        with open(target_file, 'r') as tgt:
            target_data = yaml.safe_load(tgt)

        # Check if services.airflow-scheduler exists in both files
        if (
            "services" in source_data and "airflow-scheduler" in source_data["services"]
            and "services" in target_data and "airflow-scheduler" in target_data["services"]
        ):
            # Keys to update
            keys_to_update = [
                "chart_name", "chart_branch", "branch", "commit",
                "registry", "repository", "image_tag", "image_digest"
            ]
            
            # Update only specific keys in target data
            for key in keys_to_update:
                if key in source_data["services"]["airflow-scheduler"]:
                    target_data["services"]["airflow-scheduler"][key] = source_data["services"]["airflow-scheduler"][key]

            # Write the updated data back to the target YAML file
            with open(target_file, 'w') as tgt:
                yaml.safe_dump(target_data, tgt, default_flow_style=False)

            print(f"Updated values in {target_file} successfully!")
        else:
            print("The required structure or keys are missing in one or both YAML files.")

    except Exception as e:
        print(f"An error occurred: {e}")

# Input file paths
source_yaml = "dev.yaml"  # Replace with the path to your dev.yaml file
target_yaml = "demo.yaml"  # Replace with the path to your demo.yaml file

# Call the update function
update_service_values(source_yaml, target_yaml)
