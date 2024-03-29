import numpy as np

def hull_moving_average(values, period):
    weighted_ma = 2 * np.ma.mean(values[-period//2:]) - np.ma.mean(values[-period:])
    sqrt_period = int(np.sqrt(period))
    hull_ma = np.ma.mean(values[-period:]) if len(values) >= period else np.ma.mean(values)
    
    for i in range(sqrt_period):
        hull_ma -= np.ma.mean(values[-(period - i * (period // sqrt_period)):-(i+1) * (period // sqrt_period)])
        
    return weighted_ma

# Example usage:
values = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]
hma = hull_moving_average(values, 7)
print("Hull Moving Average:", hma)
