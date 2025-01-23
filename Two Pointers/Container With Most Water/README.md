# Container With Most Water

> I looked at 3 of the hints because I did this after work. So brain was fritata :)

The clever part about this problem is how to traverse the list. 

We use the two pointer technique for this problem

```python
left: int = 0
right: int = len(heights) - 1
```

We traverse the list by going inward 
`while left < right:`

Calculate the area of the current left and right indices and keep track of the highest value of area

``` python
area = (right - left) * min(heights[right], heights[left])
maxArea = max(maxArea, area)
```

We increment the left and decrement the right based on the value of `heights` in the `left` or `right` index

``` python
if heights[left] < heights[right]:
    left += 1
else:
    right -= 1
```

Afterwards, we just return `maxArea` and problem solved
