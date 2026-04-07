def contains_duplicate(nums: list[int]) -> bool:
    # 1. Initialize an empty set
    val_set = set()

    # 2. Iterate through each number
    for num in nums:

    # 3. Check if number is in set
        if num in val_set:
            return True

    # 4. If not, add to set; if yes, return True
        else:
            val_set.add(num)
    # 5. Return False if loop completes
    return False

def contains_duplicate_2(nums: list[int]) -> bool:
    return len(nums) != len(set(nums))

if __name__ == '__main__':
    num1 = [1, 2, 3, 1]
    num2 = [1, 2, 3, 4]
    num3 = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
    print(contains_duplicate(num1))
    print(contains_duplicate_2(num1))
    print(contains_duplicate(num2))
    print(contains_duplicate(num3))