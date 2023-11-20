from table_parser import *
from stringfyer import *
from migrate import *

def main():
    # Read the raw original table and parse to json data
    vanillaJson = getJsonData('./vanilla_resource/13_australasia.txt')
    historicalJson = getJsonData('./historical_resource/13_australasia.txt')
    
    # Some modify on the data
    modifiedJson = migrate(historicalJson,vanillaJson)
    
    # output the stringfied data
    s:str = stringfy(modifiedJson)
    with open('./Output/map_data/state_regions/13_australasia.txt', 'w') as f:
        f.write(s)

if __name__ == "__main__":
    main()