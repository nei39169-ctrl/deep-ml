import numpy as np
import math

def descriptive_statistics(data: list | np.ndarray) -> dict:
    """
    Calculate various descriptive statistics metrics for a given dataset.
    
    Args:
        data: List or numpy array of numerical values
    
    Returns:
        Dictionary containing mean, median, mode, variance, standard deviation,
        percentiles (25th, 50th, 75th), and interquartile range (IQR)
    """
    data =sorted(data)
    mean = s =0.0
    for i in range(len(data)):
        s += data[i]
    mean = s/len(data)
        
    
    if len(data)%2 == 0 :
        index = len(data)//2 -1
        median = (data[index]+data[index+1])/2.0
    else:
        index=(len(data)+1)//2 -1
        median =data[index]
    mode =data[0]
    max_frequency =0
    for i in data:
        count_i = data.count(i)
        if count_i >max_frequency:
            mode = i
            max_frequency = count_i
    
    ss =0.0
    for i in range(len(data)):
        ss += pow(data[i]-mean,2)
    variance = ss/len(data)

    standard_deviation = pow(variance,0.5)

    q25 = data[math.ceil(len(data)*0.25)-1]
    q75 = data[math.ceil(len(data)*0.75)-1]

    iqr = q75 - q25
    return{'mean':mean,'median':median,'mode':mode,'variance':variance,'standard_deviation':standard_deviation,'25th_percentile':q25,'50th_percentile':median,'75th_percentile':q75,'interquartile_range':iqr}
        