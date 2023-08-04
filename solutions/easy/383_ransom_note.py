class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mag_dict = {}
        for ch in magazine:
            mag_dict[ch] = mag_dict.get(ch, 0) + 1
        for ch in ransomNote:
            if ch not in mag_dict or mag_dict[ch] == 0:
                return False
            mag_dict[ch] -= 1
        return True
