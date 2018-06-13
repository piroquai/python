t = input("Enter text ")
list1= list(t)
for x in range(len(t)):
   list1[x]=t[len(t)-x-1]
t=''.join(list1)
print("Inverted text: " + t)