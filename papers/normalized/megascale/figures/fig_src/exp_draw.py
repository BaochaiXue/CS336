import matplotlib.pyplot as plt
import numpy as np
import matplotlib
plt.style.use(["double-figure.mplstyle"])
plt.rcParams["font.family"] = "Helvetica"
plt.rcParams["ytick.direction"] = "in"
plt.rcParams["hatch.linewidth"] = 2
plt.rcParams["font.weight"] = "bold"
plt.rcParams["axes.labelweight"] = "bold"

def plot_text(x, y):
    for i in range(len(y)):
        plt.text(x[i], y[i] + 1, \
                "{:.2f}".format(y[i]), fontsize=15, ha='center')

def draw_faults():
    figure_name = "failure_breakdown.pdf"
    xticks = ['CUDA Error', 'SegFault', 'Node Crash', 'NIC Error', 'RDMA Jitter', 'NaN Loss', 'NCCL Timeout', 'Others']

    y_values = [41, 3, 11, 3, 19, 26, 22, 7]
    deno = sum(y_values)
    y_values = [y / deno * 100 for y in y_values]
    ylabel = "Percentage (%)"
    optimus = y_values
    plt.style.use(["double-figure.mplstyle"])

    fig, ax = plt.subplots(figsize=(10,4))
    bar_width = 1
    opacity = 1#0.8
    data_cnt = 1
    xticks_axis = [3 + 7 * i for i in range(len(xticks))]

    start = 0.5 * (data_cnt + 1)
    interval = 0.5 + data_cnt
    xticks_axis = [start + interval * i for i in range(len(xticks))]

    print()
    print("xticks: ", xticks_axis)

    # start_index = [1, 1*(data_cnt+3) + 1, 2*(data_cnt+3) + 1, 3*(data_cnt+3) + 1]
    start_index = [1 + (data_cnt + 0.5) * i for i in range(len(xticks))]
    index = [start_index[i] for i in range(len(optimus))]
    index = np.array(index)
    print("start index: ", index) # [0.5 0.9 1.3 1.7]
    patterns = ["/////", "\\\\\\\\\\"]
    colors = ['#1f77b4', '#d62728', '#9467bd', '#ff7f0e', '#2ca02c', '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf']
    colors = colors[:5][::-1]
    edgecolors = ["dimgrey", "lightseagreen", "tomato", "slategray", "silver"]
    print(colors)
    draw_cnt = 0

    if len(optimus) > 0:
        index = [start_index[i] + draw_cnt*bar_width for i in range(len(optimus))]
        index = np.array(index)
        rects5 = plt.bar(index, optimus, bar_width*0.8,
                        alpha=opacity,
                        color="white",  #
                        align='center',
                        edgecolor=edgecolors[1],
                        hatch="/////",
                        capsize=10,
                        linewidth=1.0)
        draw_cnt += 1
        for i in range(len(optimus)):
            plt.text(index[i], optimus[i] + 1, \
                    "{:.2f}".format(optimus[i]), fontsize=15, ha='center')
    max_y = np.max(optimus)


    ax.set_ylim([0, max_y*1.2])
    plt.xticks(xticks_axis, xticks, weight='medium',  fontsize=15, rotation=20)

    plt.ticklabel_format(axis='y')
    plt.yticks(fontsize=24)
    ax.yaxis.offsetText.set_fontsize(24)

    plt.ylabel(ylabel, fontsize=24)
    plt.tight_layout()
    # plt.savefig("figures/" + figure_name, format='pdf', dpi=500)
    plt.show()

def draw_scaling_52B():
    megatron = [49.2, 48.8, 48.2]
    optimus = [54.3, 54.1, 54.3]
    xticks = ['2240', '4480', '11200']
    xlabels = ['Megatron-LM', 'Optimus']
    ylabel = "MFU (%)"
    figure_name = "530B_scaling.pdf"
    linear_scaling = max([megatron[0], optimus[0]]) * np.array([1, 2])
    print(f"linear_scaling: {linear_scaling}")
    fig, ax = plt.subplots(figsize=(10,4))
    bar_width = 1
    opacity = 1#0.8
    data_cnt = 2
    xticks_axis = [3 + 7 * i for i in range(len(xticks))]

    start = 0.5 * (data_cnt + 1)
    interval = 1 + data_cnt
    xticks_axis = [start + interval * i for i in range(len(xticks))]
    start_index = [1 + (data_cnt + 1) * i for i in range(len(xticks))]
    index = [start_index[i] for i in range(len(optimus))]
    index = np.array(index)
    patterns = ["/////", "\\\\\\\\\\"]
    colors = ['#1f77b4', '#d62728', '#9467bd', '#ff7f0e', '#2ca02c', '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf']
    colors = colors[:5][::-1]
    edgecolors = ["dimgrey", "tomato"]
    draw_cnt = 0
    if len(megatron) > 0:
        index = [start_index[i] + draw_cnt*bar_width for i in range(len(optimus))]
        index = np.array(index)
        rects1 = plt.bar(index, megatron, bar_width*0.8,
                            alpha=opacity,
                            color="white",
                            # color=colors[0],  # (0.9,0.9,0.9),
                            align='center',
                            edgecolor=edgecolors[0],
                            capsize=10,
                            linewidth=1.5,
                            label=xlabels[0],
                            hatch=patterns[0],rasterized=True)
        plot_text(index, megatron)
        draw_cnt += 1

    if len(optimus) > 0:
        index = [start_index[i] + draw_cnt*bar_width for i in range(len(optimus))]
        index = np.array(index)
        rects5 = plt.bar(index, optimus, bar_width*0.8,
                        alpha=opacity,
                        color='white',  #
                        align='center',
                        edgecolor=edgecolors[1],
                        capsize=10,
                        linewidth=1.5,
                        label=xlabels[1],
                        hatch=patterns[1])
        plot_text(index,optimus)
        draw_cnt += 1

    max_y = np.max(linear_scaling)

    
    ax.set_ylim([40, 70])
    plt.xticks(xticks_axis, xticks, weight='medium', fontsize=24)

    plt.ticklabel_format(axis='y')
    plt.yticks(fontsize=24)
    ax.yaxis.offsetText.set_fontsize(24)
    
    legend = ax.legend(loc='upper left', shadow=False, fontsize=24, 
                        fancybox=None, 
                        columnspacing=0.3,
                        labelspacing=0.3,
                        handletextpad=0.5,
                        frameon=False, 
                        bbox_to_anchor=(-0.02,1.03),
                        handlelength=1.5,
                        #borderaxespad=0.5,
                        ncol=2)
    for label in legend.get_texts():
        label.set_fontsize(21)
    plt.ylabel(ylabel, fontsize=24)
    plt.xlabel("#GPUs", fontsize=24)
    plt.tight_layout()
    plt.savefig("figures/" + figure_name, format='pdf', dpi=500)
    plt.show()

def draw_dsp():
    megatron = [57.5, 32.5, 15, 1]
    optimus = [57, 63.2, 67.1, 1]
    xticks = ['8k', '16k', '32k', '64k']
    xlabels = ['Optimus', 'Optimus with DSP']
    ylabel = "MFU (%)"
    figure_name = "long_sequence.pdf"
    fig, ax = plt.subplots(figsize=(10,4))
    bar_width = 1
    opacity = 1
    data_cnt = 2
    xticks_axis = [3 + 7 * i for i in range(len(xticks))]

    start = 0.5 * (data_cnt + 1)
    interval = 2 + data_cnt
    xticks_axis = [start + interval * i for i in range(len(xticks))]

    start_index = [1 + (data_cnt + 2) * i for i in range(len(xticks))]
    index = [start_index[i] for i in range(len(optimus))]
    index = np.array(index)
    patterns = ["/////", "\\\\\\\\\\"]
    colors = ['#1f77b4', '#d62728', '#9467bd', '#ff7f0e', '#2ca02c', '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf']
    colors = colors[:5][::-1]
    edgecolors = ["dimgrey", "tomato"]
    print(colors)
    draw_cnt = 0
    if len(megatron) > 0:
        index = [start_index[i] + draw_cnt*bar_width for i in range(len(optimus))]
        index = np.array(index)
        rects1 = plt.bar(index, megatron, bar_width*0.8,
                            alpha=opacity,
                            color="white",
                            # color=colors[0],  # (0.9,0.9,0.9),
                            align='center',
                            edgecolor=edgecolors[0],
                            capsize=10,
                            linewidth=1.5,
                            label=xlabels[0],
                            hatch=patterns[0],rasterized=True)
        draw_cnt += 1
        plt.text(index[-1] - 0.4, megatron[-1] + 5, 'OOM', fontsize=15)

    if len(optimus) > 0:
        index = [start_index[i] + draw_cnt*bar_width for i in range(len(optimus))]
        index = np.array(index)
        rects5 = plt.bar(index, optimus, bar_width*0.8,
                        alpha=opacity,
                        color='white',  #
                        align='center',
                        edgecolor=edgecolors[1],
                        capsize=10,
                        linewidth=1.5,
                        label=xlabels[1],
                        hatch=patterns[1])
        draw_cnt += 1

    max_y = np.max(optimus)

    
    ax.set_ylim([0, max_y*1.2])
    plt.xticks(xticks_axis, xticks, weight='medium', fontsize=24)

    plt.ticklabel_format(axis='y')
    plt.yticks(fontsize=24)
    ax.yaxis.offsetText.set_fontsize(24)
    
    legend = ax.legend(loc='upper left', shadow=False, fontsize=24, 
                        fancybox=None, 
                        columnspacing=0.3,
                        labelspacing=0.3,
                        handletextpad=0.5,
                        frameon=False, 
                        bbox_to_anchor=(-0.02,1.03),
                        handlelength=1.5,
                        #borderaxespad=0.5,
                        ncol=2)
    for label in legend.get_texts():
        label.set_fontsize(21)
    plt.ylabel(ylabel, fontsize=24)
    plt.xlabel("Length of sequence", fontsize=24)
    ax.set_xlabel("Length of sequence", fontsize=24)
    plt.tight_layout()
    plt.savefig("figures/" + figure_name, format='pdf', dpi=500)
    plt.show()

def draw_scaling_175B():
    megatron= [39.3,74.1, 103.8, 132.7,433.6,851.6,1027.9,1466.8]
    optimus = [49,95.1,136.7,176.9,531.9,1030.9,1315.6,1984]
    megatron = [i * 1000 for i in megatron]
    optimus = [i * 1000 for i in optimus]
    xticks = ['256', '512', '768', '1024','3072','6144','8192','12288']
    xlabels = ['Megatron-LM', 'Optimus']
    ylabel = "Throughput \n(tokens/s)"
    figure_name = "175B_scaling.pdf"
    linear_scaling = max([megatron[0], optimus[0]]) 
    x_value = np.array([int(num) for num in xticks])
    linear_scaling = linear_scaling / 256 * x_value
    print(f"linear_scaling: {linear_scaling}")
    fig, ax = plt.subplots(figsize=(10,4))
    bar_width = 1
    opacity = 1#0.8
    data_cnt = 2
    xticks_axis = [3 + 7 * i for i in range(len(xticks))]

    start = 0.5 * (data_cnt + 1)
    interval = 1 + data_cnt
    xticks_axis = [start + interval * i for i in range(len(xticks))]
    start_index = [1 + (data_cnt + 1) * i for i in range(len(xticks))]
    index = [start_index[i] for i in range(len(optimus))]
    index = np.array(index)
    patterns = ["/////", "\\\\\\\\\\"]
    colors = ['#1f77b4', '#d62728', '#9467bd', '#ff7f0e', '#2ca02c', '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf']
    colors = colors[:5][::-1]
    edgecolors = ["dimgrey", "lightseagreen", "tomato", "slategray", "silver"]
    draw_cnt = 0
    if len(megatron) > 0:
        index = [start_index[i] + draw_cnt*bar_width for i in range(len(optimus))]
        index = np.array(index)
        plt.bar(index, megatron, bar_width*0.8,
                            alpha=opacity,
                            color="white",
                            # color=colors[0],  # (0.9,0.9,0.9),
                            align='center',
                            edgecolor=edgecolors[0],
                            capsize=10,
                            linewidth=1.5,
                            label=xlabels[0],
                            hatch=patterns[0],rasterized=True)
        # plot_text(index, megatron)
        draw_cnt += 1

    if len(optimus) > 0:
        index = [start_index[i] + draw_cnt*bar_width for i in range(len(optimus))]
        index = np.array(index)
        plt.bar(index, optimus, bar_width*0.8,
                        alpha=opacity,
                        color='white',  #
                        align='center',
                        edgecolor=edgecolors[1],
                        capsize=10,
                        linewidth=1.5,
                        label=xlabels[1],
                        hatch=patterns[1])
        # plot_text(index,optimus)
        draw_cnt += 1

    if len(linear_scaling) > 0 and False:
        index = [start_index[i]+0.5 for i in range(len(optimus))]
        index = np.array(index)
        print("Linear scaling",index)
        rects_linear = plt.bar(index, linear_scaling, bar_width*2,
                        alpha=1,
                        fill=False,
                        #color=None,  #
                        align='center',
                        edgecolor='black',
                        capsize=10,
                        label="Linear_Scaling",
                        )
    max_y = np.max(linear_scaling)

    
    # ax.set_ylim([0, max_y*1.2])
    # ax.get_yaxis().set_major_formatter(
    # matplotlib.ticker.FuncFormatter(lambda x, p: format(int(x), ',')))
    plt.xticks(xticks_axis, xticks, weight='medium', fontsize=24)
    # plt.yscale("log")
    # plt.ticklabel_format(axis='y')
    plt.ticklabel_format(style='sci', axis='y', scilimits=(0, 0))

    plt.yticks(fontsize=24)
    ax.yaxis.offsetText.set_fontsize(24)
    
    legend = ax.legend(loc='upper left', shadow=False, fontsize=24, 
                        fancybox=None, 
                        columnspacing=0.3,
                        labelspacing=0.3,
                        handletextpad=0.5,
                        frameon=False, 
                        bbox_to_anchor=(-0.02,1.03),
                        handlelength=1.5,
                        #borderaxespad=0.5,
                        ncol=2)
    for label in legend.get_texts():
        label.set_fontsize(21)
    plt.ylabel(ylabel, fontsize=24)
    plt.xlabel("#GPUs", fontsize=24)
    plt.tight_layout()
    plt.savefig("figures/" + figure_name, format='pdf', dpi=500)
    plt.show()

# draw_faults()
# draw_scaling_52B()
# draw_dsp()
draw_scaling_175B()