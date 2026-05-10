class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = []
        word = ""
        for c in s.strip():
            if c!=" ":
                word += c
            else:
                if word:
                    words.append(word)
                    word = ""
        words.append(word)
        return len(words[-1])