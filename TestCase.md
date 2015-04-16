
# Tests of matrix-generator

```
./matrix-generator
./matrix-generator -v
./matrix-generator -f
./matrix-generator -f txt/big.txt -o big.matrix
```


# Tests of sentence-checker

```
./sentence-checker
./sentence-checker -v
./sentence-checker -f
./sentence-checker -f big.matrix [sentence]
```

## Sentences in big.txt

### sentence includes special characters : natural
> "The paper was made in Bohemia," I said.

> Distributed Proofreading Team at http://www.pgdp.net

### code-style sentence : natural
> "if ord(c) > 127 and c not in s:"

> "print i, c, ord(c), big[max(0, i-10):min(N, i+10)]"

### normal sentence : natural
> This header should be the first thing seen when viewing this Project Gutenberg file.

### long sentence : natural
> "At the same time," he remarked after a pause, during which he had sat puffing at his long pipe and gazing down into the fire,

### long sentence : natural
> Therefore it is upon the logic rather than upon the crime that you should dwell. You have degraded what should have been a course of lectures into a series of tales.

### very long sentence : [awkward]
> "you can hardly be open to a charge of sensationalism, for out of these cases which you have been so kind as to interest yourself in, a fair proportion do not treat of crime, in its legal sense, at all. The small matter in which I endeavoured to help the King of Bohemia, the singular experience of Miss Mary Sutherland, the problem connected with the man with the twisted lip, and the incident of the noble bachelor, were all matters which are outside the pale of the law. But in avoiding the sensational, I fear that you may have bordered on the trivial."

## Sentences in README.md of pykov

### sentence includes special characters : natural
> "Since Pykov describes the chain with a right stochatic matrix, the steady state $x$ satisfies at the condition $p=pT$ and it is calculated with the inverse iteration method $Q^t x = e$, where $Q = I - T$ and $e = (0,0,...,1)$."

### normal sentence : natural
> You can define a Markov chain from scratch or read it from a text file according specific format.

### long sentence : natural
> The pykov.Chain class inherits from pykov.Matrix class. The OrderedDict key is a tuple of states, the OrderedDict value is the transition probability to go from the first state to the second state, in other words pykov describes the transitions of a Markov chain with a right stochastic matrix.

### long sentence : [awkward]
> Pykov is versatile, being it able to manipulate the chain, inserting and removing nodes, and to calculate various kind of quantities, like the steady state distribution, mean first passage times, random walks, absorbing times, and so on.

## Sentences in [Lorem ipsum](http://ko.wikipedia.org/wiki/%EB%A1%9C%EB%A0%98_%EC%9E%85%EC%88%A8)

### normal sentence : natural
> Lorem ipsum dolor sit amet, consectetur adipiscing elit.

### normal sentence : [awkward]
> Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus.

### long sentence : [awkward]
> Phasellus vitae tellus scelerisque purus vestibulum accumsan ac in lectus. Donec ullamcorper, tortor eget dictum lobortis, mauris felis vestibulum nisl, ultricies gravida neque mauris eget massa.

### long sentence : [awkward]
> Aliquam mauris ligula, condimentum in placerat lobortis, ultrices a est. Suspendisse tempus nibh non lectus mattis euismod. Nam consequat volutpat lacus, vel vehicula quam pharetra sit amet.

### very long sentence : [awkward]
> Sed augue eros, varius eget tempus eu, malesuada et tortor. In lectus risus, imperdiet a aliquet eget, blandit ac sapien. Proin placerat mattis nisi, et ornare mi sodales sit amet. Sed posuere purus vitae ante faucibus ullamcorper vulputate nisl facilisis. Nunc mattis metus vel ante semper nec lacinia neque consequat. In vitae odio nec lacus posuere vehicula at nec mi. Vestibulum ut neque mi, ut ultrices ipsum. Sed nibh velit, commodo eget semper vel, consectetur eget mi. Duis mollis nibh eget justo fringilla condimentum.
