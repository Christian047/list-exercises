#  Python program that sums up all the items in a list of 9 items, removes duplicates, and prints the results


my_list = [1, 2, 3, 5, 5, 6, 6, 8, 9]

# we remove duplicates with the help of set function.
my_list2 = list(set(my_list))
print("this is my new list after duplicate has been removed",my_list2)

# Sum up all the items in the list
total_sum = sum(my_list2)

# Print the result
print("The sum of all the items in the list is:", total_sum)