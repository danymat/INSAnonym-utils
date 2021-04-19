from os import path
from ..models import FileConfigModel, FileModel

class FileAsDataframe:

    def __init__(self, file: FileConfigModel):
        file = FileModel(name=file.name, path=path.join(file.path, file.name))

