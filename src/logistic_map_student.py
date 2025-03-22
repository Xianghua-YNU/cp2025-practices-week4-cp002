import numpy as np
import matplotlib.pyplot as plt

def iterate_logistic(r, x0, n):
    """
    迭代Logistic映射
    参数:
        r: 增长率参数
        x0: 初始值
        n: 迭代次数
    返回:
        x: 迭代序列数组
    """
    x = np.zeros(n)
    x[0] = x0
    for i in range(1, n):
        x[i] = r * x[i - 1] * (1 - x[i - 1])
    return x

def plot_time_series_subplots(r_values, x0, n):
    """
    绘制四幅子图，分别对应不同 r 值的时间序列
    参数:
        r_values: 不同的 r 值列表
        x0: 初始值
        n: 迭代次数
    返回:
        fig: matplotlib图像对象
    """
    fig, axs = plt.subplots(2, 2, figsize=(12, 8))
    fig.suptitle("Logistic 映射时间序列 (前60次迭代)")
    
    for i, r in enumerate(r_values):
        x = iterate_logistic(r, x0, n)
        ax = axs[i // 2, i % 2]
        ax.plot(range(n), x, label=f"r={r}")
        ax.set_xlabel("迭代次数")
        ax.set_ylabel("x 值")
        ax.legend()
        ax.set_title(f"r = {r}")
    
    plt.tight_layout()
    return fig

def plot_bifurcation(r_min, r_max, n_r, n_iterations, n_discard):
    """
    绘制分岔图（费根鲍姆图）
    参数:
        r_min: r的最小值
        r_max: r的最大值
        n_r: r的取值个数
        n_iterations: 每个r值的迭代次数
        n_discard: 每个r值丢弃的初始迭代点数
    返回:
        fig: matplotlib图像对象
    """
    r_values = np.linspace(r_min, r_max, n_r)
    x = np.zeros(n_iterations)
    fig, ax = plt.subplots(figsize=(10, 6))
    
    for r in r_values:
        x[0] = 0.5  # 初始值
        for i in range(1, n_iterations):
            x[i] = r * x[i - 1] * (1 - x[i - 1])
        ax.plot([r] * (n_iterations - n_discard), x[n_discard:], ',k', alpha=0.25)
    
    ax.set_title("Logistic 映射分岔图（费根鲍姆图）")
    ax.set_xlabel("r 值")
    ax.set_ylabel("x 值")
    return fig

def main():
    """主函数"""
    # 实验1：时间序列分析
    r_values = [2.0, 3.2, 3.45, 3.6]
    x0 = 0.5
    n = 60
    
    fig1 = plot_time_series_subplots(r_values, x0, n)
    fig1.savefig("logistic_time_series_subplots.png", dpi=300)
    plt.close(fig1)
    
    # 实验2：分岔图分析
    fig2 = plot_bifurcation(2.6, 4.0, 1000, 250, 100)
    fig2.savefig("bifurcation_feigenbaum.png", dpi=300)
    plt.close(fig2)

if __name__ == "__main__":
    main()
