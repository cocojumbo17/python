import random
import math


def r():
    return 2 * random.random() - 1


def sigmoid(x):
    return 1 / (1 + math.exp(-x))


def sigmoid_det(x):
    return (1 - x) * x


def run_ns_down(ins, neurons, synapses):
    cur_input_index = 0
    for cur_neuron in neurons:
        input_neurons = neurons[cur_neuron].get('v')
        if not input_neurons and neurons[cur_neuron]['out'] == 0:
            neurons[cur_neuron]['out'] = ins[cur_input_index]
            cur_input_index += 1
        else:
            inp = 0
            for from_neuron in input_neurons:
                w = synapses[(from_neuron, cur_neuron)].get('W')
                val = neurons[from_neuron].get('out')
                inp += w * val
            neurons[cur_neuron]['out'] = inp


def calc_error(outs, neurons, res_layer):
    num_out = 0
    sum = 0
    for k in neurons:
        cur_neuron = neurons[k]
        if res_layer == cur_neuron.get('layer'):
            sum += (outs[num_out] - cur_neuron.get('out')) ** 2
            num_out += 1
    return sum / num_out


def get_results(neurons, res_layer):
    res = []
    for k in neurons:
        cur_neuron = neurons[k]
        if res_layer == cur_neuron.get('layer'):
            res.append(cur_neuron.get('out'))
    return res


def invert_neurons_rec(neurons, index, inverted_neurons):
    for v in neurons[index].get('v'):
        inverted_neurons[v]['v'].add(index)
        invert_neurons_rec(neurons, v, inverted_neurons)


def invert_neurons(neurons, res_layer):
    res = {i: {'v': set(), 'f': False} for i in range(len(neurons))}
    for k in neurons:
        if res_layer == neurons[k].get('layer'):
            invert_neurons_rec(neurons, k, res)
    return res


def run_ns_up_out(res_layer, res, neurons, inverted_neurons):
    # calc ends at first
    cur_res_index = 0
    for k in neurons:
        cur_neuron = neurons[k]
        if res_layer == cur_neuron.get('layer'):
            out = cur_neuron.get('out')
            delta = (res[cur_res_index] - out) * (1 - out) * out
            cur_neuron['d'] = delta
            cur_res_index += 1
            inverted_neurons[k]['f'] = True


def run_ns_up_res(index, res, neurons, inverted_neurons, synapses, res_layer):
    if inverted_neurons[index].get('f'):
        return
    children = inverted_neurons[index].get('v')
    for v in children:
        run_ns_up_res(v, res, neurons, inverted_neurons, synapses, res_layer)

    speed = 0.7
    moment = 0.3

    out = neurons[index].get('out')
    acc = 0
    for v in children:
        child_delta = neurons[v].get('d')
        synapse_key = (index, v)
        w = synapses[synapse_key].get('W')
        acc += w * child_delta
        grad = out * child_delta
        prev_dw = synapses[synapse_key].get('dW')
        dw = speed * grad + moment * prev_dw
        synapses[synapse_key]['dW'] = dw
        synapses[synapse_key]['W'] = w + dw
    delta = acc * (1 - out) * out
    neurons[index]['d'] = delta


def run_ns_up(res, neurons, inverted_neurons, synapses, res_layer):
    for k in inverted_neurons:
        inverted_neurons[k]['f'] = False

    run_ns_up_out(res_layer, res, neurons, inverted_neurons)

    for k in inverted_neurons:
        run_ns_up_res(k, res, neurons, inverted_neurons, synapses, res_layer)


def ns():
    res_layer = 3
    neurons = {0: {'v': [], 'out': 0, 'd': 0, 'layer': 0},
               1: {'v': [], 'out': 0, 'd': 0, 'layer': 0},
               2: {'v': [0, 1], 'out': 0, 'd': 0, 'layer': 1},
               3: {'v': [0, 1], 'out': 0, 'd': 0, 'layer': 1},
               4: {'v': [2, 3], 'out': 0, 'd': 0, 'layer': 2},
               5: {'v': [2, 3], 'out': 0, 'd': 0, 'layer': 2},
               6: {'v': [4, 5], 'out': 0, 'd': 0, 'layer': 3}
               }
    synapses = {}
    for k in neurons:
        if neurons[k].get('v'):
            for v in neurons[k].get('v'):
                synapse_key = (v, k)
                synapses.update({synapse_key: {'dW': 0, 'W': r()}})
    print(synapses)
    inverted_neurons = invert_neurons(neurons, res_layer)
    print(inverted_neurons)

    training_input = [[0, 0], [0, 1], [1, 0], [1, 1]]
    training_output = [[0], [1], [1], [0]]
    for epoha in range(1000):
        #       for i in range(4):
        i = 1
        run_ns_down(training_input[i], neurons, synapses)
        error = calc_error(training_output[i], neurons, res_layer)
        res = get_results(neurons, res_layer)
        print(f'error={error} res={res}')
        run_ns_up(training_output[i], neurons, inverted_neurons, synapses, res_layer)


ns()
