# Optimization Orchestration

[中文README](README_CN.md)

Batch Elimination(BE), Iterative Elimination(IE) & Combined Elimination(CE).

Algorithms to find the best combination of compiler optimization flags.

Implementation of paper: [Fast and Effective Orchestration of Compiler Optimizations for Automatic Performance Tuning](https://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.142.4012&rep=rep1&type=pdf)

## Contents
- `main.py`: BE, IE, CE algorithms
- `target.py`: interfaces, **required customization** for different program

## Usage
1. Create a directory named `target` where things related to your target program reside.
2. Put your target programe in `target/`
3. customize all function in `target.py` to define your customized way to get optimization, compile, execute, and retrive execution time and log.
4. run with `python main.py`

## Licence
In the hope that this piece of code would be useful, no copyright is left and welcome to make any use of it.

## Reference
Pan Z, Eigenmann R. Fast and effective orchestration of compiler optimizations for automatic performance tuning[C]//International Symposium on Code Generation and Optimization (CGO'06). IEEE, 2006: 12 pp.-332.
