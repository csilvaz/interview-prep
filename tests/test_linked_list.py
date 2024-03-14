from linked_lists.linked_list import LinkedList

def test_insert_into_empty_list():
    list = LinkedList()
    list.insert_at_beginning(1)

    assert list.to_list() == [1]

def test_insert_into_nonempty_list():
    list = LinkedList()
    list.insert_at_beginning(1)
    list.insert_at_beginning(2)
    list.insert_at_beginning(3)
    assert list.to_list() == [3, 2, 1]

def test_find():
    list = LinkedList()
    list.insert_at_beginning(1)
    list.insert_at_beginning(2)
    list.insert_at_beginning(3)
    
    target = 2
    found_node = list.find(target)
    
    ## Verification
    assert found_node is not None ## Check object is not null
    assert found_node.data == target ## Check that the value is actually correct

    ## Edge Case: Value is not found
    missing_target = 4
    assert list.find(4) is None

    ## Edge Case: Searching an empty list
    empty_list = LinkedList()
    assert empty_list.find(target) is None