list = [] # creating an empty list

for i in range(5):
    list.append(input("Nome: "))  # add item

print(23*"=")
print("Adding")
print(23*"=")

#forloop
for name in list:
    print(name)

print(23*"=")
print("Deleting")
print(23*"=")

nome = input("Nome: ")

for i in range(len(list)):
    if nome in list:
        list.remove(nome)  # delete item at

print(23*"=")
print("After deleting\n")
print(23*"=")

#forloop
for name in list:
    print(name)
