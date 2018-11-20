# [Reverse Polish Notation](https://en.wikipedia.org/wiki/Reverse_Polish_notation)  Calculator
Implemented in different languages

## Purposes of this repository
- Learn basics of functional programming:
  - [high-order functions](https://en.wikipedia.org/wiki/Higher-order_function)
  - [recursions, recursive data types](https://en.wikipedia.org/wiki/Recursion_(computer_science))
  - [tail call optimization](https://en.wikipedia.org/wiki/Tail_call)
  - [pattern matching](https://en.wikipedia.org/wiki/Pattern_matching)
  - [persistent data sturctures](https://en.wikipedia.org/wiki/Persistent_data_structure)
- Self-education
- Fun
- ...

## Erlang

#### Compile (via interactive shell)
```
$ erl

1> c(rpn).
{ok,rpn}
```
#### Compile (via command-line compiler)
```
$ erlc rpn.erl
```


#### Run (via interactive shell)
```
$ erl

1> 0.0 == rpn:calculate("10 4 3 + 2 * - 16 5 1 - / +").
true
2> 2.0 == rpn:calculate("18 4 3 + 2 * - 2 /").
true
3> ^G, q
```

## Python

#### Run (via interactive shell)

```
$ python3

>>> import(rpn)
>>> 0.0 == rpn.calculate("10 4 3 + 2 * - 16 5 1 - / +")
True
>>> 2.0 == rpn.calculate("18 4 3 + 2 * - 2 /")
True
>>> exit()
```


## Scala

#### Compile (via command-line compiler)
```
$ scalac rpn.scala 
```

#### Run (via interactive shell)
```
$ scala
scala> 0.0 == rpn.calculate("10 4 3 + 2 * - 16 5 1 - / +")
res0: Boolean = true
scala> 2.0 == rpn.calculate("18 4 3 + 2 * - 2 /")
res1: Boolean = true
scala> :q

```