import random
import math
import pickle
from typing import Optional, Any

import numpy as np
from skimage import io

speed_of_learing = 0.7
moment_of_learing = 0.2
epohas_of_learing = 1000
neuron_numbers = [625, 9, 5, 2]
synaptic_weight = []
synaptic_delta_weight = []
neurons_outputs = []
neurons_deltas = []
training_input= []
training_output= []
biases=[]
biases_dw=[]


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


def run_ns_down(learning_index):
    for i in range(len(neuron_numbers)):
        if i == 0:
            neurons_outputs[i] = np.reshape(training_input[learning_index],[1,-1])
        else:
            neurons_outputs[i] = sigmoid(np.dot(neurons_outputs[i-1], synaptic_weight[i-1]) + biases[i-1])


def calc_error(learning_index):
    out = get_results()
    res = np.asarray([training_output[learning_index]])
    return np.average((res-out)**2)


def get_results():
    return neurons_outputs[len(neurons_outputs)-1]


def run_ns_up_out(learning_index):
    res = np.asarray([training_output[learning_index]])
    out = get_results()
    neurons_deltas[len(neurons_deltas)-1] = (res-out)*(1-out)*out


def run_ns_up_for_layer(layer):
    out = neurons_outputs[layer]
    deltas = neurons_deltas[layer+1]
    weights = synaptic_weight[layer]
    prev_dw = synaptic_delta_weight[layer]

    acc = np.sum(weights*deltas, axis=1)
    new_deltas = acc * (1 - out) * out

    temp_delta = np.ones(weights.shape)*deltas
    grads = out.T*deltas

    dw = speed_of_learing * grads + moment_of_learing * prev_dw
    synaptic_delta_weight[layer] = dw
    synaptic_weight[layer] = weights + dw

    prev_biases_dw = biases_dw[layer]
    bdw = speed_of_learing * deltas + moment_of_learing * prev_biases_dw
    biases_dw[layer] = bdw
    biases[layer] = biases[layer]+bdw

    neurons_deltas[layer] = new_deltas


def run_ns_up(learning_index):
    run_ns_up_out(learning_index)
    count_layers = len(neuron_numbers) - 2
    for layer in range(count_layers, -1, -1):
        run_ns_up_for_layer(layer)


def print_coeffs(synapses):
    for k in synapses:
        curr = synapses[k]
        print(f'{k[0]}->{k[1]}: W={curr["W"]}', end=' ')
    print()


def create_ns():
    read_training_data('learning_data2.bin')
    for i in range(len(neuron_numbers)-1):
        n1 = neuron_numbers[i]
        n2 = neuron_numbers[i+1]
        synaptic_weight.append(2*np.random.random((n1,n2))-1)
        synaptic_delta_weight.append(np.zeros((n1,n2)))
        biases.append(np.random.random((1,n2)))
        biases_dw.append(np.zeros((1,n2)))
    for n in neuron_numbers:
        neurons_outputs.append(np.zeros((n)))
        neurons_deltas.append(np.zeros((n)))#TODO: remove delta for bias neuron


def read_training_data(file_name):
    f = open(file_name, 'rb')
    for i in range(20):
        is_smile = pickle.load(f)
        training_output.append([1, 0] if is_smile else [0, 1])
        data = pickle.load(f)
        training_input.append(data)
    f.close()

def learn_ns():
    create_ns()
    print('start learning')
    for epoha in range(epohas_of_learing):
        learning_indexes=list(range(20))
        random.shuffle(learning_indexes)
        for i in learning_indexes:
            run_ns_down(i)
            run_ns_up(i)
        if epoha % 10 == 0:
            errors=[]
            for j in range(20):
                run_ns_down(j)
                errors.append(calc_error(j))
            print(f'errors = {errors}')
            #print('.', end='')

    print('\nfinish learning')


def save_to_file(file_name):
    f = open(file_name, 'wb')
    pickle.dump(synaptic_weight, f)
    pickle.dump(synaptic_delta_weight, f)
    pickle.dump(neurons_outputs, f)
    pickle.dump(neurons_deltas, f)
    pickle.dump(biases, f)
    pickle.dump(biases_dw, f)
    f.close()


def load_from_file(file_name):
    f = open(file_name, 'rb')
    synaptic_weight = pickle.load(f)
    synaptic_delta_weight = pickle.load(f)
    neurons_outputs = pickle.load(f)
    neurons_deltas = pickle.load(f)
    biases = pickle.load(f)
    biases_dw = pickle.load(f)
    f.close()


def user_input(neurons, synapses):
    #print_coeffs(synapses)
    training_input, training_output = read_training_data('learning_data2.bin')
    is_exit = False
    while not is_exit:
        inp = input('test data (0-19) or "e" to exit: ')
        if inp == 'e':
            is_exit = True
        else:
            index = int(inp)
            if 0<=index<20:
                test_input = training_input[index]
                run_ns_down(test_input, neurons, synapses)
                res = get_results(neurons)
                str_res = "none"
                if res[0] > 0.8 and res[1] < 0.2:
                    str_res = "smile"
                elif res[1] > 0.8 and res[0] < 0.2:
                    str_res = "sad"
                print('result is ', str_res)


def ns(with_learning, file_name):
    if with_learning:
        learn_ns()
        save_to_file(file_name)
    else:
        neurons, synapses = load_from_file(file_name)
    #user_input(neurons, synapses)

def test_image(imagefile_name, ns_file_name):
    image_data = io.imread(imagefile_name, True)
    pixels = []
    for i in range(image_data.shape[0]):
        for j in range(image_data.shape[1]):
            pixels.append(image_data[i][j])
    neurons, synapses = load_from_file(ns_file_name)
    run_ns_down(pixels, neurons, synapses)
    res = get_results(neurons)
    str_res = "none"
    if res[0] > 0.8 and res[1] < 0.2:
        str_res = "smile"
    elif res[1] > 0.8 and res[0] < 0.2:
        str_res = "sad"
    print('result is ', res, str_res)


def main():
    ns(True, 'myns3.txt')
    #test_image('test.png', 'image_brain.txt')


if __name__ == '__main__': main()
