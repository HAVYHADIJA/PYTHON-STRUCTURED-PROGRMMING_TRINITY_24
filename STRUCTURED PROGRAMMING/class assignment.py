
#number 1
classnames = ["Joan","Gilbert","Emma","Gabriella"]

i = 0

while i < len(classnames):
    print(classnames[i])
    i +=1


#number 2
districts =["Kampala","Mukono","Jinja","Gulu","Arua","Mbale","Buikwe","Mbarara","Masaka","Busia"]
#modifying the list
districts.append("Kotido")
districts.append("Lira")
districts.append("Bushenyi")
#displaying the size of the list
print("Size of the list", len(districts))

for h in districts:
    print(h)
    
#deleting one district with index 0
districts =["Kampala","Mukono","Jinja","Gulu","Arua","Mbale","Buikwe","Mbarara","Masaka","Busia"]
del districts[0]
print("list after removing element of index 0",districts)

h= 0
for element in districts:
    h = h+1
print("Number of districts is", h)

    
