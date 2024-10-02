#NAKALYOWA HADIJAH M24B13/029  B27519
#NUMBER 1
def sum_list(items):
    return sum(items)

items = [1, 2, 3, 4]
print(sum_list(items))  

#NUMBER 2
def multiply_list(items):
    result = 1
    for item in items:
        result *= item
    return result

items = [1, 2, 3, 4]
print(multiply_list(items))  

#NUMBER 3
def max_num_in_list(items):
    return max(items)

items = [1, 2, 3, 4]
print(max_num_in_list(items)) 


#NUMBER 4
def min_num_in_list(items):
    return min(items)
items = [1, 2, 3, 4]
print(min_num_in_list(items))

#NUMBER 7
def remove_duplicates(input_list):
    # Use a set to remove duplicates
    unique_items = list(set(input_list))
    return unique_items

my_list = [1, 2, 2, 3, 4, 4, 5, 6, 6, 7, 8, 8, 9, 9]
print("Original list:", my_list)
print("List after removing duplicates:", remove_duplicates(my_list))

#NUMBER 8
def is_list_empty(input_list):
    # Check if the list is empty
    if not input_list:
        return True
    else:
        return False
    my_list = []
if is_list_empty(my_list):
    print("The list is empty.")
else:
    print("The list is not empty.")
    
#NUMBER 10
def words_longer_than_n(words, n):
    return [word for word in words if len(word) > n]

print(words_longer_than_n(['hello', 'world', 'python', 'is', 'awesome'], 4))


#NUMBER 9
def clone_list(lst):
    return lst.copy()

original_list = [1, 2, 3, 4]
cloned_list = clone_list(original_list)
print(cloned_list) 

#NUMBER 5
def count_special_strings(lst):
    count = 0
    for string in lst:
        if len(string) >= 2 and string[0] == string[-1]:
            count += 1
    return count

# Example usage:
print(count_special_strings(['abc', 'xyz', 'aba', '1221']))  # Output: 2

#NUMBER 6
def sort_by_last_element(tuples):
    return sorted(tuples, key=lambda x: x[-1])

print(sort_by_last_element([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]))

