# INFO408Project

Data to be used: https://www.kaggle.com/datasets/datasnaek/youtube-new?resource=download

To generate the correct data the order to use the programs in is:

csv2json.py (for each csv file)

mergejson.py (then import the data into a MongoDB collection named Videos)

mongo.py (for each JSON file -> be sure to set connection details, then each JSON can be added to their own collection)
