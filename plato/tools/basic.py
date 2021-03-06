from plato.interfaces.decorators import symbolic_standard
import theano
import theano.tensor as tt
import numpy as np

__author__ = 'peter'


def softmax(x, axis):
    """ Theano didn't implement softmax very nicely so we have to do some reshaping. """
    e_x = tt.exp(x-x.max(axis=axis, keepdims = True))
    out = e_x/e_x.sum(axis=axis, keepdims=True)
    return out


@symbolic_standard
def running_average(data):
    n_points = theano.shared(np.array(1).astype(int))
    avg = theano.shared(np.zeros_like(data.tag.test_value).astype(theano.config.floatX))
    new_avg = data*(1./n_points) + avg*(n_points-1.)/n_points
    return (new_avg, ), [(avg, new_avg), (n_points, n_points+1)]