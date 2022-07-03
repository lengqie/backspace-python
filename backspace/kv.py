class KV:
    def __init__(self, k="", v=""):
        self.k = str(k)
        v_list = [v]
        self.v = v_list

    def set_val(self, v):
        self.v = str(v)

    def print(self):
        print(self.k, ":", self.v)


