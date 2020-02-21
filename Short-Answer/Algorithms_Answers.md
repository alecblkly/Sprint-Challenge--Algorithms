#### Please add your answers to the **_Analysis of Algorithms_** exercises here.

## Exercise I

a) For this problem, it looks like this would be polynomial scaling O(n^2). As "n" becomes larger, the operation scales quickly per number of elements. Comparing the output graph to the complexity chart, the graph is more in-line with O(n^2); the line does grow quickly, but not as quick as O(2^n).

b) For this problem, it looks like this would be logarithmic scaling O(log n). The operations do scale as more elements are added, however; it scales by 1 operation, stays there for a few elements, and then increases.

c) For this problem, it looks like this would be linearithmic scaling O(n log n). For each iteration of this function, increases the operations by 2 while the number of elements increases by 1.

## Exercise II

For this problem, we want to continue dropping eggs as we go up the building floors. Each floor would be represented by `dropped floor + 1`, starting off with the base floor of just `dropped floor = 0`. When the egg is dropped, would check to see of egg is broken, if egg is broken the function would print the `dropped floor - 1` -- this would be the floor it was safe to drop an egg from. If the egg did not break at this floor, the function again would call `dropped floor + 1` and again check to see if the egg had broken. Because we are increasing the `dropped floor` by the same rate, until we find a solution, this would give us O(n) for the runtime complexity.
