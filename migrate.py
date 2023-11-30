from pathlib import Path
from dirIterator import FileIterator
from token_parser import getData
from output import stringfy
import json


historical_path = Path('./historical_resource')
vanilla_path = Path('./vanilla_resource')
output_path = Path('./Output/map_data/state_regions')

global_inded = 1
argriculture_index = 1
mining_index = 1
sailing_index = 1

def migrate(historical_data, vanilla_data):
    for continent_key,continent_value in historical_data.items():
        for region_key, region_value in continent_value.items():
            capped_resources = region_value.get('capped_resources', {})
            for resource, amount in capped_resources.items():
                print(f"{resource} {amount}")
    return vanilla_data

def main():
    vanilla_Iterator = FileIterator(vanilla_path, ['.txt'])
    historical_Iterator = FileIterator(historical_path, ['.txt'])
    vanilla_data = vanilla_Iterator.iterate_files(getData)
    historical_data = historical_Iterator.iterate_files(getData)
    vanilla_data = migrate(historical_data, vanilla_data)
    # for k,v in vanilla_data.items():
    #     file_path = output_path / f"{k}"
    #     with file_path.open('w') as file:
    #         s = stringfy(json.dumps(v, indent=4))
    #         file.write(s)
          
if __name__ == "__main__":
    main()