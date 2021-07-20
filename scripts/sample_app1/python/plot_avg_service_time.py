from plot_generic_result import plot_generic_result

def plot_avg_service_time():

    plot_generic_result(1, 5, ['Service Time (sec)'], 'ALL_APPS', '')
    plot_generic_result(1, 5, ['Service Time for','Augmented Reality App (sec)'], 'AUGMENTED_REALITY', '')
    plot_generic_result(1, 5, ['Service Time for Health App (sec)'], 'HEALTH_APP', '')
    plot_generic_result(1, 5, ['Service Time for Infotainment App (sec)'], 'INFOTAINMENT_APP', '')
    plot_generic_result(1, 5, ['Service Time for','Compute Intensive App (sec)'], 'HEAVY_COMP_APP', '')

    plot_generic_result(2, 5, ['Service Time on Edge (sec)'], 'ALL_APPS', '')
    plot_generic_result(2, 5, ['Service Time on Edge','for Augmented Reality App (sec)'], 'AUGMENTED_REALITY', '')
    plot_generic_result(2, 5, ['Service Time on Edge for Health App (sec)'], 'HEALTH_APP', '')
    plot_generic_result(2, 5, ['Service Time on Edge','for Infotainment App (sec)'], 'INFOTAINMENT_APP', '')
    plot_generic_result(2, 5, ['Service Time on Edge','for Heavy Comp. App (sec)'], 'HEAVY_COMP_APP', '')

    plot_generic_result(3, 5, ['Service Time on Cloud (sec)'], 'ALL_APPS', '')
    plot_generic_result(3, 5, ['Service Time on Cloud','for Augmented Reality App (sec)'], 'AUGMENTED_REALITY', '')
    plot_generic_result(3, 5, ['Service Time on Cloud for Health App (sec)'], 'HEALTH_APP', '')
    plot_generic_result(3, 5, ['Service Time on Cloud','for Infotainment App (sec)'], 'INFOTAINMENT_APP', '')
    plot_generic_result(3, 5, ['Service Time on Cloud','for Heavy Comp. App (sec)'], 'HEAVY_COMP_APP', '')

def main():
    plot_avg_service_time()

if __name__ == '__main__':
    main()
