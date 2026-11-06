# import matplotlib.pyplot as plt
#
# def bld_plot_2(xaxis1, xaxis2, xaxis3, yaxis, xlabel, ylabel, plot_label):
#     fig = plt.figure()
#     fig.patch.set_facecolor('#32384D')
#     fig.patch.set_alpha(0.9)
#
#     ax = fig.add_subplot(111)
#     ax.patch.set_facecolor('#000000') # in
#     ax.patch.set_alpha(1)
#
#     plt.plot(yaxis, xaxis1, color='#D8412F', label='Ukb=0V ', linewidth=2.5)
#     plt.plot(yaxis, xaxis2, color='#3F681C', label='Ukb=5V ', linewidth=2.5)
#     plt.plot(yaxis, xaxis3, color='#FAAF08', label='Ukb=10V', linewidth=2.5)
#     plt.xlabel(xlabel)
#     plt.ylabel(ylabel)
#     plt.title(plot_label)
#     plt.legend(loc='lower left')
#     plt.grid()
#     plt.show()
#
# gr_ueb = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
# gr_1_ie = [0, 0, 0, 0, 0, 0.001, 0.059, 1.205, 16.47, 51.39]
# gr_2_ie = [0, 0, 0, 0, 0, 0.007, 0.270, 7.341, 77.70, 203.5]
# gr_3_ie = [0, 0, 0, 0, 0, 0.008, 0.282, 9.722, 79.94, 230.7]
#
# bld_plot_2(gr_1_ie, gr_2_ie, gr_3_ie, gr_ueb, 'Ukb - (V)', 'Ik - (mA)', 'Schedule 1')

# LAB_3 Graf 1

import matplotlib.pyplot as plt
# Build graph func

def bld_plot_2(yaxis1, yaxis2, yaxis3, xaxis, xlabel, ylabel, plot_label):
    fig = plt.figure()
    fig.patch.set_facecolor('#32384D')
    fig.patch.set_alpha(0.9)

    ax = fig.add_subplot(111)
    ax.patch.set_facecolor('#000000') # in
    ax.patch.set_alpha(1)
    plt.plot(xaxis, yaxis1, color='#D8412F', label='Uke=0 V', linewidth=2.5)
    plt.plot(xaxis, yaxis2, color='#3F681C', label='Uke=5 V', linewidth=2.5)
    plt.plot(xaxis, yaxis3, color='#FAAF08', label='Uke=10V', linewidth=2.5)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(plot_label)
    plt.legend(loc='upper left')
    plt.grid()
    plt.show()


gr_ube = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
# fill next 3 lists /w experimental data
gr_1_ib = [0, 0, 0, 0, 0.000002, 0.000063, 0.002698, 0.0751, 3.06, 20.06]
gr_2_ib = [0, 0, 0, 0, 0.000001, 0.0000061, 0.00011, 0.002345, 0.11, 0.809]
gr_3_ib = [0, 0, 0, 0, 0.000001, 0.0000052, 0.000104, 0.002392, 0.09444, 0.808]

bld_plot_2(gr_1_ib, gr_2_ib, gr_3_ib, gr_ube, 'Ube - (V)', 'Ib - (mA)', 'Schedule 1')




# LAB_3 Graf 2
# Build graph func
def bld_plot_2(yaxis1, yaxis2, xaxis, xlabel, ylabel, plot_label):
    fig = plt.figure()
    fig.patch.set_facecolor('#32384D')
    fig.patch.set_alpha(0.9)

    ax = fig.add_subplot(111)
    ax.patch.set_facecolor('#000000')  # in
    ax.patch.set_alpha(1)

    plt.plot(xaxis, yaxis1, color='#3F681C', label='Ib=0.1 mA', linewidth=2.5)
    plt.plot(xaxis, yaxis2, color='#FAAF08', label='Ib=0.2 mA', linewidth=2.5)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(plot_label)
    plt.legend(loc='lower right')
    plt.grid()
    plt.show()


gr_uke = [0, 1, 2, 3, 4, 5, 6, 7, 8]
# fill next 3 lists /w experimental data
gr_1_ik = [0.0940, 16.28, 16.92, 17.70, 19.69, 19.90, 19.99, 20.13, 20.30]
gr_2_ik = [0.2210, 27.90, 31.31, 32.19, 32.23, 33.80, 33.98, 34.50, 35.08]

bld_plot_2(gr_1_ik, gr_2_ik, gr_uke, 'Uke - (V)', 'Ik - (mA)', 'Schedule 2')
