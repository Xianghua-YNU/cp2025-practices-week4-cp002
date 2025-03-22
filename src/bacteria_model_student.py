import os
import numpy as np
import matplotlib.pyplot as plt


class BacteriaModel:
    def __init__(self, A, tau):
        self.A = A
        self.tau = tau

    def v_model(self, t):
        return 1 - np.exp(-t / self.tau)

    def w_model(self, t):
        return self.A * (np.exp(-t / self.tau) - 1 + t / self.tau)

    def plot_models(self, t, save_path=None):
        v = self.v_model(t)
        w = self.w_model(t)

        plt.plot(t, v, label='V(t)')
        plt.plot(t, w, label='W(t)')
        plt.xlabel('Time')
        plt.ylabel('Response')
        plt.title('Bacteria Growth Models')
        plt.legend()

        if save_path:
            # 确保保存路径的文件夹存在
            os.makedirs(os.path.dirname(save_path), exist_ok=True)
            plt.savefig(save_path)  # 保存图像到指定路径
        else:
            plt.show()


def load_bacteria_data(filepath):
    try:
        data = np.loadtxt(filepath, delimiter=',')
        return data['time'], data['response']
    except Exception as e:
        print(f"Error loading data: {e}")
        return np.loadtxt(filepath, delimiter=',', unpack=True)


def main():
    # 初始化模型参数
    model = BacteriaModel(A=1.0, tau=2.0)

    # 生成时间序列
    t = np.linspace(0, 10, 100)

    # 绘制模型曲线并保存
    model.plot_models(t, save_path=r"C:\Users\84786\Desktop\1\model_plot.png")

    # 加载实验数据
    time_data, response_data = load_bacteria_data(r"C:\Users\84786\Desktop\1\g149novickA.txt")

    # 绘制实验数据并保存
    plt.scatter(time_data, response_data, label='Experimental Data')
    plt.legend()
    os.makedirs(r"C:\Users\84786\Desktop\1", exist_ok=True)  # 确保文件夹存在
    plt.savefig(r"C:\Users\84786\Desktop\1\experimental_data.png")  # 保存实验数据图
    plt.show()


if __name__ == "__main__":
    main()
