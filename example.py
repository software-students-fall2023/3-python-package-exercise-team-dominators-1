# Import the stringmanipulate package
from stringmanipulate import groupAnagrams, checkInclusion, lengthOfLongestSubstring, decodeString

def main():
    # Demonstration of groupAnagrams
    print("Group Anagrams:")
    anagrams = groupAnagrams(["bat", "tab", "eat", "tea", "tan", "nat"])
    print(anagrams)

    # Demonstration of checkInclusion
    print("\nCheck Inclusion:")
    inclusion_result = checkInclusion("ab", "eidbaooo")
    print(f"Is 'ab' a permutation of any substring in 'eidbaooo'? {inclusion_result}")

    # Demonstration of lengthOfLongestSubstring
    print("\nLength of Longest Substring without Repeating Characters:")
    length = lengthOfLongestSubstring("abcabcbb")
    print(f"Length: {length}")

    # Demonstration of decodeString
    print("\nDecode String:")
    decoded = decodeString("3[a]2[bc]")
    print(f"Decoded string: {decoded}")

if __name__ == "__main__":
    main()
