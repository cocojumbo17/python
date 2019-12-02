import random
import math
import pickle


def r():
    return 2 * random.random() - 1


def sigmoid(x):
    return 1 / (1 + math.exp(-x))


def run_ns_down(ins, neurons, synapses):
    cur_input_index = 0
    for k in neurons:
        cur_neuron = neurons[k]
        input_neurons = cur_neuron['v']
        if not input_neurons and not cur_neuron['bias']:
            cur_neuron['out'] = ins[cur_input_index]
            cur_input_index += 1
        else:
            inp = 0
            for from_neuron in input_neurons:
                w = synapses[(from_neuron, k)].get('W')
                val = neurons[from_neuron].get('out')
                inp += w * val
            cur_neuron['out'] = sigmoid(inp)


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


def run_ns_up_rec(index, res, neurons, inverted_neurons, synapses, res_layer):
    if inverted_neurons[index].get('f'):
        return
    children = inverted_neurons[index].get('v')
    for v in children:
        run_ns_up_rec(v, res, neurons, inverted_neurons, synapses, res_layer)

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
        run_ns_up_rec(k, res, neurons, inverted_neurons, synapses, res_layer)


def print_coeffs(synapses):
    for k in synapses:
        curr = synapses[k]
        print(f'{k[0]}->{k[1]}: W={curr["W"]}', end=' ')
    print()


def create_neurons(neuron_numbers, neurons):
    res_layer = len(neuron_numbers) - 1
    v_index = 0
    curr_layer = 0
    parent_v = []
    for n in neuron_numbers:
        prev_parent = []
        for i in range(n):
            neurons.update({v_index: {'v': parent_v, 'out': 0, 'd': 0, 'layer': curr_layer, 'bias': False}})
            prev_parent.append(v_index)
            v_index += 1
        if curr_layer != res_layer:
            neurons.update({v_index: {'v': [], 'out': 1, 'd': 0, 'layer': curr_layer, 'bias': True}})
            prev_parent.append(v_index)
            v_index += 1

        curr_layer += 1
        parent_v = prev_parent


def learn_ns(neurons, synapses):
    neuron_numbers = [2, 2, 1]
    create_neurons(neuron_numbers, neurons)

    for k in neurons:
        if neurons[k].get('v'):
            for v in neurons[k].get('v'):
                synapse_key = (v, k)
                synapses.update({synapse_key: {'dW': 0, 'W': r()}})
    # print(synapses)
    res_layer = len(neuron_numbers) - 1
    inverted_neurons = invert_neurons(neurons, res_layer)
    # print(inverted_neurons)

    training_input = [[0, 0], [0, 1], [1, 0], [1, 1]]
    training_output = [[0], [1], [1], [0]]
    print('start learning')
    for epoha in range(1000):
        for i in range(4):
            run_ns_down(training_input[i], neurons, synapses)
            error = calc_error(training_output[i], neurons, res_layer)
            res = get_results(neurons, res_layer)
            print(f'input={training_input[i]} output={res} error={error}')
            run_ns_up(training_output[i], neurons, inverted_neurons, synapses, res_layer)
        if epoha % 100 == 0:
            print('.', end='')
    print('\nfinish learning')


def save_to_file(neurons, synapses, file_name):
    f = open(file_name, 'wb')
    #store = {'n':neurons, 's':synapses}
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
    res_layer = neurons[len(neurons) - 1]['layer']
    print_coeffs(synapses)
    is_exit = False
    while not is_exit:
        inp = input('test data (2 "0" or "1") or "e" to exit: ')
        if inp == 'e':
            is_exit = True
        else:
            test_input = list(map(int, inp.split()))
            run_ns_down(test_input, neurons, synapses)
            res = get_results(neurons, res_layer)
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
    ns(True, 'myns.txt')

if __name__ == '__main__':main()