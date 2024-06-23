import numpy as np

class LMSFilter:
    def __init__(self, filter_order, step_size):
        self.filter_order = filter_order
        self.step_size = step_size
        self.weights = np.zeros(filter_order)

    def adapt(self, desired, input_signal):
        n = len(input_signal)
        output = np.zeros(n)
        error = np.zeros(n)
        
        for i in range(self.filter_order, n):
            x = input_signal[i:i-self.filter_order:-1]
            output[i] = np.dot(self.weights, x)
            error[i] = desired[i] - output[i]
            self.weights += 2 * self.step_size * error[i] * x
        
        return output, error
