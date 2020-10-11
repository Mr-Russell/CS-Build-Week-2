# Given a string s, find the length of the longest substring without repeating characters.

# Example 1:

  # Input: s = "abcabcbb"
  # Output: 3
  # Explanation: The answer is "abc", with the length of 3.

# Example 2:

  # Input: s = "bbbbb"
  # Output: 1
  # Explanation: The answer is "b", with the length of 1.

# Example 3:

  # Input: s = "pwwkew"
  # Output: 3
  # Explanation: The answer is "wke", with the length of 3.
  # Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

# Example 4:

  # Input: s = ""
  # Output: 0


##### BRUTE FORCE #####
# def lengthOfLongestSubstring(s):
#   cache = set()
#   longest = 0
#   length = 0
  
#   for i in s:
#     if i not in cache:
#       cache.add(i)
#       length += 1
#       if length > longest:
#         longest = length
#     else:
#       substring = self.lengthOfLongestSubstring(s[1:])
#       if longest < substring:
#         longest = substring
#       break
  
#   return longest


##### OPTIMIZED #####
def lengthOfLongestSubstring(self, s: str) -> int:
  cache = set()
  longest = 0
  left = 0
  right = 0
  
  while right < len(s):
    if s[right] not in cache:
      cache.add(s[right])
      length = (right - left) + 1
      if length > longest:
        longest = length
      right += 1
    else:
      cache.remove(s[left])
      left += 1
          
  return longest
