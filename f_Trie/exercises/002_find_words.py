from f_Trie.trie import Trie, TrieNode

"""
You have to implement the find_words() function which will return a sorted list of all the words stored in a trie.
"""


def get_words(root, result, level, word):
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
            get_words(root.children[i], result, level + 1, word)


def find_words(root):
    result = []
    word = [None] * 20  # assuming max level is 20
    get_words(root, result, 0, word)

    return result


if __name__ == '__main__':
    keys = ["the", "a", "there", "answer", "any", "by", "bye", "their", "abc", "abcd"]
    t = Trie()
    for i in range(len(keys)):
        t.insert(keys[i])
    lst = find_words(t.root)
    print(str(lst))
