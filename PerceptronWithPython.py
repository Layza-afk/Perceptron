# Codigo em Python do Perceptron

# Tar.: Identificar entradas de operadores lógicos e enviar saídas relacionadas a 0 e 1.

# Ope. log.: AND e OR.

# Treino: identificar, por meio de números aleatorios, as devidas saídas para as
#   entradas lógicas AND e OR. todas validadas por seu treinador.

# Pós treino: identificar entradas e responde-las com suas respectivas saídas
#   esperadas.

import random;

class Perceptron():
    def __init__(self, l_rate): # inicializa os pesos, o vies e a taxa de aprendizagem
        self.w_1 = random.uniform(-1, 1);
        self.w_2 = random.uniform(-1, 1);
        self.bias = random.uniform(-1, 1);
        self.l_rate = l_rate;

    def activation(self, y):
        return 1 if y >= 0 else 0;

    def predict(self, input_1, input_2):
        y = input_1 * self.w_1 + input_2 * self.w_2 + self.bias;
        output = self.activation(y);
        print(f"entrada: ({input_1}, {input_2}) --> Saída: {output}");
        return output;
    
    def training(self, training_data, epochs):
        for i in range(epochs):
            for input_1, input_2, expected in training_data:
                prediction = self.predict(input_1, input_2);
                error = expected - prediction;

                self.w_1 += self.l_rate * error * input_1;
                self.w_2 += self.l_rate * error * input_2;
                self.bias += self.l_rate * error;

    def test(self, input_1, input_2):
        return self.predict(input_1, input_2);


# Chamada dos métodos 
and_values = [
        (0, 0, 0),
        (1, 1, 1),
        (1, 0, 1),
        (0, 1, 1)
    ]

p = Perceptron(l_rate=0.1);
p.training(and_values, epochs=10);

print("TESTE");
p.test(0, 0);
p.test(1, 1);



