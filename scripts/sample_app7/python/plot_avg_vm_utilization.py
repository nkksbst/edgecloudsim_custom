from plot_generic_result import plot_generic_result

def plot_avg_vm_utilization():

    plot_generic_result(2, 8, ['Average VM Utilization (%)'], 'ALL_APPS', '')
    plot_generic_result(2, 8, ['Average VM Utilization','for Augmented Reality App (%)'], 'AUGMENTED_REALITY', '')
    plot_generic_result(2, 8, ['Average VM Utilization for Health App (%)'], 'HEALTH_APP', '')
    plot_generic_result(2, 8, ['Average VM Utilization for Infotainment App (%)'], 'INFOTAINMENT_APP', '')
    plot_generic_result(2, 8, ['Average VM Utilization for Heavy Comp. App (%)'], 'HEAVY_COMP_APP', '')

def main():
    plot_avg_vm_utilization()

if __name__ == '__main__':
    main()
