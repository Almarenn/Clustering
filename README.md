# given a file with strings, each string in a row, the program return divison to groups of the most similar strings. 
# 1.The algorithm first calculates a matrix of levenshtein distance: for each string (which fits a row index by order) it calculates the levenshtein edit distance between this string to the rest of the strings, which represented by column index.
# 2.Clustering: iterate over the strings and try to add it to an existing group (a group that already benn added to the cluestring dictionary). 
#   Check if there exists a levenshtein distance value between this string and the already iterated strings which is under a given thereshold. 
#     a. If yes, find this list's key and then add the string to the list. 
#     b. If no, open a new list with this string as a key and add the list to the cluesring dictionary.
# 3. Finally, return the different lists in the cluestring dictionary, so we can find whatever information we want out of it.
