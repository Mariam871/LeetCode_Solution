class TrieNode:
    def __init__(self):
        self.children = {}
        self.prefix_count = 0  # Tracks how many words share this prefix

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            node.prefix_count += 1

    def get_prefix_score(self, word):
        node = self.root
        score = 0
        for char in word:
            node = node.children[char]
            score += node.prefix_count
        return score

class Solution:
    def sumPrefixScores(self, words):
        trie = Trie()
        # First insert all words into the Trie
        for word in words:
            trie.insert(word)

        result = []
        # Then calculate the score for each word based on the Trie
        for word in words:
            score = trie.get_prefix_score(word)
            result.append(score)

        return result
