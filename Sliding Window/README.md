# Permutation in String

> I had to use all 3 hints. The last hint basically gave away the solution:

> We use a sliding window approach on `s2` with a fixed window size equal to the length of `s1`. To track the current window, we maintain a running frequency count of characters in `s2`. This frequency count represents the characters in the current window. At each step, if the frequency count matches that of `s1`, we return true.

This is a fixed sliding window problem. The fixed size being the size of `s1`. 

Iterate through `s2` by index `i`

We traverse each subarray from `i` to `len(s1)`

Create a dictionary of frequencies of `s1` and the subarray of `s2`

``` python
for i in range(len(s2) - len(s1) + 1):
            if Counter(s1) == Counter(s2[i : i + len(s1)]):
```

Compare the 2 dictionaries for equality and return True once a match is found
