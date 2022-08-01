#sigmoid activation
class Activation_Softmax:

  #forward pass
  def forward(self, inputs, training):
    #save i/p and cal/save o/p of hte sigmoid function

    self.inputs = inputs 
    self.output = 1/(1 + np.exp(-inputs))

  #Backward pass
  def backward(self, dvalues):
    self.dinputs = dvalues * (1 -self.output) * self.output

  #calcualte predictions for outputs
  def predictions(self, outputs):
    return (outputs > 0.5) * 1
