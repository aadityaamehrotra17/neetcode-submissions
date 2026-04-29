class Solution:

    def encode(self, strs: List[str]) -> str:
        '''
        len|separator|str
        eg: hello -> 5#hello, 5#hello -> 7#5#hello
        '''
        res = ''

        for word in strs:
            res += str(len(word)) + '#' + word

        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            j = i

            while s[j] != '#':
                j += 1
            num = int(s[i:j])

            i = j + 1
            res.append(s[i:i+num])
            i += num
        
        return res