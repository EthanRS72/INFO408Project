#Ethan Smith INFO408 Project
#csv2json.py
#Program to take the CSV data and convert it to JSON format
#Program also makes the required changes to the data to align
#with how I want to store it in MongoDB

import csv
import json
from datetime import datetime

#Function to take a string representing a boolean and convert it to a boolean
def format_boolean(boolean):
    #Case changes between files so convert to a consistent standard
    if boolean.lower() == 'true':
        return True
    return False


def main():
    #Change the code to the country code of the file to be converted
    code = "US"
    #set input and output file names (CSV in, JSON out)
    csv_file = f'{code}videos.csv'
    json_file = f'{code}videos.json'
    #create a list to store the data and a set to store the video ids to check for duplicates
    data = []
    ids = set()

    # Read the CSV file and convert it to a list of dictionaries
    # Use utf-8 encoding to preserve non-english characters
    with open(csv_file, mode='r', newline='', encoding = 'utf-8') as file:
        reader = csv.DictReader(file)
        try:
            #each row represents a document
            for row in reader:
                #indicator to be used to remove the tags key if there are no tags
                rm_key = False
                #duplicate videos exist so don't add them to the data
                if row['video_id'] not in ids:

                    #iterate through each key and format the data as required
                    for key, value in row.items():

                        #convert the numeric values to integers
                        if key in ['category_id', 'views', 'likes', 'dislikes', 'comment_count']:
                            row[key] = int(value)

                        #convert the date and time values to ISO format
                        elif key in ['trending_date', 'publish_time']:
                            if key == 'trending_date':
                                trending_date = datetime.strptime(row["trending_date"], "%y.%d.%m")
                                row["trending_date"] = trending_date.isoformat()    
                            else:
                                publish_time = datetime.strptime(row["publish_time"], "%Y-%m-%dT%H:%M:%S.%fZ")
                                row["publish_time"] = publish_time.isoformat()    

                        #convert the boolean values to booleans
                        elif key in ['comments_disabled', 'ratings_disabled', 'video_error_or_removed']:
                            row[key] = format_boolean(value)

                        #format the tags as a list of strings
                        elif key == 'tags':
                            #if there are no tags set the key to be removed
                            if row[key] == "[none]":
                                rm_key = True
                            else:
                                #otherwise format the tags as a list of strings
                                rm_key = False
                                row[key] = value.split('|')
                                row[key] = [tag.strip('" ') for tag in row[key]] 
                    
                    #if the tags key is to be removed delete it from the document
                    if rm_key == True:
                        del row['tags']
                    
                    #add the document to the data and the video id to the set
                    data.append(row)
                    ids.add(row['video_id'])
        #catch errors that may arise from the encoding of non-english characters
        except UnicodeDecodeError as e:
            print(f"Error decoding data: {e}")

    # Write the data to a JSON file - use utf-8 encoding to preserve non-english characters
    with open(json_file, mode='w', encoding= 'utf-8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

    print(f'CSV file "{csv_file}" has been converted to JSON file "{json_file}".')


main()