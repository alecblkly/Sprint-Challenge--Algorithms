#### Please add your answers to the **_Analysis of Algorithms_** exercises here.

## Exercise I

a) For this problem, it looks like this would be linear scaling O(n). For the while loop, this would continue running as long as the condition of `a` being less than `n * n * n` is True. With each iteration, `n^2` is being added to `a`. Which each iteration, this would turn into `n^3/n^2`, resulting in it just being `n` --> increasing at the same rate with each iteration.

b) For this problem, it looks like this would be logarithmic scaling O(log n). The operations do scale as more elements are added, however; it scales by 1 operation, stays there for a few elements, and then increases.

c) For this problem, it looks like this would be linear scaling O(n). For each iteration of this function, increases the operations by 2 while the number of elements increases by 1. To be linear scaling, the function needs to grow at the same rate, which is what this achieves.

## Exercise II

For this problem, we want to continue dropping eggs as we go up the building floors. Each floor would be represented by `dropped floor + 1`, starting off with the base floor of just `dropped floor = 0`. When the egg is dropped, would check to see of egg is broken, if egg is broken the function would print the `dropped floor - 1` -- this would be the floor it was safe to drop an egg from. If the egg did not break at this floor, the function again would call `dropped floor + 1` and again check to see if the egg had broken. Because we are increasing the `dropped floor` by the same rate, until we find a solution, this would give us O(n) for the runtime complexity.
