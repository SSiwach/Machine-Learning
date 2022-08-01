# Dropout
class Layer_Dropout:

  #initialize 
  def __init__(self, rate):
    #store rate , we invert it as for example for dropout of 0.1 we need succes rate  0.9

    self.rate = 1 - rate
  
  #forward pass
  def forward(self, inputs, training):

    #save input values
    self.inputs = inputs

    # if not in the training mode - return values
    if not training:
      self.output = inputs.copy()
      return

    #generate and save scaled mask
    self.binary_mask =  np.random.binomial(1, self.rate,
                                           size = inputs.shape)/self.rate
    

    #Apply mask to output values
    self.output = inputs*self.binary_mask
#backward pass
  def backward(self, dvalues):
    #Gradient on values
    self.dinputs = dvalues * self.binary_mask

                                
