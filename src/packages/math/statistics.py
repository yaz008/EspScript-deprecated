import numpy as np
from typing import Iterable

Numeric = int | float | complex

def mean(stdin: Iterable[Numeric]) -> Numeric:
    return np.mean(stdin)

def median(stdin: Iterable[Numeric]) -> Numeric:
    return np.median(stdin)

def variance(stdin: Iterable[Numeric]) -> Numeric:
    return np.var(stdin)