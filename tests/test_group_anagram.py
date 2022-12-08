from group_anagram import Solution


testcase = [
    {"testcase": ["eat", "ate", "ant", "tna"], "result": [["eat", "ate"], ["ant", "tna"]]}
]

def test_group_anagram():
    for tc in testcase:
        str_list = tc["testcase"]
        ans = Solution().groupAnagrams(str_list)
        assert list(ans) == tc["result"]
