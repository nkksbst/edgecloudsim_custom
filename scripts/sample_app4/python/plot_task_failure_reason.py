from plot_generic_result import plot_generic_result

def plot_task_failure_reason():

    plot_generic_result(1, 10, ['Failed Task due to VM Capacity (%)'], 'ALL_APPS', 'percentage_for_failed')
    plot_generic_result(1, 10, ['Failed Task due to VM Capacity','for Augmented Reality App (%)'], 'AUGMENTED_REALITY', 'percentage_for_failed')
    plot_generic_result(1, 10, ['Failed Task due to VM Capacity','for Health App (%)'], 'HEALTH_APP', 'percentage_for_failed')
    plot_generic_result(1, 10, ['Failed Task due to VM Capacity','for Infotainment App (%)'], 'INFOTAINMENT_APP', 'percentage_for_failed')
    plot_generic_result(1, 10, ['Failed Task due to VM Capacity','for Heavy Computation App (%)'], 'HEAVY_COMP_APP', 'percentage_for_failed')

    plot_generic_result(1, 11, ['Failed Task due to Mobility (%)'], 'ALL_APPS', 'percentage_for_failed')
    plot_generic_result(1, 11, ['Failed Task due to Mobility','for Augmented Reality App (%)'], 'AUGMENTED_REALITY', 'percentage_for_failed')
    plot_generic_result(1, 11, ['Failed Task due to Mobility','for Health App (%)'], 'HEALTH_APP', 'percentage_for_failed')
    plot_generic_result(1, 11, ['Failed Task due to Mobility','for Infotainment App (%)'], 'INFOTAINMENT_APP', 'percentage_for_failed')
    plot_generic_result(1, 11, ['Failed Task due to Mobility','for Heavy Computation App (%)'], 'HEAVY_COMP_APP', 'percentage_for_failed')

    plot_generic_result(5, 5, ['Failed Tasks due to WLAN failure (%)'], 'ALL_APPS', 'percentage_for_failed')
    plot_generic_result(5, 5, ['Failed Tasks due to WLAN failure','for Augmented Reality App (%)'], 'AUGMENTED_REALITY', 'percentage_for_failed')
    plot_generic_result(5, 5, ['Failed Tasks due to WLAN failure','for Health App (%)'], 'HEALTH_APP', 'percentage_for_failed')
    plot_generic_result(5, 5, ['Failed Tasks due to WLAN failure','for Infotainment App (%)'], 'INFOTAINMENT_APP', 'percentage_for_failed')
    plot_generic_result(5, 5, ['Failed Tasks due to WLAN failure','for Heavy Comp. App (%)'], 'HEAVY_COMP_APP', 'percentage_for_failed')

    plot_generic_result(5, 7, ['Failed Tasks due to WAN failure (%)'], 'ALL_APPS', 'percentage_for_failed')
    plot_generic_result(5, 7, ['Failed Tasks due to WAN failure','for Augmented Reality App (%)'], 'AUGMENTED_REALITY', 'percentage_for_failed')
    plot_generic_result(5, 7, ['Failed Tasks due to WAN failure','for Health App (%)'], 'HEALTH_APP', 'percentage_for_failed')
    plot_generic_result(5, 7, ['Failed Tasks due to WAN failure','for Infotainment App (%)'], 'INFOTAINMENT_APP', 'percentage_for_failed')
    plot_generic_result(5, 7, ['Failed Tasks due to WAN failure','for Heavy Comp. App (%)'], 'HEAVY_COMP_APP', 'percentage_for_failed')

def main():
    plot_task_failure_reason()

if __name__ == '__main__':
    main()
