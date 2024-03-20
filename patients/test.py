def warn(*args, **kwargs):
    pass
import warnings
warnings.warn = warn
import numpy as np
from joblib import load
clf = load("model.joblib")
prediction = clf.predict(np.random.randn(1, 22))
print("May have a stroke!" if prediction[0] == 1 else "Nope you all good my guy!")
