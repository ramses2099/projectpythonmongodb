from pymongo import MongoClient
from datetime import datetime
from pprint import pprint
from os import system


def main():
    system("clear")
    try:
        # CONNECTION TO MONGODB WITH PYMONGO
        clinet = MongoClient("mongodb://root:pwd01@localhost:27017/")
        # CONNECT TO DBTEST
        db = clinet["dbtest"]
        # COLLECTION
        posts = db["posts"]

        # post = {
        #     "author": "Mike",
        #     "text": "My first blog post!!!",
        #     "tags": ["mongodb", "python", "pymongo"],
        #     "date": datetime.now(),
        # }

        # post_id = posts.insert_one(post).inserted_id

        # print(f"post id: {post_id}")

        # FIND ALL DOCUMENTS
        # pprint(posts.find_one())

        # # INSERT MANY DOCUMENTS
        # new_posts = [
        #     {
        #         "author": "Mike",
        #         "text": "Another post!!!",
        #         "tags": [],
        #         "date": datetime.now(),
        #     },{
        #         "author": "Eliot",
        #         "title":"Mongodb is fun!!!",
        #         "text": "and pretty easy fun",
        #         "tags": ["mongodb"],
        #         "date": datetime.now(),
        #     }
        # ]
        
        # rs = posts.insert_many(new_posts)
        # print(f"_Id: {rs.inserted_ids}")
        
        # SHOW ALL DOCUMENTS
        # for p in posts.find():
        #     pprint(p)
        
        # COUNT DOCUMENTS
        print(f"count documents {posts.count_documents({})}")

    except Exception as e:
        raise e

    print("Goodbye!!")


if __name__ == "__main__":
    main()
