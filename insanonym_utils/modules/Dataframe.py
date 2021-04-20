from os import path
from pandas import read_json, read_csv
from numpy import NaN
from ..models import FileConfigModel, FileModel

class FileAsDataframe:

    def __init__(self, file: FileConfigModel):
        _file = FileModel(name=file.name, path=path.join(file.path, file.name))
        self.file = file
        self._verifyRows(_file.path)
        if file.file_type == 'json':
            self._dataframe = read_json(path_or_buf=_file.path, orient='index')
        elif file.file_type == 'csv':
           self._dataframe = read_csv(filepath_or_buffer=_file.path, sep=file.columns_delimiter)
        column_names = list(map(lambda x: x.name, file.columns))
        self._dataframe.columns = column_names

    def _verifyRows(self, file):
        with open(file, 'r') as csv:
            first_line = csv.readline()
        if first_line.count(self.file.columns_delimiter) + 1 != len(self.file.columns):
            raise Exception('Number of columns differ')


    def execute(self):
        for algo in self.file.algorithms:
            if algo.name == "pseudo":
                print(pseudo(self._dataframe, algo.options['columns']))

def pseudo(df, rows):
    """
    Pseudo algorithm that replace each specified row by Nan values
    """
    for row in rows:
        df.iloc[:, row] = NaN

    return df
