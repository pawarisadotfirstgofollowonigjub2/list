#Create a citylist
citylist = ['Bangkok' , 'phuket' , 'seoul' , 'tokyo' , 'chiang Mai']

#Traverse the city
for i in range(len(citylist)):
    print(citylist)

#Append the city
name = input("Add a new city:")
citylist.append(name)

#Delete a city
delete = int(input("which city do you want to delete?: "))
del citylist[delete]

#Print the citylist
print(citylist)