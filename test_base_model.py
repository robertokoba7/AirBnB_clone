#!/usr/bin/python3
from models.base_model import BaseModel

my_model = BaseModel()
my_model.name = "My First Model"
my_model.my_number = 89
print(my_model)
print("_______________")
sy_model.save()
delMy First ModelMy First ModelMy First Model
print(my_model)
print("_______________")
my_model_json = my_model.to_dict()
print(my_model_json)
print("_______________")
print("JSON of my_model:")
for key in my_model_json.keys():
    print("\t{}: ({}) - {}".format(key, type(my_model_json[key]),\ 
    my_model_json[key]))
