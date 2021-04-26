Module insanonym_utils.models
=============================

Classes
-------

`Column(**data: Any)`
:   Create a new model by parsing and validating input data from keyword arguments.
    
    Raises ValidationError if the input data cannot be parsed to form a valid model.

    ### Ancestors (in MRO)

    * pydantic.main.BaseModel
    * pydantic.utils.Representation

    ### Class variables

    `column_type: str`
    :

    `name: str`
    :

`CustomAlgorithm(**data: Any)`
:   Create a new model by parsing and validating input data from keyword arguments.
    
    Raises ValidationError if the input data cannot be parsed to form a valid model.

    ### Ancestors (in MRO)

    * pydantic.main.BaseModel
    * pydantic.utils.Representation

    ### Class variables

    `name: str`
    :

    `options: Optional[dict]`
    :

`DeleteAlgorithm(**data: Any)`
:   Create a new model by parsing and validating input data from keyword arguments.
    
    Raises ValidationError if the input data cannot be parsed to form a valid model.

    ### Ancestors (in MRO)

    * pydantic.main.BaseModel
    * pydantic.utils.Representation

    ### Class variables

    `name: Literal['delete']`
    :

    `options: insanonym_utils.models.DeleteOptions`
    :

`DeleteIdAlgorithm(**data: Any)`
:   Create a new model by parsing and validating input data from keyword arguments.
    
    Raises ValidationError if the input data cannot be parsed to form a valid model.

    ### Ancestors (in MRO)

    * pydantic.main.BaseModel
    * pydantic.utils.Representation

    ### Class variables

    `name: Literal['delete_ids']`
    :

    `options: insanonym_utils.models.DeleteIdOptions`
    :

`DeleteIdOptions(**data: Any)`
:   Create a new model by parsing and validating input data from keyword arguments.
    
    Raises ValidationError if the input data cannot be parsed to form a valid model.

    ### Ancestors (in MRO)

    * pydantic.main.BaseModel
    * pydantic.utils.Representation

    ### Class variables

    `alias: str`
    :

    `column: int`
    :

    `ids: List[int]`
    :

`DeleteOptions(**data: Any)`
:   Create a new model by parsing and validating input data from keyword arguments.
    
    Raises ValidationError if the input data cannot be parsed to form a valid model.

    ### Ancestors (in MRO)

    * pydantic.main.BaseModel
    * pydantic.utils.Representation

    ### Class variables

    `alias: str`
    :

    `columns: List[int]`
    :

`Exporter(**data: Any)`
:   Create a new model by parsing and validating input data from keyword arguments.
    
    Raises ValidationError if the input data cannot be parsed to form a valid model.

    ### Ancestors (in MRO)

    * pydantic.main.BaseModel
    * pydantic.utils.Representation

    ### Class variables

    `output_format: Literal['csv', 'json']`
    :

    `output_name: str`
    :

`FileConfigModel(**data: Any)`
:   Create a new model by parsing and validating input data from keyword arguments.
    
    Raises ValidationError if the input data cannot be parsed to form a valid model.

    ### Ancestors (in MRO)

    * pydantic.main.BaseModel
    * pydantic.utils.Representation

    ### Class variables

    `algorithms: List[Union[insanonym_utils.models.DeleteAlgorithm, insanonym_utils.models.DeleteIdAlgorithm, insanonym_utils.models.CustomAlgorithm]]`
    :

    `columns: List[insanonym_utils.models.Column]`
    :

    `columns_delimiter: Literal['\t', '\n']`
    :

    `export: bool`
    :

    `export_rules: insanonym_utils.models.Exporter`
    :

    `file_type: Literal['csv', 'json']`
    :

    `name: str`
    :

    `path: pydantic.types.DirectoryPath`
    :

`FileModel(**data: Any)`
:   Create a new model by parsing and validating input data from keyword arguments.
    
    Raises ValidationError if the input data cannot be parsed to form a valid model.

    ### Ancestors (in MRO)

    * pydantic.main.BaseModel
    * pydantic.utils.Representation

    ### Class variables

    `name: str`
    :

    `path: pydantic.types.FilePath`
    :