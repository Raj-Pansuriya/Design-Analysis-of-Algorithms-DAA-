MAX_COST = 999999

# A utility function to get sum of array elements freq[i] to freq[j]
def sum(freq, i, j):
    sum = 0
    for k in range(i, j + 1):
        sum += freq[k]
    return sum

def optimal_binary_search_tree(keys, freq, n):
    """
    A Dynamic Programming based function that
    calculates minimum cost of a Binary Search Tree.
    """

    # Create an auxiliary 2D matrix to store results of subproblems
    cost = [ [0 for x in range(n)] for y in range(n) ]

    # cost[i][j] = Optimal cost of binary search tree that can be formed from keys[i] to keys[j].
    # cost[0][n-1] will store the resultant cost

    # For a single key, cost is equal to frequency of the key
    for i in range(n):
        cost[i][i] = freq[i]

        # Now we need to consider chains of length 2, 3, ... . L is chain length.
        for L in range(2, n + 1):
            for i in range(n - L + 2):
                # Get column number j from row number i and chain length L
                j = i + L - 1
                if i >= n or j >= n:
                    break
                cost[i][j] = MAX_COST

                # Try making all keys in interval, keys[i..j] as root
                for r in range(i, j + 1):

                    # r_cost = cost when keys[r] becomes root of this subtree
                    r_cost = 0
                    if (r > i):
                        r_cost += cost[i][r - 1]
                    if (r < j):
                        r_cost += cost[r + 1][j]
                    r_cost += sum(freq, i, j)
                    if (r_cost < cost[i][j]):
                        cost[i][j] = r_cost
    return cost[0][n - 1]




# Driver Code
feed=input("Enter the keys as comma separated numbers:\n")
keys=[int(number) for number in feed.split(",")]

feed=input("Enter the respective frequencies as comma separated numbers:\n")
frequencies=[int(number) for number in feed.split(",")]

if(len(frequencies)!=len(keys)):
    print("Your keys and frequencies differ in count, please check again!!")
else:
    n=len(keys)
    print("Cost of Optimal BST is",optimal_binary_search_tree(keys, frequencies, n))
