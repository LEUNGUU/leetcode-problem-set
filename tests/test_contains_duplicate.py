from contains_duplicate import containsDuplicate_set, containsDuplicate_twopointer


def test_217_contains_duplicate():
    nums = [1, 2, 3, 1]
    ans1 = containsDuplicate_set(nums)
    assert ans1 is True
    ans2 = containsDuplicate_twopointer(nums)
    assert ans2 is True
