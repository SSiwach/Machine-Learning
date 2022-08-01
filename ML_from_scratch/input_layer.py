class Layer_Input :
  #forward pass

  def forward(self, inputs, training):
    #remember input values 
    self.inputs = inputs
    #calculate output values from inputs
    self.output = np.maximum(0, inputs)

  #Backward pass
  def backward(self, dvalues):
    #as we need to modify original variable, we nedd to copy
    self.dinputs = dvalues.copy()

    #zero gradeint where i/p were negative
    self.dinputs[self.inputs <= 0] = 0

  def predictions(self, outputs):
    return outputs
