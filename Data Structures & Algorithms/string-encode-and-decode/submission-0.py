class Solution:

    def encode(self, strs: List[str]) -> str:
        ret = ""
        for word in strs:
            ret += str(len(word))
            ret += '#'
            ret += word
        return ret

    def decode(self, s: str) -> List[str]:
        ret = []
        length = ""
        i = 0
        while i < len(s):
            if s[i] == "#":
                length = int(length)
                ret.append(s[i+1:i+1+length])
                i = i+1+length
                length = ""
            else:
                length += s[i]
                i+=1
        return ret

