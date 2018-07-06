import matplotlib.pyplot as plt


def plot_line_graph(x_vals, data_vals_array, data_labels_array, title, fig_number=0, x_label="Time (s)", plot_mars=False):
    """plot line graph
    can supply multiple lines to plot or just one
    remember to use plt.show"""
    plt.figure(fig_number)
    plt.title(title)
    plt.xlabel(x_label)
    plt.grid()

    #emphasise zeros
    plt.axhline(color='k')
    plt.axvline(color='k')
    
    if(isinstance(data_vals_array, list) == False):
        # cast to list if not one already
        data_vals_array = [data_vals_array]
        data_labels_array = [data_labels_array]

    for i in range(0, len(data_vals_array)):
            plt.plot(x_vals, data_vals_array[i], label=data_labels_array[i])
            plt.legend()

    if(plot_mars):
        R =3.39E6
        mars = plt.Circle((0,0), radius=R, fill=False)

        #plot on axes
        fig = plt.gcf()
        ax = fig.gca()
        ax.add_artist(mars)
        ax.set_aspect('equal')
