class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {')':'(', ']':'[', '}':'{'}
        store = []

        if len(s) % 2 == 1:
            return False

        for i in s:
            if i not in brackets:
                store.append(i)
            elif i in brackets:
                if not store or brackets[i] != store[-1]:
                    return False
                store.pop()

        return len(store) == 0
