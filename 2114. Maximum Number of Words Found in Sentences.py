class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        length_of_sentences = [len(sentence.split(" ")) for sentence in sentences]
        return max(length_of_sentences)
