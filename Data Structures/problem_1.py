'''
Least Recently Used Cache
We have briefly discussed caching as part of a practice problem while studying hash maps.

The lookup operation (i.e., get()) and put() / set() is supposed to be fast for a cache memory.

While doing the get() operation, if the entry is found in the cache, it is known as a cache hit. If, however, the entry is not found, it is known as a cache miss.

When designing a cache, we also place an upper bound on the size of the cache. If the cache is full and we want to add a new entry to the cache, we use some criteria to remove an element. After removing an element, we use the put() operation to insert the new element. The remove operation should also be fast.

For our first problem, the goal will be to design a data structure known as a Least Recently Used (LRU) cache. An LRU cache is a type of cache in which we remove the least recently used entry when the cache memory reaches its limit. For the current problem, consider both get and set operations as an use operation.

Your job is to use an appropriate data structure(s) to implement the cache.

In case of a cache hit, your get() operation should return the appropriate value.
In case of a cache miss, your get() should return -1.
While putting an element in the cache, your put() / set() operation must insert the element. If the cache is full, you must write code that removes the least recently used entry first and then insert the element.
All operations must take O(1) time.
'''

# OrderedDict is used to add items to the front
from collections import OrderedDict

class LRU_Cache:
    def __init__(self, capacity):
        # Initialize class variables
        self.capacity = capacity
        self.current = 0
        self.cache = OrderedDict()

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent.
        value = self.cache.get(key) or -1  # Dictionary get function
        if value != -1:
            self.cache.pop(key)            # Dictionary pop function
            self.cache[key] = value        # Adds to the End
        return value

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item.
        # If there is no capacity, do nothing
        if self.capacity < 1:
            return
        # If there is no value, place key:value
        entry = self.get(key)
        if entry != -1:
            self.cache[key] = value
            return
        # If there is still space in the cache, increase items occupying cache
        if self.current < self.capacity:
            self.current += 1
        # Otherwise pop last item and add value
        else:
            self.cache.popitem(last = False)
        self.cache[key] = value

    def print_cache(self):
        print(self.cache)

# Test 1
print('Test 1:')
our_cache = LRU_Cache(5)
our_cache.set(1, 1)
# print(our_cache.print_cache())        # [(1, 1)]
our_cache.set(2, 2)
# print(our_cache.print_cache())        # [(1, 1), (2, 2)]
our_cache.set(3, 3)
# print(our_cache.print_cache())        # [(1, 1), (2, 2), (3, 3)]
our_cache.set(4, 4)
# print(our_cache.print_cache())        # [(1, 1), (2, 2), (3, 3), (4, 4)]
print('get: 1 = ', our_cache.get(1))        # returns 1
# print(our_cache.print_cache())        # [(2, 2), (3, 3), (4, 4), (1, 1)]
print('get: 2 = ', our_cache.get(2))        # returns 2
# print(our_cache.print_cache())        # [(3, 3), (4, 4), (1, 1), (2, 2)]
print('get: 9 = ', our_cache.get(9))        # returns -1 because 9 is not present in the cache
# print(our_cache.print_cache())
our_cache.set(5, 5)                     # [(3, 3), (4, 4), (1, 1), (2, 2), (5, 5)]
# print(our_cache.print_cache())
our_cache.set(6, 6)                     # [(4, 4), (1, 1), (2, 2), (5, 5), (6, 6)]
# print(our_cache.print_cache())
print('get: 3 = ', our_cache.get(3))        # returns -1 because the cache reached it's capacity and 3 was the least recently used entry

print('\n')
# Test 2
print('Test 2:')
our_cache = LRU_Cache(5)
# print(our_cache.print_cache())
our_cache.set(1, 1)
# print(our_cache.print_cache())        # [(1, 1)]
our_cache.set(2, 2)
# print(our_cache.print_cache())        # [(1, 1), (2, 2)]
our_cache.set(3, 3)
# print(our_cache.print_cache())        # [(1, 1), (2, 2), (3, 3)]
our_cache.set(4, 4)
# print(our_cache.print_cache())        # [(1, 1), (2, 2), (3, 3), (4, 4)]
print('get: 4 = ', our_cache.get(4))       # returns 4
# print(our_cache.print_cache())        # [(1, 1), (2, 2), (3, 3), (4, 4)] Stays same
print('get: 3 = ', our_cache.get(3))       # returns 3
# print(our_cache.print_cache())        # [(1, 1), (2, 2), (4, 4), (3, 3)]
print('get: 1 = ', our_cache.get(1))       # returns 1
# print(our_cache.print_cache())        # [(2, 2), (3, 3), (4, 4), (1, 1)]
our_cache.set(5, 5)
# print(our_cache.print_cache())        # [(2, 2), (3, 3), (4, 4), (1, 1), (5, 5)]
our_cache.set(6, 6)
# print(our_cache.print_cache())        # [(3, 3), (4, 4), (1, 1), (5, 5), (6, 6)]
print('get: 3 = ', our_cache.get(3))      # returns 3
# print(our_cache.print_cache())        # [(4, 4), (1, 1), (5, 5), (6, 6), (3, 3)]

print('\n')
# Test 3
print('Test 3:')
our_cache = LRU_Cache(1)
our_cache.set(1, 1)
# print(our_cache.print_cache())        # [(1, 1)]
our_cache.set(2, 2);
# print(our_cache.print_cache())        # [(2, 2)]
print('get 1 = ', our_cache.get(1))       # returns -1
# print(our_cache.print_cache())        # [(2, 2)]
print('get 2 = ',our_cache.get(2))        # returns 2
# print(our_cache.print_cache())        # [(2, 2)]