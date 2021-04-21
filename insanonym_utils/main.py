from .config import config
from .models import FileModel, FileConfigModel,Column
from .modules.Dataframe import FileAsDataframe
from .modules.FileConfig import readModel
from pydantic import ValidationError
import argparse
from os import getcwd

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--directory', help="specify a different directory to fetch config file", default=getcwd())
    args = parser.parse_args()

    try: 
        model = readModel(args.directory, 'parser.cfg')
        df = FileAsDataframe(model)
        df.execute()
        df.save()

    except ValidationError as e:
        print(e)



