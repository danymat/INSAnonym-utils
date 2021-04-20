from typing import List, Literal
from pydantic import BaseModel, DirectoryPath, FilePath, Field


class Column(BaseModel):
    name: str
    column_type: Literal['int', 'str', 'datetime'] 
    
class FileModel(BaseModel):
    name: str
    path: FilePath

class Algorithm(BaseModel):
    name: str
    options: dict
    
class FileConfigModel(BaseModel):
    name: str
    path: DirectoryPath
    columns: List[Column] = Field(..., description= "Columns of submitted file")
    columns_delimiter: Literal['\t', '\n'] = '\t'
    algorithms: List[Algorithm]
    file_type: Literal['csv', 'json']
