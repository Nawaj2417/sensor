from pymongo.mongo_client import MongoClient
# from pymongo.server_api import ServerApi
import pandas as pd
import json
uri = "mongodb+srv://broklymaster:broklymaster@cluster0.0oz49su.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
# Create a new client and connect to the server
client = MongoClient(uri)

#create the database name and collection name
DATABASE_NAME = "CODINGGLORY"
COLLECTION_NAME = "waferfault"


#read the data as a dataframe
df = pd.read_csv("C:\Users\hello\Videos\Data science project\Wafer Fault  Detection\notebooks\wafer.csv")
df = df.drop("Unnamed: 0",axis=1)
# convert the data into json
json_record = list(json.loads(df.T.to_json()).values())

#Now dump the data into the database
client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)

