from collections import defaultdict

class Solution:

    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        
        word_mapping = defaultdict(int)
        
        # calculate the word frequency
        for word in words:
            word_mapping[word] += 1

        result = sorted(word_mapping.keys(), key=lambda x:(-word_mapping[x], x))

        return result[:k]