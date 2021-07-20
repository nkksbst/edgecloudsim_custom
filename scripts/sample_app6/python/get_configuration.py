#--------------------------------------------------------------
# description
# returns a value according to the given arguments
#--------------------------------------------------------------

def get_configuration(arg_type):

    ret_val = None

    if(arg_type == 1):
        ret_val = "/Users/monikkabusto/Desktop/src/EdgeCloudSim/scripts/sample_app6/output/20-07-2021_14-17/default_config"
    elif(arg_type == 2):
        ret_val = 60 * 5 #simulation time (in seconds)
    elif(arg_type == 3):
        ret_val = 1 #Number of iterations
    elif(arg_type == 4):
        ret_val = 1 # tick interval for number of mobile devices
    elif(arg_type == 5):
        ret_val = ['Q_LEARNING']#['FUZZY_BASED','UTILIZATION_BASED','NETWORK_BASED','FUZZY_COMPETITOR','HYBRID', 'ALWAYS_CLOUD']
    elif(arg_type == 6):
        ret_val = ['fuzzy','util.','bw','Flores*','hybrid', 'always_cloud']
    elif(arg_type == 7):
        ret_val = [10, 3, 9, 8] #position of figure
    elif(arg_type == 8):
        ret_val = 0
    elif(arg_type == 9):
        ret_val= 'Number of Mobile Devices'# %Common text for x axis
    elif(arg_type == 10):
        ret_val = 500 # %min number of mobile device
    elif(arg_type == 11):
        ret_val = 100# %step size of mobile device count
    elif(arg_type == 12):
        ret_val = 700 #max number of mobile device
    elif(arg_type == 20):
        ret_val=1 #return 1 if graph is plotted colorful
    elif(arg_type == 21):
        ret_val=[0.55, 0, 0] #color of first line
    elif(arg_type == 22):
        ret_val=[0, 0.15, 0.6] #color of second line
    elif(arg_type == 23):
        ret_val=[0 ,0.23 ,0] #color of third line
    elif(arg_type == 24):
        ret_val=[0.6, 0 ,0.6] #color of fourth line
    elif(arg_type == 25):
        ret_val=[0.08 ,0.08, 0.08] #color of fifth line
    elif(arg_type == 26):
        ret_val=[0 ,0.8 ,0.8] #color of sixth line
    elif(arg_type == 27):
        ret_val=[0.8, 0.4, 0] #color of seventh line
    elif(arg_type == 28):
        ret_val=[0.8, 0.8 ,0] #color of eighth line
    elif(arg_type == 40):
        ret_val={'-k*','-ko','-ks','-kv','-kp','-kd','-kx','-kh'} #line style (marker): of the colerless line
    elif(arg_type == 50):
        ret_val={':k*',':ko',':ks',':kv',':kp',':kd',':kx',':kh'} #line style (marker): of the colerfull line

    return ret_val
