class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for string in strs:
            new = ""
            for c in string:
                new = new + chr(ord(c)+5)
            encoded_string = encoded_string + new + " "
        print(encoded_string)
        return encoded_string

    def decode(self, s: str) -> List[str]:
        strs = s.split(" ")
        decoded_strs = []
        for string in strs:
            word = ""
            for c in string:
                word = word + chr(ord(c)-5)
            decoded_strs.append(word)
        decoded_strs.pop()
        print(decoded_strs)
        return decoded_strs


