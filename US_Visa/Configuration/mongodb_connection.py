import sys
from us_visa.Exception import USvisaException
from us_visa.logger import logging
import pymongo
import os
from us_visa.Constants import DATABASE_NAME,MONGODB_URL





class MongoDBClient:
    client = None
    def __init__(self,database_name=DATABASE_NAME):
        try:
            if MongoDBClient.client is None:
                mongo_db_url=os.getenv(MONGODB_URL)
                if mongo_db_url is None:
                    raise Exception(f"enivornment key is not set or does not exist{MONGODB_URL}")
                
                MongoDBClient.client = pymongo.MongoClient(mongo_db_url)
                logging.info("Successfully connected to MongoDB")


        
            self.Client=MongoDBClient.client
            self.database_name=database_name
            self.database = self.Client[database_name]
            
            logging.info("MongoDB connection succesfull")

        except Exception as e:
            raise USvisaException(e,sys)    