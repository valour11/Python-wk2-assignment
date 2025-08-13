# 1. create an empty list called my_list
my_list = []

# 2. append the following elements to my_list: 10, 20, 30, 40
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

# 3. insert the value 15 at the second position in the list
my_list.insert(1,15)

# 4. extend my_list with another list: [50, 60, 70]
my_list.extend([50, 60, 70])

# 5. remove the last element from my_list
my_list.pop()

# 6. sort my_list in ascending order
my_list.sort()

# 7. find and print the index of the value 30 in my_list
index_of_30 = my_list.index(30)

print(index_of_30)