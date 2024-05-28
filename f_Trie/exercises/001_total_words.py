from f_Trie.trie import Trie

"""
Implement the total_words() function which will find the total number of words in a trie.
"""


def total_words(root):
    """
    For a trie with n number of nodes, the algorithm runs in O(n) because each node has to be traversed
    :param root:
    :return:
    """
    result = 0
    print('before adding', result)
    # Leaf denotes end of a word
    if root.is_end_word:
        result += 1

    print('after adding', result)

    for i, letter in enumerate(root.children):
        mapping = letter.char if letter else 'Not exist'
        print('root char', root.char, 'current letter', mapping,  'mapping char', chr(i+ord('a')))
        if letter is not None:
            result += total_words(letter)
    return result


if __name__ == '__main__':
    keys = ["the", "a", "there", "answer", "any", "by", "bye", "their", "abc"]

    trie = Trie()

    for key in keys:
        trie.insert(key)

    print(total_words(trie.root))
