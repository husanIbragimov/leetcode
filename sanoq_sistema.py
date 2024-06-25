class SANOQ_SISTEMA:
    def __init__(self, num):
        self.num = num

    def bin_to_dec(self):
        return int(self.num, 2)

    def oct_to_dec(self):
        return int(self.num, 8)

    def hex_to_dec(self):
        return int(self.num, 16)


num = input("Son kiriting 10 lik sanoq sistemasida: ")
san = SANOQ_SISTEMA(num)

print("2 lik sanoq sistemasida:", san.bin_to_dec())
print("8 lik sanoq sistemasida:", san.oct_to_dec())
print("16 lik sanoq sistemasida:", san.hex_to_dec())
