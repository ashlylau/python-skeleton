# ONLY EDIT FUNCTIONS MARKED CLEARLY FOR EDITING

import numpy as np

def question01(portfolios): # input is an array of portfolios represented as their decimal values [p1,...,pN] where N<=100
                            # each has a maximum value of 2^16-1
  max = 0
  for i in range(len(portfolios)):
      p = portfolios[i]
      for j in range(i+1, len(portfolios)):
          q = portfolios[j]
          if p ^ q > max:
              max = p ^ q

  return max
