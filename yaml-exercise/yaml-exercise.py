#!/usr/bin/python
# -*- coding:utf-8 -*-

import yaml
import json


yaml_file_name = "name_info.yaml"
json_file_name = "name_info.json"


def load_yaml():
    with open(yaml_file_name, 'r') as yaml_fp:
        yaml_data = yaml.load(yaml_fp)

    if yaml_data is None:
        print("{0} empty or not exist".format(yaml_file_name))
        return
    print("Yaml data:{0}".format(yaml_data))
    print("json data:\n{0}".format(json.dumps(yaml_data, indent=4, ensure_ascii=False)))
    with open(json_file_name, 'w') as json_fp:
        json.dump(yaml_data, json_fp, indent=4, ensure_ascii=False)


def dump_yaml():
    with open(json_file_name, 'r') as json_fp:
        json_data = json.load(json_fp)

    if json_data is None:
        print("{0} empty or not exist".format(json_file_name))
        return
    print("Json data:{0}".format(json_data))
    print("Yaml data:\n{0}".format(yaml.dump(json_data)))
    with open(yaml_file_name, 'w') as yaml_fp:
        yaml.dump(json_data, yaml_fp)


def main():
    load_yaml()
    dump_yaml()

if __name__ == '__main__':
    main()
