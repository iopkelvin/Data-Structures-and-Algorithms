'''
Building a Trie in Python
Before we start let us reiterate the key components of a Trie or Prefix Tree. A trie is a tree-like data structure that stores a dynamic set of strings. Tries are commonly used to facilitate operations like predictive text or autocomplete features on mobile phones or web search.

Before we move into the autocomplete function we need to create a working trie for storing strings. We will create two classes:

A Trie class that contains the root node (empty string)
A TrieNode class that exposes the general functionality of the Trie, like inserting a word or finding the node which represents a prefix.
Give it a try by implementing the TrieNode and Trie classes below!
'''
from collections import defaultdict


# The Trie itself containing the root node and insert/find functions
class Trie:
    def __init__(self):
        # Initialize this Trie (add a root node)
        self.root = TrieNode()

    def insert(self, words):
        # Add a word to the Trie
        node = self.root
        for char in words:
            if char not in node.child:
                node.insert(char)
            node = node.child[char]
        node.is_word = True

    def find(self, prefixes):
        # Find the Trie node that represents this prefix
        node = self.root
        for char in prefixes:
            if char not in node.child:
                return False
            node = node.child[char]
        return node

'''
Finding Suffixes
Now that we have a functioning Trie, we need to add the ability to list suffixes to implement our autocomplete feature.
To do that, we need to implement a new function on the TrieNode object that will return all complete word suffixes that exist below it in the trie.
For example, if our Trie contains the words ["fun", "function", "factory"] and we ask for suffixes from the f node, we would expect to receive ["un", "unction", "actory"] back from node.suffixes().

Using the code you wrote for the TrieNode above, try to add the suffixes function below.
(Hint: recurse down the trie, collecting suffixes as you go.)
'''


class TrieNode:
    def __init__(self):
        # Initialize this node in the Trie
        self.child = defaultdict(TrieNode)
        self.is_word = False

    def insert(self, char):
        # Add a child node in this Trie
        self.child[char] = TrieNode()

    def suffixes(self, suffix=''):
        # Recursive function that collects the suffix for
        # all complete words below this point
        suffixes = []
        for char, node in self.child.items():
            if node.is_word:
                suffixes.append(suffix + char)
            if node.child:
                suffixes.extend(node.suffixes(suffix + char))
        return suffixes


'''
Testing it all out
Run the following code to add some words to your trie and then use the interactive search box to see what your code returns.
'''

MyTrie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym",
    "fun", "function", "factory",
    "trie", "trigger", "trigonometry", "tripod"
]
for word in wordList:
    MyTrie.insert(word)

print('List of words:\n', wordList, '\n')
prefix = MyTrie.find('ant')
print('\tPrefix: ', 'ant')
print(prefix.suffixes())

prefix = MyTrie.find('f')
print('\tpreffix: ', 'f')
print(prefix.suffixes())

prefix = MyTrie.find('tri')
print('\tpreffix: ', 'tri')
print(prefix.suffixes())

## Edge case
## Empty prefix
prefix = MyTrie.find('')
print('\tpreffix: ', '')
print(prefix.suffixes())

## No suffixes
prefix = MyTrie.find('job')
print('\tpreffix: ', 'job')
if prefix:
    print(prefix.suffixes())
else:
    print('Suffixes Not found')
