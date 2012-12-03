# Dermuba Triangle
Dermuba Triangle is the universe-famous flat and triangular region in the L-PAX planet in the Geometria galaxy. Actually nobody knows whether the region is triangular or how it came into existence or how big it is. But the people of Dermuba firmly believe that the region extends to infinity. They live in equilateral triangular fields with sides exactly equal to 1km. Houses are always built at the circumcentres of the triangular fields. Their houses are numbered as shown in the figure below.
![Neighborhood Layout](https://raw.github.com/Kusold/ProgrammingChallenges/master/images/Dermuba_Triangle.gif)

When Dermubian people wishes to visit each other, they follow the shortest path from their house to the destination house. This shortest path is obviously the straight line distance that connects these two houses. Moreover, they also visit all the houses that lie in the straight line they travel. Now, comes your task. You have to write a program which computes the length of the shortest path between two houses given their house numbers.

## Input
Input consists of several lines with two non-negative integer values *n* and *m* which specify the start and destination house numbers. *0 < n, m < 2147483647*. Actually, there are houses beyond this region, but some seventh-sense people in Dermuba say that these houses are left for the dead people.

## Output
For each line in the input, print the shortest distance between the given houses in kilometers rounded off to three decimal places.

## Sample Input
    0 7
    2 8
    9 10
    10 11

## Sample Output
    1.528
    1.528
    0.577
    0.577
