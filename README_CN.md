# Optimization Orchestration
> [简单介绍](https://wq-peng.github.io/optOrchestration.html)
Batch Elimination(BE), Iterative Elimination(IE) & Combined Elimination(CE).

选择最佳的编译器优化选项的组合。

实现了该论文提出的算法： [Fast and Effective Orchestration of Compiler Optimizations for Automatic Performance Tuning](https://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.142.4012&rep=rep1&type=pdf)

## 文件
- `main.py`: BE, IE, CE 算法实现
- `target.py`: 接口，**需要根据每个程序调整**

## 使用
1. 新建 `target` 文件夹，之后目标程序相关都会放在该文件夹.
2. 将目标程序放入 `target/` 文件夹
3. 修改 `target.py` 里面的所有函数，从而实现：获取优化选项的列表、编译、运行、获取运行时间、log 
4. 运行：`python main.py`

## 许可证

WTFPL

## 参考文献
Pan Z, Eigenmann R. Fast and effective orchestration of compiler optimizations for automatic performance tuning[C]//International Symposium on Code Generation and Optimization (CGO'06). IEEE, 2006: 12 pp.-332.
