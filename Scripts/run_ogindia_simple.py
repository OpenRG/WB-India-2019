# import modules
import multiprocessing
from dask.distributed import Client
import time
import numpy as np

from taxcalc import Calculator
from ogindia import postprocess
from ogindia.execute import runner
from ogindia.utils import REFORM_DIR, BASELINE_DIR


def run_micro_macro(user_params):
    # Specify IIT reform
    reform = {
        'II_rt7': {2020: 0.7},
        'PT_rt7': {2020: 0.7}
    }

    # Define parameters to use for multiprocessing
    client = Client(processes=False)
    num_workers = min(multiprocessing.cpu_count(), 7)
    print('Number of workers = ', num_workers)
    run_start_time = time.time()

    # Set some model parameters
    # See parameters.py for description of these parameters
    user_params = {'start_year': 2020,
                   'debt_ratio_ss': 1.5,
                   'age_specific': False}

    '''
    ------------------------------------------------------------------------
    Run baseline policy first
    ------------------------------------------------------------------------
    '''
    output_base = BASELINE_DIR
    kwargs = {'output_base': output_base, 'baseline_dir': BASELINE_DIR,
              'test': False, 'time_path': True, 'baseline': True,
              'user_params': user_params, 'guid': '_example',
              'run_micro': True, 'data': 'cps', 'client': client,
              'num_workers': num_workers}

    start_time = time.time()
    runner(**kwargs)
    print('run time = ', time.time() - start_time)

    '''
    ------------------------------------------------------------------------
    Run reform policy
    ------------------------------------------------------------------------
    '''
    output_base = REFORM_DIR
    kwargs = {'output_base': output_base, 'baseline_dir': BASELINE_DIR,
              'test': False, 'time_path': True, 'baseline': False,
              'user_params': user_params, 'guid': '_example',
              'reform': reform, 'run_micro': True, 'data': 'cps',
              'client': client, 'num_workers': num_workers}

    start_time = time.time()
    runner(**kwargs)
    print('run time = ', time.time()-start_time)

    # return ans - the percentage changes in macro aggregates and prices
    # due to policy changes from the baseline to the reform
    ans = postprocess.create_diff(
        baseline_dir=BASELINE_DIR, policy_dir=REFORM_DIR)

    print("total time was ", (time.time() - run_start_time))
    print('Percentage changes in aggregates:', ans)


if __name__ == "__main__":
    run_micro_macro(user_params={})
