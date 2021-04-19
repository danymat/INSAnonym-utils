from typing import List, Literal
from pydantic import BaseModel, DirectoryPath, FilePath, Field


class Row(BaseModel):
    name: str
    row_type: Literal['int', 'str', 'datetime'] 
    
class FileModel(BaseModel):
    name: str
    path: FilePath

class FileConfigModel(BaseModel):
    name: str
    path: DirectoryPath
    rows: List[Row] = Field(..., description= "Rows of submitted file")
    rows_delimiter: Literal['\t', '\n'] = '\t'
