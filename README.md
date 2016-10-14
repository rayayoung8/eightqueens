# eightqueens
An algorithm written in Python to solve the Eight Queens problem in chess

For an 8x8 chessboard, try to place 8 queens in such a way that no queen can attack any other queen.
A queen can move unlimited spaces diagonally, horizontally, or vertically.

Recursive Algorithm:

Start at the leftmost column and move from left to right.

For the given spot, check if there are any queens in that row, or in either of the diagonals.
If the spot is safe, place a queen there. If you're at the rightmost column, you're done. If not, move to the right one column and do the algorithm again.

If the spot is unsafe, move down one row (same column) and apply the algorithm to that spot. 
If you've reached the bottom (last row), then that column is entirely unsafe. Move backwards one column (left) and move that queen down one spot and apply the algorithm there.

Keep doing this until you have a full chessboard of 8 queens.
