# The-Minion-Game
One of HakerRank Problem

## To Do:
### Game Rules

Both players are given the same string, S.
Both players have to make substrings using the letters of the string S.
Stuart has to make words starting with consonants.
Kevin has to make words starting with vowels.
The game ends when both players have made all possible substrings.

### Scoring
A player gets +1 point for each occurrence of the substring in the string S.

For Example:
String S = BANANA
Kevin's vowel beginning word = ANA
Here, ANA occurs twice in BANANA. Hence, Kevin will get 2 Points.

Your task is to determine the winner of the game and their score.

## Solution:
Provide 1 point for every occurrence of substring in S to one of the player each time.
-Use a for loop in range of 0 to length of S
-Inside the loop use if condition for checking the vowel present in S
-Then print the name and score of player with higher score or if same score then simply print "Draw".
