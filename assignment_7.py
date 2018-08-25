#DICTIONARIES
#Q-1.
dict={}
for i in range(1,4):
    key = input("Enter key")
    value = input("Enter value")
    dict[key] = value
print(dict)

#Q-2.
dct={}
dct1={}
for i in range(1,3):
    dct1={}
    name = input("Enter name ")
    for j in range(1,3):
              sub=input("enter subject")
              marks=int(input("enter marks"))
              dct1[sub]=marks
    dct[name]=dct1
print(dct)
std=input("enter the student's name whose marks u want to see")
print(dct[std])
