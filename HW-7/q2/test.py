from remove_dups_linked_list import Node, LinkedList
import pytest

def test_linked_list():
    '''
    Unit testing for the linked list implementation found in remove_dups_linked_list.py

    Coverage report can be found in htmlcov/index.html 
    (we have 100% code coverage )
    '''

    linked_list = LinkedList()
    assert linked_list.size() == 0, "Size of empty linked list is not 0, but it should be"
    try: linked_list.print_list()
    except ValueError as error: print("Exception caught when trying to print empty linked list: " + str(error))
    
    linked_list.insert(10)
    assert linked_list.size() == 1, "Size of linked list is not 1, but it should be"
    
    for v in [10,10,12,12,12,11,11,11]: linked_list.insert(v)
    assert linked_list.size() == 9, "Size of linked list is not 9, but it should be"
    
    for v in [10,10,10,12,12,12,11,11,11]: linked_list.insert(v)
    assert linked_list.size() == 18, "Size of linked list is not 18, but it should be"
    
    linked_list.remove_dups()
    print("After removing duplicates, the linked list should be [10,12,11] and it is:")
    linked_list.print_list()
    assert linked_list.size() == 3, "Size of linked list is not 3, but it should be"
    
    linked_list.insert(13)
    linked_list.remove_dups()
    print("After removing duplicates, the linked list should be [10,12,11,13] and it is:")
    linked_list.print_list()
    assert linked_list.size() == 4, "Size of linked list is not 4, but it should be"