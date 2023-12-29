class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        half = int(len(s) / 2)
        voewls = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
        first_half = s[:half]
        second_half = s[half:]
        first_half_vovels = 0
        second_half_vovels = 0
        for f_item, s_item in zip(first_half, second_half):
            if f_item in voewls:
                first_half_vovels += 1
            if s_item in voewls:
                second_half_vovels += 1
        return first_half_vovels == second_half_vovels
