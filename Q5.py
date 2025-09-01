with open("numbers.txt","r") as f:
        data = f.read()
        count = 0
        
        nums = data.split(",")
        for val in nums:
                if(int(val)%2 ==0):
                        count+=1

print(count)
                
