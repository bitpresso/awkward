# awkward - Awkward Sentence Checker

`awkward` is a python script to check if sentence is awkward.

This script uses **2-character markov chain** to calculate that a next character is valid. For this action, you should have a text file to create state transition probability matrix. If you don't have a large text file, you can use big.txt file in this repository.

`awkward` is tested on Python 2.7.6 and Python 3.4.3

## Preparation

You have to install [`pykov`](https://github.com/riccardoscalco/Pykov) python module first to use `awkward`.

### Install `pip`

```
$ sudo easy_install pip
```

### Install `pykov`

```
$ sudo pip install git+git://github.com/riccardoscalco/Pykov@master
```

### Download `awkward`
```
$ git clone https://github.com/bitpresso/awkward.git
```

## Usage

Sentence checking by `awkward` has two steps.

1. Generate a matrix file from text file using `matrix-generator`.
1. Check a sentence using `sentence-checker`


### matrix-generator
```
usage: matrix-generator [-h] [-v] [-f FILE] [-o OUTPUT]
                        [sentence [sentence ...]]

Generate or update the state transition probaility matrix from text files or
input sentences.

positional arguments:
  sentence              sentences to update the matrix

optional arguments:
  -h, --help            show this help message and exit
  -v, --verbose         print the matrix
  -f FILE, --file FILE  a text file to update the matrix
  -o OUTPUT, --output OUTPUT
                        an output file to save the matrix
```

### sentence-checker
```
usage: sentence-checker [-h] [-v] -f FILE [sentence [sentence ...]]

Check if the sentence is awkward.

positional arguments:
  sentence              sentences you want to check if it is awkward

optional arguments:
  -h, --help            show this help message and exit
  -v, --verbose         print the matrix
  -f FILE, --file FILE  a state transition probability matrix file
```

## Example

```
$ python3 matrix-generator -f txt/big.txt -o big.mat
Add text from txt/big.txt
  Add 128457 lines ...
Completed!
Save matrix to big.mat
  Store 587 items ...
Completed!

$ python3 sentence-checker -f big.mat Therefore it is upon the logic rather than upon the crime that you should dwell. You have degraded what should have been a course of lectures into a series of tales.
Load matrix from big.mat
  Restore 587 items ...
Completed!
--------------------------------------------------------------------------------
Therefore it is upon the logic rather than upon the crime that you should dwell. You have degraded what should have been a course of lectures into a series of tales.
--------------------------------------------------------------------------------
This sentence is natural!

$ python3 sentence-checker -f big.mat Phasellus vitae tellus scelerisque purus vestibulum accumsan ac in lectus. Donec ullamcorper, tortor eget dictum lobortis, mauris felis vestibulum nisl, ultricies gravida neque mauris eget massa.
Load matrix from big.mat
  Restore 587 items ...
Completed!
--------------------------------------------------------------------------------
Phasellus vitae tellus scelerisque purus vestibulum accumsan ac in lectus. Donec ullamcorper, tortor eget dictum lobortis, mauris felis vestibulum nisl, ultricies gravida neque mauris eget massa.
--------------------------------------------------------------------------------
This sentence is [awkward]!

```

You can check other test cases in this page.  
<https://github.com/bitpresso/awkward/blob/master/TestCase.md>

## References

### Markov chain
- <http://secom.hanbat.ac.kr/or/chapter1/right04.html>
- <http://electronicsdo.tistory.com/83>
- [Pykov is a tiny Python module](https://github.com/riccardoscalco/Pykov)

### Python
- [Python documentation](https://docs.python.org/3/)
- [점프 투 파이썬](https://wikidocs.net/book/1)
- Nice guys in [StackOverflow](http://stackoverflow.com)
- And God [Google](https://www.google.com)!
