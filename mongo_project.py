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
        return conn
    except pymongo.errors.ConnectionFailure as e:
        print("Somethinngs up buddy: %s") % e

def show_menu():
    #print empty string first to leave a blank line at the top of the menu each time
    print("")
    print("1. Add a Record")
    print("2. Find a Record by Name")
    print("3. Edit a Record")
    print("4. Delete a Record")
    print("5. Exit")

    option = input("Enter option: ")
    return option


#helper function DRY
def get_record():
    print("")
    first = input("Enter Firsst Name > ")
    last = input("Enter Last Name > ")

    try:
        doc = coll.find_one({"first": first.lower(), "last":last.lower()})
    except: 
        print("error accessing the database")
    
    #if no record is found
    if not doc:
        print("")
        print("Error! No results found.")

    return doc


def add_record():
    print("")
    first = input("Enter Firsst Name > ")
    last = input("Enter Last Name > ")
    dob = input("Enter DOB > ")
    gender = input("Enter Gender > ")
    hair_color = input("Enter Hair Color > ")
    occupation = input("Enter Occupation > ")
    nationality = input("Enter Nationality > ")

    new_doc = {
        "first": first.lower(),
        "last": last.lower(),
        "dob": dob,
        "gender": gender.lower(),
        "hair_color": hair_color.lower(),
        "occupation": occupation.lower(),
        "nationality": nationality.lower(),
    }

    try:
        coll.insert(new_doc)
        print("")
        print("Document inserted")
    except:
        print("error accessing the database")


def find_record():
    doc = get_record()
    if doc:
        print("")


def main_loop():
    while True:
        option = show_menu()
        if option == "1":
            add_record()
        elif option == "2":
            print("You have selected option 2")
        elif option == "3":
            print("You have selected option 3")
        elif option == "4":
            print("You have selected option 4")
        elif option == "5":
            conn.close()
            break
        else:
            print("invalid choice")
        print("")


# call function
conn = mongo_connect(MONGO_URI)
coll = conn[DATABASE][COLLECTION]
main_loop()