# N_Queens_Problem
The N-Queens problem is a problem in computer science in which an algorithm has to place n queens on a n x n board such that no two queens are attacking each other.
As the number of queens increases, the number of solutions and the search space increases exponentially.
There are 92 solutions to the standard 8-queens problem, and the greatest n for which all distinct solutions are known is 26.
The traditional method for generating 1 solution is backtracking, which goes row by row placing 1 queen per row until either a valid solution
is generated or there are no more ways to place queens.  If there are no more ways to place queens, then the algorithm "backtracks", deleting the position
of the last placed queen and trying again.

This program either generates 1 valid solution for any number n for the n-queens problem or finds the number of all distinct solutions.
