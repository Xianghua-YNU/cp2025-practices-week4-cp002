import numpy as np
import matplotlib.pyplot as plt

class HIVModel:
    def __init__(self, A, alpha, B, beta):
        self.A = A
        self.alpha = alpha
        self.B = B
        self.beta = beta# TODO: 初始化模型参数
    

    def viral_load(self, time):#计算对应时间的病毒载量
        return self.A * np.exp(-self.alpha * time) + self.B * np.exp(-self.beta * time)
        

    def plot_model(self, time):
        viral load = self.viral load (time)#根据所给的时间数据，按照公式计算
        plt. plot(time, viral_load)#绘制模型曲线
        plt. xlabel ('Time (days)')#设置x轴的标签
        plt. ylabel ('Viral Load')
        plt. title ('HIV Viral Load Model.')
        plt. show()#显示图表
        

def load_hiv_data(filepath):
    try:
        data = np.loadtxt(filepath)#加载文件
        return data['time_in days'], data[ 'viral_load']# 从加载的数据中提取'time_in_days'键对应的数据作为时间数据，从加载的数据中提取'viral_load'键对应的数据作为病毒载量数据
    except:
        return p. loadtxt(filepath, delimiter=',', unpack=True)# 如果不是.npz文件，尝试以逗号分隔的格式加载.csv文件


def main():
    model = HIVModel(A=1000,alpha=0.5,B=500, beta=0.1)# 创建HIVModel类的实例，传入初始的模型参数A=1000, alpha=0.5, B=500, beta=0.1
    time = np. linspace(0, 10, 100)# 生成一个从0到10，包含100个等间距点的时间序列
    model. plot_model(time)# 调用模型实例的plot_model方法绘制模型曲线
    time_data, load_data = load_hiv_data('data/HIVseries.npz')# 调用load_hiv_data函数加载HIV数据，传入数据文件路径'data/HIVseries.npz'

    plt. scatter (time_data, load data, label='Experimental Data')# 绘制实验数据点，使用散点图表示
    plt. legend()# 显示图例，用于区分模型曲线和实验数据点
    plt. show()# 显示图表
    

if __name__ == "__main__":
    main()
