from ..models import FileModel, FileConfigModel
from os import path

def readModel(directory, name):
    configFile = FileModel(name=name, path=path.join(directory, name))
    f = open(configFile.path, "r")
    configContent = f.read()
    model = FileConfigModel.parse_raw(configContent)
    return model
