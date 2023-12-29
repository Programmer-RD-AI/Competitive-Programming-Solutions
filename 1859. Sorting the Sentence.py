class Solution:
    def sortSentence(self, s: str) -> str:
        words = s.split(" ")
        new_words = [None] * len(words)
        for word in words:
            last_idx = len(word) - 1
            new_words[int(word[last_idx]) - 1] = word[:last_idx]
        return " ".join(new_words)
