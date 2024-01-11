from dataclasses import dataclass

@dataclass
class Application:
    def __init__(self, **kwargs):

        for key, value in kwargs.items():

            setattr(self, key, value)
