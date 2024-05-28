from typing import List, Union


class TrieNode:
    def __init__(self, char='root'):
        self.children: Union[List[None], List[TrieNode]] = [None] * 26  # This will store pointers to the children
        self.is_end_word = False  # true if the node represents the end of word
        self.char = char  # To store the value of a particular key


class Trie:
    def __init__(self):
        self.root = TrieNode()  # Root node

    # Function to get the index of character 't'
    @staticmethod
    def get_index(target):
        return ord(target) - ord('a')

    # Function to insert a key in the Trie
    def insert(self, key):
        if key is None:
            return False  # None key

        key = key.lower()  # Keys are stored in lowercase
        current = self.root

        # Iterate over each letter in the key
        # If the letter exists, go down a level
        # Else simply create a TrieNode and go down a level
        for letter in key:
            index = self.get_index(letter)

            if current.children[index] is None:
                current.children[index] = TrieNode(letter)  # noqa
                print(letter, "<--- inserted")

            current = current.children[index]

        current.is_end_word = True
        print("'" + key + "' inserted")

    # Function to search a given key in Trie
    def search(self, key):
        if key is None:
            return False  # None key

        key = key.lower()
        current = self.root

        # Iterate over each letter in the key
        # If the letter doesn't exist, return False
        # If the letter exists, go down a level
        # We will return true only if we reach the leafNode and
        # have traversed the Trie based on the length of the key

        for letter in key:
            index = self.get_index(letter)
            if current.children[index] is None:
                return False
            current = current.children[index]

        if current is not None and current.is_end_word:
            return True

        return False

    # Recursive function to delete given key
    def delete_helper(self, key, current, length, level):
        """
        :param key:
        :param current: start from root
        :param length: key length
        :param level: start from 0
        :return:
        """
        deleted_self = False

        if current is None:
            print("Key does not exist")
            return deleted_self

        # Base Case:
        # We have reached at the node which points
        # to the alphabet at the end of the key
        if level == length:
            # If there are no nodes ahead of this node in
            # this path, then we can delete this node
            print("Level is length, we are at the end")

            if current.children.count(None) == len(current.children):
                print("- Node", current.char, ": has no children, delete it")
                deleted_self = True

            # If there are nodes ahead of current in this path
            # Then we cannot delete current. We simply unmark this as leaf
            else:
                print("- Node", current.char, ": has children, don't delete \
                it")
                current.is_end_word = False
                deleted_self = False
        else:
            index = self.get_index(key[level])
            print('level', level, 'index', index)
            child_node = current.children[index]
            print("current", current.char, 'child_node', child_node.char)
            child_deleted = self.delete_helper(key, child_node, length, level + 1)
            print("Returned from", key[level], "as", child_deleted, 'and current is', current.char)
            if child_deleted:
                # Setting children pointer to None as child is deleted
                print("- Delete link from", current.char, "to", key[level])
                current.children[index] = None
                # If current is a leaf node then
                # current is part of another key
                # So, we cannot delete this node, and it's parent path nodes
                if current.is_end_word:
                    print("- - Don't delete node", current.char, ": word end")
                    deleted_self = False

                # If child_node is deleted and current has more children,
                # then current must be part of another key
                # So, we cannot delete current Node
                elif current.children.count(None) != len(current.children):
                    print("- - Don't delete node", current.char, ": has deleted_self = False")
                # Else we can delete current
                else:
                    print("- - Delete node", current.char, ": has no children")
                    deleted_self = True
            else:
                deleted_self = False

        return deleted_self

    # Function to delete given key from Trie
    def delete(self, key):
        if self.root is None or key is None:
            print("None key or empty trie error")
            return
        self.delete_helper(key, self.root, len(key), 0)
        print("\nDeleting:", key)

    # ---------- 常見問題 ----------
    def total_words(self, root):
        """
        Trie裡面總共出現多少個詞
        :return:
        """
        count = 0
        current = root

        if current.is_end_word is True:
            count += 1

        for child_node in current.children:
            # Check whether base case or not
            if child_node is not None:
                count += self.total_words(current)

        return count

    def find_words_helper(self, root, result, level, word):

        # Leaf denotes end of a word
        if root.is_end_word:
            # current word is stored till the 'level' in the character array
            temp = ""
            for x in range(level):
                temp += word[x]
            result.append(str(temp))

        for i in range(26):
            if root.children[i]:
                # Non-None child, so add that index to the character array
                word[level] = chr(i + ord('a'))  # Add character for the level
                self.find_words_helper(root.children[i], result, level + 1, word)

    def find_all_words(self):
        """
        找出的結果會按照prefix的排序，列出所有的在trie裡面的字
        :return:
        """
        result = []
        current = self.root
        word = [None] * 20  # assuming max level is 20
        self.find_words_helper(current, result, 0, word)

        return result

    def is_formed_by_words(self, key):
        """
        輸入的key是否可以由trie裡面的字構成
        :param key:
        :return:
        """
        current = self.root

        for i in range(len(key)):
            char_of_index = self.get_index(key[i])

            if current.children[char_of_index] is None:
                return False

            if current.children[char_of_index].is_end_word:  # noqa
                return self.search(key[i+1:])

            current = current.children[char_of_index]

        return False


if __name__ == '__main__':
    # Input keys (use only 'a' through 'z')
    keys = ["the", "a", "there", "answer", "any",
            "by", "bye", "their", "abc"]
    res = ["Not present in trie", "Present in trie"]

    t = Trie()
    print("Keys to insert: \n", keys)

    # Construct Trie
    for words in keys:
        t.insert(words)

    # Search for different keys
    print("the --- " + res[1] if t.search("the") else "the --- " + res[0])
    print("these --- " + res[1] if t.search("these") else "these --- " + res[0])
    print("abc --- " + res[1] if t.search("abc") else "abc --- " + res[0])

    # Delete abc
    t.delete("abc")
    print("Deleted key \"abc\" \n")

    print("abc --- " + res[1] if t.search("abc") else "abc --- " + res[0])
