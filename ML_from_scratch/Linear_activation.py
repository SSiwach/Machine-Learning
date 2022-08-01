class Activation_Linear:

  #forward pass
  def forward(self, inputs, training):
    self.inputs = inputs
    self.output = inputs
  
  #Backward pass
  def backward(self, dvalues):
    #derivative is 1, 1*dvalues = dvalues - the chain rule
    self.dinputs = dvalues.copy()

  #calculate predictions for outputs
  def predictions(self, outputs):
    return outputs
