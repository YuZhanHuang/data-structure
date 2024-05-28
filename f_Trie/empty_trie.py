class TrieNode:
    def __init__(self, char='root'):
        self.is_end_word = False
        self.char = char
        self.children = [None] * 26


class Trie:
    def __init__(self):
        self.root = TrieNode()

    @staticmethod
    def get_index(key):
        return ord(key) - ord('a')

    def insert(self, key):
        current = self.root
        for letter in key:
            bucket_index = self.get_index(letter)
            if current.children[bucket_index] is None:
                current.children[bucket_index] = TrieNode(letter)  # noqa

            current = current.children[bucket_index]

        current.is_end_word = True

    def search(self, key) -> bool:
        current = self.root
        for letter in key:
            bucket_index = self.get_index(letter)
            if current.children[bucket_index] is None:
                return False
            current = current.children[bucket_index]

        if current and current.is_end_word:
            return True

        return False

    def delete_helper(self, key, current, length, level):
        deleted_self = False

        # Base Case
        if current is None:
            return

        if level == length:
            if current.children.count(None) == len(current.children):
                deleted_self = True
            else:
                current.is_end_word = False
                deleted_self = False
        else:
            bucket_index = self.get_index(key[level])
            child_node = current.children[bucket_index]
            child_deleted = self.delete_helper(key, child_node, len(key), level)

            if child_deleted:
                current.children[bucket_index] = None
                if current.is_end_word:
                    deleted_self = False
                else:
                    deleted_self = True
            else:
                deleted_self = False

        return deleted_self

    def delete(self, key):
        if not self.root or key is None:
            return

        self.delete_helper(key, self.root, len(key), 0)
        print(f'Deleting the word {key}')

    # ------------------------------------------
    def total_words(self):
        ...

    def find_all_words(self):
        ...

    def is_formed_by_words(self):
        ...


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
