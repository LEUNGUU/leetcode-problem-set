from encode_decode_string import Solution
import logging

logger = logging.getLogger(__name__)

testcase = [
    {
        "testcase": ["neet", "code", "like", "you"],
        "result": ["neet", "code", "like", "you"],
    }
]


def test_encode_decode_string():
    for tc in testcase:
        strs = tc["testcase"]
        middle = Solution().encode(strs)
        logger.info(print(middle))
        ans = Solution().decode(middle)
        logger.info(print(ans))
        assert ans == tc["result"]
