import json
dict={}
n=int(input("enter no. of. states:"))
for i in range(n):
    state=input("enter the state name:")
    capital=input("enter the capital name:")
    dict[state]=capital
with open("states.json","a") as f:
    json.dump(dict,f,indent=4)