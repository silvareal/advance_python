#property without decorator
def Color:

    def __init_(self, rgb_code, name):
        self.rgb_code  = rgb_code
        self._name     = name

    def _get_name(self):
        return self._name

    def _set_name(self, name):
        self._name = name

    name = property(_set_name, _set_name)

    