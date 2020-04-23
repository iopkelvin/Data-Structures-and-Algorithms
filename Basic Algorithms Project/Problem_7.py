'''
Problem 7: Request Routing in a Web Server with a Trie
HTTPRouter using a Trie
For this exercise we are going to implement an HTTPRouter like you would find in a typical web server using the Trie data structure we learned previously.

There are many different implementations of HTTP Routers such as regular expressions or simple string matching, but the Trie is an excellent and very efficient data structure for this purpose.

The purpose of an HTTP Router is to take a URL path like "/", "/about", or "/blog/2019-01-15/my-awesome-blog-post" and figure out what content to return.
In a dynamic web server, the content will often come from a block of code called a handler.

First we need to implement a slightly different Trie than the one we used for autocomplete.
Instead of simple words the Trie will contain a part of the http path at each node, building from the root node /

In addition to a path though, we need to know which function will handle the http request.
In a real router we would probably pass an instance of a class like Python's SimpleHTTPRequestHandler which would be responsible for handling requests to that path.
For the sake of simplicity we will just use a string that we can print out to ensure we got the right handler

We could split the path into letters similar to how we did the autocomplete Trie, but this would result in a Trie with a very large number of nodes and lengthy traversals if we have a lot of pages on our site.
A more sensible way to split things would be on the parts of the path that are separated by slashes ("/").
A Trie with a single path entry of: "/about/me" would look like:

(root, None) -> ("about", None) -> ("me", "About Me handler")

We can also simplify our RouteTrie a bit by excluding the suffixes method and the endOfWord property on RouteTrieNodes.
We really just need to insert and find nodes, and if a RouteTrieNode is not a leaf node, it won't have a handler which is fine.
'''
from collections import defaultdict


# A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class RouteTrieNode:
    def __init__(self, handler=None):
        # Initialize the node with children as before, plus a handler
        self.child = defaultdict(RouteTrieNode)
        self.handler = handler

    def insert(self, path_part):
        # Insert the node as before
        if path_part not in self.child:
            self.child[path_part] = RouteTrieNode()


# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self, handler):
        # Initialize the trie with an root node and a handler, this is the root path or home page node
        self.root = RouteTrieNode(handler)
        self.handler = handler

    def insert(self, path_parts, handler):
        # Similar to our previous example you will want to recursively add nodes
        # Make sure you assign the handler to only the leaf (deepest) node of this path
        node = self.root
        for path_part in path_parts:
            node.insert(path_part)
            node = node.child[path_part]
        node.handler = handler

    def find(self, path_parts):
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match
        node = self.root
        for path_part in path_parts:
            if path_part in node.child:
                node = node.child[path_part]
            else:
                return None
        return node.handler
'''
Next we need to implement the actual Router. The router will initialize itself with a RouteTrie for holding routes and associated handlers.
It should also support adding a handler by path and looking up a handler by path. 
All of these operations will be delegated to the RouteTrie.

Hint: the RouteTrie stores handlers under path parts, so remember to split your path around the '/' character
Bonus Points: Add a not found handler to your Router which is returned whenever a path is not found in the Trie.

More Bonus Points: Handle trailing slashes! A request for '/about' or '/about/' are probably looking for the same page. 
Requests for '' or '/' are probably looking for the root handler. Handle these edge cases in your Router.
'''


# The Router class will wrap the Trie and handle
class Router:
    def __init__(self, handler, handler_notfound):
        # Create a new RouteTrie for holding our routes
        # You could also add a handler for 404 page not found responses as well!
        self.routeTrie = RouteTrie(handler)
        self.handler_notfound = handler_notfound

    def add_handler(self, path, handler):
        # Add a handler for a path
        # You will need to split the path and pass the pass parts
        # as a list to the RouteTrie
        path_part = self.split_path(path)
        self.routeTrie.insert(path_part, handler)

    def lookup(self, path):
        # lookup path (by parts) and return the associated handler
        # you can return None if it's not found or
        # return the "not found" handler if you added one
        # bonus points if a path works with and without a trailing slash
        # e.g. /about and /about/ both return the /about handler
        path_parts = self.split_path(path)

        # Shows first handler "root handler"
        if len(path_parts) == 0:
            return self.routeTrie.handler
        handler = self.routeTrie.find(path_parts)
        # Shows handler not found
        if handler is None:
            return self.handler_notfound
        else:
            return handler

    @staticmethod
    def split_path(path):
        # you need to split the path into parts for
        # both the add_handler and lookup functions,
        # so it should be placed in a function here
        path = path.split("/")
        return [element for element in path if element != '']


if __name__ == "__main__":
    '''
    Test Cases
    '''
    # Here are some test cases and expected outputs you can use to test your implementation
    print('Test 1')
    # create the router and add a route
    router = Router("root handler", "not found handler") # remove the 'not found handler' if you did not implement this
    router.add_handler("/home/about", "about handler")  # add a route

    # some lookups with the expected output
    print(router.lookup("/")) # should print 'root handler'
    print(router.lookup("/home")) # should print 'not found handler'
    print(router.lookup("/home/about")) # should print 'about handler'
    print(router.lookup("/home/about/")) # should print 'about handler'
    print(router.lookup("/home/about/me")) # should print 'not found handler'

    # Test 2
    print('\nTest 2')
    router = Router("root handler", "not found handler") # remove the 'not found handler'
    router.add_handler("/home/documents/nanodegree/algorithms", "algorithms handler")  # add a route
    router.add_handler("/home/documents/nanodegree", "nanodegree handler")  # add a route
    router.add_handler("/home/documents", "documents handler")  # add a route

    print(router.lookup("/"))  # should print 'root handler'
    print(router.lookup("/home"))  # should print 'not found handler'
    print(router.lookup("/home/documents"))  # should print 'documents handler'
    print(router.lookup("/home/documents/nanodegree"))  # should print 'nanodegree handler'
    print(router.lookup("/home/documents/nanodegree/algorithms"))  # should print 'algorithms handler'
    print(router.lookup("/home/documents/nanodegree/algorithms/"))  # should print 'algorithms handler'
