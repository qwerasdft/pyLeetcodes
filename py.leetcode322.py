class Solution:
    """
    You are given coins of different denominations and a total amount of money amount. 
    Write a function to compute the fewest number of coins that you need to make up that amount. 
    If that amount of money cannot be made up by any combination of the coins, return -1.
    """

    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """

        # Sort our coins so that we can try
        # the larger ones first (greedy)
        coins.sort(reverse=True)
        n = len(coins)

        # An upper bound for the solution is
        # (value of smallest coin)*amount + 1
        maxbound = coins[n-1]*amount+1

        # Initialize our current best result with
        # our upper bound
        current_best = maxbound

        # Recursive depth first search
        def dfs(index, total, level):
            nonlocal current_best

            # If we've reached the target amount, we're done
            if total == amount:
                current_best = min(current_best, level)
                return

            # Otherwise try adding each coin to our running total,
            # starting from the current coin
            for i in range(index, n):
                coin = coins[i]

                # It's only worth exploring further if two conditions are met:
                # 1. We're not past the target amount.
                # 2. We could potentially improve our current best score from
                #    this position, meaning we could reach the target amount from here with
                #    less than (current_best-level) coins. If the value of our largest
                #    coin times (current_best-level) is lesser or equal to amount, we have no
                #    chance to improve our best score.
                #
                # if total+coin <= amount and amount-total < coin*(current_best-level):
                if coin <= amount-total < coin*(current_best-level):
                    dfs(i, total+coin, level+1)

        # Start our recursion at zero
        dfs(0, 0, 0)

        if current_best != maxbound:
            return current_best

        return -1


if __name__ == "__main__":
    coins = [1, 2, 5]
    amount = 5

    print(Solution().coinChange(coins, amount))
