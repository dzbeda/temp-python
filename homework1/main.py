### How to run me :  YAML_OUTPUT_PATH=dudu.json python3 main.py people.json age_ranges.json
import json
import os
import argparse
import yaml
from re import L
import sys

yaml_output_path = os.environ.get("YAML_OUTPUT_PATH")
#yaml_output_path = 'output.yml'
print(yaml_output_path)

#people_file_path = 'people.json'
people_file_path = sys.argv[1]
print(f'people file path is : {people_file_path}')

#age_range_file_path = 'age_ranges.json'
age_range_file_path = sys.argv[2]
print(f'age_ranges file path is : {age_range_file_path}')

def run(people_file_path, age_range_file_path):
    with open(people_file_path) as people_list:
        list_of_people_name = json.load(people_list).get('people')
        max_age = max(list_of_people_name, key=lambda x: x['age'])

    with open(age_range_file_path) as age_range_list:
        age_ranges = json.load(age_range_list).get("ranges")
        age_ranges.insert(0, 0)
        age_ranges.append(max_age['age'])
        main_output = {}
        for i in range(len(age_ranges) - 1):
            partial_range = range(age_ranges[i], age_ranges[i + 1])
            matched_name_based_on_age = {}
            for name in list_of_people_name:
                if name['age'] in partial_range:
                    matched_name_based_on_age[name['name']] = name['age']
                else:
                    continue
            sort_matched_name_based_on_age = {k: v for k, v in sorted(matched_name_based_on_age.items(), key=lambda item: item[1])}
            main_output[f'{age_ranges[i]}-{age_ranges[i + 1]}'] = sort_matched_name_based_on_age
        print(main_output)
        with open(yaml_output_path, 'w') as yaml_output:
               yaml.dump(main_output, yaml_output, sort_keys=False, explicit_start=True)


if __name__ == '__main__':
    run(people_file_path, age_range_file_path)
