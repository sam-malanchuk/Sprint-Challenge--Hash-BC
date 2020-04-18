#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length

    """
    YOUR CODE HERE
    """
    # insert each ticket into the hash table by source airport
    for ticket in tickets:
        hash_table_insert(hashtable, ticket.source, ticket.destination)

    # array to hold the route results
    route_array = []

    # hold the search location (starts with NONE)
    search = "NONE"
    # get the destination for the search location
    ticket = hash_table_retrieve(hashtable, search)
    # check while the destination of the search location is not NONE (final destination)
    while ticket != "NONE":
        # add the next destination to the route array
        ticket = hash_table_retrieve(hashtable, search)
        # if we reach NONE then return the array
        if ticket == "NONE":
            return route_array
        # if we have a valid location, add and update the search term
        else:
            route_array.append(ticket)
        search = ticket

# Understand: Get an array of n amount of ticket objects. Each ticket object has
# a source and destination airport. The location of departure has a source of NONE
# and the final destination has a destination of NONE. Need to add the tickets to a
# hash table and then reconstruct the trip starting with None and ending at None. 