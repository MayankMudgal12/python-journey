with open("practice.txt","r") as f:
    data = f.read()
    
new_data = data.find("learning")

print( new_data)
