import numpy as np
import os
import time

from cw2 import experiment, cw_error
from cw2.cw_data import cw_logging
from cw2 import cluster_work

import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)
warnings.filterwarnings("ignore", category=UserWarning)


# MY_CW_MAIN.py
from cw2 import experiment, cw_error
from cw2.cw_data import cw_logging

import proj

class SlurmTest(experiment.AbstractExperiment):
    def initialize(self, config: dict, rep: int, logger: cw_logging.LoggerArray) -> None:
        # Skip for Quickguide
        pass

    def run(self, config: dict, rep: int, logger: cw_logging.LoggerArray) -> None:
        # Perform your existing task
        proj.project_main()
    
    def finalize(self, surrender: cw_error.ExperimentSurrender = None, crash: bool = False):
        # Skip for Quickguide
        pass


if __name__ == "__main__":
    cw = cluster_work.ClusterWork(SlurmTest)
    # RUN
    cw.run()
    print('clusterworks: done')

