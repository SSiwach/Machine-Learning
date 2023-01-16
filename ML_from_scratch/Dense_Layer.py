!pip install nnfs



import numpy as np  #importing the numpy 
import nnfs    #data set
import os    #to import operating system
import cv2
import pickle
import copy #make the copy of the data


class Layer_Dense: #define a layer with number of inputs, weights, weights, bias and regularizer
  def __init__(self, n_inputs, n_neurons, weight_regularizer_l1 =0,
               weight_regularizer_l2 = 0, bias_regularizer_l1 = 0,
               bias_regularizer_l2 = 0):
    #initialize weights and biases
    self.weights = 0.01*np.random.randn(n_inputs, n_neurons)
    self.biases = np.zeros(1, n_neurons)

    #set regularization strength
    self.weight_regularizer_l1 = weight_regularizer_l1
    self.weight_regularizer_l2 = weight_regularizer_l2
    self.bias_regularizer_l1 = bias_regularizer_l1
    self.bias_regularizer_l2 = bias_regularizer_l2

  #Forward pass
  def forward(self, inputs, training):
    #remember input values
    self.inputs = inputs
    #calculate output values from inputs, weights and biases
    self.output = np.dot(inputs, self.weights) + self.biases

  #Backward pass
  def backward(self, dvalues):
    self.dweights = np.dot(self.inputs.T, dvalues)
    self.dbiases = np.sum(dvalues, axis = 0, keepdims = True)

    #Gradient on regularization
    # L1 on weights
    if self.weight_regularizer_l1 > 0:
      dL1 = np.ones_like(self.weights)
      dL1[self.weights < 0 ] = -1
      self.dweights += self.weight_regularizer_l1 * dL1
# L2 on weights
    if self.weight_regularizer_l2 > 0:
      self.dweights += 2*self.weight_regularizer_l2 * self.weights

    if self.bias_regularizer_l1 > 0:
      dL1 = np.ones_like(self.biases)
      dL1[self.biases < 0] = -1
      self.dbiases += self.bias_regularizer_l1 *dL1

    #L2 on biases
    if self.bias_regularizer_l2 > 0:
      self.dbiases +=2*self.bias_regularizer_l2* self.biases

    #gradient on values 
    self.dinputs = np.dot(dvalues, self.weights.T)
  
  #retrive layer parameters
  def get_parameters(self):
    return self.weights, self.biases

  #set weights and biases in a layer instance
  def set_parameters(self, weights, biases):
    self.weights = weights
    self.biases = biases

    
