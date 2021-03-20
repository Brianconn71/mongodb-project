import os 
import pymongo
#grab hideen variables
if os.path.exists("env.py"):
    import env

MONGO_URI = os.environ.get("MONGO_URI")
DATABASE = "myFirstDB"
COLLECTION = "celebrities"


# connect to the mongo db
def mongo_connect(url):
    try:
        conn = pymongo.MongoClient(url)
        print("Mongo is connected!")
        return conn
    except pymongo.errors.ConnectionFailure as e:
        print("Somethinngs up buddy: %s") % e


# call function
conn = mongo_connect(MONGO_URI)

#print all records
coll = conn[DATABASE][COLLECTION]

#insert new record
# new_doc = {"first":"douglas", "last":"adams", "dob":"11/02/1987", "hair_color":"grey", "occupation":"writer", "nationality":"british"}

# coll.insert(new_doc)

# ultiple inserts
# new_docs = [{
#     "first": "terry",
#     "last":"pratchett",
#     "dob": "28/08/2965",
#     "gender": "m",
#     "hair_color": "bald",
#     "occupation":"writer",
#     "nationality":"british"
# },  {
#     "first": "george",
#     "last":"rr martin",
#     "dob": "28/08/1985",
#     "gender": "m",
#     "hair_color": "white",
#     "occupation":"writer",
#     "nationality":"american"
# }]

# coll.insert_many(new_docs)

# documents = coll.find({"first":"douglas"})

# coll.remove({"first":"douglas"})

coll.update_many({"nationality":"american"}, {"$set": {"hair_color":"ginger"}})
documents = coll.find({"nationality":"american"})

for doc in documents:
    print(doc)
