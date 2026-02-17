import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import torch

df = pd.read_excel("Filtered Data with Subtypes Again.xlsx")

accounts = df["Accounts"]
contributions = df["Contributions"]
grants = df["Grants"]
assets = df["Assets"]

accounts_tensor = torch.tensor(accounts.values, dtype = torch.float32)
contributions_tensor = torch.tensor(contributions.values, dtype = torch.float32)
grants_tensor = torch.tensor(grants.values, dtype = torch.float32)
assets_tensor = torch.tensor(assets.values, dtype=torch.float32)
lr = .0001
