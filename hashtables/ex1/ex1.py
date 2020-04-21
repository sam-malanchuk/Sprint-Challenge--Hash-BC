#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    # Create the hash table
    ht = HashTable(16)

    # go over array
    for index, weight in enumerate(weights):
        # see if the total - current exists in the array already
        x = hash_table_retrieve(ht, limit - weight)
        # if it does then return the current and the one found
        if x is not None:
            return (index, x)
        # if it does not then add the current to the hashtable 
        else:
            hash_table_insert(ht, weight, index)
    # if no match found by the end, return None
    return None

def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")

# Understand: function takes in an array of weights, the length of the array and the weight
# limit for the calculation. Store every value and it's index in the array in the hash table.
# Then pulling out first to last every value from the hash table check if there is a second
# value that can help reach it's sum. When found return the index of the two values.

# weights_2 = [4, 4, 4]
# answer_2 = get_indices_of_item_weights(weights_2, 2, 8)

# weights_3 = [4, 6, 10, 15, 16]
# answer_3 = get_indices_of_item_weights(weights_3, 5, 21)

# weights_4 = [12, 6, 7, 14, 19, 3, 0, 25, 40]
# answer_4 = get_indices_of_item_weights(weights_4, 9, 7)

# print(answer_2)
# print(answer_3)
# print(answer_4)