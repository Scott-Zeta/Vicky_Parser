from pathlib import Path
from dirIterator import FileIterator
from token_parser import getData
import json

historical_path = Path('./historical_resource')
vanilla_path = Path('./vanilla_resource')
output_path = Path('./Output/map_data/state_regions')

def main():
    vanilla_Iterator = FileIterator(vanilla_path, ['.txt'])
    historical_Iterator = FileIterator(historical_path, ['.txt'])
    vanilla_data = vanilla_Iterator.iterate_files(getData)
    historical_data = historical_Iterator.iterate_files(getData)
    for k,v in vanilla_data.items():
        file_path = output_path / f"{k}"
        with file_path.open('w') as file:
            json.dump(v, file, indent=4)
          
if __name__ == "__main__":
    main()