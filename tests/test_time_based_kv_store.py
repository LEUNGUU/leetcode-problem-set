from time_based_kv_store import TimeMap

testcase = [
    {
        "op": ["set", "get", "get", "set", "get", "get"],
        "value": [
            ["foo", "bar", 1],
            ["foo", 1],
            ["foo", 3],
            ["foo", "bar2", 4],
            ["foo", 4],
            ["foo", 5],
        ],
        "result": ["", "bar", "bar", "", "bar2", "bar2"],
    }
]


def test_time_based_kv_store():
    tm = TimeMap()
    for tc in testcase:
        op_times = len(tc["op"])
        res = []
        for index in range(op_times):
            if tc["op"][index] == "set":
                tm.set(
                    tc["value"][index][0], tc["value"][index][1], tc["value"][index][2]
                )
                res.append("")
            else:
                res.append(tm.get(tc["value"][index][0], tc["value"][index][1]))
        assert res == tc["result"]
