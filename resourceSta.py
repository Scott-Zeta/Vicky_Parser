from pathlib import Path
from dirIterator import FileIterator
from token_parser import getData

historical_path = Path('./historical_resource')
vanilla_path = Path('./vanilla_resource')
output_path = Path('./Output/map_data/state_regions')

def printFileName(file_path):
    print(file_path.name)

def main():
    vanilla_Iterator = FileIterator(vanilla_path, ['.txt'])
    vanilla_Iterator.iterate_files(printFileName)
if __name__ == "__main__":
    main()