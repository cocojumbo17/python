import random
import math
import pickle


def r():
    return 2 * random.random() - 1


def sigmoid(x):
    return 1 / (1 + math.exp(-x))


def run_ns_down(ins, neurons, synapses):
    for layer in neurons:
        curr_layer = neurons[layer]
        if layer == 0:
            cur_input_index = 0
            for neuron in curr_layer:
                curr_neuron = curr_layer[neuron]
                if not curr_neuron['bias']:
                    curr_neuron['output'] = ins[cur_input_index]
                    cur_input_index += 1
        else:
            prev_layer = neurons[layer-1]
            inp = 0
            for neuron in curr_layer:
                curr_neuron = curr_layer[neuron]
                if curr_neuron['bias']:
                    continue
                for neuron2 in prev_layer:
                    prev_neuron = prev_layer[neuron2]
                    w = synapses[(neuron2, neuron)]['W']
                    val = prev_neuron['output']
                    inp += w * val
                curr_neuron['output'] = sigmoid(inp)


def calc_error(outs, neurons):
    layer_index = len(neurons)-1
    last_layer = neurons[layer_index]
    num_out = 0
    acc = 0
    for n in last_layer:
        curr_neuron = last_layer[n]
        acc += (outs[num_out] - curr_neuron['output']) ** 2
        num_out += 1
    return acc / num_out


def get_results(neurons):
    res = []
    layer_index = len(neurons)-1
    last_layer = neurons[layer_index]
    for n in last_layer:
        curr_neuron = last_layer[n]
        res.append(curr_neuron['output'])
    return res


def run_ns_up_out(res, neurons):
    layer_index = len(neurons)-1
    last_layer = neurons[layer_index]
    cur_res_index = 0
    for n in last_layer:
        curr_neuron = last_layer[n]
        out = curr_neuron['output']
        delta = (res[cur_res_index] - out) * (1 - out) * out
        curr_neuron['delta'] = delta
        cur_res_index += 1


def run_ns_up_for_layer(neurons, synapses, layer):
    speed = 0.7
    moment = 0.3

    curr_layer = neurons[layer]
    for n in curr_layer:
        curr_neuron = curr_layer[n]
        out = curr_neuron['output']
        acc = 0
        next_layer = neurons[layer+1]
        for n2 in next_layer:
            next_neuron = next_layer[n2]
            if next_neuron['bias']:
                continue
            delta = next_neuron['delta']
            synapse_key = (n, n2)
            w = synapses[synapse_key].get('W')
            acc += w * delta
            grad = out * delta
            prev_dw = synapses[synapse_key]['dW']
            dw = speed * grad + moment * prev_dw
            synapses[synapse_key]['dW'] = dw
            synapses[synapse_key]['W'] = w + dw
        if not curr_neuron['bias']:
            delta = acc * (1 - out) * out
            curr_neuron['delta'] = delta


def run_ns_up(res, neurons, synapses):
    run_ns_up_out(res, neurons)
    count_layers = len(neurons)-2
    for layer in range(count_layers, -1, -1):
        run_ns_up_for_layer(neurons, synapses, layer)


def print_coeffs(synapses):
    for k in synapses:
        curr = synapses[k]
        print(f'{k[0]}->{k[1]}: W={curr["W"]}', end=' ')
    print()


def create_neurons(neuron_numbers, neurons):
    curr_layer = 0
    v_index = 0
    for n in neuron_numbers:
        layer = {}
        for i in range(n):
            layer.update({v_index: {'output': 0, 'delta': 0, 'bias': False}})
            v_index += 1
        if curr_layer < len(neuron_numbers) - 1:
            layer.update({v_index: {'output': 1, 'delta': 0, 'bias': True}})
            v_index += 1
        neurons[curr_layer] = layer
        curr_layer += 1


def create_synapses(neurons, synapses):
    for layer in neurons:
        if layer < len(neurons)-1:
            curr_layer = neurons[layer]
            next_layer = neurons[layer+1]
            for curr_neuron in curr_layer:
                for next_neuron in next_layer:
                    if next_layer[next_neuron]['bias']:
                        continue
                    synapse_key = (curr_neuron, next_neuron)
                    synapses.update({synapse_key: {'dW': 0, 'W': r()}})
    #print(synapses)



def learn_ns(neurons, synapses):
    neuron_numbers = [2, 2, 1]
    create_neurons(neuron_numbers, neurons)
    create_synapses(neurons, synapses)

    #res_layer = len(neuron_numbers) - 1
    #inverted_neurons = invert_neurons(neurons, res_layer)
    # print(inverted_neurons)

    training_input = [[0, 0], [0, 1], [1, 0], [1, 1]]
    training_output = [[0], [1], [1], [0]]
    print('start learning')
    for epoha in range(1000):
        for i in range(4):
            run_ns_down(training_input[i], neurons, synapses)
            error = calc_error(training_output[i], neurons)
            res = get_results(neurons)
            print(f'input={training_input[i]} output={res} error={error}')
            run_ns_up(training_output[i], neurons, synapses)
        if epoha % 100 == 0:
            print('.', end='')
    print('\nfinish learning')


def save_to_file(neurons, synapses, file_name):
    f = open(file_name, 'wb')
    pickle.dump(neurons, f)
    pickle.dump(synapses, f)
    f.close()


def load_from_file(file_name):
    f = open(file_name, 'rb')
    neurons = pickle.load(f)
    synapses = pickle.load(f)
    f.close()
    return neurons, synapses


def user_input(neurons, synapses):
    print_coeffs(synapses)
    is_exit = False
    while not is_exit:
        inp = input('test data (2 "0" or "1") or "e" to exit: ')
        if inp == 'e':
            is_exit = True
        else:
            test_input = list(map(int, inp.split()))
            run_ns_down(test_input, neurons, synapses)
            res = get_results(neurons)
            print(f'result is {round(res[0])}')


def ns(with_learning, file_name):
    neurons = {}
    synapses = {}
    if with_learning:
        learn_ns(neurons, synapses)
        save_to_file(neurons, synapses, file_name)
    else:
        neurons, synapses = load_from_file(file_name)
    user_input(neurons, synapses)


def main():
    ns(False, 'myns.txt')


if __name__ == '__main__': main()
