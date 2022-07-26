from curses import curs_set
from pydoc import doc
from pymongo import MongoClient
import pymongo
from dotenv import load_dotenv
import os
load_dotenv()
MONGO_USER = os.getenv('MONGO_USER')
MONGO_PW = os.getenv('MONGO_PW')
CONNECTION_STRING = f"mongodb+srv://{MONGO_USER}:{MONGO_PW}@frenchie-connection-db.nxc9c.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"


def main():
    mylist = []
    cluster = MongoClient(CONNECTION_STRING)
    main_db = cluster.list_database_names()[0]
    frenchie_collection = cluster[main_db]
    all_collections = frenchie_collection.list_collection_names()
    waitlists = frenchie_collection.get_collection('waitlists')
    cursor = waitlists.find({})

    for document in cursor:
      print(document)
      mylist.append(document)
    tilde = "~" * 30
    print(tilde)

    for collection in all_collections:
      print(collection)


if __name__ == "__main__":
    main()