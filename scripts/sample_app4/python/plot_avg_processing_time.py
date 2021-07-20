from plot_generic_result import plot_generic_result

def plot_avg_processing_time():

    plot_generic_result(1, 6, ['Processing Time (sec)'], 'ALL_APPS', '')
    plot_generic_result(1, 6, ['Processing Time for Augmented Reality App (sec)'], 'AUGMENTED_REALITY', '')
    plot_generic_result(1, 6, ['Processing Time for Health App (sec)'], 'HEALTH_APP', '')
    plot_generic_result(1, 6, ['Processing Time for Infotainment App (sec)'], 'INFOTAINMENT_APP', '')
    plot_generic_result(1, 6, ['Processing Time for Heavy Comp. App (sec)'], 'HEAVY_COMP_APP', '')

    plot_generic_result(2, 6, ['Processing Time on Edge (sec)'], 'ALL_APPS', '')
    plot_generic_result(2, 6, ['Processing Time on Edge','for Augmented Reality App (sec)'], 'AUGMENTED_REALITY', '')
    plot_generic_result(2, 6, ['Processing Time on Edge','for Health App (sec)'], 'HEALTH_APP', '')
    plot_generic_result(2, 6, ['Processing Time on Edge','for Infotainment App (sec)'], 'INFOTAINMENT_APP', '')
    plot_generic_result(2, 6, ['Processing Time on Edge','for Heavy Computation App (sec)'], 'HEAVY_COMP_APP', '')

    plot_generic_result(3, 6, ['Processing Time on Cloud (sec)'], 'ALL_APPS', '')
    plot_generic_result(3, 6, ['Processing Time on Cloud','for Augmented Reality App (sec)'], 'AUGMENTED_REALITY', '')
    plot_generic_result(3, 6, ['Processing Time on Cloud','for Health App (sec)'], 'HEALTH_APP', '')
    plot_generic_result(3, 6, ['Processing Time on Cloud','for Infotainment App (sec)'], 'INFOTAINMENT_APP', '')
    plot_generic_result(3, 6, ['Processing Time on Cloud','for Heavy Computation App (sec)'], 'HEAVY_COMP_APP', '')

def main():
    plot_avg_processing_time()

if __name__ == '__main__':
    main()
