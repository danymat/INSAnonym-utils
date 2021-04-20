from os import path
from pandas import read_json, read_csv
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
            if algo.name == "delete":
                print(pseudo(self._dataframe, algo.options))
            else: raise NotImplementedError

    def save(self):
        if not self.file.export: return
        exporter = self.file.export_rules
        if exporter.output_format == 'csv':
            self._dataframe.to_csv(path_or_buf=exporter.output_name, sep=self.file.columns_delimiter, index=False)
        elif exporter.output_format == 'json':
            self._dataframe.to_json(exporter.output_name, index=False)
        else: raise NotImplementedError


def pseudo(df, options):
    """
    Pseudo algorithm that replace each specified row by Nan values
    """
    for row in options.columns:
        df.iloc[:, row] = options.alias

    return df
