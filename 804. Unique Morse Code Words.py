class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        code_words = [
            ".-",
            "-...",
            "-.-.",
            "-..",
            ".",
            "..-.",
            "--.",
            "....",
            "..",
            ".---",
            "-.-",
            ".-..",
            "--",
            "-.",
            "---",
            ".--.",
            "--.-",
            ".-.",
            "...",
            "-",
            "..-",
            "...-",
            ".--",
            "-..-",
            "-.--",
            "--..",
        ]
        correct_order = list("abcdefghijklmnopqrstuvwxyz")
        count = []
        for word in words:
            word = list(word)
            word_translated = ""
            for letter in word:
                idx = correct_order.index(letter)
                word_translated += code_words[idx]
            if word_translated not in count:
                count.append(word_translated)
        return len(count)
