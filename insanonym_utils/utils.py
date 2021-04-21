from .models import FileModel, FileConfigModel
from os import path

def readModel(directory, name):
    configFile = FileModel(name=name, path=path.join(directory, name))
    model = FileConfigModel.parse_file(configFile.path)
    return model
