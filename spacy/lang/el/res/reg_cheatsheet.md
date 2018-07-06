# Symbols
1. \d : digit
2. \w : ASCII character
3. \s : whitespace, newline,tab
4. \D : not a digit character
5. \W : not a word character
6. \S : not a whitespace/newline/tab character
7. + : Whatever it is on the left side, one or more times
8. {n} : what is left, exactly n times
9. {n,m} : minimum n, maximum
10. {n, } : n or more times
11. * : zero or more times
12. ? : once or none
13. . : any character except newline
14. () ?
15. [ ]: one of the characters inside the brackets
16. [x-y]: one of the characters in range [x,y].
17. [^x]: one character that is not x
18. ^x: string to begin with x
19. $: end of the string
20. (?=y)x: search after x for something that matches y.
21. (?<=y)x: search before x for something that matches y.
22. (?!y)x: search after x in order not to find something that matches y.
23. (?<!y)x: search before x in order not to find something that matches y.


# Match object


# Functions
1. re.match(pattern,string,flags=0): searches from left to right to find match.
2. re.search(pattern,string, flags=0): searches the first occurrence of RE pattern to string
