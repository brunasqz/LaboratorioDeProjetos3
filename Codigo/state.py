class CraneState:

    state = 'stopped'
    electromagnet = False

    def __init__(self):
        super().__init__()

    def stop(self):
        self.state = 'stopped'
        print(self.state)

    def turnOnElectromagnet(self):
        self.electromagnet = True
        self.state = 'electromagnet'
        print(self.state)

    def turnOffElectromagnet(self):
        self.electromagnet = False
        self.state = 'stopped'
        print(self.state)
