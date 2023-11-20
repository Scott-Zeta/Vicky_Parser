import copy
from typing import List

arable_resources_list:List[str] = [
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

def migrate(historical_data, vanilla_data):
    modified_data = copy.deepcopy(vanilla_data)
    # iterate the entire historacal_data, key -> state, value -> detail
    for k,v in historical_data.items():
        print(f"Processing {k}")
        if k in modified_data:
            #initial new capped_resources, arable_resources, arable_land for modfied_data
            mod_capped_resources = {}
            mod_arable_resources = set()
            mod_arable_land = 0
            #iterate the capped_resources in historical_data
            for resource,number in historical_data[k]['capped_resources'].items():
                # if the resource belongs to arable_resources_list, 
                # add it to mod_arable_resources follow vanilla game setting
                if resource in arable_resources_list:
                    #deal with two special custmized ranche cases
                    if resource == "bg_cattle_ranches" or resource == "bg_sheep_ranches":
                        resource = "bg_livestock_ranches"
                    mod_arable_resources.add(resource)
                    # the number add to sum of mod_arable_land
                    mod_arable_land += number
                else:
                    # for other resources, add key value pairs to mod_capped_resources
                    mod_capped_resources[resource] = number
            # conver set to list for json output
            mod_arable_resources = list(mod_arable_resources)
            # assign moded value to modfied_data
            modified_data[k]["capped_resources"] = mod_capped_resources
            modified_data[k]["arable_resources"] = mod_arable_resources
            modified_data[k]["arable_land"] = mod_arable_land
    return modified_data