""" 
    Title: pytech_insert.py
    Name: Thomas Eagle
    Date: 7/1/2022
    Assignment: 5.3 pytech
"""

""" import statements """
from pymongo import MongoClient

# MongoDB connection string 
url = "mongodb+srv://admin:admin@cluster0.ohpdktx.mongodb.net/?retryWrites=true&w=majority"

# connect to the MongoDB cluster 
client = MongoClient(url)

# connect pytech database
db = client.pytech

""" three student documents"""
# Peter Parker data document 
peter = {
    "student_id": "1007",
    "first_name": "Peter",
    "last_name": "Parker",
    "enrollments": [
        {
            "term": "Session 2",
            "gpa": "4.0",
            "start_date": "July 1, 2022",
            "end_date": "September 1, 2022",
            "courses": [
                {
                    "course_id": "ASM121",
                    "description": "Super Heroics and Teenagers",
                    "instructor": "Professor Reilly",
                    "grade": "A+"
                },
                {
                    "course_id": "USM112",
                    "description": "Secret Identities and You",
                    "instructor": "Professor Watson",
                    "grade": "A+"
                }
             ]
         }
    ]
}

# Bobby Drake's data document 
bobby = {
    "student_id": "1008",
    "first_name": "Bobby",
    "last_name": "Drake",
    "enrollments": [
        {
            "term": "Session 2",
            "gpa": "4.0",
            "start_date": "July 1, 2022",
            "end_date": "September 1, 2022",
            "courses": [
                {
                    "course_id": "ASM121",
                    "description": "Super Heroics and Teenagers",
                    "instructor": "Professor Reilly",
                    "grade": "A+"
                },
                {
                    "course_id": "USM112",
                    "description": "Secret Identities and You",
                    "instructor": "Professor Watson",
                    "grade": "A+"
                }
             ]
         }
    ]
}

# Johnny Storm's data document 
johnny = {
    "student_id": "1007",
    "first_name": "Johnny",
    "last_name": "Storm",
    "enrollments": [
        {
            "term": "Session 2",
            "gpa": "4.0",
            "start_date": "July 1, 2022",
            "end_date": "September 1, 2022",
            "courses": [
                {
                    "course_id": "ASM121",
                    "description": "Super Heroics and Teenagers",
                    "instructor": "Professor Reilly",
                    "grade": "A+"
                },
                {
                    "course_id": "USM112",
                    "description": "Secret Identities and You",
                    "instructor": "Professor Watson",
                    "grade": "A+"
                }
             ]
         }
    ]
}




# get the students collection 
students = db.students

# insert statements with output 
print("\n  -- INSERT STATEMENTS --")
peter_student_id = students.insert_one(peter).inserted_id
print("  Inserted student record Peter Parker into the students collection with document_id " + str(peter_student_id))

bobby_student_id = students.insert_one(bobby).inserted_id
print("  Inserted student record Bobby Drake into the students collection with document_id " + str(bobby_student_id))

johnny_student_id = students.insert_one(johnny).inserted_id
print("  Inserted student record Johnny Storm into the students collection with document_id " + str(johnny_student_id))

input("\n\n  End of program, press any key to exit... ")
