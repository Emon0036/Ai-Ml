#dictionary (mutable): (key : value)
#------------------------------------


info = {
    "name":"Emon Rahman",
    "sub" : ["DSA" , "DBMS" , "Ai"],
    "score" : ["Ct1-20" , "Ct2-19","Ct3-18"],
    3.1416 : "Pi"
}


# for key , value in info.items():
#     print(f"{key}:{value}")


#method
#-------

#keys-> return all the keys of the dictionary
print(info.keys())

#values-> return all the values

print(info.values())

#items()->print all the value into key value pair

print(info.items())

#get(if I pass the key name then it gives me the value)
print(info.get("name"))

# update -> if I want to add some value into the dictionary then I have to use this 

info.update({"gender" : "Male"})

print(info.items())

print(info.get("sub"))



