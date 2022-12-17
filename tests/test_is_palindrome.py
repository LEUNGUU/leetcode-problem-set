from is_palindrome import Solution

testcase = [{"testcase": "race a car", "result": False}]


def test_is_palindrome():
    for tc in testcase:
        s = tc["testcase"]
        ans = Solution().isPalindrome(s)
        assert ans == tc["result"]
