from os import path
from pandas import read_json
from ..models import FileConfigModel, FileModel

class FileAsDataframe:

    def __init__(self, file: FileConfigModel):
        _file = FileModel(name=file.name, path=path.join(file.path, file.name))
        self._dataframe = read_json(path_or_buf=_file.path)
        print(self._dataframe)


