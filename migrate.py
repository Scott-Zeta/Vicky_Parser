from typing import List

arable_resources_list:List[str] = [
    # Agriculture
    "bg_rye_farms", "bg_wheat_farms", "bg_rice_farms", 
    "bg_maize_farms", "bg_millet_farms", "bg_vineyard_plantations",
    # Ranching
    "bg_livestock_ranches",
    #custmised ranching
    "bg_cattle_ranches", "bg_sheep_ranches"
    # Plantation
    "bg_coffee_plantations", "bg_cotton_plantations", "bg_silk_plantations",
    "bg_dye_plantations", "bg_opium_plantations", "bg_tea_plantations",
    "bg_tobacco_plantations", "bg_sugar_plantations", "bg_banana_plantations"
    ]

def migrate(historical_data, vanilla_data):
    modified_data = vanilla_data
    # iterate the entire historacal_data, key -> state, value -> detail
    for k,v in historical_data.items():
        print(f"Processing {k}")
        if(modified_data[k]):
            #initial new capped_resources, arable_resources, arable_land for modfied_data
            mod_capped_resources = {}
            mod_arable_resources = []
            mod_arable_land = 0
            #iterate the capped_resources in historical_data
            for resource,number in historical_data[k]['capped_resources'].items():
                print(resource)
    return modified_data