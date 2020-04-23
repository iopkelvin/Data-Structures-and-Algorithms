## Problem 1:
## Design:
To find the floor sqrt of a number I first need to check for negative, 0, and 1 values.
Then, I use recursion from (0 to number) and see if the middle-value-squared is equal to the sqrt.
Based on if it is bigger or smaller, I can recurse using only half of the value on every recursion.
## Time Complexity:
O(logn) - This recursion is similar to Binary Search, because on every recursion the number of values is cut in half.
## Space Complexity:
O(logn) - It is dependent on the depth of the recursion O(logn), and the memory complexity of a single call O(1).

##Problem 2:
## Design:
To find the index of the number, whether ordered or unordered, I use a recursive algorithm that continuously splits the array in two.
Each split checks the middle value, else it continues splitting recursively.
If a split doesn't contain the value, it returns -1. In the end, only one split will find the value, and so the returning result is the biggest value among the splits.
## Time complexity:
O(logn) - It is dependent on the binary recursive algorithm. There are two recursive algorithms working alongside.
Therefore it is O(2 * logn).
## Space complexity:
O(n * logn) - depth * breadth
Depth is times of recursion (2*logn = logn)
Breadth is values accounted per recursion. Each recursion is using n values log(n)

## Problem 3:
## Design:
In order to separate the array in two largest arrays, the MergeSort algorithm is used.
The array of numbers is recursively split in smaller pieces, and each small split is sorted and added back.
The result is an array with sorted descending values.
The next step is to separate the sorted array into two large splits.
The way of doing this is by separating by odds and even indexes.
## Time complexity:
O(nlogn) = It is O(nlogn + n)
Even though the arrays are split in half, on each split, the MergeSort algorithm also has to check each value to be sorted.
- O(1), by separating the list by middle indexes
- O(logn), by the recursion that splits the array in halves
- O(n), each recursion has to check each value to sort it.
Also,
- O(n), The is also the next part of the algorithm that loops through the sorted array and it splits it by odd and even indexes.
## Space Complexity:
- O(n), We occupy space equal to the number of values in the array

## Problem 4:
In this problem I am asked to sort a series of values from 0 to 2 through only one traversal.
I over each value in the array, and keep track of every 0 and 2 values. For every 0 value saved, I input the 0 at the beginning of the array.
and the 0 tracker increases by 1. Similarly, for each 2 value found, the 2-tracker increases by one, and the last value gets the value 2 (while at the same time the loop decreases by 1 so that it doesnt go over the last value in the array).
## Time complexity:
O(n) - Since every element in the array is observed (the array is traversed).
## Space complexity:
O(n) - The space complexity is dependent on the size of the array given. The array is sorted in place, but n is dependent on the number of values in the array.

## Problem 5:
## Design
This problem is related to the Trie Data Structure. Every character in a word is a node in the Trie which connects to the following character Node. When the word is completed at the last character Node, a flag 'is_word' is set to True.
The Trie Class creates the main architecture of the Trie, as it inserts words in existing TrieNodes, and searches over the entire Trie for complete words.
The TrieNode class is the actual Node, which is able to insert new character Nodes, or retrieve completed branches following the current TrieNode.
The suffixes method in TrieNode recursively forms strings of completed branches within the TrieNode.
## Time complexity:
* insert and Find: 
O(n) - The insert and find methods on the Trie look for each Node in the Trie and loop through each character in the word. Complexity is based on length of word, linear.
* suffixes:
O(m * n) - It loops through every character in the TrieNode (m), and collect every completed words. (n)
## Space complexity:
* insert:
O(n) - It loops through every word in the list, and it adds every word to the Trie by also adding each character in the word.
At worst, it will loop through every word O(m) times all new words with different needs to add a new TrieNode O(n). It is linear
* suffixes:
O(n) - Suffixes is also O(m * n), where m is the number of possible branches in the NodeTrie.
n is the the extending of sub-branches NodeTries within NodeTries.

## Problem 6:
## Design:
To find the min and max value of the array, I start with the test case of no values in the array. Then, I keep track of min and max variables which at the beginning are the first values in the array.
I loop through the values in the array, and if the value is less than or bigger than the variables saved, then they are switched. This way, the function loops through every value in the array and it checks where that value beats the lowest of highest value.
## Time complexity:
O(n) - Linear because the every value in the array is observed.
## Space complexity:
O(1) - Constant because the space saved (2) variables are switched in place, and they only save one value. O(1 + 1)
There is also the cost of the input array, which is the length of the input array. O(1)

## Problem 7:
## Design:
This problem uses the Trie data structure.
It works by keeping each path from to to end into dictionaries inside dictionaries.
There is also an implementation of handler not found and trailing '/'.
1) The TrieNode serves as a basic Node to hold the path parts and handler.
2) The RouteTrie serves to hold the Trie Dictionary information. It incorporates the insert and look methods.
3) The Router is where we send our inputs which communicates with the RouTrie. The Router also accounts for empty roots, handler not found, and trailing slashes.

## Time complexity:
* insert:
O(n) - Each part of the path is observed and added into the Trie, and there is also a handle for every completed path part.
O(m * n) where m is the length of each part of the path, and n is the number of sub paths that the entire path has.
* find:
O(n) - It is dependent on the length of the entire path. It loops through each part in the path.
## Space complexity:
* insert:
O(n) - There is a new Trie node for each part of the path. Each part of the path is a list of strings of the path separated by '/'.
So the space allocated to insert a path is the number of subpaths.
find:
O(n) - We loop through each subpart of the path until we reach the end, then we have the handler, else, the path is not in the Router.
The space for find is based on the number of sub parts of the path. n, Length of a list of strings.

