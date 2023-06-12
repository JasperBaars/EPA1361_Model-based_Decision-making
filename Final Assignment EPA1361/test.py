# proberen om de error in MOEA.ipynb te fixen

from multiprocessing import freeze_support

from ema_workbench import (Model, RealParameter, ScalarOutcome,
                           MultiprocessingEvaluator, ema_logging,
                           Constant)
from problem_formulation import get_model_for_problem_formulation

from ema_workbench import MultiprocessingEvaluator, ema_logging
from ema_workbench.em_framework.evaluators import MultiprocessingEvaluator


def test():
    ema_logging.log_to_stderr(ema_logging.INFO)

    dike_model, planning_steps = get_model_for_problem_formulation(3)

    with MultiprocessingEvaluator(dike_model) as evaluator:
        results2 = evaluator.optimize(nfe=5e3, searchover='levers', epsilons=[0.1] * len(dike_model.outcomes))


if __name__ == '__main__':
    test()
