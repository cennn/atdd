import random
from collections import namedtuple

import numpy as np
import torch

#
diagnose_params = namedtuple("diagnose_params", {
    "beta1", "beta2", "beta3", # "alpha1", "alpha2", "alpha3",
    "gamma", "delta", "zeta", "eta1", "eta2",  # theta
    "dd_max_threshold", "dd_min_threshold", "dd_threshold_VG",
    "window_size_float", "window_size_min"
})



def get_ave(lst):
    return sum(lst) / len(lst)


def set_seed(seed, msg="", logger=None):
    if seed is None:
        seed = random.randint(11, 111)
    s = msg + "_seed: " + str(seed)
    print(s)
    if logger is not None:
        logger.info(s)
    torch.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)
    np.random.seed(seed)
    random.seed(seed)
    torch.backends.cudnn.deterministic = True
