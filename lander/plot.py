import matplotlib.pyplot as plt

def plot_line_graph(x_vals, data_vals_array, data_labels_array, title, fig_number=0, x_label="Time (s)"):
    """plot line graph
    can supply multiple lines to plot or just one
    remember to use plt.show"""
    plt.figure(fig_number)
    plt.title(title)
    plt.xlabel(x_label)
    plt.grid()
    
    if(isinstance(data_vals_array, list) == False):
        # cast to list if not one already
        data_vals_array = [data_vals_array]
        data_labels_array = [data_labels_array]

    for i in range(0, len(data_vals_array)):
            plt.plot(x_vals, data_vals_array[i], label=data_labels_array[i])
            plt.legend()
