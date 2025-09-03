'''
https://github.com/vnegnev/marcos_extras/wiki/tut_write_simple_sequence
'''

import numpy as np
import matplotlib.pyplot as plt
import pdb

st = pdb.set_trace


import external  # imports external.py
import experiment as ex  #


def my_first_experiment():
    exp = ex.Experiment(lo_freq=5, rx_t=3.125)
    tx0_times = np.array([50,130])  # pulse start 50 us after beginng of experiment
                                    # pulse turn off 80 us later (130 us after start of experiment)
    tx0_amps = np.array([1,0])    # 50 % Amplitude 

    event_dict = {"tx0":(tx0_times, tx0_amps)}  # creating a dictionary
    exp.add_flodict(event_dict)
    exp.add_flodict({'rx0_en': (np.array([200, 400]), np.array([1, 0]))})

    #exp.plot_sequence()        # for debugging
    #plt.show()                 # for debugging

    rxd, msgs = exp.run()               # for simulation
    exp.close_server(only_if_sim=True)  # for simulation

if __name__ == "__main__":
    my_first_experiment()