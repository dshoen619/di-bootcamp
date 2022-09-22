import json
sampleJson = """{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payable":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""

print(sampleJson[10])

# with open(sampleJson,'r') as file_obj:
#     exercise2=json.load(file_obj)

# print(exercise2.company.employee)
