from pathlib import Path
from dirIterator import FileIterator
from token_parser import getData
from output import stringfy
import math
import json


historical_path = Path('./historical_resource')
vanilla_path = Path('./vanilla_resource')
output_path = Path('./Output/map_data/state_regions')

global_index = 1
argriculture_index = 1
mining_index = 1
sailing_index = 1
gold_index = 1
logging_index = 1
oil_index = 1

arable_resources_list = [
    # Agriculture
    "bg_rye_farms", "bg_wheat_farms", "bg_rice_farms", 
    "bg_maize_farms", "bg_millet_farms", "bg_vineyard_plantations",
    # Ranching
    "bg_livestock_ranches",
    #custmised ranching
    "bg_cattle_ranches", "bg_sheep_ranches",
    # Plantation
    "bg_coffee_plantations", "bg_cotton_plantations", "bg_silk_plantations",
    "bg_dye_plantations", "bg_opium_plantations", "bg_tea_plantations",
    "bg_tobacco_plantations", "bg_sugar_plantations", "bg_banana_plantations"
    ]

mining_resources_list = ["bg_iron_mining", "bg_lead_mining", "bg_coal_mining", "bg_sulfur_mining"]

sailling_resources_list = ["bg_fishing", "bg_whaling"]

gold_resources_list = ["bg_gold_mining", "bg_gold_fields"]

logging_resource_list = ["bg_logging"]

oil_resource_list = ["bg_oil_extraction"]

# scale use to adjust the global total production back to vanilla game setting
scale = {"arable": 0.9, "bg_iron_mining": 2.1, "bg_lead_mining": 1.7, "bg_logging": 0.4, 
         "'bg_oil_extraction'": 0.5, "bg_coal_mining":2.1, "bg_fishing":0.8, "bg_sulfur_mining": 2.1,
         "bg_gold_mining": 0.5, "'bg_rubber'": 1, "bg_whaling": 0.9, "'bg_gold_fields'": 0.4}

def migrate(historical_data, vanilla_data):
    for continent_key,continent_value in historical_data.items():
        for region_key, region_value in continent_value.items():
            # Deal with regular capped_resources
            capped_resources = region_value.get('capped_resources', {})
            mod_capped_resources = {}
            mod_arable_resources = set()
            mod_arable_land = 0
            for resource, amount in capped_resources.items():
                # if the resource belongs to arable_resources_list, 
                # add it to mod_arable_resources follow vanilla game setting
                if resource in arable_resources_list:
                    #deal with two special custmized ranche cases
                    if resource == "bg_cattle_ranches" or resource == "bg_sheep_ranches":
                        resource = "bg_livestock_ranches"
                    mod_arable_resources.add(f"'{resource}'")
                    # the number add to sum of mod_arable_land
                    mod_arable_land += math.ceil(amount * scale.get('arable', 1) * argriculture_index * global_index)
                elif resource in mining_resources_list:
                    mod_capped_resources[resource] = math.ceil(amount * scale.get(resource, 1) * mining_index * global_index)
                elif resource in sailling_resources_list:
                    mod_capped_resources[resource] = math.ceil(amount * scale.get(resource, 1) * sailing_index * global_index)
                elif resource in gold_resources_list:
                    mod_capped_resources[resource] = math.ceil(amount * scale.get(resource, 1) * gold_index * global_index)
                elif resource in logging_resource_list:
                    mod_capped_resources[resource] = math.ceil(amount * scale.get(resource, 1) * logging_index * global_index)
                else:
                    mod_capped_resources[resource] = math.ceil(amount * scale.get(resource, 1) * global_index)
                #assign moded value to modfied_data
            vanilla_data[continent_key][region_key]["capped_resources"] = mod_capped_resources
            vanilla_data[continent_key][region_key]["arable_resources"] = list(mod_arable_resources)
            vanilla_data[continent_key][region_key]["arable_land"] = mod_arable_land
            
            ## Deal with undiscovered resources
            # assign the resources(undiscovered), remove the non-exist resources
            for undiscoverd_key in ["resource", "resource_Dup1", "resource_Dup2", "resource_Dup3"]:
                if undiscoverd_key in region_value:
                    vanilla_data[continent_key][region_key][undiscoverd_key] = region_value[undiscoverd_key]
                    resource = vanilla_data[continent_key][region_key][undiscoverd_key]
                    for num in ['undiscovered_amount', 'discovered_amount']:
                        amount = resource.get(num, 0)
                        if resource['type'] in gold_resources_list:
                            resource[num] = math.ceil(amount * scale.get(resource['type'], 1) * gold_index * global_index)
                        elif resource['type'] in oil_resource_list:
                            resource[num] = math.ceil(amount * scale.get(resource['type'], 1) * oil_index * global_index)
                        else:
                            resource[num] = math.ceil(amount * scale.get(resource['type'], 1) * global_index)
                else:
                    if undiscoverd_key in vanilla_data[continent_key][region_key]:
                        del vanilla_data[continent_key][region_key][undiscoverd_key]
    return vanilla_data

def main():
    vanilla_Iterator = FileIterator(vanilla_path, ['.txt'])
    historical_Iterator = FileIterator(historical_path, ['.txt'])
    vanilla_data = vanilla_Iterator.iterate_files(getData)
    historical_data = historical_Iterator.iterate_files(getData)
    vanilla_data = migrate(historical_data, vanilla_data)
    # print(vanilla_data)
    for k,v in vanilla_data.items():
        file_path = output_path / f"{k}"
        with file_path.open('w') as file:
            s = stringfy(json.dumps(v, indent=4))
            file.write(s)
          
if __name__ == "__main__":
    main()