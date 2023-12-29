class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        new_words = []
        for word in words:
            new_words.extend(word.split(separator))
        final_words = []
        for w in new_words:
            if w != "":
                final_words.append(w)
        return final_words
