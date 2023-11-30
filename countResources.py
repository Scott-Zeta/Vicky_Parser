from pathlib import Path
from dirIterator import FileIterator
from token_parser import getData
import json
import pandas as pd

historical_path = Path('./historical_resource')
vanilla_path = Path('./vanilla_resource')
output_path = Path('./Output/map_data/state_regions')

def printFileName(file_path):
    print(file_path.name)

def countResource(data):
    total = {}
    for continent_key,continent_value in data.items():
        for region_key, region_value in continent_value.items():
            # print(f"Processing {continent_key}, {region_key}")
            if 'capped_resources' in region_value:
                # Deal with regular capped resources
                for capped_resourceKey, capped_resourceValue in region_value['capped_resources'].items():
                    if capped_resourceKey in total:
                        total[capped_resourceKey] += capped_resourceValue
                    else:
                        total[capped_resourceKey] = capped_resourceValue
    return total
def main():
    vanilla_Iterator = FileIterator(vanilla_path, ['.txt'])
    historical_Iterator = FileIterator(historical_path, ['.txt'])
    vanilla_data = vanilla_Iterator.iterate_files(getData)
    historical_data = historical_Iterator.iterate_files(getData)
    dic1 = countResource(vanilla_data)
    dic2 = countResource(historical_data)
    df1 = pd.DataFrame(list(dic1.items()), columns=['Category', 'Vanilla'])
    df2 = pd.DataFrame(list(dic2.items()), columns=['Category', 'Historical'])

    # Merging the DataFrames on 'Category'
    merged_df = pd.merge(df1, df2, on='Category', how='outer')

    # Fill missing values with 0
    merged_df.fillna(0, inplace=True)
    merged_df.to_csv('./comparison.csv', index=False)

    # s = json.dumps(vanilla_data['08_middle_east.txt'], indent=4)
    # with open('./out.txt', 'w', encoding='utf-8-sig') as f:
    #     f.write(s)
    # historical_data = historical_Iterator.iterate_files(getData)
    # print(countResource(vanilla_data))
if __name__ == "__main__":
    main()