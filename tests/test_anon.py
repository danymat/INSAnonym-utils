from insanonym_utils.runner import Runner
from insanonym_utils.utils import readModel
from insanonym_utils.models import FileConfigModel, DeleteAlgorithm, DeleteOptions

from os import getcwd
from pandas import isnull

def test_create_dataframe():
    model = readModel(getcwd(), 'parser.cfg')
    df = Runner(model)
    assert df.dataframe.empty == False 

def test_delete_columns():
    model = readModel(getcwd(), 'parser.cfg')
    deleteAlgorithm = DeleteAlgorithm(name='delete', options=DeleteOptions(columns=[1,2]))
    model.algorithms = [ deleteAlgorithm ]
    df = Runner(model)
    df.execute()
    assert isnull(df.dataframe.iloc[:,1]).any()
    assert isnull(df.dataframe.iloc[:,2]).any()
