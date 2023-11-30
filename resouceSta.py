from pathlib import Path
from dirIterator import dirIterator

historical_path = Path('./historical_resource')
vanilla_path = Path('./vanilla_resource')
output_path = Path('./Output/map_data/state_regions')

def printFileName(file_path):
    print(file_path.name)

def main():
    dirIterator(printFileName, vanilla_path)
if __name__ == "__main__":
    main()