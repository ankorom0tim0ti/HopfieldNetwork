import numpy as np

im_b_v = np.arange(25)
input_weight = np.eye(25) * 2  # 単純な重み（対角に2）

y = input_weight @ im_b_v
y = np.sign(y)
THETA = np.zeros(25)

print("y =", y)
print("weight = ", input_weight)
print("shape:", y - THETA)  # (25,)