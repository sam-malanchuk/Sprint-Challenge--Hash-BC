#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    # Create the hash table
    ht = HashTable(16)

    # add all the weights and their indexs to the hash table
    for index, weight in enumerate(weights):
        hash_table_insert(ht, weight, index)

    # for every index in the hash table
    for i in range(ht.capacity):
        linkedPair = ht.storage[i]
        # if the value is not empty
        if linkedPair is not None:
            # if the value is a linked pair with more than one
            if linkedPair.next is not None:
                first_pair = linkedPair
                while first_pair is not None:
                    # sum minus current values equals value that needs to exist to make sum
                    difference = limit - first_pair.key
                    # grab the pair if exists
                    second_pair = hash_table_retrieve(ht, difference)
                    # if it does exist, then we can return it
                    if second_pair is not None:
                        if first_pair.value > second_pair.value:
                            print(first_pair.value, second_pair.value)
                            return (first_pair.value, second_pair.value)
                        else:
                            print(second_pair.value, first_pair.value)
                            return (second_pair.value, first_pair.value)
                    first_pair = first_pair.next
            # if there is just one in the linkedPair at index
            else:
                first_pair = linkedPair
                # sum minus current values equals value that needs to exist to make sum
                difference = limit - first_pair.key
                # grab the pair if exists
                second_pair = hash_table_retrieve(ht, difference)
                # if it does exist, then we can return it
                if second_pair is not None:
                    if first_pair.value > second_pair.value:
                        print(first_pair.value, second_pair.value)
                        return (first_pair.value, second_pair.value)
                    else:
                        print(second_pair.value, first_pair.value)
                        return (second_pair.value, first_pair.value)

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

# weights_2 = [4, 4]
# answer_2 = get_indices_of_item_weights(weights_2, 2, 8)

# weights_3 = [4, 6, 10, 15, 16]
# answer_3 = get_indices_of_item_weights(weights_3, 5, 21)

# weights_4 = [12, 6, 7, 14, 19, 3, 0, 25, 40]
# answer_4 = get_indices_of_item_weights(weights_4, 9, 7)

# print(answer_2)
# print(answer_3)
# print(answer_4)