def subsets_with_dup(nums):
    def backtrack(start, current):
        result.append(list(current))

        for i in range(start, len(nums)):
            # skip duplicates at the same depth
            if i > start and nums[i] == nums[i - 1]:
                continue

            current.append(nums[i])
            backtrack(i + 1, current)
            current.pop()

    nums.sort()
    result = []
    backtrack(0, [])
    return result
