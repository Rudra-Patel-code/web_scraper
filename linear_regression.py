import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from sklearn.datasets import fetch_california_housing


dataset = fetch_california_housing()

print(dataset.DESCR)
