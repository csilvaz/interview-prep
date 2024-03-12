from linked_lists.linked_list import LinkedList

def test_insert_into_empty_list():
    list = LinkedList()
    list.insert_at_beginning(1)

    assert list.to_list() == [1]