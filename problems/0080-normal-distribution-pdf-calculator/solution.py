import math

def normal_pdf(x, mean, std_dev):
	"""
	Calculate the probability density function (PDF) of the normal distribution.
	:param x: The value at which the PDF is evaluated.
	:param mean: The mean (μ) of the distribution.
	:param std_dev: The standard deviation (σ) of the distribution.
	"""
	val =(math.exp(-pow(x-mean,2)/(2*pow(std_dev,2))))/(std_dev*pow(2*math.pi,0.5))
	return round(val,5)