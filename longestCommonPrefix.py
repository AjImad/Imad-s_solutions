# Problem link: https://leetcode.com/problems/longest-common-prefix/

def longestCommonPrefix(strs:list[str]) -> str:

    # Assuming first string is the longest common prefix
    lcp = strs[0]

    for s in strs[1:]:
        if not lcp.strip():
            return ""
        for i, char in enumerate(lcp):
            if not char == s[i:i+1]:
                lcp = lcp[:i]

    return lcp 