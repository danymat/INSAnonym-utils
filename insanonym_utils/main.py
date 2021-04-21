from .models import FileModel, FileConfigModel,Column
from .runner import Runner
from .utils import readModel
from pydantic import ValidationError
import argparse
from os import getcwd

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--directory', help="specify a different directory to fetch config file", default=getcwd())
    args = parser.parse_args()

    try: 
        model = readModel(args.directory, 'parser.cfg')
        df = Runner(model)
        df.execute()

    except ValidationError as e:
        print(e)



