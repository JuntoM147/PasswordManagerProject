class aes:
    def __init__(self):
        self.key_size = 128
        self.total_rounds = 10
        self.curr_round = 0
    
    def key_expansion(self):
        pass

    def add_roundKey(self):
        pass
    
    def sub_bytes(self):
        pass

    def shift_rows(self):
        pass

    def mix_columns(self):
        pass

    def key_schedule(self):
        round_constant = 0
        if self.curr_round == 1:
            round_constant = 1
        

