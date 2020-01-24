# Create a list of the BRICS countries
country = [ 
            "Brazil", 
            "Russia", 
            "India", 
            "China", 
            "South Africa"
          ]

"""Create a dictionary of BRICS capitals.
Note that South Africa has 3 capitals. Therefore, we embed a list inside
the dictionary.
"""

capitals = {
    "Brazil": "Brasilia",
    "Russia": "Moscow",
    "India": "New Delhi",
    "China": "Beijing",
    "South Africa": [
                        "Pretoria",
                        "Cape Town",
                        "Bloemfontein"
                    ]
           }

# Print the list and dictionary
print( "country" )
print( "capitals" )
"""
What response did you get?
Why did the list and dictionary contents not print?
Fix the code and run the script again.
"""

print( capitals[["South Africa"][1] )

"""
Why did you get an error for the 2nd capital of South Africa?
Hint: Check the syntax for the index value.
"""

firtsname=input("What is your name?"+space)
Lastname=input("What is your last name?"+space)
Location=input("What is your location?"+space)
Age=input("What is your Age?"+space)

print(Lastname,Location,Age,firtsname)

vlan=1
lan=1
if vlan==lan:
    print("correcto")
else:
    print("incorrecto")



aclNum =int(input("Edad? "))

if aclNum>=1 and aclNum<=99:
    print("This std IP")


elif aclNum>=100 and aclNum<=199:
    print("This extended IP")
else:
    print("not std or extended ip")
    
    
    
    
    
edad =int(input("Edad? "))

if edad<12 and edad>0:
    print("Nino")


elif edad>12 and edad<=18:
    print("adoleceste")
elif edad>18 and edad<=60:
    print("adulto")
else:
    print("adulto mayor")
 
    
edad =int(input("Edad? "))
if edad>=0 and edad<=125:
   
    if edad<12 and edad>0:
        print("Nino")


    elif edad>12 and edad<=18:
        print("adoleceste")
    elif edad>18 and edad<=60:
        print("adulto")
    else:
        print("adulto mayor")
else:
    print("Edad no valida")
    
    
devices=["r1","s1","s2","s3","r3"]
for ix in devices:
   print(ix)    
    
for ix in devices:
    if "r" in ix:
        print(ix)
        
switches=[]
for ij in devices:
    if "s" in ij:
        switches.append(ij)
        print(ij)
    
    
x=int(input("Enter a number to count: "))
y=1

while y<=x:
    print(y)
    y=y+1





x=int(input("Enter a number to count: "))
y=-2

while y<=x:
    print(x-y)
    y=y+2
    
    
x=input("Enter a number to count: ")
x=int(x)
y=1
while True:
    print(y)
    y=y+1
    if y>x:
        break
    
    
    
 while True:
     x=input("Enter a number to count to: ")
     if x=="q" or x=="quit":
         break
    
     x=int(x)
     y=1
     while True:
         print (y)
         y=y+1
         if y>x:
             break

file=open("devices.txt","r")
for item in devices:
    print (item)
file.close()

    
    
file=open("devices.txt","r")
for item in file:
    item=item.strip()
    print (item)
file.close()    
    
    
    
devices=[]

file=open("devices.txt","r")
for item in file:
    item=item.strip()
    print (item)
    devices.append(item)
file.close()   
    
print(devices)
    



    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    