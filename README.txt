Author: Siddharth Shah

The python files within this directory contain an exploration into all possible end
states of a tic-tac-toe board following every legal move sequence. The boards are not
contrained to 3x3 (tested 4x3 and 4x4 boards with winning sequence length of 4). The
result.txt file contains the summarized findings of my analysis

For my methodology, I employed depth-first-searching backed by recursion along with
constraint satisfaction programming to determine when the given tic-tac-toe board had
reached an end state. Terminal boards were designated as wins for X, O, or draws under
the assumption that X always plays first.