class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        hasWord = [False] * (len(s) + 1)
        hasWord[len(s)] = True

        for i in range(len(s), -1, -1):
            for word in wordDict:
                if word == s[i:i+len(word)]:
                    hasWord[i] = hasWord[i+len(word)]
                if hasWord[i]:
                    break
        return hasWord[0]