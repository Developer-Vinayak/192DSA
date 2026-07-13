class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start=0
        max_len=0
        char_map={}
        for end,ch in enumerate(s):
            if ch in char_map and char_map[ch]>=start:
                start=char_map[ch]+1
            char_map[ch]=end
            curr_len=end-start+1
            max_len=max(max_len,curr_len)
        return max_len
