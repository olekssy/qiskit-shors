# Shor's Algorithm
Version 0.1

The implementation of a scalable instance of Shor's algorithm for factoring large integers using a combination of classical and quantum computing algorithms.

## Motivation
The vision of this project is to lower the use barrier for physicists and industry domain experts to engage with quatum algorithms. The goal of this project is to develop a robust, transaprent, and scalable instance of Shor's algorithm, that will become accessible by integrating it into the native Qiskit Aqua repo.

## Abstract
The proliferation of noisy intermediate-scale quantum (NISQ) devices has allowed interested individuals to discover and develop scalable applications of quantum computing (QC). The benefit of quantum computing posits that they can solve real-world problems more efficiently then classical computers. Shor's algorithm is a manifestation of QC's advantage over classical computers. 

As of today, numerous research papers [citations] claim to have implemented Shor's algorithm on NISQ devices to the end of factoring composite integers. However, the methods of [citations] do not reveal the content of the so-called quantum "black-boxes", which presumably contain the an optimized quantum circuit for factorization. Further investigation of current methods revealed that many implementations of Shor's algorithm rely on mapping classical circuits to quantum circuits, without using a single Hadamard gate, thus simply running a classical circuit on the NISQ. 

In addition to the method detailed above, [additional_citations] perform quantum factorization after the results is determined classically.  With the correct result in mind, quantum gates are organized to return the binary of the desired factors, e.g. for n = p * q = 15: p = bin(3) = 11, q = bin(5) = 101. The unusual focus of many researchers on factoring numbers 15 and 21 caused a sequence of publications that reveals the fallacy of their approaches.

A wholly QC based approach to Shor's algorithm requires control of quantum mechanics, mathematics, quantum information, computation science, and high fidelity NISQ devices.

**Thus, none of the papers known to the authors of this article as of today provide DIY instructions for Shor's algorithm.**

## Description
The algorithm presented in [file_name] factors a composite integer n by selecting *random* integers within the range *1 < a < n*, then computes the factors of n by a using Euclid's algorithm. If the *GCD(a,n) > 1*, then *{a,n}* are co-prime numbers. The Algorithm proceeds with factorization via modular exponentiation function period finding. Once even period r is found, the function calculates the first factor *p = a^r/2 - 1*. the second factor can be found by the formula *q = a^r/2 + 1*, or dividing n by the first known factor p.

There is no known efficient algorithm of period finding using the modular exponentiation function on classical computers. However, period finding problem can be solved efficiently by QC. To solve the period finding problem on a QC, the existing problem is mapped to an equivalent quantum Fourier transform (QFT) problem that returns periods of *a (mod n)*.

## Algorithm
0. Initialize composite integer n for factoring
1. Select sample of (random) integers a
2. Verify that {a,n} are co-prime numbers via Euclidean algorithm. If GCD(a,n) > 1, first factor p = GCD(a,n), second factor q = n/p.
3. (a) Classical approach. If GCD(a,n) = 1, proceed with modular exponentiation period finding. Count set of unique remainders r = a^k (mod n) for each a in a sample, where order k -> 128, to avoid exceeding the range of int64. Compute period r.
3. (b) Quantum approach [TBD]. Estimate period r(a) by mapping the problem into QFT. Convert {a,n} into binary, construct the quantum circuit of n + 1 qubits, where additional qubit serves as the q-control for recycling the output of sequential circuits.
4. If r is even, calculate factor p = a^r/2 - 1.
5. Calculate second factor q = n/p
6. (Optional) Check if p and q are prime by initializing them as the input n in the first stage of the algorithm.

## Requirements
Python 3.x, numpy, matplotlib, qiskit-terra, qiskit-aer, qiskit-aqua

## Contributions
The goal is to make Shor's algorithm accessible for everyone by integrating it into the native Qiskit Aqua. The project is under active development, contributions are welcome and highly appreciated.

## Reference
1. IBM Quantum Experience
2. Shor's algorithm
3. Qiskit
