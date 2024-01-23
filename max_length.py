def maxLength(arr):
    # Initialize the result with an empty string to consider the case of not picking any strings
    res = [""]

    for s in arr:
        # Skip strings with duplicate characters
        if len(set(s)) < len(s):
            continue

        # Prepare a new list for this iteration to store combinations including the current string
        new_res = []
        for combination in res:
            # Form a new combination if there is no character conflict
            if not set(s) & set(combination):
                new_res.append(combination + s)

        # Update the result list with new combinations formed in this iteration
        res += new_res

    # Return the length of the longest unique character combination found
    return max(len(s) for s in res)


if __name__ == '__main__':
    # Example 1
    print(maxLength(["un", "iq", "ue"]))  # Output: 4

    # Example 2
    print(maxLength(["cha", "r", "act", "ers"]))  # Output: 6

    # Example 3
    print(maxLength(["abcdefghijklmnopqrstuvwxyz"]))  # Output: 26
