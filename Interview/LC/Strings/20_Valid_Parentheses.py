class Solution:
    # @return a boolean
    def isValid(self, s):
        stack = []
        dict = {"]":"[", "}":"{", ")":"("}
        for char in s:
            if char in dict.values():
                stack.append(char)
            else:
                if char in dict.keys():
                    if stack == [] or dict[char] != stack.pop():
                        return False
        return stack == []

my_str = Solution()
print my_str.isValid(s='()[]')