'''
Blockchain
A Blockchain is a sequential chain of records, similar to a linked list. Each block contains some information and how it is connected related to the other blocks in the chain. Each block contains a cryptographic hash of the previous block, a timestamp, and transaction data. For our blockchain we will be using a SHA-256 hash, the Greenwich Mean Time when the block was created, and text strings as the data.

Use your knowledge of linked lists and hashing to create a blockchain implementation.


We can break the blockchain down into three main parts.

First is the information hash:
'''

import hashlib
from datetime import datetime

'''
We do this for the information we want to store in the block chain such as transaction time, data, and information like the previous chain.

The next main component is the block on the blockchain:
'''
class Block:

    def __init__(self, data, previous_hash):
        self.timestamp = self.get_time()
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash(self.data)
        self.next = None


    def calc_hash(self, hash_str):
        sha = hashlib.sha256()
        hash_str = hash_str.encode('utf-8')
        sha.update(hash_str)
        return sha.hexdigest()

    def get_time(self):
        format = '%H:%M %d/%m/%Y'
        return datetime.now().strftime(format)

'''
Above is an example of attributes you could find in a Block class.

Finally you need to link all of this together in a block chain, which you will be doing by implementing it in a linked list. 
All of this will help you build up to a simple but full blockchain implementation!
'''

# LinkedList BlockChain
class BlockChain:
    def __init__(self):
        self.head = None

    def add_block(self, data):
        if self.head is None:
            self.head = Block(data, 0)

        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            prev_hash = temp.hash
            temp.next = Block(data, prev_hash)
    #     if self.head is None:
    #         self.head = Block(data, 0)
    #         self.last = self.head
    #     else:
    #         temp = self.last
    #         self.last = Block(data, temp)
    #         self.last.previous_hash = temp

    def print_blockchain(self):
        if self.head == None:
            print("There is no block!")
            return
        else:
            current = self.head
            index = 0
            print()
            print("......................")
            print(" Printing Blockchain")
            print("......................")
            while current:
                print("Index:", index)
                print("Timestamp:", current.timestamp)
                print("Data:", current.data)
                print("SHA256 Hash:", current.hash)
                print("Previous_Hash:", current.previous_hash)
                print("......................")
                current = current.next
                index += 1
            print("")

if __name__ == "__main__":

    # Test 1
    print("\nTest 1\n")
    blockchain = BlockChain()
    blockchain.add_block("block1 Data")
    blockchain.add_block("block2 Data")
    blockchain.add_block("block3 Data")
    blockchain.print_blockchain()

    # Test 2
    print("\nTest 2\n")
    blockchain = BlockChain()
    blockchain.print_blockchain()

    # Test 3
    print("\nTest 3\n")
    blockchain = BlockChain()
    blockchain.add_block('New Data1')
    blockchain.print_blockchain()