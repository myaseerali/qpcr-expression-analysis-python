import pandas as pd
import numpy as np


def calculate_fold_change(ddct_df):
    result = ddct_df.copy()

    result["FC_IFNG"] = np.power(2, -result["ddCt_IFNG"])
    result["FC_IL2RA"] = np.power(2, -result["ddCt_IL2RA"])
    result["FC_TNFA"] = np.power(2, -result["ddCt_TNFA"])

    return result