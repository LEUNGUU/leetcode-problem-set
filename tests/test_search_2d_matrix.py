from search_2d_matrix import Solution

testcase = [
    {
        "testcase": [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]],
        "target": 3,
        "result": True,
    }
]


def test_search_2d_matrix():
    for tc in testcase:
        matrix = tc["testcase"]
        target = tc["target"]
        ans = Solution().searchMatrix(matrix, target)
        assert ans == tc["result"]
