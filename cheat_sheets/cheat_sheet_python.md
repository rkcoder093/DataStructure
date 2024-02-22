# **Cheat Sheet for PYTHON for DSA**
*input in python -* `input()`

*output in python -* `print(sub=?, end=?, flush=?)`
****
### **Data types**
1. *int - integer*
2. *float -  decimal value*
3. *complex -  for complex number eg 2i+4j*
4. *bool - for boolean values*
5. *str - string or character*
6. *List - for store multiple data*
7. *sets - diffrent type of but but not copied one*
8. *tuples - collections of data it store*
9. *dictonary - stor the data in key and value pair*
10. *None - it is null value*
****
### **if-else statement**
    if (condition):
        //Statements
    elif(condition):
        //statement
    else:
        //statement
### **Switch Case**
    swithch(condition):
        //Statements
    case1(condition):
        //statement
    case2(condition):
        //statement
    case3(condition):
        //statement
        Break
    case4(condition):
        //statement
    default:
        //statement
****
### Loops
*for Loop*

    for i in sequence:
        //Statement

*while Loop*

    while(condition):**
        //Statement
        //Statement to break the loop
*****
*Functions*
    
    def <function_name>(): -> None
        //statements
****
**Time Complexity**
*The rate at which the time, required to run a code, changes with respect to the input size, is considered the time complexity.*

**Space Complexity**
*the memory space that a code uses while being executed.*
****


**Lists** - *List is an collection of multiple datatype it can be multiple is it can not be,it is accesable by the indexing as left to right it is start from 0 and from right to left it start from -1. <u>list is mutable.</u> Creating the list the square bracker **[ ]***

**Example**
**`list1 = [1,2,3,4,'dog',True,3.2,'C']`**

`Example list = [1,2,3,4,'dog',True,3.2,'C']`
| **Functions** | **Description** | **Examples** |
|---|----|-----|
| `list[index]` | 0 is the index to access the list element | `list[3]` `list[-1]` |
|`list[start:end]` | return the elemnt form the start index to end index | `list1[1:5]`|
| `append()` | use to add the element at the end | `list1.append('cat')`|
| `count()` | use to count the element | `list1.count(1)` |
| `insert()` | insert the element on the specified index | `list1.inser(0,'False') `| 
| `pop()` | remove the last element from the list |  `list.pop()` |
| `remove()` | remove the given object from the list | `list1.remove(3.2)` |
| `del[a:b]` |  delete all the elment fron start a index till b index | `list1.del[1:3]`|
|`extend()` | this is used too add the list to the another list | `list1.extend(list2)`|
| `reverse()` | return the reversed list | `list1.reverse()`|
| `sort()` | arrange the list in accending or decending or user defined order | `list1.sort()` |  
| `min()` | return the minimum element from the list | `min(list1)`|
| `max()` | return the maximun element from the list | `max(list1)` |
| `len()` | return the length of the list | `len(list1)`|
| `clear()` | remove all the element form the list | `list1.clear()`|

****
**Tuple -**  *it is simolar to the list but it is not mutable once created it is not modified, tuple can also contian multiple types of elment like list. tuple is creating with the Parentheses **( )***

**Example:**  `tup = (1,2,3,'Dog','Cat',True)`

| **Functions** | **Description** | **Examples** |
|---|----|-----|
|`tup[index]`| return the elemnt present in the index | `tup[3]`|
| `tup[start:end]` | slicing in tuple | `tup[1:4] `| 
|`all()`|Returns true if all element are true or if tuple is empty| `tup.all()`|
| `any()`|return true if any element of the tuple is true. if tuple is empty, return false | `tup.any()`|
|`len()` |Returns length of the tuple | `tup.len()`|
| `enumerate()`|Returns enumerate object of tuple | `obj = enumerate(tup)`|
|`max()`|return maximum element of given tuple| `max(tup)`|
| `min()`|	return minimum element of given tuple |`min(tup)`|
|`sum()`|Sums up the numbers in the tuple | `sum(tup)`|
| `sorted()`| input elements in the tuple and return a new sorted list | `sorted(tup)`|
|`tuple()`|	Convert an iterable to a tuple. | `tuple('PYTHON')`| 
****

**Set-** *unordered collection data type that is iterable, mutable and has no duplicate elements. set is an unordered so we cannot access the element by the index.*

**Example:** `s = {1,2,3,5,'dog', False}`

| **Functions** | **Description** | **Examples** |
|---|----|-----| 
|`add()` | add the element to the set | `s.add('d')` |
| `update()` | add element to teh set | `s.update(another_set)`|
|`frozenset()`|  immutable objects that only support methods and operators that produce a result without affecting the frozen set | `frozenset(["e", "f", "g"])`|
| `union()` |  marge two sets into one | `s.union(another_set)`  or ` s \| another_set`|
| `intersection()` | find the common element form the two sets| `s.intersection(another_set)` or `s & another_set`|
|`difference()` | findign diffrend form  the sets | `s.difference(another_set)` or `s - another_set`|
| `clear()` | cleat the set | `s.clear()`|
| `pop()` | remove the elemnt from the set one by one |` pop(s)`|
|`remove()` remove the element form the set | ` s.remove(2)`|
|`discard()` | remove the element from the set | `s.discard(3)`| 
****
**String:** *Strings is the immutable array of bytes representing Unicode characters.*

|**operations**| **Examples**|
|-----|------|
| Creating a String | `str = 'string'` or `str = "string"` or `str='''string'''`  
| Access the character of String | `str[0]` |
| strign slicing  | `str[2:6]`|
| reverse the string | by slicing method `str[::-1]` or `reversed(str)`|
| length of the string | `len(str)` |
****
**Dictionary:** *unordered collection of data that stores data in the format of key:value pair*

**Example:** `Dict = {1 : 'dog', 2:"cat", 3 :678, 4 : True, 5:False}`

**Description** | **Examples** |
|----|-----| 
|accessing the value by the key | `Dict[1]` or `Dict.get(2)` |
|add or modify items in a dictionary by assigning values to new or existing keys |  `my_dict['d'] = 4` or `my_dict['a'] = 100`|
|emove items from a dictionary using the `del` keyword or the `pop()` method | `del my_dict['a'] ` or `my_dict.pop('b')`|
| Returns a view object that displays a list of all the keys in the dictionary `keys()` | `my_dict.keys()` |
|  view object that displays a list of all the values in the dictionary `values() `| `my_dict.values()`|
view object that displays a list of tuples containing the key-value pairs `items()` | `my_dict.items()` |
|Removes all items from the dictionary `clear()` | `my_dict.clear()` | 
|Returns a shallow copy of the dictionary `copy()`| `my_dict.copy()` |
|Updates the dictionary with elements from another dictionary or from an iterable of key-value pairs `update()` | `my_dict.values(another_dict)`|2
****

**Matrix:** *A matrix is a 2D array where each element is of strictly the same size. To create a matrix we will be using the NumPy package*

**Bytearray** *Python Bytearray gives a mutable sequence of integers in the range 0 <= x < 256.*

**Example of bytearray** 
- `a = bytearray((12, 8, 25, 2))`
- `print(a)`
- output - `bytearray(b'\x0c\x08\x19\x02')`

### Hashing 

*Hashing is nothing but the two steps invilved in it first is pre-storing by hashing and another is fetching.*
