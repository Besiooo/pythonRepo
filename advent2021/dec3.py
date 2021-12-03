def dec_bin(num_as_str):
    if type(num_as_str) is int:
        num_as_str = str(num_as_str)
    num_as_str = num_as_str.lstrip("0")
    bits_num = len(num_as_str)
    dec = 0
    for digit in num_as_str:
        if digit == "1":
            dec += 2 ** bits_num
        bits_num -= 1
    return dec / 2


class Diff1:
    data = []
    seq_len = 12
    gamma_rate = None
    epsilon_rate = None

    def get_input(self):
        with open("inputs/dec3_txt.txt") as data:
            for line in data.readlines():
                self.data.append(line.rstrip("\n"))

    def get_rates(self, rate):
        bits = [0 for x in range(self.seq_len)]
        for value in self.data:
            for index, digit in enumerate(value):
                bits[index] += int(digit)
        print(bits)
        if rate == "gamma":
            bits = ['1' if bits[n] > 500 else '0' for n in range(len(bits))]
        elif rate == "epsilon":
            bits = ['1' if bits[n] < 500 else '0' for n in range(len(bits))]
        bits = "".join(bits)
        if rate == "gamma":
            self.gamma_rate = dec_bin(bits)
        elif rate == "epsilon":
            self.epsilon_rate = dec_bin(bits)

    def __init__(self):
        self.get_input()
        print(self.data)
        print(self.seq_len)
        self.get_rates(rate="gamma")
        self.get_rates(rate="epsilon")
        print(f"{self.gamma_rate} * {self.epsilon_rate} = {self.gamma_rate * self.epsilon_rate}")


class Diff2:
    data = []
    seq_len = 12
    oxygen_rate = None
    co2_rate = None

    def get_input(self):
        with open("inputs/dec3_txt.txt") as data:
            for line in data.readlines():
                self.data.append(line.rstrip("\n"))

    def get_rates(self, rate):
        selective_data = self.data
        condition = ""
        for n in range(self.seq_len):
            bits = sum(int(value[n]) for value in selective_data)

            if rate == "oxygen":
                bit = "1" if bits >= len(selective_data) / 2 else "0"
            else:
                bit = "0" if bits >= len(selective_data) / 2 else "1"
            print(f"rate = {rate}, bits = {bits}, bit = {bit}, elements = {len(selective_data)}, condition = {condition}")

            condition += bit
            selective_data = [value for value in selective_data if value.startswith(condition)]

            if len(selective_data) == 1:
                ratio = selective_data[0]
                if rate == "oxygen":
                    self.oxygen_rate = dec_bin(ratio)
                else:
                    self.co2_rate = dec_bin(ratio)
                break

    def __init__(self):
        self.get_input()
        self.get_rates(rate="co2")
        self.get_rates(rate="oxygen")
        print(self.co2_rate)
        print(self.oxygen_rate)
        print(f"{self.oxygen_rate} * {self.co2_rate} = {self.oxygen_rate * self.co2_rate}")


Diff1()
print("***")
Diff2()


