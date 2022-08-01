class Activation_Softmax:

  #forward pass
  def forward(self, inputs, training):

    #remember input values
    self.inputs = inputs

    #get unnormarlized probabliteis
    exp_values = np.exp(inputs - np.max(inputs, axis = 1, keepdims = True))

    #normalize them for each sample
    probabilities = exp_values / np.sum(exp_values, axis = 1, keepdims = True)

    self.output = probabilities

  #backward pass
  def backward(self, dvalues):

    for index, (single_output, single_dvalues) in enumerate(zip(self.output, dvalues)):

      #Flatetn output arrays
      single_output = single_output.reshape(-1,1)

      #calculate Jacobian matrix of the output
      jacobian_matrix = np.diagflat(single_output) - np.dot(single_output, single_output.T)

      #calculate sample-wise gradient and add it to the array of sample gradients
      self.dinputs[index] = np.dot(jacobian_matrix, single_dvalues)


  def predictions(self, outputs):
    return np.argmax(output, axis = 1)
