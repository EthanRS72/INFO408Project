#Ethan Smith INFO408 Project
#mergejson.py
#Program to take each of the preformatted JSON data for each country and
#merge without duplicates into one JSON file to store as the primary collection in MongoDB

import json

def main():
    #All the files to be merged
    json_files = ['CAvideos.json','DEvideos.json', 'FRvideos.json', 'GBvideos.json', 'INvideos.json',
                'JPvideos.json', 'KRvideos.json', 'MXvideos.json', 'RUvideos.json', 'USvideos.json']
    #create variables to store the new data and a set to store the video ids to check for duplicates
    data = []
    added = set()

    #load each countries data file using utf-8 encoding to preserve non-english characters
    #and merge the data
    for file in json_files:
        with open(file, mode='r', encoding='utf-8') as f:
            dt = json.load(f)

            #if a non-duplicate document is found add it to the data
            for item in dt:
                if item['video_id'] not in added:
                    data.append(item)
                    added.add(item['video_id'])

    #write the merged JSON using utf-8 encoding to preserve non-english characters
    with open('allvideos.json', mode='w', encoding = 'utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

    print("All JSON files merged without duplicates.")

if __name__ == '__main__':
    main()