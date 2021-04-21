from insanonym_utils.modules.Dataframe import FileAsDataframe
from insanonym_utils.modules.FileConfig import readModel
from insanonym_utils.models import FileConfigModel, DeleteAlgorithm, DeleteOptions
from os import getcwd
from pandas import isnull

def test_create_dataframe():
    model = readModel(getcwd(), 'parser.cfg')
    df = FileAsDataframe(model)
    assert df._dataframe.empty == False 

def test_delete_columns():
    model = readModel(getcwd(), 'parser.cfg')
    deleteAlgorithm = DeleteAlgorithm(name='delete', options=DeleteOptions(columns=[1,2]))
    model.algorithms = [ deleteAlgorithm ]
    df = FileAsDataframe(model)
    df.execute()
    assert isnull(df._dataframe.iloc[:,1]).any()
