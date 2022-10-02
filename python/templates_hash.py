class Hashes:
    def __init__(self, s, base = 131, mod = 10 ** 9 + 7) -> None:
        self.s = s
        self.base = base
        self.mod = mod
        self.powers = [1]
        self.psa = [0]
        
        for i in range(len(s)):
            self.powers.append(self.powers[-1] * self.base % self.mod)
            self.psa.append((self.psa[-1] + ord(s[i]) * self.powers[-1]) % self.mod)
        
    
    def get(self, l, r):
        return (self.psa[r + 1] - self.psa[l]) * self.powers[len(self.s) - r] % self.mod
