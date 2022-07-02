class KV:
    def __init__(self, k="", v=""):
        self.k = str(k)
        self.v = str(v)

    def set_val(self, v):
        self.v = str(v)

    def print(self):
        print(self.k, ":", self.v)


