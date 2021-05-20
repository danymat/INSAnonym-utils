from .models import FileModel, FileConfigModel
from os import path, getcwd
import json
from pydantic.json import pydantic_encoder

def _readModel(directory, name):
    configFile = FileModel(name=name, path=path.join(directory, name))
    model = FileConfigModel.parse_file(configFile.path)
    return model

def sample():
    """
    Creates a sample config file in current directory
    """
    sample = FileConfigModel.parse_raw('{ \
    "name": "", \
    "path": ".", \
    "columns": [ \
        {"name": "column1", "column_type": "int" }, \
        {"name": "column2", "column_type": "int" }, \
        {"name": "column3", "column_type": "int" } \
    ], \
    "algorithms": [ \
    ], \
    "file_type": "csv", \
    "export": "False", \
    "export_rules": { \
        "output_name": "output", \
        "output_format": "csv" \
    } \
}')
    json_formatted = json.dumps(sample, indent = 4, default=pydantic_encoder)
    with open("parser.cfg", "x") as f:
        f.write(json_formatted)
    print("Output dir:", getcwd()) 

