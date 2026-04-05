
def two_sum(nums: list[int], target: int) -> list[int]:
    # 1. Create a map to store value -> index
    prev_map = {}

    # 2. Loop through nums with index
    for i, val in enumerate(nums):

    # 3. Find complement
        diff = target - val
    # 4. Return result or update map
        if diff in prev_map:
            return [prev_map[diff], i]
        prev_map[val] = i
    return []

if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    target = 9
    print(two_sum(nums, target))

    nums2 = [3, 2, 4]
    target2 = 6
    print(two_sum(nums2, target2))