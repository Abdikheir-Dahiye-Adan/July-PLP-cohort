# creating empty list
my_list = []

# use of append()
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
print(my_list)


# use of insert
my_list.insert(1, 15)
print(my_list)


# use of extend
list2 =[ 50, 60, 70]
my_list.extend(list2)
print("extended list", my_list)


# use remove()
my_list.remove(70)
print(my_list)

# use of sort()
my_list.sort()
print(my_list)

# use of index()
index_of_30 = my_list.index(30)
print(index_of_30)