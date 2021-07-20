from get_configuration import get_configuration
from scipy.stats import t
import numpy as np
import matplotlib.pyplot as plt

def delim_read(file_path, row_offset, col_offset):
    with open(file_path) as g:
        data = [line for line in g.readlines()]

    data = [line.strip().split(';') for line in data][row_offset:]
    read_data = np.zeros((len(data), max([len(line) for line in data]) - col_offset))

    for row in range(len(data)):
        if(col_offset < len(data[row])):
            data_available = np.array(data[row][col_offset:])
            read_data[row,:len(data_available)] =  data_available

    return read_data

def plot_generic_result(row_offset, col_offset, y_label, app_type, calculate_percentage):

    # number of mobile devices, axis common to most plots
    folder_path = get_configuration(1)
    num_simulations = get_configuration(3)
    step_of_axis = get_configuration(4)
    scenario_type = get_configuration(5)
    legends = get_configuration(6)
    mobile_device_loop_start = get_configuration(10)
    mobile_device_loop_step = get_configuration(11)
    mobile_device_loop_end = get_configuration(12)
    num_mobile_devices = (mobile_device_loop_end - mobile_device_loop_start)/mobile_device_loop_step + 1

    #x_tick_label_coefficient = get_configuration(6)
    #pos = get_configuration(9) # position of figure

    all_results = np.zeros((num_simulations, len(scenario_type), num_mobile_devices))
    min_results = np.zeros((len(scenario_type), num_mobile_devices))
    max_results = np.zeros((len(scenario_type), num_mobile_devices))

    for s in range(num_simulations):
        for i in range(len(scenario_type)):
            for j in range(num_mobile_devices):
                mobile_device_number = mobile_device_loop_start + mobile_device_loop_step * j
                file_path = folder_path + '/ite' +  str(s + 1) + '/SIMRESULT_TWO_TIER_WITH_EO_' + scenario_type[i] +  '_' + str(mobile_device_number) + 'DEVICES_' + app_type + '_GENERIC.log'
                file = open(file_path,"r")

                # read everything into an array
                read_data = delim_read(file_path, row_offset, 0)
                value = read_data[0, col_offset - 1]
                if calculate_percentage == 'percentage_for_all':
                    read_data = delim_read(file_path, 1, 0)
                    total_task = read_data[0, 0] + read_data[0, 1]
                    value = (100 * value) / total_task
                elif calculate_percentage == 'percentage_for_completed':
                    read_data = delim_read(file_path, 1, 0)
                    total_task = read_data[0,0]
                    value = (100 * value) / total_task
                elif calculate_percentage == 'percentage_for_failed':
                    read_data = delim_read(file_path, 1, 0)
                    total_task = read_data[0,1]
                    value = (100 * value) / total_task
                all_results[s,i,j] = value

    if(num_simulations == 1):
        results = all_results
    else:
        results = np.mean(all_results, axis = 0)

    #results = squeeze(results)

    for i in range(len(scenario_type)):
        for j in range(num_mobile_devices):
            x = all_results[:, i, j]                        # data
            SEM = np.std(x, axis = 0) / np.sqrt(len(x))     # standard error
            ts = t.ppf([0.05,  0.95], len(x) - 1)           # T-score
            CI = np.mean(x, axis = 0) + ts * SEM            # confidence intervals

            if(CI[0] < 0):
                CI[0] = 0

            if(CI[1] < 0):
                CI[1] = 0
            min_results[i,j] = results[i,j] - CI[0]
            max_results[i,j] = CI[1] - results[i,j]

    types = np.zeros((1, num_mobile_devices))
    for i in range(num_mobile_devices):
        types[0][i] = mobile_device_loop_start + i * mobile_device_loop_step

    x_index = [mobile_device_loop_start + i * mobile_device_loop_step for i in range(num_mobile_devices)]
    plt.figure().clear()
    for i, scenario_type in enumerate(scenario_type):
        plt.plot(x_index, results[i,:], label = scenario_type)

    plt.legend()

    figure_name = '_'.join(y_label) + '.png'
    print(figure_name)
    plt.savefig(figure_name)
