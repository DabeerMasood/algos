class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if word == word.upper() or word == word.lower() or word==word.lower().capitalize():
            return True
        return False
