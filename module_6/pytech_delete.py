""" 
    Title: pytech_delete.py
    Name: Thomas Eagle
    Date: 07/01/2022
    Assignment: Pytech Deleting Docs 6.3
"""

""" import statements """
from pymongo import MongoClient

# MongoDB connection string 
url = "mongodb+srv://admin:admin@cluster0.ohpdktx.mongodb.net/?retryWrites=true&w=majority"

# connect to the MongoDB cluster 
client = MongoClient(url)

# connect pytech database
db = client.pytech

# get the students collection 
students = db.students

# find all students in the collection 
student_list = students.find({})

# display message 
print("\n  -- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")

# loop over the collection and output the results 
for doc in student_list:
    print("  Student ID: " + doc["student_id"] + "\n  First Name: " + doc["first_name"] + "\n  Last Name: " + doc["last_name"] + "\n")

# new student document 
new_student = {
    "student_id": "1010",
    "first_name": "Gwen",
    "last_name": "Stacy"
}

# insert the test document into MongoDB atlas 
new_student_id = students.insert_one(new_student).inserted_id

# insert statements with output 
print("\n  -- INSERT STATEMENTS --")
print("  Inserted student record into the students collection with document_id " + str(new_student_id))

# call the find_one() method by student_id 1010
student_new = students.find_one({"student_id": "1010"})

# display the results 
print("\n  -- DISPLAYING STUDENT TEST DOC -- ")
print("  Student ID: " + student_new["student_id"] + "\n  First Name: " + student_new["first_name"] + "\n  Last Name: " + student_new["last_name"] + "\n")

# call the delete_one method to remove the student_test_doc
deleted_new_student = students.delete_one({"student_id": "1010"})

# find all students in the collection 
new_student_list = students.find({})

# display message 
print("\n  -- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")

# loop over the collection and output the results 
for doc in new_student_list:
    print("  Student ID: " + doc["student_id"] + "\n  First Name: " + doc["first_name"] + "\n  Last Name: " + doc["last_name"] + "\n")

# exit message 
input("\n\n  End of program, press any key to continue...")
