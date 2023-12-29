class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split(" ")
        new_words = []
        for word in words:
            new_word = ""
            for w_idx in range(len(word) - 1, -1, -1):
                new_word += word[w_idx]
            new_words.append(new_word)
        return " ".join(new_words)
