## Lecture			Whenever you want!
Lab				the most important part of this course
Discussion		the most important part of this course
Office hours		the most important part of this course
Tutoring			the most important part of this course
Textbook		composingprograms.com

## 01 assignment
```python
from math import pi 
a=2*pi
```

## 02-functions
defining functions
function v.s. assignment: much powerful way of abstraction
```python
def <name>(<formal params>):
    return expression

```

### looking up environment

environment is sequence of frame
local frame-->global frame

finish textbook 1.1/1.2

- finish installing
- first example

dealing with errors
- test incrementally
- separate them 
- check assumptions
- consult others

### 1.2elements of programing

describing a language, with three mechanism
- primitive expressions and statements.
- means of combination
- means of abstraction

two kinds of elements: functions and data, but which is not clearly distinct.

expressions/standard lib/names and environment
http://docs.python.org/py3k/library/index.html
python standard lib
from now on to read the instructions from the source and it tells you all about everything want to be familiar with

names can be carried: = assignment /import statement
assignment operator is the simplest means of abstraction.

the interpreter must keep track of the names and that is environment
pure functions and non-pure
 pure is good, in chapter4 chapter 2 will show some non-pure


---

## conditional statements
from compound statements, always executed
but conditional is 
if <condition>
    <statement>
elif <condition>
    <statement>
else
    <statement>

while i<3:
    i=i+1
    total=total+i


## iteration example
fibonacci sequence
```python
def fib(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fib(n-1)+fib(n-2)

def fib(n):
    pred,curr=0,1
    k=1
    while k<n:
        pred,curr=curr,pred+curr
        k=k+1
    return curr
```

## return statements
return is completion of a call progress, which goes back to the previous environment
```python
def end(n,d):
    """print the final digits of n in reverse order until d is found"""
    while n>d:
        print(n%10)
        n=n/10
        if d==last:
            return None
```

## design functions
function behave is the relationship between teh input and output

design a round() that takes the number and digits
```python
def round(n,digits):
    if digits==0:
        return n
    else:
        return round(n/10,digits-1)*10+n%10
```
without repeating itself
>see ./round.py

## control
try to write a function does like if
```python
def if_(true1,ret1,false1):
    if true1:
        return ret1
    else:
        return false1
```

## conditional expression

``<consequent> if <predicate> else <alternative>``

## book chapter 1.3/1.4/1.5

### 1.3 defining new functions
