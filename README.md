# ReolePlayingGame
Here we learn how to write averaging function

Reads .csv file in -> stores data as a matrix -> averages out every column returning a vector -> writes the vector into a .csv file

>>> x

matrix([[ 0,  1,  2,  3],
        [ 4,  5,  6,  7],
        [ 8,  9, 10, 11]])
        
        
>>> x.mean()


5.5


>>> x.mean(0)


matrix([[4., 5., 6., 7.]])
