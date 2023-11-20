# -*-Q 24 ASSIGNMENT -*-
"""
 A Government  company claims that an average light bulb lasts 270 days. 
 A researcher randomly selects 18 bulbs for testing. 
 The sampled bulbs last an average of 260 days, with a standard deviation 
 of 90 days. If the CEO's claim were true, what is the probability that 
 18 randomly selected bulbs would have an average 
 life of no more than 260 days
"""

from scipy.stats import t, norm

sm=260 # sample mean
pm=270 # population mean 
std=90 # standard devation
ss=18 # sample size
df=17 # degrees of freedom 
       # (sample size - 1) 
       
t_score =(sm-pm)/(std/(ss**0.5))      
t_score

# probability for 18 randomly selected bulbs

p= t.cdf(t_score,df)
p
