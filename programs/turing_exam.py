def longest_alternating_subsequence(nums):
  """Finds the longest alternating subsequence of a given array of 0s and 1s.

  Args:
    nums: A list of 0s and 1s.

  Returns:
    The length of the longest alternating subsequence.
  """

  # Create a table to store the lengths of the longest alternating subsequences
  # ending at each index.
  las = [[0, 0] for _ in range(len(nums))]

  # Initialize the table.
  las[0][0] = 1 if nums[0] == 0 else 0
  las[0][1] = 1 if nums[0] == 1 else 0

  # Iterate over the array.
  for i in range(1, len(nums)):
    # If the current number is different from the previous number, then we can
    # extend the longest alternating subsequence.
    if nums[i] != nums[i - 1]:
      las[i][0] = las[i - 1][1] + 1
      las[i][1] = las[i - 1][0] + 1
    # Otherwise, we can't extend the longest alternating subsequence.
    else:
      las[i][0] = las[i - 1][0]
      las[i][1] = las[i - 1][1]

  # Return the length of the longest alternating subsequence.
  return max(las[-1][0], las[-1][1])


# Example usage:
nums = [1, 0, 1, 0, 1]
# print(longest_alternating_subsequence(nums))  # 4


def longest_common_subsequence(arrays):
    from collections import defaultdict
    
    # Step 1: Find the common elements
    common_elements = defaultdict(int)
    for arr in arrays:
        for card in arr:
            common_elements[card] += 1
    
    # Step 2: Filter elements that are common in all arrays
    total_arrays = len(arrays)
    common_in_all = [key for key, count in common_elements.items() if count == total_arrays]
    
    # Step 3: Find the longest common subsequence preserving the order
    def filter_common_elements(arr, common):
        result = []
        common_set = set(common)
        for card in arr:
            if card in common_set:
                result.append(card)
        return result
    
    filtered_arrays = [filter_common_elements(arr, common_in_all) for arr in arrays]
    
    # Step 4: Apply a variation of LCS algorithm on filtered arrays
    def find_lcs_of_two(a, b):
        m, n = len(a), len(b)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        for i in range(m + 1):
            for j in range(n + 1):
                if i == 0 or j == 0:
                    dp[i][j] = 0
                elif a[i-1] == b[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        
        # Backtrack to find the LCS
        index = dp[m][n]
        lcs = [""] * index
        i, j = m, n
        while i > 0 and j > 0:
            if a[i-1] == b[j-1]:
                lcs[index-1] = a[i-1]
                i -= 1
                j -= 1
                index -= 1
            elif dp[i-1][j] > dp[i][j-1]:
                i -= 1
            else:
                j -= 1
        
        return lcs
    
    # LCS of multiple arrays
    def find_lcs_multiple(arrays):
        lcs = arrays[0]
        for i in range(1, len(arrays)):
            lcs = find_lcs_of_two(lcs, arrays[i])
        return lcs
    
    return find_lcs_multiple(filtered_arrays)

# Example usage:
k = [[3, 4, 7, 9], [2, 3, 4, 6, 7, 8, 11], [3, 4, 5, 7, 10]]
# print(longest_common_subsequence(k))  # Output: [3, 4, 7]


def count_unique_sublists(arr, limit, divisor):
    n = len(arr)
    start = 0
    count_sublists = 0
    count_divisibles = 0
    
    for end in range(n):
        # Check if the current element is divisible by the divisor
        if arr[end] % divisor == 0:
            count_divisibles += 1
        
        # If the count of divisibles exceeds the limit, move the start pointer
        while count_divisibles > limit:
            if arr[start] % divisor == 0:
                count_divisibles -= 1
            start += 1
        
        # All sublists from start to end are valid
        count_sublists += (end - start + 1)
    
    return count_sublists

# Example usage
arr = [6, 9, 9, 6, 6]
limit = 3
divisor = 3
result = count_unique_sublists(arr, limit, divisor)
print(result)  # Output: 9