def empirical_pmf(samples):
    """
    Given an iterable of integer samples, return a list of (value, probability)
    pairs sorted by value ascending.
    """
    res=[]
    for x in sorted(set(samples)):
        probability = samples.count(x)/len(samples)
        res.append((x,probability))
    return res