class Solution:

    def encode(self, strs: List[str]) -> str:
        word = ""
        for string in strs:
            word += str(len(string))+"#"+string
        return word

    def decode(self, s: str) -> List[str]:
        if s == "None": return []
        i = 0
        wrd = []
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            wrd.append(s[j+1:j+length+1])
            i=j+length+1
        return wrd


            