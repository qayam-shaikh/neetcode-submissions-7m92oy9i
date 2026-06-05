class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mag = Counter(magazine)
        ran = Counter(ransomNote)
        for ch in ransomNote:
            if ch not in mag or mag[ch]<ran[ch]:
                return False
        return True