# Shor's Algorithm
Version 0.1

The implementation of a scalable instance of Shor's Algorithm for factoring large integers using combination of Classical and Quantum Computing Algorithms

## Motivation
The vision of this project is to lower the barrier of Quantum computing for a general public, and industry domain experts with no Quantum computing background. The goal of this project is to develop robust, transaprent and scalable instance of Shor's Algorithm, that will become accessible for everyone by integrating it into the native Qiskit Aqua repo.

## Abstract
The era of Noisy Intermediate-Scale Quantum (NISQ) devices is opening doors to a general public, to individuals, who are interested in discovering and developing scalable applications of Quantum Computing (QC), which would allow to solve real-world problems efficiently. Shor's Algorithm is a manifestation of advantage of QC over classical computers. As of today, there are numerous research papers published by authors, who claim that they managed to implement Shor's Algorithm on the real NISQ device and successfully factor composite integer.

For some reason, some authors do not reveal the content of the so-called quantum "black-boxes", which (presumably) contain the quantum circuit that suppose to perform factorization. Investigation of some papers revealed that the problem is "solved" by mapping classical circuits into quantum circuits without using a single Hadamard gate, thus simply running a *classical* circuit on the QC. In some other cases, factorization is performed *after* compiler already knows the answer, and proceeds with constructing conditional (and trivial) circuits that always return the binary of the desired factor, e.g. for n = p * q = 15: p = bin(3) = 11, q = bin(5) = 101. The unusual focus of many researchers on factoring numbers 15 and 21 caused a sequence of publications that reveals the fallacy of their approaches.

The third type of papers requires deep understanding of Quantum mechanics, Mathematics, Quantum information and computation science, that makes the content inaccessible for the average readers outside of the QC domain.

**Thus, none of the papers known to the author of this article as of today provide DIY instructions for Shor's Algorithm.**

## Description
The algorithm factors composite integer n by selecting (random) integers in range *1 < a < n*, computes factors of n by Euclidean algorithm. If *GCD(a,n) > 1*, then *{a,n}* are co-prime numbers. Algorithm proceeds with factorization via Modular Exponentiation function period finding. Once even period r is found, the function calculates first factor *p = a^r/2 - 1*. Second factor can be found by the formula *q = a^r/2 + 1*, or dividing n by the first known factor p.

There is no known efficient algorithm of period finding from Modular Exponentiation function on classical computers. Hence, period finding problem can be solved efficiently by Quantum Computer, s.t. the problem is mapped into Quantum Fourier Transform problem, that returns periods of *a (mod n)*.

## Algorithm
0. Initialize composite integer n for factoring
1. Select sample of (random) integers a
2. Verify that {a,n} are co-prime numbers via Euclidean Algorithm. If GCD(a,n) > 1, first factor p = GCD(a,n), second factor q = n/p.
3. (a) Classical approach. If GCD(a,n) = 1, proceed with Modular Exponentiation period finding. Count set of unique remainders r = a^k (mod n) for each a in a sample, where order k -> 128, to avoid exceeding the range of int64. Compute period r.
3. (b) Quantum approach [TBD]. Estimate period r(a) by mapping the problem into Quantum Fourier Tranform (QFT). Convert {a,n} into binary, construct the quantum circuit of n + 1 qubits, where additional qubit serves as the q-control for recycling the output of sequential circuits.
4. If r is even, calculate factor p = a^r/2 - 1.
5. Calculate second factor q = n/p
6. (Optional) Check if p and q are prime by initializing them as the input n in the first stage of the algorithm.

## Requirements
Python 3.x, numpy, matplotlib, qiskit-terra, qiskit-aer, qiskit-aqua

## Contributions
The goal is to make Shor's Algorithm accessible for everyone by integrating it into the native Qiskit Aqua. The project is under active development, contributions are welcome and highly appreciated.

## Reference
1. IBM Quantum Experience
2. Shor's Algorithm
3. Qiskit
