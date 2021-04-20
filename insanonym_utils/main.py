from .config import config
from .models import FileModel, FileConfigModel,Column
from .modules.Dataframe import FileAsDataframe
from pydantic import ValidationError
import argparse
from os import getcwd, path

parser = argparse.ArgumentParser()
parser.add_argument('-d', '--directory', help="specify a different directory to fetch config file", default=getcwd())

args = parser.parse_args()
configFileName = 'parser.cfg' 
try:
    configFile = FileModel(name=configFileName, path=path.join(args.directory, configFileName)  )
    f = open(configFile.path, "r")
    configContent = f.read()
    model = FileConfigModel.parse_raw(configContent)

    df = FileAsDataframe(model)
    df.execute()

except ValidationError as e:
    print(e)



