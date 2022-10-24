---
layout: page
title: Practical 6
permalink: /practical6/
use_math : true
---

# Objectives

The learning objectives for this practical are:

 * Implement a program in Python that decides if a given number is solitary or
   could have a friend.
 * Implement a program in Python that decides if a given number is highly
   abundant.
 * Implement a program in Python that calculates the percentage of CpG
   dinucleotides in a DNA sequence stored in a FASTA file.
 * Implement a program in Python that calculates the number of `CAG`
   tri-nucleotides, and the position of the first `CAG` tri-nucleotide found,
   in a DNA sequence stored in a FASTA file.
 * Make syntax errors in Python.
 * Correct syntax errors in Python.
 * Debug your program when it doesn't work.

Whenever you are stuck with an error, please consult the section
entitled "Debugging" from [practical 4](/practical4#debugging).

# Setup and background

To do this practical you need an installation of Python version 3. You can find
the instructions in the [setup](/setup/) link on how to install Python version 3
in your system. Once Python is installed, you should be able to call it from
the shell in the terminal window. You can check whether that is possible by typing:

```
$ which python
$ python --version
```

It may happen that you have two Python installations, one corresponding
to version 2.x and another to version 3.x. In that situation the previous command
may say that your Python version is 2.x and to access the version 3 you need to call
the executable `python3`. Try then for instance:

```
$ python3 --version
```

If this is your case, then whenever the executable `python` is invoked in the rest of
this practical, please use `python3` instead.

# Solitary numbers

The Wikipedia [page](https://en.wikipedia.org/wiki/Friendly_number) for friendly
numbers says:

> In number theory, friendly numbers are two or more natural numbers with a
> common abundancy index, the ratio between the sum of divisors of a number and
> the number itself.

Therefore, one says that two positive integer numbers are friendly, or simply
_friends_, if the ratio between the sum of their respective divisors and themselves
is the same. While with this definition we can decide whether two numbers are
friends, there is no criterion to know whether a given number has friends at all.
One says that a positive integer number is
[solitary](https://en.wikipedia.org/wiki/Friendly_number#Solitary_numbers)
if it has no friends and it is known that this happens to those numbers whose
[greatest common divisor (GCD)](https://en.wikipedia.org/wiki/Greatest_common_divisor)
between the sum of its divisors and itself is 1. Remember that the `GCD(x, y)` of
two positive integer numbers `x` and `y` is the largest divisor common to `x` and
`y`.

Implement a program in Python that given a positive integer number, it says
whether that number is solitary our could have a friend, providing some message
with the `print()` function. It is important that the program does *not* ask for
the number, but instead it takes it as the first argument from the Unix shell
command-line call, i.e., by doing something like:

```
$ python solitary.py 10
```

# Highly abundant numbers

The Wikipedia [page](https://en.wikipedia.org/wiki/Highly_abundant_number) for
highly abundant numbers says:

> In mathematics, a highly abundant number is a natural number with the property
> that the sum of its divisors (including itself) is greater than the sum of the
> divisors of any smaller natural number.

Implement a program in Python that given a positive integer number, it says
whether that number is highly abundant or not, providing some message with the
`print()` function. It is important that the program does *not* ask for
the number, but instead it takes it as the first argument from the Unix shell
command-line call, i.e., by doing something like:

```
$ python highlyabundant.py 10
```

# CpG dinucleotides

The Wikipedia[page](https://en.wikipedia.org/wiki/DNA) for DNA says:

> Deoxyribonucleic acid (DNA) is a polymer is a polymer composed of two
> polynucleotide chains that coil around each other to form a double helix.

The nucleotides forming DNA are adenine (denoted by `A`), cytosine (`C`),
guanine (`G`) and thymine (`T`). The Wikipedia
[page](https://en.wikipedia.org/wiki/CpG_site) for a CpG site says:

> CpG is shorthand for 5'—C—phosphate—G—3' , that is, cytosine and guanine
> separated by only one phosphate group; phosphate links any two nucleosides
> together in DNA. The CpG notation is used to distinguish this single-stranded
> linear sequence from the CG base-pairing of cytosine and guanine for
> double-stranded sequences.
> [...]
> CpG dinucleotides have long been observed to occur with a much lower frequency
> in the sequence of vertebrate genomes than would be expected due to random chance.
> [...]
> This underrepresentation is a consequence of the high mutation rate of
> methylated CpG sites.
> [...]
> CpG islands (or CG islands) are regions with a high frequency of CpG sites.
> [...]
> CpG islands typically occur at or near the transcription start site of genes,
> particularly housekeeping genes, in vertebrates.
> [...]
> In cancers, loss of expression of genes occurs about 10 times more frequently
> by hypermethylation of promoter CpG islands than by mutations.

Implement a program in Python that given the name of a FASTA file containing
the DNA sequence of a gene, it calculates the percentage of `CpG` sites for
every line of DNA in the FASTA file. It is important that the program does
*not* ask for the name of the FASTA file, but instead it takes it as the first
argument from the Unix shell command-line call, i.e., by doing something like:

```
$ python cpg.py <filename.fa>
```

Try your program with the DNA of the
[Breast cancer type 1 susceptibility gene (_BRCA1_)](https://www.ncbi.nlm.nih.gov/gene/672),
a tumor suppressor gene encoding a DNA repair enzyme that becomes hypermetilated
in cancer and whose
[role in breast cancer susceptibility](https://en.wikipedia.org/wiki/BRCA1)
was discovered by
[Mary-Claire King](https://en.wikipedia.org/wiki/Mary-Claire_King) (in your
spare time watch this 12-minute [video](https://www.youtube.com/watch?v=tOP5pUIYhv4)
where she explains the few days before she was defending in front of a panel at the
[NIH](https://www.nih.gov) the grant application that was ultimately approved
and allowed her to develop her research on the role of the _BRCA1_ gene as a
breast cancer susceptibility gene). The first 10 lines of output of your program
should be the following percentage values:

```
$ python cpg.py BRCA.fa
5
2
11
14
5
8
11
17
8
0
```

Try also to have a modular design of your program, for instance by having
a function for the calculation of the percentage of `CGs` given a vector of
nucleotides.

# CAG tri-nucleotides

[Hungtingon's disease](https://en.wikipedia.org/wiki/Huntington%27s_disease) is
an hereditary genetic disorder, caused by an expansion of consecutive repetitions
of the `CAG` tri-nucleotide in a gene named after the disease, the
[Huntingtin (_HTT_)](https://www.ncbi.nlm.nih.gov/gene/3064) gene. Unaffected
individuals usually have no more than 30 consecutive repetitions of the `CAG`
tri-nucleotide in the _HTT_ gene, while affected individuals usually have more
than 37.

Implement a program in Python that given the name of a FASTA file containing
the DNA sequence of a gene, it calculates the total number of `CAG` tri-nucleotides
and the position of the first `CAG` tri-nucleotide found in the DNA sequence. It
is important that the program does *not* ask for the name of the FASTA file, but
instead it takes it as the first argument from the Unix shell command-line call,
i.e., by doing something like:

```
$ python cags.py <filename>
```

Try your program with the DNA of the _HTT_ gene. The output for the _HTT_ gene
should this one:

```
$ python cags.py HTT.fa
3982 CAG tri-nucleotides
first CAG at position 33
```

Note that this is a simplified version of the biological question. Your program
needs not to calculate the number of _consecutive_ `CAG` tri-nucleotides, but
simply the total number of `CAG` tri-nucleotides.
