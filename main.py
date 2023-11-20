from table_parser import *
from stringfyer import *

def main():
    # Read the raw original table and parse to json data
    vanillaJson = getJsonData('./vanilla_resource/13_australasia.txt')
    
    # Some modify on the data
    # Test modify
    vanillaJson['STATE_NEW_SOUTH_WALES']["arable_land"] = 500
    vanillaJson['STATE_NEW_SOUTH_WALES']["capped_resources"]["bg_fishing"] = 1
    vanillaJson['STATE_NEW_SOUTH_WALES']["arable_resources"] = vanillaJson['STATE_TASMANIA']["arable_resources"]
    # If Test succuess, NSW should have 500 arable_land, 1 bg_fishing, and arable_resources same as TASMANIA
    
    
    # output the stringfied data
    s:str = stringfy(vanillaJson)
    with open('./Output/map_data/state_regions/13_australasia.txt', 'w') as f:
        f.write(s)

if __name__ == "__main__":
    main()