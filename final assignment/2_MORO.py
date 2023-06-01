import numpy as np
import scipy as sp
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import networkx as nx
import pickle

from ema_workbench import (
    Model,
    Policy,
    ema_logging,
    SequentialEvaluator,
    MultiprocessingEvaluator,
    util,
    ScalarOutcome,
)
from dike_model_function import DikeNetwork  # @UnresolvedImport
from problem_formulation import get_model_for_problem_formulation, sum_over, sum_over_time
from ema_workbench.em_framework.samplers import sample_uncertainties

ema_logging.log_to_stderr(ema_logging.INFO)


def robust_analysis():
    # choose problem formulation number, between 0-5
    # each problem formulation has its own list of outcomes
    dike_model, planning_steps = get_model_for_problem_formulation(5)

    def signal_to_noise(data):
        mean = np.mean(data)
        std = np.std(data)
        print(mean, std)
        sn = mean / std
        print(sn)
        return sn

    MAXIMIZE = ScalarOutcome.MAXIMIZE
    MINIMIZE = ScalarOutcome.MINIMIZE

    var_list_deaths = ['A.1_Expected Number of Deaths 0', 'A.1_Expected Number of Deaths 1',
                       'A.1_Expected Number of Deaths 2',
                       'A.2_Expected Number of Deaths 0', 'A.2_Expected Number of Deaths 1',
                       'A.2_Expected Number of Deaths 2',
                       'A.3_Expected Number of Deaths 0', 'A.3_Expected Number of Deaths 1',
                       'A.3_Expected Number of Deaths 2',
                       'A.4_Expected Number of Deaths 0', 'A.4_Expected Number of Deaths 1',
                       'A.4_Expected Number of Deaths 2',
                       'A.5_Expected Number of Deaths 0', 'A.5_Expected Number of Deaths 1',
                       'A.5_Expected Number of Deaths 2']

    robustness_functions = [
        ScalarOutcome("mean p", kind=MINIMIZE, variable_name="A.5_Expected Number of Deaths", function=np.mean),
        ScalarOutcome("std p", kind=MINIMIZE, variable_name="A.5_Expected Number of Deaths", function=np.std),
#        ScalarOutcome("sn reliability", kind=MAXIMIZE, variable_name="Expected Evacuation Costs", function=signal_to_noise),
        ScalarOutcome("sn reliability", kind=MINIMIZE, variable_name="Expected Evacuation Costs",
                      function=np.std),
    ]

    n_scenarios = 10
    scenarios = sample_uncertainties(dike_model, n_scenarios)
    nfe = 10

    with MultiprocessingEvaluator(dike_model) as evaluator:
        evaluator.robust_optimize(
            robustness_functions,
            scenarios,
            nfe=nfe,
            epsilons=[0.1] * len(robustness_functions),
            population_size=5,
        )


if __name__ == '__main__':
    robust_analysis()

