from typing import List, Literal, Union
from numpy import NaN
from pydantic import BaseModel, DirectoryPath, FilePath, Field


class Column(BaseModel):
    name: str
    column_type: Literal['int', 'str', 'datetime'] 
    
class FileModel(BaseModel):
    name: str
    path: FilePath

class DeleteOptions(BaseModel):
    columns: List[int]
    alias: str = NaN

class DeleteAlgorithm(BaseModel):
    name: Literal['delete']
    options: DeleteOptions

class Exporter(BaseModel):
    output_name: str
    output_format: Literal['csv', 'json']
    
class FileConfigModel(BaseModel):
    name: str
    path: DirectoryPath
    columns: List[Column] = Field(..., description= "Columns of submitted file")
    columns_delimiter: Literal['\t', '\n'] = '\t'
    algorithms: List[Union[DeleteAlgorithm]]
    file_type: Literal['csv', 'json']
    export: bool = True
    export_rules: Exporter

