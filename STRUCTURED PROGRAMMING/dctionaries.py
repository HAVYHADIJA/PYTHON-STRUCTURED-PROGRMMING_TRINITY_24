#number 2
# Sample dictionary
sample_dict = {0: 10, 1: 20}

# Adding a new key-value pair
sample_dict[2] = 30

print("Updated dictionary:", sample_dict)

#number 1
# Sample dictionary
sample_dict = {0: 10, 1: 20, 2: 30}

# Sorting in ascending order
sorted_asc = dict(sorted(sample_dict.items(), key=lambda item: item[1]))

# Sorting in descending order
sorted_desc = dict(sorted(sample_dict.items(), key=lambda item: item[1], reverse=True))

print("Ascending order:", sorted_asc)
print("Descending order:", sorted_desc)
#NAKALYOWA HADIJAH M24B13/029  B27519
