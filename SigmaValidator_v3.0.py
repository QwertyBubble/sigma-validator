import argparse
import configparser
import Rx
import Check
import yaml
import os

def main():
    parser = argparse.ArgumentParser(description='SIGMA validator v3.0')
    parser.add_argument('-d', '--directory')
    args = parser.parse_args()
    directory = os.fsencode(args.directory)
    rx = Rx.Factory({ "register_core_types": True })

    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        if filename.endswith(".yml") or filename.endswith(".yaml"):
            with open("sigma_schema.yaml", 'r') as schemaFile:
                with open(os.path.join(directory, file), 'r') as file:
                    schema = yaml.safe_load(schemaFile)
                    rules = yaml.safe_load(file)
                    rxSchema = rx.make_schema(schema)
                    semaphore = False #check feed file or separated
                    for v in rules.keys():
                        if 'rules' in v:
                            semaphore = True
                        else:
                            semaphore = False
                    if semaphore: #in case feed, should use for loop because of iteration
                        for rule in rules['rules']:
                            try:
                                if "id" in rule:
                                    id = rule["id"]
                                Check.validate(rule)
                                rxSchema.validate(rule)
                            except Rx.SchemaMismatch as e:
                                print(f"{id}: {e}")
                                # break
                    else: #in case separated, should work with files
                        try:
                            Check.validate(rules)
                            rxSchema.validate(rules)
                        except Rx.SchemaMismatch as e:
                            print(f"Title: {filename}; Error: {e} \n")
                            # break
        else:
            continue

if __name__ == '__main__':
    main()
