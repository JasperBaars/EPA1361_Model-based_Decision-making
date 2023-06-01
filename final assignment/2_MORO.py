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
    dike_model, planning_steps = get_model_for_problem_formulation(0)

    dike_model.outcomes

    def signal_to_noise(data):
        mean = np.mean(data)
        std = np.std(data)
        sn = mean / std
        return sn

    MAXIMIZE = ScalarOutcome.MAXIMIZE
    MINIMIZE = ScalarOutcome.MINIMIZE
    robustness_functions = [
        ScalarOutcome("mean p", kind=MINIMIZE, variable_name="4_RfR 2", function=np.mean),
        ScalarOutcome("std p", kind=MINIMIZE, variable_name="4_RfR 2", function=np.std),
        ScalarOutcome("sn reliability", kind=MAXIMIZE, variable_name="4_RfR 2", function=signal_to_noise),
    ]

    n_scenarios = 10
    scenarios = sample_uncertainties(dike_model, n_scenarios)
    nfe = 1000

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

