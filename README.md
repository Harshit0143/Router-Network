# Router-Network
# Motivation
* Consider a simple computer network consisting of ```routers``` communicating information to one another through ```links``` </br>
* Each pair of ```routers``` communicates through ```links``` between them. 
* To send a large file over a network, it is customary to divide it into ```smaller packets``` (we are linited by the capacity of a link).  
* Having too small packets is undesirable due to a ```per-packet overhead``` involved in the transfer.    
* Therefore,given a source and a destination in the network, we wish to find the size of the ```largest packet```
that can be transferred through the network from the ```source``` to the ```destination```.


# Problem Definition
***Inputs:*** </br>
```n``` :   the number of routers in our network.  
Routers are labeled 0, . . . , n − 1.   

Router Link: ```(u, v, c)``` :  
```u``` and ```v``` : endpoints of the ***bidirectinal*** link.  
```c``` :  capacity of link.   

Such a link is able to transfer a packet of size at most ```c``` from ```u``` to ```v``` and from v to u (every link is bidirectional
and has the same capacity in either direction).

***Output:***</br>
Given the identities ```s``` and ```t``` of the source and the target router
respectively, we wish to determine the largest ```C``` such that a packet of size ```C``` can be transferred over the
network from ```s``` to ```t```. And also report ```one``` such path.   

Assumption: 
The network is connected.
Routers can have zero, one, or more than one links of different capacities between them.

# Required time complexity:
```O(m log m)   ```

# Input Specifications
function ```findMaxCapacity(n, L, s, t)```
1. ```n``` : the number of routers in the network.  
2. ```L``` : a list of 3-tuples of integers. A tuple ```(u, v, c)``` in this list representing a link of
capacity ```c``` between ```u``` and ```v```, where ```u ,v  ∈ {0, . . . , n − 1}```,
3. ```s```: the source router , ```s ∈ {0, . . . , n − 1}``` 
4. ```t```: the target router , ```t ∈ {0, . . . , n − 1}```

# Output Specifications

```findMaxCapacity(n, L, s, t)``` returns a pair ```(C,route)``` where,
1. ```C``` is the largest number such that a packet of size C can be transferred over the network from ```s``` to ```t```.
2. route is a list of numbers from the set ```{0, . . . , n − 1}```such that ```route[0]``` is ```s```, ```route[len(route)-1]```
is ```t```, and for each ```i```, there exists a link of capacity at least ```C``` between ```route[i-1]``` and r```oute[i]```.

# Example Test Cases 
```
findMaxCapacity(3,[(0,1,1),(1,2,1)],0,1) 
(1,[0,1])
findMaxCapacity(4,[(0,1,30),(0,3,10),(1,2,40),(2,3,50),(0,1,60),(1,3,50)],0,3)
(50,[0,1,3])
findMaxCapacity(4,[(0,1,30),(1,2,40),(2,3,50),(0,3,10)],0,3)
(30,[0,1,2,3])
findMaxCapacity(5,[(0,1,3),(1,2,5),(2,3,2),(3,4,3),(4,0,8),(0,3,7),(1,3,4)],0,2)
(4,[0,3,1,2])
findMaxCapacity(7,[(0,1,2),(0,2,5),(1,3,4), (2,3,4),(3,4,6),(3,5,4),(2,6,1),(6,5,2)],0,5)
(4,[0, 2, 3, 5])
```
