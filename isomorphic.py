class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        mappingDict = {}
        if s is None:
            return True
        for i in range(len(s)):
            char_s = s[i]
            char_t = t[i]
            if char_s not in mappingDict.keys():
                if char_t in mappingDict.values():
                    return False
                mappingDict[char_s] = char_t
            else:
                if mappingDict[char_s] != char_t:
                    return False
        return True