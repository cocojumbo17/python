import random
import math


def r():
    return 2 * random.random() - 1


def sigmoid(x):
    return 1 / (1 + math.exp(-x))


def sigmoid_det(x):
    return (1 - x) * x


def deltaO(ideal, x):
    return (ideal - x) * sigmoid_det(x)


def deltaH(out, w, do):
    return sigmoid_det(out) * w * do

def run_ns_down(ins,neurons,synapses):
    cur_input_index=0
    for cur_neuron in neurons:
        input_neurons = neurons[cur_neuron].get('v')
        if not input_neurons:
            neurons[cur_neuron]['out'] = ins[cur_input_index]
            cur_input_index += 1
        else:
            inp = 0
            for from_neuron in input_neurons:
                w = synapses[(from_neuron,cur_neuron)].get('W')
                val = neurons[from_neuron].get('out')
                inp += w*val
            neurons[cur_neuron]['out'] = inp


def calc_error(outs, neurons):
    num_out = 0
    sum = 0
    for k in neurons:
        cur_neuron = neurons[k]
        if cur_neuron.get('is_res'):
            sum += (outs[num_out] - cur_neuron.get('out'))**2
            num_out += 1
    return sum/num_out


def get_results(neurons):
    res=[]
    for k in neurons:
        cur_neuron = neurons[k]
        if cur_neuron.get('is_res'):
            res.append(cur_neuron.get('out'))
    return res

def ns():
    speed = 0.7
    moment = 0.3
    neurons = {0: {'v':[], 'out':0, 'd':0, 'is_res':False},
                 1: {'v':[], 'out':0, 'd':0, 'is_res':False},
                 2: {'v':[0,1], 'out':0, 'd':0, 'is_res':False},
                 3: {'v':[0,1], 'out':0, 'd':0, 'is_res':False},
                 4: {'v':[2,3], 'out':0, 'd':0, 'is_res':True}}
    synapses = {}
    for k in neurons:
        if neurons[k].get('v'):
            for v in neurons[k].get('v'):
                synapse_key = (v,k)
                synapses.update({synapse_key: {'dW':0, 'W':r()}})
    print(synapses)

    training_input = [[0.00001, 0.000001], [0, 1], [1, 0], [1, 1]]
    training_output = [[0], [1], [1], [0]]
    for i in range(4):
        run_ns_down(training_input[i], neurons, synapses)
        error = calc_error(training_output[i], neurons)
        res = get_results(neurons)
        print(f'error={error} res={res}')

#        deltas = [0] * 5
#        deltas[4] = deltaO(main_output, outputs[2])
#        deltas[2] = deltaH(outputs[0], synaptic_weight[4], deltas[4])
#        gradient4 = outputs[0] * deltas[4]
#        delta_w = speed * gradient4 + moment * synaptic_weight_delta[4]
#        synaptic_weight_delta[4] = delta_w
#        synaptic_weight[4] += delta_w


ns()
