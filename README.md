# A short tutorial on array reshape and rotation

by [Marco Pascucci](https://github.com/mpascucci)

Please consider the more readable [HTML version of this document](https://mpascucci.github.io/numpy-array-rotate-guide/index.html)

Array reshaping and rotation can be confusing. in this short guide I will try to visualize what happens when using the numpy functions corresponding to these operations.


```python
from IPython.display import HTML
import numpy as np
from html_3d_array import asvolume
```


```python
# Skip this cell.
# Build an array for this tutorial.
l=['♥','♣','♦','♠']
# l=[x for x in l]
p=np.vstack((l,l,l))
a=np.stack((p,p),axis=1)
```

# Reshape


```python
# The tutorial starts with this 3D array
# 3D means it has 3 dimensions.
print(a)
print("shape:", a.shape)
print("dimensions:", len(a.shape))
# We can think o
```

    [[['♥' '♣' '♦' '♠']
      ['♥' '♣' '♦' '♠']]
    
     [['♥' '♣' '♦' '♠']
      ['♥' '♣' '♦' '♠']]
    
     [['♥' '♣' '♦' '♠']
      ['♥' '♣' '♦' '♠']]]
    shape: (3, 2, 4)
    dimensions: 3



```python
# reshape(...) gives a new shape to an array without changing its data.
# The array dta is a flat sequence of characters registered somewhere in memory
data = a.flatten()
print("data:", ''.join(data))
```

    data: ♥♣♦♠♥♣♦♠♥♣♦♠♥♣♦♠♥♣♦♠♥♣♦♠


An array can be reshaped only if the product of the dimensions is the same.
for example:

- (3,2,4) (3,4,2) (2,3,4) (2,3,4) (4,2,3) (4,3,2)

are all valid shapes


```python
# let's do a reshape manually

# new shape
i=2
j=3
k=4

# print the data in rows according to the new shape
for z in range(i):
    for y in range(j):
        for x in range(k):
            # take a value from the data
            v=data[z*j*k + y*k + x]
            print(v, end='')
        print()
    print()
        
# this is analougous to
print(a.reshape(i,j,k))

HTML(asvolume(a.reshape(i,j,k)))

# and the same result can be obtained with np.moveaxis(a, 0, 1)
```

    ♥♣♦♠
    ♥♣♦♠
    ♥♣♦♠
    
    ♥♣♦♠
    ♥♣♦♠
    ♥♣♦♠
    
    [[['♥' '♣' '♦' '♠']
      ['♥' '♣' '♦' '♠']
      ['♥' '♣' '♦' '♠']]
    
     [['♥' '♣' '♦' '♠']
      ['♥' '♣' '♦' '♠']
      ['♥' '♣' '♦' '♠']]]





<table><tr style='padding:3px!'><td style=padding:3px><text style=color:red>♥</text></td>&nbsp<td style=padding:3px><text style=color:blue>♣</text></td>&nbsp<td style=padding:3px><text style=color:green>♦</text></td>&nbsp<td style=padding:3px><text style=color:black>♠</text></td>&nbsp<td style=padding:3px><text style=color:black>&nbsp</text></td></tr><tr style='padding:3px!'><td style=padding:3px><text style=color:red>♥</text></td>&nbsp<td style=padding:3px><text style=color:red>♥</text></td>&nbsp<td style=padding:3px><text style=color:blue>♣</text></td>&nbsp<td style=padding:3px><text style=color:green>♦</text></td>&nbsp<td style=padding:3px><text style=color:black>♠</text></td></tr><tr style='padding:3px!'><td style=padding:3px><text style=color:red>♥</text></td>&nbsp<td style=padding:3px><text style=color:red>♥</text></td>&nbsp<td style=padding:3px><text style=color:blue>♣</text></td>&nbsp<td style=padding:3px><text style=color:green>♦</text></td>&nbsp<td style=padding:3px><text style=color:black>♠</text></td></tr><tr style='padding:3px!'><td style=padding:3px><text style=color:black>&nbsp</text></td>&nbsp<td style=padding:3px><text style=color:red>♥</text></td>&nbsp<td style=padding:3px><text style=color:blue>♣</text></td>&nbsp<td style=padding:3px><text style=color:green>♦</text></td>&nbsp<td style=padding:3px><text style=color:black>♠</text></td></tr></table>



What `reshape` does is just "cut the array data according to the values ijk".

Fr example, we can not obtain the following volume by only reshaping 'a'... Try if you don't believe me.


```python
HTML(asvolume(a.swapaxes(0,2)))
```




<table><tr style='padding:3px!'><td style=padding:3px><text style=color:red>♥</text></td>&nbsp<td style=padding:3px><text style=color:red>♥</text></td>&nbsp<td style=padding:3px><text style=color:red>♥</text></td>&nbsp<td style=padding:3px><text style=color:black>&nbsp</text></td>&nbsp<td style=padding:3px><text style=color:black>&nbsp</text></td>&nbsp<td style=padding:3px><text style=color:black>&nbsp</text></td></tr><tr style='padding:3px!'><td style=padding:3px><text style=color:red>♥</text></td>&nbsp<td style=padding:3px><text style=color:blue>♣</text></td>&nbsp<td style=padding:3px><text style=color:blue>♣</text></td>&nbsp<td style=padding:3px><text style=color:blue>♣</text></td>&nbsp<td style=padding:3px><text style=color:black>&nbsp</text></td>&nbsp<td style=padding:3px><text style=color:black>&nbsp</text></td></tr><tr style='padding:3px!'><td style=padding:3px><text style=color:black>&nbsp</text></td>&nbsp<td style=padding:3px><text style=color:blue>♣</text></td>&nbsp<td style=padding:3px><text style=color:green>♦</text></td>&nbsp<td style=padding:3px><text style=color:green>♦</text></td>&nbsp<td style=padding:3px><text style=color:green>♦</text></td>&nbsp<td style=padding:3px><text style=color:black>&nbsp</text></td></tr><tr style='padding:3px!'><td style=padding:3px><text style=color:black>&nbsp</text></td>&nbsp<td style=padding:3px><text style=color:black>&nbsp</text></td>&nbsp<td style=padding:3px><text style=color:green>♦</text></td>&nbsp<td style=padding:3px><text style=color:black>♠</text></td>&nbsp<td style=padding:3px><text style=color:black>♠</text></td>&nbsp<td style=padding:3px><text style=color:black>♠</text></td></tr><tr style='padding:3px!'><td style=padding:3px><text style=color:black>&nbsp</text></td>&nbsp<td style=padding:3px><text style=color:black>&nbsp</text></td>&nbsp<td style=padding:3px><text style=color:black>&nbsp</text></td>&nbsp<td style=padding:3px><text style=color:black>♠</text></td>&nbsp<td style=padding:3px><text style=color:black>♠</text></td>&nbsp<td style=padding:3px><text style=color:black>♠</text></td></tr></table>



# 3D volume rotation

Take your time to learn to visualize 3D arrays as volumes.

The following volume has $i$ pages, each page has $j$ rows and $k$ columns

- the page index increases from first to last
- the row index increases from top to bottom (in the page)
- the column index increases from left to right (in the page)


```python
print(a)
HTML(asvolume(a))
```

    [[['♥' '♣' '♦' '♠']
      ['♥' '♣' '♦' '♠']]
    
     [['♥' '♣' '♦' '♠']
      ['♥' '♣' '♦' '♠']]
    
     [['♥' '♣' '♦' '♠']
      ['♥' '♣' '♦' '♠']]]





<table><tr style='padding:3px!'><td style=padding:3px><text style=color:red>♥</text></td>&nbsp<td style=padding:3px><text style=color:blue>♣</text></td>&nbsp<td style=padding:3px><text style=color:green>♦</text></td>&nbsp<td style=padding:3px><text style=color:black>♠</text></td>&nbsp<td style=padding:3px><text style=color:black>&nbsp</text></td>&nbsp<td style=padding:3px><text style=color:black>&nbsp</text></td></tr><tr style='padding:3px!'><td style=padding:3px><text style=color:red>♥</text></td>&nbsp<td style=padding:3px><text style=color:red>♥</text></td>&nbsp<td style=padding:3px><text style=color:blue>♣</text></td>&nbsp<td style=padding:3px><text style=color:green>♦</text></td>&nbsp<td style=padding:3px><text style=color:black>♠</text></td>&nbsp<td style=padding:3px><text style=color:black>&nbsp</text></td></tr><tr style='padding:3px!'><td style=padding:3px><text style=color:black>&nbsp</text></td>&nbsp<td style=padding:3px><text style=color:red>♥</text></td>&nbsp<td style=padding:3px><text style=color:red>♥</text></td>&nbsp<td style=padding:3px><text style=color:blue>♣</text></td>&nbsp<td style=padding:3px><text style=color:green>♦</text></td>&nbsp<td style=padding:3px><text style=color:black>♠</text></td></tr><tr style='padding:3px!'><td style=padding:3px><text style=color:black>&nbsp</text></td>&nbsp<td style=padding:3px><text style=color:black>&nbsp</text></td>&nbsp<td style=padding:3px><text style=color:red>♥</text></td>&nbsp<td style=padding:3px><text style=color:blue>♣</text></td>&nbsp<td style=padding:3px><text style=color:green>♦</text></td>&nbsp<td style=padding:3px><text style=color:black>♠</text></td></tr></table>



This array has 3 dimensions: $i,j,k$ which can be rearranged in $3!=6$ permutations

- $ijk$, $ikj$, $jik$, $jki$, $kij$, $kji$

In 3D it can be seen as a parallelepiped, with 6 faces, which can be rotated so that we see a particular face in front of us.

Each such rotation corresponds to a particular permutation of $i,j,k$

The elementary operation that change the permutation of the index is an "axis swap" (e.g. ijk -> kji where `i` and `k` have been swapped).

A ciclical shift of the axes corresponds to two successive swapping on two orthogonal faces

- $ijk \rightarrow jki = ijk \rightarrow kji \rightarrow jki$

# Functions which apply volume rotations


```python
# swapaxis can do wathever volume rotation. It interchanges two axes of an array.
# here let's swap axis 0 and 2 (first and last)
# 3,2,4 -> 4,2,3
b=a.swapaxes(0,2)
print(b)

# The array data has changed 
print("data of array a:", ''.join(a.flatten()))
print("data of array b:", ''.join(b.flatten()))
HTML(asvolume(b))
```

    [[['♥' '♥' '♥']
      ['♥' '♥' '♥']]
    
     [['♣' '♣' '♣']
      ['♣' '♣' '♣']]
    
     [['♦' '♦' '♦']
      ['♦' '♦' '♦']]
    
     [['♠' '♠' '♠']
      ['♠' '♠' '♠']]]
    data of array a: ♥♣♦♠♥♣♦♠♥♣♦♠♥♣♦♠♥♣♦♠♥♣♦♠
    data of array b: ♥♥♥♥♥♥♣♣♣♣♣♣♦♦♦♦♦♦♠♠♠♠♠♠





<table><tr style='padding:3px!'><td style=padding:3px><text style=color:red>♥</text></td>&nbsp<td style=padding:3px><text style=color:red>♥</text></td>&nbsp<td style=padding:3px><text style=color:red>♥</text></td>&nbsp<td style=padding:3px><text style=color:black>&nbsp</text></td>&nbsp<td style=padding:3px><text style=color:black>&nbsp</text></td>&nbsp<td style=padding:3px><text style=color:black>&nbsp</text></td></tr><tr style='padding:3px!'><td style=padding:3px><text style=color:red>♥</text></td>&nbsp<td style=padding:3px><text style=color:blue>♣</text></td>&nbsp<td style=padding:3px><text style=color:blue>♣</text></td>&nbsp<td style=padding:3px><text style=color:blue>♣</text></td>&nbsp<td style=padding:3px><text style=color:black>&nbsp</text></td>&nbsp<td style=padding:3px><text style=color:black>&nbsp</text></td></tr><tr style='padding:3px!'><td style=padding:3px><text style=color:black>&nbsp</text></td>&nbsp<td style=padding:3px><text style=color:blue>♣</text></td>&nbsp<td style=padding:3px><text style=color:green>♦</text></td>&nbsp<td style=padding:3px><text style=color:green>♦</text></td>&nbsp<td style=padding:3px><text style=color:green>♦</text></td>&nbsp<td style=padding:3px><text style=color:black>&nbsp</text></td></tr><tr style='padding:3px!'><td style=padding:3px><text style=color:black>&nbsp</text></td>&nbsp<td style=padding:3px><text style=color:black>&nbsp</text></td>&nbsp<td style=padding:3px><text style=color:green>♦</text></td>&nbsp<td style=padding:3px><text style=color:black>♠</text></td>&nbsp<td style=padding:3px><text style=color:black>♠</text></td>&nbsp<td style=padding:3px><text style=color:black>♠</text></td></tr><tr style='padding:3px!'><td style=padding:3px><text style=color:black>&nbsp</text></td>&nbsp<td style=padding:3px><text style=color:black>&nbsp</text></td>&nbsp<td style=padding:3px><text style=color:black>&nbsp</text></td>&nbsp<td style=padding:3px><text style=color:black>♠</text></td>&nbsp<td style=padding:3px><text style=color:black>♠</text></td>&nbsp<td style=padding:3px><text style=color:black>♠</text></td></tr></table>




```python
# rot90(a, axes=(0,1))
# Rotate an array by 90 degrees in the plane specified by axes.
# Rotation direction is from the first towards the second axis.

# it is equivalent to swapaxis(...) but with a more understandable logic

b=np.rot90(a,axes=(2,0))
print(b)
HTML(asvolume(b))
```

    [[['♥' '♥' '♥']
      ['♥' '♥' '♥']]
    
     [['♣' '♣' '♣']
      ['♣' '♣' '♣']]
    
     [['♦' '♦' '♦']
      ['♦' '♦' '♦']]
    
     [['♠' '♠' '♠']
      ['♠' '♠' '♠']]]





<table><tr style='padding:3px!'><td style=padding:3px><text style=color:red>♥</text></td>&nbsp<td style=padding:3px><text style=color:red>♥</text></td>&nbsp<td style=padding:3px><text style=color:red>♥</text></td>&nbsp<td style=padding:3px><text style=color:black>&nbsp</text></td>&nbsp<td style=padding:3px><text style=color:black>&nbsp</text></td>&nbsp<td style=padding:3px><text style=color:black>&nbsp</text></td></tr><tr style='padding:3px!'><td style=padding:3px><text style=color:red>♥</text></td>&nbsp<td style=padding:3px><text style=color:blue>♣</text></td>&nbsp<td style=padding:3px><text style=color:blue>♣</text></td>&nbsp<td style=padding:3px><text style=color:blue>♣</text></td>&nbsp<td style=padding:3px><text style=color:black>&nbsp</text></td>&nbsp<td style=padding:3px><text style=color:black>&nbsp</text></td></tr><tr style='padding:3px!'><td style=padding:3px><text style=color:black>&nbsp</text></td>&nbsp<td style=padding:3px><text style=color:blue>♣</text></td>&nbsp<td style=padding:3px><text style=color:green>♦</text></td>&nbsp<td style=padding:3px><text style=color:green>♦</text></td>&nbsp<td style=padding:3px><text style=color:green>♦</text></td>&nbsp<td style=padding:3px><text style=color:black>&nbsp</text></td></tr><tr style='padding:3px!'><td style=padding:3px><text style=color:black>&nbsp</text></td>&nbsp<td style=padding:3px><text style=color:black>&nbsp</text></td>&nbsp<td style=padding:3px><text style=color:green>♦</text></td>&nbsp<td style=padding:3px><text style=color:black>♠</text></td>&nbsp<td style=padding:3px><text style=color:black>♠</text></td>&nbsp<td style=padding:3px><text style=color:black>♠</text></td></tr><tr style='padding:3px!'><td style=padding:3px><text style=color:black>&nbsp</text></td>&nbsp<td style=padding:3px><text style=color:black>&nbsp</text></td>&nbsp<td style=padding:3px><text style=color:black>&nbsp</text></td>&nbsp<td style=padding:3px><text style=color:black>♠</text></td>&nbsp<td style=padding:3px><text style=color:black>♠</text></td>&nbsp<td style=padding:3px><text style=color:black>♠</text></td></tr></table>




```python
# we can rotate in the opporsite direction and look the volume from behind
# (look at the order of the symbols)
b=np.rot90(a,axes=(0,2))
print(b)
HTML(asvolume(b))
```

    [[['♠' '♠' '♠']
      ['♠' '♠' '♠']]
    
     [['♦' '♦' '♦']
      ['♦' '♦' '♦']]
    
     [['♣' '♣' '♣']
      ['♣' '♣' '♣']]
    
     [['♥' '♥' '♥']
      ['♥' '♥' '♥']]]





<table><tr style='padding:3px!'><td style=padding:3px><text style=color:black>♠</text></td>&nbsp<td style=padding:3px><text style=color:black>♠</text></td>&nbsp<td style=padding:3px><text style=color:black>♠</text></td>&nbsp<td style=padding:3px><text style=color:black>&nbsp</text></td>&nbsp<td style=padding:3px><text style=color:black>&nbsp</text></td>&nbsp<td style=padding:3px><text style=color:black>&nbsp</text></td></tr><tr style='padding:3px!'><td style=padding:3px><text style=color:black>♠</text></td>&nbsp<td style=padding:3px><text style=color:green>♦</text></td>&nbsp<td style=padding:3px><text style=color:green>♦</text></td>&nbsp<td style=padding:3px><text style=color:green>♦</text></td>&nbsp<td style=padding:3px><text style=color:black>&nbsp</text></td>&nbsp<td style=padding:3px><text style=color:black>&nbsp</text></td></tr><tr style='padding:3px!'><td style=padding:3px><text style=color:black>&nbsp</text></td>&nbsp<td style=padding:3px><text style=color:green>♦</text></td>&nbsp<td style=padding:3px><text style=color:blue>♣</text></td>&nbsp<td style=padding:3px><text style=color:blue>♣</text></td>&nbsp<td style=padding:3px><text style=color:blue>♣</text></td>&nbsp<td style=padding:3px><text style=color:black>&nbsp</text></td></tr><tr style='padding:3px!'><td style=padding:3px><text style=color:black>&nbsp</text></td>&nbsp<td style=padding:3px><text style=color:black>&nbsp</text></td>&nbsp<td style=padding:3px><text style=color:blue>♣</text></td>&nbsp<td style=padding:3px><text style=color:red>♥</text></td>&nbsp<td style=padding:3px><text style=color:red>♥</text></td>&nbsp<td style=padding:3px><text style=color:red>♥</text></td></tr><tr style='padding:3px!'><td style=padding:3px><text style=color:black>&nbsp</text></td>&nbsp<td style=padding:3px><text style=color:black>&nbsp</text></td>&nbsp<td style=padding:3px><text style=color:black>&nbsp</text></td>&nbsp<td style=padding:3px><text style=color:red>♥</text></td>&nbsp<td style=padding:3px><text style=color:red>♥</text></td>&nbsp<td style=padding:3px><text style=color:red>♥</text></td></tr></table>




```python
# then we might want to rotate it on its front face
c=np.rot90(b,axes=(1,2))
print(c) # rotate on front face
HTML(asvolume(c))
```

    [[['♠' '♠']
      ['♠' '♠']
      ['♠' '♠']]
    
     [['♦' '♦']
      ['♦' '♦']
      ['♦' '♦']]
    
     [['♣' '♣']
      ['♣' '♣']
      ['♣' '♣']]
    
     [['♥' '♥']
      ['♥' '♥']
      ['♥' '♥']]]





<table><tr style='padding:3px!'><td style=padding:3px><text style=color:black>♠</text></td>&nbsp<td style=padding:3px><text style=color:black>♠</text></td>&nbsp<td style=padding:3px><text style=color:black>&nbsp</text></td>&nbsp<td style=padding:3px><text style=color:black>&nbsp</text></td>&nbsp<td style=padding:3px><text style=color:black>&nbsp</text></td></tr><tr style='padding:3px!'><td style=padding:3px><text style=color:black>♠</text></td>&nbsp<td style=padding:3px><text style=color:green>♦</text></td>&nbsp<td style=padding:3px><text style=color:green>♦</text></td>&nbsp<td style=padding:3px><text style=color:black>&nbsp</text></td>&nbsp<td style=padding:3px><text style=color:black>&nbsp</text></td></tr><tr style='padding:3px!'><td style=padding:3px><text style=color:black>♠</text></td>&nbsp<td style=padding:3px><text style=color:green>♦</text></td>&nbsp<td style=padding:3px><text style=color:blue>♣</text></td>&nbsp<td style=padding:3px><text style=color:blue>♣</text></td>&nbsp<td style=padding:3px><text style=color:black>&nbsp</text></td></tr><tr style='padding:3px!'><td style=padding:3px><text style=color:black>&nbsp</text></td>&nbsp<td style=padding:3px><text style=color:green>♦</text></td>&nbsp<td style=padding:3px><text style=color:blue>♣</text></td>&nbsp<td style=padding:3px><text style=color:red>♥</text></td>&nbsp<td style=padding:3px><text style=color:red>♥</text></td></tr><tr style='padding:3px!'><td style=padding:3px><text style=color:black>&nbsp</text></td>&nbsp<td style=padding:3px><text style=color:black>&nbsp</text></td>&nbsp<td style=padding:3px><text style=color:blue>♣</text></td>&nbsp<td style=padding:3px><text style=color:red>♥</text></td>&nbsp<td style=padding:3px><text style=color:red>♥</text></td></tr><tr style='padding:3px!'><td style=padding:3px><text style=color:black>&nbsp</text></td>&nbsp<td style=padding:3px><text style=color:black>&nbsp</text></td>&nbsp<td style=padding:3px><text style=color:black>&nbsp</text></td>&nbsp<td style=padding:3px><text style=color:red>♥</text></td>&nbsp<td style=padding:3px><text style=color:red>♥</text></td></tr></table>




```python
# Finally, the most powerful einsum
# which can do rotations and much more.
# np.einsum('abc->cba',a)
b = np.einsum('abc->cab',a)
print(b)
HTML(asvolume(b))
```

    [[['♥' '♥']
      ['♥' '♥']
      ['♥' '♥']]
    
     [['♣' '♣']
      ['♣' '♣']
      ['♣' '♣']]
    
     [['♦' '♦']
      ['♦' '♦']
      ['♦' '♦']]
    
     [['♠' '♠']
      ['♠' '♠']
      ['♠' '♠']]]





<table><tr style='padding:3px!'><td style=padding:3px><text style=color:red>♥</text></td>&nbsp<td style=padding:3px><text style=color:red>♥</text></td>&nbsp<td style=padding:3px><text style=color:black>&nbsp</text></td>&nbsp<td style=padding:3px><text style=color:black>&nbsp</text></td>&nbsp<td style=padding:3px><text style=color:black>&nbsp</text></td></tr><tr style='padding:3px!'><td style=padding:3px><text style=color:red>♥</text></td>&nbsp<td style=padding:3px><text style=color:blue>♣</text></td>&nbsp<td style=padding:3px><text style=color:blue>♣</text></td>&nbsp<td style=padding:3px><text style=color:black>&nbsp</text></td>&nbsp<td style=padding:3px><text style=color:black>&nbsp</text></td></tr><tr style='padding:3px!'><td style=padding:3px><text style=color:red>♥</text></td>&nbsp<td style=padding:3px><text style=color:blue>♣</text></td>&nbsp<td style=padding:3px><text style=color:green>♦</text></td>&nbsp<td style=padding:3px><text style=color:green>♦</text></td>&nbsp<td style=padding:3px><text style=color:black>&nbsp</text></td></tr><tr style='padding:3px!'><td style=padding:3px><text style=color:black>&nbsp</text></td>&nbsp<td style=padding:3px><text style=color:blue>♣</text></td>&nbsp<td style=padding:3px><text style=color:green>♦</text></td>&nbsp<td style=padding:3px><text style=color:black>♠</text></td>&nbsp<td style=padding:3px><text style=color:black>♠</text></td></tr><tr style='padding:3px!'><td style=padding:3px><text style=color:black>&nbsp</text></td>&nbsp<td style=padding:3px><text style=color:black>&nbsp</text></td>&nbsp<td style=padding:3px><text style=color:green>♦</text></td>&nbsp<td style=padding:3px><text style=color:black>♠</text></td>&nbsp<td style=padding:3px><text style=color:black>♠</text></td></tr><tr style='padding:3px!'><td style=padding:3px><text style=color:black>&nbsp</text></td>&nbsp<td style=padding:3px><text style=color:black>&nbsp</text></td>&nbsp<td style=padding:3px><text style=color:black>&nbsp</text></td>&nbsp<td style=padding:3px><text style=color:black>♠</text></td>&nbsp<td style=padding:3px><text style=color:black>♠</text></td></tr></table>



# A practical exercice


```python
# transform array 'u' (2D) into array 'v' (3D)

u=np.array([['♥']*15, ['♦']*15, ['♣']*15, ['♠']*15])
v=np.array([[['♥']*5, ['♦']*5, ['♣']*5, ['♠']*5]]*3 )

print(u)
print()
print(v)
HTML(asvolume(v))
```

    [['♥' '♥' '♥' '♥' '♥' '♥' '♥' '♥' '♥' '♥' '♥' '♥' '♥' '♥' '♥']
     ['♦' '♦' '♦' '♦' '♦' '♦' '♦' '♦' '♦' '♦' '♦' '♦' '♦' '♦' '♦']
     ['♣' '♣' '♣' '♣' '♣' '♣' '♣' '♣' '♣' '♣' '♣' '♣' '♣' '♣' '♣']
     ['♠' '♠' '♠' '♠' '♠' '♠' '♠' '♠' '♠' '♠' '♠' '♠' '♠' '♠' '♠']]
    
    [[['♥' '♥' '♥' '♥' '♥']
      ['♦' '♦' '♦' '♦' '♦']
      ['♣' '♣' '♣' '♣' '♣']
      ['♠' '♠' '♠' '♠' '♠']]
    
     [['♥' '♥' '♥' '♥' '♥']
      ['♦' '♦' '♦' '♦' '♦']
      ['♣' '♣' '♣' '♣' '♣']
      ['♠' '♠' '♠' '♠' '♠']]
    
     [['♥' '♥' '♥' '♥' '♥']
      ['♦' '♦' '♦' '♦' '♦']
      ['♣' '♣' '♣' '♣' '♣']
      ['♠' '♠' '♠' '♠' '♠']]]





<table><tr style='padding:3px!'><td style=padding:3px><text style=color:red>♥</text></td>&nbsp<td style=padding:3px><text style=color:red>♥</text></td>&nbsp<td style=padding:3px><text style=color:red>♥</text></td>&nbsp<td style=padding:3px><text style=color:red>♥</text></td>&nbsp<td style=padding:3px><text style=color:red>♥</text></td>&nbsp<td style=padding:3px><text style=color:black>&nbsp</text></td>&nbsp<td style=padding:3px><text style=color:black>&nbsp</text></td></tr><tr style='padding:3px!'><td style=padding:3px><text style=color:green>♦</text></td>&nbsp<td style=padding:3px><text style=color:red>♥</text></td>&nbsp<td style=padding:3px><text style=color:red>♥</text></td>&nbsp<td style=padding:3px><text style=color:red>♥</text></td>&nbsp<td style=padding:3px><text style=color:red>♥</text></td>&nbsp<td style=padding:3px><text style=color:red>♥</text></td>&nbsp<td style=padding:3px><text style=color:black>&nbsp</text></td></tr><tr style='padding:3px!'><td style=padding:3px><text style=color:blue>♣</text></td>&nbsp<td style=padding:3px><text style=color:green>♦</text></td>&nbsp<td style=padding:3px><text style=color:red>♥</text></td>&nbsp<td style=padding:3px><text style=color:red>♥</text></td>&nbsp<td style=padding:3px><text style=color:red>♥</text></td>&nbsp<td style=padding:3px><text style=color:red>♥</text></td>&nbsp<td style=padding:3px><text style=color:red>♥</text></td></tr><tr style='padding:3px!'><td style=padding:3px><text style=color:black>♠</text></td>&nbsp<td style=padding:3px><text style=color:blue>♣</text></td>&nbsp<td style=padding:3px><text style=color:green>♦</text></td>&nbsp<td style=padding:3px><text style=color:green>♦</text></td>&nbsp<td style=padding:3px><text style=color:green>♦</text></td>&nbsp<td style=padding:3px><text style=color:green>♦</text></td>&nbsp<td style=padding:3px><text style=color:green>♦</text></td></tr><tr style='padding:3px!'><td style=padding:3px><text style=color:black>&nbsp</text></td>&nbsp<td style=padding:3px><text style=color:black>♠</text></td>&nbsp<td style=padding:3px><text style=color:blue>♣</text></td>&nbsp<td style=padding:3px><text style=color:blue>♣</text></td>&nbsp<td style=padding:3px><text style=color:blue>♣</text></td>&nbsp<td style=padding:3px><text style=color:blue>♣</text></td>&nbsp<td style=padding:3px><text style=color:blue>♣</text></td></tr><tr style='padding:3px!'><td style=padding:3px><text style=color:black>&nbsp</text></td>&nbsp<td style=padding:3px><text style=color:black>&nbsp</text></td>&nbsp<td style=padding:3px><text style=color:black>♠</text></td>&nbsp<td style=padding:3px><text style=color:black>♠</text></td>&nbsp<td style=padding:3px><text style=color:black>♠</text></td>&nbsp<td style=padding:3px><text style=color:black>♠</text></td>&nbsp<td style=padding:3px><text style=color:black>♠</text></td></tr></table>




```python
# let's first reshape 'a' into a 3D shape
# what we want is 3 pages of the same symbol
w=u.reshape(4,3,5)
print(w)
HTML(asvolume(w))
```

    [[['♥' '♥' '♥' '♥' '♥']
      ['♥' '♥' '♥' '♥' '♥']
      ['♥' '♥' '♥' '♥' '♥']]
    
     [['♦' '♦' '♦' '♦' '♦']
      ['♦' '♦' '♦' '♦' '♦']
      ['♦' '♦' '♦' '♦' '♦']]
    
     [['♣' '♣' '♣' '♣' '♣']
      ['♣' '♣' '♣' '♣' '♣']
      ['♣' '♣' '♣' '♣' '♣']]
    
     [['♠' '♠' '♠' '♠' '♠']
      ['♠' '♠' '♠' '♠' '♠']
      ['♠' '♠' '♠' '♠' '♠']]]





<table><tr style='padding:3px!'><td style=padding:3px><text style=color:red>♥</text></td>&nbsp<td style=padding:3px><text style=color:red>♥</text></td>&nbsp<td style=padding:3px><text style=color:red>♥</text></td>&nbsp<td style=padding:3px><text style=color:red>♥</text></td>&nbsp<td style=padding:3px><text style=color:red>♥</text></td>&nbsp<td style=padding:3px><text style=color:black>&nbsp</text></td>&nbsp<td style=padding:3px><text style=color:black>&nbsp</text></td>&nbsp<td style=padding:3px><text style=color:black>&nbsp</text></td></tr><tr style='padding:3px!'><td style=padding:3px><text style=color:red>♥</text></td>&nbsp<td style=padding:3px><text style=color:green>♦</text></td>&nbsp<td style=padding:3px><text style=color:green>♦</text></td>&nbsp<td style=padding:3px><text style=color:green>♦</text></td>&nbsp<td style=padding:3px><text style=color:green>♦</text></td>&nbsp<td style=padding:3px><text style=color:green>♦</text></td>&nbsp<td style=padding:3px><text style=color:black>&nbsp</text></td>&nbsp<td style=padding:3px><text style=color:black>&nbsp</text></td></tr><tr style='padding:3px!'><td style=padding:3px><text style=color:red>♥</text></td>&nbsp<td style=padding:3px><text style=color:green>♦</text></td>&nbsp<td style=padding:3px><text style=color:blue>♣</text></td>&nbsp<td style=padding:3px><text style=color:blue>♣</text></td>&nbsp<td style=padding:3px><text style=color:blue>♣</text></td>&nbsp<td style=padding:3px><text style=color:blue>♣</text></td>&nbsp<td style=padding:3px><text style=color:blue>♣</text></td>&nbsp<td style=padding:3px><text style=color:black>&nbsp</text></td></tr><tr style='padding:3px!'><td style=padding:3px><text style=color:black>&nbsp</text></td>&nbsp<td style=padding:3px><text style=color:green>♦</text></td>&nbsp<td style=padding:3px><text style=color:blue>♣</text></td>&nbsp<td style=padding:3px><text style=color:black>♠</text></td>&nbsp<td style=padding:3px><text style=color:black>♠</text></td>&nbsp<td style=padding:3px><text style=color:black>♠</text></td>&nbsp<td style=padding:3px><text style=color:black>♠</text></td>&nbsp<td style=padding:3px><text style=color:black>♠</text></td></tr><tr style='padding:3px!'><td style=padding:3px><text style=color:black>&nbsp</text></td>&nbsp<td style=padding:3px><text style=color:black>&nbsp</text></td>&nbsp<td style=padding:3px><text style=color:blue>♣</text></td>&nbsp<td style=padding:3px><text style=color:black>♠</text></td>&nbsp<td style=padding:3px><text style=color:black>♠</text></td>&nbsp<td style=padding:3px><text style=color:black>♠</text></td>&nbsp<td style=padding:3px><text style=color:black>♠</text></td>&nbsp<td style=padding:3px><text style=color:black>♠</text></td></tr><tr style='padding:3px!'><td style=padding:3px><text style=color:black>&nbsp</text></td>&nbsp<td style=padding:3px><text style=color:black>&nbsp</text></td>&nbsp<td style=padding:3px><text style=color:black>&nbsp</text></td>&nbsp<td style=padding:3px><text style=color:black>♠</text></td>&nbsp<td style=padding:3px><text style=color:black>♠</text></td>&nbsp<td style=padding:3px><text style=color:black>♠</text></td>&nbsp<td style=padding:3px><text style=color:black>♠</text></td>&nbsp<td style=padding:3px><text style=color:black>♠</text></td></tr></table>




```python
# now what we have to do is just rotate the volume
# we send the first axes (pointing at you from the first to the last page) into the second axis (page rows, top to bottom)
t=np.rot90(w,axes=(0,1))
print(t)
HTML(asvolume(t))
```

    [[['♥' '♥' '♥' '♥' '♥']
      ['♦' '♦' '♦' '♦' '♦']
      ['♣' '♣' '♣' '♣' '♣']
      ['♠' '♠' '♠' '♠' '♠']]
    
     [['♥' '♥' '♥' '♥' '♥']
      ['♦' '♦' '♦' '♦' '♦']
      ['♣' '♣' '♣' '♣' '♣']
      ['♠' '♠' '♠' '♠' '♠']]
    
     [['♥' '♥' '♥' '♥' '♥']
      ['♦' '♦' '♦' '♦' '♦']
      ['♣' '♣' '♣' '♣' '♣']
      ['♠' '♠' '♠' '♠' '♠']]]





<table><tr style='padding:3px!'><td style=padding:3px><text style=color:red>♥</text></td>&nbsp<td style=padding:3px><text style=color:red>♥</text></td>&nbsp<td style=padding:3px><text style=color:red>♥</text></td>&nbsp<td style=padding:3px><text style=color:red>♥</text></td>&nbsp<td style=padding:3px><text style=color:red>♥</text></td>&nbsp<td style=padding:3px><text style=color:black>&nbsp</text></td>&nbsp<td style=padding:3px><text style=color:black>&nbsp</text></td></tr><tr style='padding:3px!'><td style=padding:3px><text style=color:green>♦</text></td>&nbsp<td style=padding:3px><text style=color:red>♥</text></td>&nbsp<td style=padding:3px><text style=color:red>♥</text></td>&nbsp<td style=padding:3px><text style=color:red>♥</text></td>&nbsp<td style=padding:3px><text style=color:red>♥</text></td>&nbsp<td style=padding:3px><text style=color:red>♥</text></td>&nbsp<td style=padding:3px><text style=color:black>&nbsp</text></td></tr><tr style='padding:3px!'><td style=padding:3px><text style=color:blue>♣</text></td>&nbsp<td style=padding:3px><text style=color:green>♦</text></td>&nbsp<td style=padding:3px><text style=color:red>♥</text></td>&nbsp<td style=padding:3px><text style=color:red>♥</text></td>&nbsp<td style=padding:3px><text style=color:red>♥</text></td>&nbsp<td style=padding:3px><text style=color:red>♥</text></td>&nbsp<td style=padding:3px><text style=color:red>♥</text></td></tr><tr style='padding:3px!'><td style=padding:3px><text style=color:black>♠</text></td>&nbsp<td style=padding:3px><text style=color:blue>♣</text></td>&nbsp<td style=padding:3px><text style=color:green>♦</text></td>&nbsp<td style=padding:3px><text style=color:green>♦</text></td>&nbsp<td style=padding:3px><text style=color:green>♦</text></td>&nbsp<td style=padding:3px><text style=color:green>♦</text></td>&nbsp<td style=padding:3px><text style=color:green>♦</text></td></tr><tr style='padding:3px!'><td style=padding:3px><text style=color:black>&nbsp</text></td>&nbsp<td style=padding:3px><text style=color:black>♠</text></td>&nbsp<td style=padding:3px><text style=color:blue>♣</text></td>&nbsp<td style=padding:3px><text style=color:blue>♣</text></td>&nbsp<td style=padding:3px><text style=color:blue>♣</text></td>&nbsp<td style=padding:3px><text style=color:blue>♣</text></td>&nbsp<td style=padding:3px><text style=color:blue>♣</text></td></tr><tr style='padding:3px!'><td style=padding:3px><text style=color:black>&nbsp</text></td>&nbsp<td style=padding:3px><text style=color:black>&nbsp</text></td>&nbsp<td style=padding:3px><text style=color:black>♠</text></td>&nbsp<td style=padding:3px><text style=color:black>♠</text></td>&nbsp<td style=padding:3px><text style=color:black>♠</text></td>&nbsp<td style=padding:3px><text style=color:black>♠</text></td>&nbsp<td style=padding:3px><text style=color:black>♠</text></td></tr></table>



# with numbers


```python
u=np.array([[22]*15, [27]*15, [32]*15, [37]*15])
v=u.reshape(4,3,5)
HTML(asvolume(v))
```




<table><tr style='padding:3px!'><td style=padding:3px><text style=color:black>22</text></td>&nbsp<td style=padding:3px><text style=color:black>22</text></td>&nbsp<td style=padding:3px><text style=color:black>22</text></td>&nbsp<td style=padding:3px><text style=color:black>22</text></td>&nbsp<td style=padding:3px><text style=color:black>22</text></td>&nbsp<td style=padding:3px><text style=color:black>&nbsp</text></td>&nbsp<td style=padding:3px><text style=color:black>&nbsp</text></td>&nbsp<td style=padding:3px><text style=color:black>&nbsp</text></td></tr><tr style='padding:3px!'><td style=padding:3px><text style=color:black>22</text></td>&nbsp<td style=padding:3px><text style=color:blue>27</text></td>&nbsp<td style=padding:3px><text style=color:blue>27</text></td>&nbsp<td style=padding:3px><text style=color:blue>27</text></td>&nbsp<td style=padding:3px><text style=color:blue>27</text></td>&nbsp<td style=padding:3px><text style=color:blue>27</text></td>&nbsp<td style=padding:3px><text style=color:black>&nbsp</text></td>&nbsp<td style=padding:3px><text style=color:black>&nbsp</text></td></tr><tr style='padding:3px!'><td style=padding:3px><text style=color:black>22</text></td>&nbsp<td style=padding:3px><text style=color:blue>27</text></td>&nbsp<td style=padding:3px><text style=color:red>32</text></td>&nbsp<td style=padding:3px><text style=color:red>32</text></td>&nbsp<td style=padding:3px><text style=color:red>32</text></td>&nbsp<td style=padding:3px><text style=color:red>32</text></td>&nbsp<td style=padding:3px><text style=color:red>32</text></td>&nbsp<td style=padding:3px><text style=color:black>&nbsp</text></td></tr><tr style='padding:3px!'><td style=padding:3px><text style=color:black>&nbsp</text></td>&nbsp<td style=padding:3px><text style=color:blue>27</text></td>&nbsp<td style=padding:3px><text style=color:red>32</text></td>&nbsp<td style=padding:3px><text style=color:green>37</text></td>&nbsp<td style=padding:3px><text style=color:green>37</text></td>&nbsp<td style=padding:3px><text style=color:green>37</text></td>&nbsp<td style=padding:3px><text style=color:green>37</text></td>&nbsp<td style=padding:3px><text style=color:green>37</text></td></tr><tr style='padding:3px!'><td style=padding:3px><text style=color:black>&nbsp</text></td>&nbsp<td style=padding:3px><text style=color:black>&nbsp</text></td>&nbsp<td style=padding:3px><text style=color:red>32</text></td>&nbsp<td style=padding:3px><text style=color:green>37</text></td>&nbsp<td style=padding:3px><text style=color:green>37</text></td>&nbsp<td style=padding:3px><text style=color:green>37</text></td>&nbsp<td style=padding:3px><text style=color:green>37</text></td>&nbsp<td style=padding:3px><text style=color:green>37</text></td></tr><tr style='padding:3px!'><td style=padding:3px><text style=color:black>&nbsp</text></td>&nbsp<td style=padding:3px><text style=color:black>&nbsp</text></td>&nbsp<td style=padding:3px><text style=color:black>&nbsp</text></td>&nbsp<td style=padding:3px><text style=color:green>37</text></td>&nbsp<td style=padding:3px><text style=color:green>37</text></td>&nbsp<td style=padding:3px><text style=color:green>37</text></td>&nbsp<td style=padding:3px><text style=color:green>37</text></td>&nbsp<td style=padding:3px><text style=color:green>37</text></td></tr></table>




```python
HTML(asvolume(np.rot90(v,axes=(0,1)), color=True))
```




<table><tr style='padding:3px!'><td style=padding:3px><text style=color:black>22</text></td>&nbsp<td style=padding:3px><text style=color:black>22</text></td>&nbsp<td style=padding:3px><text style=color:black>22</text></td>&nbsp<td style=padding:3px><text style=color:black>22</text></td>&nbsp<td style=padding:3px><text style=color:black>22</text></td>&nbsp<td style=padding:3px><text style=color:black>&nbsp</text></td>&nbsp<td style=padding:3px><text style=color:black>&nbsp</text></td></tr><tr style='padding:3px!'><td style=padding:3px><text style=color:blue>27</text></td>&nbsp<td style=padding:3px><text style=color:black>22</text></td>&nbsp<td style=padding:3px><text style=color:black>22</text></td>&nbsp<td style=padding:3px><text style=color:black>22</text></td>&nbsp<td style=padding:3px><text style=color:black>22</text></td>&nbsp<td style=padding:3px><text style=color:black>22</text></td>&nbsp<td style=padding:3px><text style=color:black>&nbsp</text></td></tr><tr style='padding:3px!'><td style=padding:3px><text style=color:red>32</text></td>&nbsp<td style=padding:3px><text style=color:blue>27</text></td>&nbsp<td style=padding:3px><text style=color:black>22</text></td>&nbsp<td style=padding:3px><text style=color:black>22</text></td>&nbsp<td style=padding:3px><text style=color:black>22</text></td>&nbsp<td style=padding:3px><text style=color:black>22</text></td>&nbsp<td style=padding:3px><text style=color:black>22</text></td></tr><tr style='padding:3px!'><td style=padding:3px><text style=color:green>37</text></td>&nbsp<td style=padding:3px><text style=color:red>32</text></td>&nbsp<td style=padding:3px><text style=color:blue>27</text></td>&nbsp<td style=padding:3px><text style=color:blue>27</text></td>&nbsp<td style=padding:3px><text style=color:blue>27</text></td>&nbsp<td style=padding:3px><text style=color:blue>27</text></td>&nbsp<td style=padding:3px><text style=color:blue>27</text></td></tr><tr style='padding:3px!'><td style=padding:3px><text style=color:black>&nbsp</text></td>&nbsp<td style=padding:3px><text style=color:green>37</text></td>&nbsp<td style=padding:3px><text style=color:red>32</text></td>&nbsp<td style=padding:3px><text style=color:red>32</text></td>&nbsp<td style=padding:3px><text style=color:red>32</text></td>&nbsp<td style=padding:3px><text style=color:red>32</text></td>&nbsp<td style=padding:3px><text style=color:red>32</text></td></tr><tr style='padding:3px!'><td style=padding:3px><text style=color:black>&nbsp</text></td>&nbsp<td style=padding:3px><text style=color:black>&nbsp</text></td>&nbsp<td style=padding:3px><text style=color:green>37</text></td>&nbsp<td style=padding:3px><text style=color:green>37</text></td>&nbsp<td style=padding:3px><text style=color:green>37</text></td>&nbsp<td style=padding:3px><text style=color:green>37</text></td>&nbsp<td style=padding:3px><text style=color:green>37</text></td></tr></table>


