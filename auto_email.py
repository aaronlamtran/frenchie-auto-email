from curses import curs_set
from pydoc import doc
from pymongo import MongoClient
import pymongo
from dotenv import load_dotenv
import os
from operator import attrgetter, itemgetter
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
        _id, name, email, phone, dog, waitlistPosition, createdAt, updatedAt = itemgetter('_id', 'name', 'email', 'phone', 'dog', 'waitlistPosition', 'createdAt', 'updatedAt')(document)
        print(name, email, phone, createdAt)

        # mylist.append(document)
    # tilde = "~" * 30
    print("~" * 30)

    for collection in all_collections:
      print(collection)


if __name__ == "__main__":
    main()

# {'_id': ObjectId('62eaffade9c26e12d5145f64'), 'name': 'Jen Foster', 'email': 'soccerjen2000@hotmail.com', 'phone': '+1 (760) 855-8311', 'dog': ObjectId('6258e5b0e351100c23230d02'), 'waitlistPosition': 40, 'createdAt': datetime.datetime(2022, 8, 3, 23, 7, 25, 133000), 'updatedAt': datetime.datetime(2022, 8, 3, 23, 7, 25, 133000), '__v': 0}
