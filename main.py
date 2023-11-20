from pathlib import Path
from table_parser import *
from stringfyer import *
from migrate import *


historical_path = Path('./historical_resource')
vanilla_path = Path('./vanilla_resource')
output_path = Path('./Output/map_data/state_regions')
    
def migration(fileName = None):
    if fileName == None:
        for file_path in historical_path.iterdir():
            if file_path.is_file():
                try:
                    # Read the raw original table and parse to json data
                    vanillaJson = getJsonData(vanilla_path / file_path.name)
                    historicalJson = getJsonData(file_path)
                    
                    # Start to migrate
                    modifiedJson = migrate(historicalJson,vanillaJson)
                    
                    # output the stringfied data
                    s:str = stringfy(modifiedJson)
                    with open(output_path / file_path.name, 'w') as f:
                        f.write(s)
                except Exception as e:
                    print(f"Error when processing file {file_path.name}: {e}")
    else:
        try:
            # Read the raw original table and parse to json data
            vanillaJson = getJsonData(vanilla_path / fileName)
            historicalJson = getJsonData(historical_path / fileName)
                    
            # Start to migrate
            modifiedJson = migrate(historicalJson,vanillaJson)
                    
            # output the stringfied data
            s:str = stringfy(modifiedJson)
            with open(output_path / fileName, 'w') as f:
                f.write(s)
        except Exception as e:
            print(f"Error when processing file {fileName}: {e}")
                
def main():
    migration("10_india.txt")

if __name__ == "__main__":
    main()