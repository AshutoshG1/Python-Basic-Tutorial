# info = {
#     "key":"value",
#     "name":"Techie Ashutosh",
#     "learning": "coding",
#     "age" : 35,
#     "is_adult" : True,
#     "subjects" : ["python","java","angular"],
#     "topics" : ("dict","set"),
#     12.99 : 94
# }
# print(info)
# print(type(info))
# print(info["name"])

# #Nested Dictionary
# student = {
#     "name" : "Techie Ashutosh",
#     "subjects" : {
#         "phy" : 97,
#         "chem" : 90,
#         "math" : 99
#     }
# }
# print(student)
# print(student["subjects"])
# print(student["subjects"]["phy"])


# dict = {
#     "key":"value",
#     "name":"Techie Ashutosh",
#     "learning": "coding",
#     "age" : 35,
#     "is_adult" : True,
#     "subjects" : ["python","java","angular"],
#     "topics" : ("dict","set"),
#     12.99 : 94
# }
# # print(dict.keys())
# # print(list(dict.keys()))
# # print(len(dict.keys()))
# # print(dict.values())
# # print(list(dict.values()))
# # print(dict.items())
# # print(dict.get("name"))
# # print(dict["name"])
# dict.update({"city":"delhi"})
# print(dict)


# #Set 
# collection = {1,2,3,4,"Hello",4,True, False, None}
# print(collection)
# print(type(collection))
# print(len(collection))

# #Empty set
# collection = set()
# print(type(collection))

# collection = set()
# collection.add(1)
# collection.add(2)
# collection.add(2)
# print(collection)
# collection.add(3)
# collection.remove(2) # here 2 acts as key
# print(collection)
# collection.pop()
# print(collection)
# collection.clear()
# print(collection)

set1 = {1,2,3,4}
set2 = {4,5,6,7}
print(set1.union(set2))
print(set1.intersection(set2))
