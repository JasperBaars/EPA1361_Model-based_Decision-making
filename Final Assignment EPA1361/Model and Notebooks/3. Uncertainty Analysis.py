#   import packages
import numpy as np
import scipy as sp
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import seaborn.objects as so
import networkx as nx
import pickle
import functools

from ema_workbench import (
    Model,
    Policy,
    Scenario,
    ema_logging,
    SequentialEvaluator,
    MultiprocessingEvaluator,
    util,
    ScalarOutcome,
)
from dike_model_function import DikeNetwork  # @UnresolvedImport
from problem_formulation import get_model_for_problem_formulation, sum_over, sum_over_time
from ema_workbench.em_framework.samplers import sample_uncertainties
from ema_workbench.em_framework.optimization import ArchiveLogger, EpsilonProgress
from ema_workbench.em_framework import parameters_from_csv
from ema_workbench.em_framework.evaluators import BaseEvaluator
from ema_workbench.analysis import parcoords
from ema_workbench.analysis import prim
from ema_workbench import Samplers

def model_run():
    dike_model, planning_steps = get_model_for_problem_formulation(5)
    ema_logging.log_to_stderr(ema_logging.INFO)


    pareto_policies = pd.read_pickle(r'../generated_datasets/initial_Pareto_policies.pkl')


    policies = []
    for row_number in range(pareto_policies.shape[0]):
        policies.append(
            Policy(name=row_number, **pareto_policies.iloc[row_number, :-5].to_dict())
        )

    n_scenarios = int(5_000)  # naar 5000 veranderen


    with MultiprocessingEvaluator(dike_model) as evaluator:
        results = evaluator.perform_experiments(scenarios=n_scenarios,
                                                policies=policies,
                                                uncertainty_sampling=Samplers.LHS
                                                )


    with open(r'../generated_datasets/policy_uncertainty_test.pkl', 'wb') as file_pi:
        pickle.dump(results, file_pi)

if __name__ == '__main__':
    model_run()