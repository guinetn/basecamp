# CONFIG FILES

# Class that corresponds to the "abstract" data in the configuration (parsing logic)

from __future__ import annotations
from typing import List
import attr

@attr.frozen
class Configuration:
    @attr.frozen
    class Files:
            input_dir: str
            output_dir: str
    files: Files
    @attr.frozen
    class Parameters:
            patterns: List[str]
    parameters: Parameters

# function to parse this class out of dictionaries (assumes the configuration will use dashes, not underscores)
def configuration_from_dict(details):
    files = Configuration.Files(
            input_dir=details["files"]["input-dir"],
            output_dir=details["files"]["output-dir"],
    )
    parameters = Configuration.Parameters(
            patterns=details["parameters"]["patterns"]
    )
    return Configuration(
            files=files,
            parameters=parameters,
    )



# JSON

json_config = """
{
    "files": {
            "input-dir": "inputs",
            "output-dir": "outputs"
    },
    "parameters": {
            "patterns": [
                    "*.txt",
                    "*.md"
            ]
    }
}
"""

import json
def configuration_from_json(data):
    parsed = json.loads(data)
    return configuration_from_dict(parsed)

config = configuration_from_json(json_config)
print("input_dir: ", config.files.input_dir)
print("input_dir: ", config.files.output_dir)
print("patterns: ", config.parameters.patterns)
print("Files: ", config.files)
print(config)

# INI

ini_config="""
[files]
input-dir = inputs
output-dir = outputs

[parameters]
patterns = ['*.txt', '*.md']
"""

import configparser
def configuration_from_ini(data):
    parser = configparser.ConfigParser()
    parser.read_string(data)
    return configuration_from_dict(parser)




# YAML -extension of JSON that is designed to be easier to write by hand

yaml_config = """
files:
    input-dir: inputs
    output-dir: outputs
parameters:
    patterns:
    - '*.txt'
    - '*.md'
"""

import io
import yaml
def configuration_from_yaml(data):
    fp = io.StringIO(data)
    parsed = yaml.safe_load(fp)
    return configuration_from_dict(parsed)




# TOML (Tom's Own Markup Language): lightweight alternative to YAML
# The specification is shorter, and it is already popular in some places (for example, Rust's package manager, Cargo, uses it for package configuration).

toml_config = """
[files]
input-dir = "inputs"
output-dir = "outputs"

[parameters]
patterns = [ "*.txt", "*.md",]
"""

import toml
def configuration_from_toml(data):
    parsed = toml.loads(data)
    return configuration_from_dict(parsed)