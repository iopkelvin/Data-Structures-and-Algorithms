'''
Active Directory
In Windows Active Directory, a group can consist of user(s) and group(s) themselves. We can construct this hierarchy as such.
Where User is represented by str representing their ids.
'''
class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name

'''
Write a function that provides an efficient look up of whether the user is in a group.
'''

def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    if group == None:
        return False

    if user in group.get_users():
        return True
    else:
        # Check if there are groups inside the group
        if len(group.get_groups()) == 0:
            return False
        else:
            # Do Recursion on sub groups
            for sub_group in group.get_groups():
                found = is_user_in_group(user, sub_group)
                if found:
                    return True
    return False


if __name__ == "__main__":
    parent = Group("parent")

    child = Group("child")
    sub_child = Group("subchild")
    sub_child_user = "sub_child_user"
    sub_child.add_user(sub_child_user)
    child.add_group(sub_child)
    parent.add_group(child)

    child_2 = Group("child2")
    sub_child_2 = Group("subchild2")
    sub_child_user2 = "child_user_2"
    sub_child_2.add_user(sub_child_user2)
    child_2.add_group(sub_child_2)
    parent.add_group(child_2)

    child_3 = Group("child3")
    child_user3 = "child_user_3"
    child_3.add_user(child_user3)
    parent.add_group(child_3)

    print('child: ', is_user_in_group("child", child)) # False because child is not a file, it is a directory
    print("'': ", is_user_in_group("", child))  # False because there is nothing
    print('sub_child_user: ', is_user_in_group(sub_child_user, parent))  # True
    print('sub_child_user2: ', is_user_in_group(sub_child_user2, parent))  # True
    print('child_user_3: ', is_user_in_group(child_user3, parent)) # True
    print('child2: ', is_user_in_group(child_2, None))  # False because group is None
    print('None: ', is_user_in_group(None, parent))  # False because user is None
