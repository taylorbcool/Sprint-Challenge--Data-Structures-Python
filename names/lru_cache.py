from doubly_linked_list import DoublyLinkedList, ListNode

class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """
    def __init__(self, limit=10):
        # self.limit can be set with params
        self.limit = limit
        self.size = 0
        self.cache = DoublyLinkedList()
        # self.storage needs to be a dictionary
        self.storage = {}

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    def get(self, key):
        # make sure key exists
        if key not in self.storage:
            return
        
        # find the right node and move it to the front
        current = self.cache.head
        # iterate until the right node is found
        while current.value['key'] != key:
            current = current.next
        # take the right node, move to front
        self.cache.move_to_front(current)

        # return value from node
        return self.storage[key]

    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """
    def set(self, key, value):
        # YOU GOTTA UPDATE CACHE ***AND*** STORAGE DUDE
        # make sure key doesn't already exist
        if key in self.storage:
        # if it does exist, update value
        # do this first to make sure nothing is deleted without reason
            self.get(key)
            self.cache.head.value['value'] = value
            self.storage[key] = value
        # if it doesn't exist, check if cache is full
        else:
            if self.size == self.limit:
                # if full, delete the oldest entry
                del self.storage[self.cache.tail.value['key']]
                self.cache.remove_from_tail()
                # if not full, pass
            # DON'T USE ELSE OR IT Will *EITHER* DELETE *OR* ADD, NOT BOTH
            # add key-value pair to head of list, storage, and increase size
            self.cache.add_to_head({'key': key, 'value': value})
            # set size to length of cache
            self.storage[key] = value
            self.size = len(self.cache)
        
        # printing for test debugging
        # print(self.storage)
