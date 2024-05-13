from os import getenv
from certifi import where
from dotenv import load_dotenv
from MonsterLab import Monster
from pandas import DataFrame
from pymongo import MongoClient

class Database:
    #connects to mongodb
    def __init__(self):
        load_dotenv()
        #normally this string would be placed into the .env file for security reasons but I was force to place it here to fill the database
        client = MongoClient("mongodb+srv://bysire:blackburn200@cluster0.sfeqpsg.mongodb.net/", tlsCAFile=where())["bandersnatch"]
        self.collection = client.get_collection('Name')
    
    #seeds the database with the selected amount of records using monster lab to make the records
    def seed(self, amount=1000):
        if amount == 1:
            record = Monster().to_dict()
            return self.collection.insert_one(record).acknowledged
        if amount > 1:
            records = [Monster().to_dict() for i in range(amount)]
            return self.collection.insert_many(records).acknowledged
    
    #Deletes all documents from the collection, effectively resetting the collection to an empty state. It returns the number of deleted documents.
    def reset(self):
        result = self.collection.delete_many({})
        return result.deleted_count
    
    #count(self) -> int: Returns the total number of documents in the collection.
    def count(self) -> int:
        return self.collection.count_documents({})
    
    #Retrieves all documents from the collection and converts them into a pandas DataFrame.
    def dataframe(self) -> DataFrame:
        cursor = self.collection.find({})
        df = DataFrame(list(cursor))
        return df
    
    #Converts the DataFrame obtained from dataframe() into an HTML table representation.
    def html_table(self) -> str:
        df = self.dataframe()
        html_table = df.to_html(index=False)
        return html_table

if __name__ == "__main__":
    db=Database()
    db.reset()
    db.seed(1000)
    print(db.html_table())