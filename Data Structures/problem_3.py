'''
Huffman Coding
A Huffman code is a type of optimal prefix code that is used for compressing data. The Huffman encoding and decoding schema is also lossless, meaning that when compressing the data to make it smaller, there is no loss of information.

The Huffman algorithm works by assigning codes that correspond to the relative frequency of each character for each character. The Huffman code can be of any length and does not require a prefix; therefore, this binary code can be visualized on a binary tree with each encoded character being stored on leafs.

There are many types of pseudocode for this algorithm. At the basic core, it is comprised of building a Huffman tree, encoding the data, and, lastly, decoding the data.

Here is one type of pseudocode for this coding schema:

Take a string and determine the relevant frequencies of the characters.
Build and sort a list of tuples from lowest to highest frequencies.
Build the Huffman Tree by assigning a binary code to each letter, using shorter codes for the more frequent letters. (This is the heart of the Huffman algorithm.)
Trim the Huffman Tree (remove the frequencies from the previously built tree).
Encode the text into its compressed form.
Decode the text from its compressed form.
You then will need to create encoding, decoding, and sizing schemas.

For Example:
'''


import sys
# Heapq is a Python module which provides an implementation of the Min heap.
# It makes use of Binary heap and exposes several functions to implement a priority queue.
import heapq
from collections import Counter

class Node:
    def __init__(self, character, frequency):
        self.char = character
        self.freq = frequency
        self.left = None
        self.right = None
    # Greater than
    def __gt__(self, other):
        if not other:
            return -1
        if not isinstance(other, Node):
            return -1
        return self.freq > other.freq


class HuffmanCoding:

    def encode(self, text):
        if text == str():
            return str(), None
        # Get dictionary with frequency of characters
        frequency_dict = self.frequency_dict(text)
        # Min-Heap with Nodes(key, frequency)
        min_heap = self.min_heap_list(frequency_dict)

        merged_heap = self.merge_nodes(min_heap)

        binary_tree = heapq.heappop(merged_heap)
        codes = self.make_codes(binary_tree)
        encoded_text = self.get_encoded_text(text, codes)
        return encoded_text, binary_tree

    def decode(self, encoded_text, binary_tree):
        decoded_string = str()

        if encoded_text == str():
            return decoded_string

        current_node = binary_tree

        for char in encoded_text:
            if char == str(0):
                current_node = current_node.left
            else:
                current_node = current_node.right
            if current_node.char is not None:
                decoded_string += current_node.char
                current_node = binary_tree
        return decoded_string

    def frequency_dict(self, text):
        '''
        Create Dictionary with Frequency of each character in the text
        :param text: text
        :return: dict = character > frequency
        '''
        counter = Counter()
        for char in text:
            counter[char] += 1
        return counter

    def min_heap_list(self, frequency_dict):
        heap = []
        for key in frequency_dict:
            node = Node(key, frequency_dict[key])
            # Maintain heap structure, insert
            heapq.heappush(heap, node)
        return heap

    def merge_nodes(self, heap):
        if len(heap) == 1:
            # heappop deletes the min node in the heap
            node = heapq.heappop(heap)
            new_node = Node(None, node.freq)
            new_node.left = node
            heapq.heappush(heap, new_node)
        while len(heap) > 1:
            node1 = heapq.heappop(heap)
            node2 = heapq.heappop(heap)

            new_node = Node(None, node1.freq + node2.freq)
            new_node.left = node1
            new_node.right = node2

            heapq.heappush(heap, new_node)
        return heap

    def make_codes(self, binary_tree):
        if binary_tree.left is None and binary_tree.right is None:
            return {binary_tree.char: str(0)}
        return self.make_codes_recursion(binary_tree, str())

    def make_codes_recursion(self, root, current_code):
        codes = dict()

        if root is None:
            return dict()
        if root.char is not None:
            codes[root.char] = current_code

        codes.update(self.make_codes_recursion(root.left, current_code + str(0)))
        codes.update(self.make_codes_recursion(root.right, current_code + str(1)))
        return codes

    def get_encoded_text(self, text, codes):
        encoded_text = str()
        for char in text:
            encoded_text += codes[char]
        return encoded_text


def testing(a_great_sentence):
    '''
    Function for printing the testing results
    :param a_great_sentence: sentence to encode and decode
    :return: printing results
    '''
    huffman_coding = HuffmanCoding()

    print("The size of the data is: {}".format(sys.getsizeof(a_great_sentence)))
    print("The content of the data is: {}".format(a_great_sentence))

    encoded_data, tree = huffman_coding.encode(a_great_sentence)
    print("The size of the encoded data is: {}".format(sys.getsizeof(int(encoded_data, base=2))))
    print("The content of the encoded data is: {}".format(encoded_data))

    decoded_data = huffman_coding.decode(encoded_data, tree)
    print("The size of the decoded data is: {}".format(sys.getsizeof(decoded_data)))
    print("The content of the encoded data is: {}".format(decoded_data))
    # print('\n')
    return


if __name__ == "__main__":

    print("Test 1\nRegular Sentence")
    test_sentence = "The bird is the word"
    testing(test_sentence)

    print("\nTest 2\nSingle Character")
    test_sentence = "k"
    testing(test_sentence)

    print("\nTest 3\nSingle Character Repeated")
    test_sentence = "kkkkk"
    testing(test_sentence)

    print("\nTest 4\nSame Letter, Different Case")
    test_sentence = "cccCCCaaaAAAtttTTT"
    testing(test_sentence)

