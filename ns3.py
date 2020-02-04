import random
import math
import pickle
from typing import Optional, Any

import numpy as np
from skimage import io

speed_of_learing = 0.6
moment_of_learing = 0.2
epohas_of_learing = 1000
neuron_numbers = [625, 9, 5, 2]
synaptic_weight = []
synaptic_delta_weight = []
neurons_outputs = []
neurons_deltas = []
training_input = []
training_output = []
biases = []
biases_dw = []


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


def run_ns_down(input_data):
    for i in range(len(neuron_numbers)):
        if i == 0:
            neurons_outputs[i] = np.reshape(input_data, [1, -1])
        else:
            neurons_outputs[i] = sigmoid(np.dot(neurons_outputs[i - 1], synaptic_weight[i - 1]) + biases[i - 1])

def cross_entropy_loss(index):
    real_out = get_results()
    ideal_out = training_output[index]
    e = - np.sum(ideal_out*np.log(real_out))/len(real_out)
    return e


def calc_error(learning_index):
    out = get_results()
    res = np.asarray([training_output[learning_index]])
    return np.average((res - out) ** 2)


def get_results():
    return neurons_outputs[len(neurons_outputs) - 1]


def run_ns_up_out(output):
    res = np.asarray(output)
    out = get_results()
    neurons_deltas[len(neurons_deltas) - 1] = (res - out) * (1 - out) * out


def run_ns_up_for_layer(layer):
    out = neurons_outputs[layer]
    deltas = neurons_deltas[layer + 1]
    weights = synaptic_weight[layer]
    prev_dw = synaptic_delta_weight[layer]

    acc = np.sum(weights * deltas, axis=1)
    new_deltas = acc * (1 - out) * out

    grads = out.T * deltas

    dw = speed_of_learing * grads + moment_of_learing * prev_dw
    synaptic_delta_weight[layer] = dw
    synaptic_weight[layer] = weights + dw

    prev_biases_dw = biases_dw[layer]
    bdw = speed_of_learing * deltas + moment_of_learing * prev_biases_dw
    biases_dw[layer] = bdw
    biases[layer] = biases[layer] + bdw

    neurons_deltas[layer] = new_deltas


def run_ns_up(out):
    run_ns_up_out(out)
    count_layers = len(neuron_numbers) - 2
    for layer in range(count_layers, -1, -1):
        run_ns_up_for_layer(layer)


def print_coeffs(synapses):
    for k in synapses:
        curr = synapses[k]
        print(f'{k[0]}->{k[1]}: W={curr["W"]}', end=' ')
    print()


def create_ns():
    read_training_data('learning_data3.bin')
    for i in range(len(neuron_numbers) - 1):
        n1 = neuron_numbers[i]
        n2 = neuron_numbers[i + 1]
        synaptic_weight.append(2 * np.random.random((n1, n2)) - 1)
        synaptic_delta_weight.append(np.zeros((n1, n2)))
        biases.append(np.random.random((1, n2)))
        biases_dw.append(np.zeros((1, n2)))
    for n in neuron_numbers:
        neurons_outputs.append(np.zeros((n)))
        neurons_deltas.append(np.zeros((n)))  # TODO: remove delta for bias neuron


def read_training_data(file_name):
    training_input.clear()
    training_output.clear()
    f = open(file_name, 'rb')
    num_items = pickle.load(f)
    for i in range(num_items):
        is_smile = pickle.load(f)
        training_output.append([1, 0] if is_smile else [0, 1])
        data = pickle.load(f)
        training_input.append(data)
    f.close()


def learn_ns():
    create_ns()
    print('start learning')
    for epoha in range(epohas_of_learing):
        learning_indexes = list(range(len(training_input)))
        random.shuffle(learning_indexes)
        for i in learning_indexes:
            run_ns_down(training_input[i])
            run_ns_up(training_output[i])
            print(f'error is {cross_entropy_loss(i)}')
        """
        if epoha % 10 == 0:
            errors = []
            for j in range(len(training_input)):
                run_ns_down(training_input[j])
                errors.append(calc_error(j))
            print(f'errors = {errors}')
        """

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
    global synaptic_weight, synaptic_delta_weight, neurons_outputs, neurons_deltas, biases, biases_dw
    synaptic_weight = pickle.load(f)
    synaptic_delta_weight = pickle.load(f)
    neurons_outputs = pickle.load(f)
    neurons_deltas = pickle.load(f)
    biases = pickle.load(f)
    biases_dw = pickle.load(f)
    f.close()


def user_input():
    read_training_data('learning_data3.bin')
    is_exit = False
    num_items = len(training_input)
    while not is_exit:
        inp = input(f'test data (0-{num_items}) or "e" to exit: ')
        if inp == 'e':
            is_exit = True
        else:
            index = int(inp)
            if 0 <= index < num_items:
                run_ns_down(training_input[index])
                res = get_results()
                str_res = "none"
                if res[0][0] > 0.8 and res[0][1] < 0.2:
                    str_res = "happy smile"
                elif res[0][1] > 0.8 and res[0][0] < 0.2:
                    str_res = "sad smile"
                print('result is ', res, str_res)


def ns(with_learning, file_name):
    if with_learning:
        learn_ns()
        save_to_file(file_name)
    else:
        load_from_file(file_name)
    user_input()


def run_ns_gen_for_layer(layer):
    sums = -np.log(1/neurons_outputs[layer]-1)
    sums = sums - biases[layer-1]
    test_result = np.dot(neurons_outputs[layer-1], synaptic_weight[layer-1])
    print(test_result)
    total_w = np.sum(synaptic_weight[layer-1],axis=0)
    k = sums / total_w
    neurons_outputs[layer-1] = synaptic_weight[layer - 1]*k
    print(sums)

def run_ns_gen(output):
    res = np.asarray(output)
    last_layer = len(neurons_outputs) - 1
    #neurons_outputs[last_layer] = res
    for layer in range(last_layer, 0, -1):
        run_ns_gen_for_layer(layer)

def generate(out, ns_file_name):
    load_from_file(ns_file_name)
    run_ns_gen(out)

def test_image(imagefile_name, ns_file_name):
    image_data = io.imread(imagefile_name, True)
    load_from_file(ns_file_name)
    run_ns_down(image_data)
    res = get_results()
    str_res = "none"
    if res[0][0] > 0.8 and res[0][1] < 0.2:
        str_res = "happy smile"
    elif res[0][1] > 0.8 and res[0][0] < 0.2:
        str_res = "sad smile"
    print('result is ', res, str_res)


def main():
    ns(False, 'myns3.txt')
    #test_image('test.png', 'image_brain3.txt')
    #generate([0.95,0.05], 'image_brain3.txt')


if __name__ == '__main__': main()
