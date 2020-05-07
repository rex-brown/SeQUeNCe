class Process:
    def __init__(self, owner, activation_method, act_params):
        self.owner = owner
        self.activation = activation_method
        self.act_params = act_params

    # return activation method with act_params as arguments
    def run(self) -> None:
        return getattr(self.owner, self.activation)(*self.act_params)
