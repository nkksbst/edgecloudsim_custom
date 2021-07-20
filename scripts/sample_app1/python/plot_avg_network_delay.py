from plot_generic_result import plot_generic_result

def plot_avg_net_delay():

    plot_generic_result(1, 7, ['Average Network Delay (sec)'], 'ALL_APPS', '')
    plot_generic_result(1, 7, ['Average Network Delay','for Augmented Reality App (sec)'], 'AUGMENTED_REALITY', '')
    plot_generic_result(1, 7, ['Average Network Delay for Health App (sec)'], 'HEALTH_APP', ''),
    plot_generic_result(1, 7, ['Average Network Delay','for Infotainment App (sec)'], 'INFOTAINMENT_APP', '')
    plot_generic_result(1, 7, ['Average Network Delay','for Heavy Comp. App (sec)'], 'HEAVY_COMP_APP', '')

    plot_generic_result(5, 1, ['Average WLAN Delay (sec)'], 'ALL_APPS', ''),
    plot_generic_result(5, 1, ['Average WLAN Delay','for Augmented Reality App (sec)'], 'AUGMENTED_REALITY', '')
    plot_generic_result(5, 1, ['Average WLAN Delay for Health App (sec)'], 'HEALTH_APP', '')
    plot_generic_result(5, 1, ['Average WLAN Delay','for Infotainment App (sec)'], 'INFOTAINMENT_APP', '')
    plot_generic_result(5, 1, ['Average WLAN Delay','for Heavy Comp. App %(sec)'], 'HEAVY_COMP_APP', '')

    plot_generic_result(5, 3, ['Average WAN Delay (sec)'], 'ALL_APPS', '')
    plot_generic_result(5, 3, ['Average WAN Delay','for Augmented Reality App (sec)'], 'AUGMENTED_REALITY', '')
    plot_generic_result(5, 3, ['Average WAN Delay for Health App (sec)'], 'HEALTH_APP', '')
    plot_generic_result(5, 3, ['Average WAN Delay','for Infotainment App (sec)'], 'INFOTAINMENT_APP', '')
    plot_generic_result(5, 3, ['Average WAN Delay','for Heavy Comp. App (sec)'], 'HEAVY_COMP_APP', '')

def main():
    plot_avg_net_delay()

if __name__ == '__main__':
    main()
