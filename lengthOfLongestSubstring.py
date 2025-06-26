def lengthOfLongestSubstring(s: str) -> int:
    index = 0

    substr_map = {index: ""}

    for c in s:
        if not c in substr_map[index]:
            substr_map[index] += c
        else:
            old_index = index
            index += 1
            c_index = substr_map[old_index].index(c)
            substr_map[index] = substr_map[old_index][c_index+1:] + c

    long_substr = max(list(substr_map.values()), key=lambda x: len(x))

    return len(long_substr)