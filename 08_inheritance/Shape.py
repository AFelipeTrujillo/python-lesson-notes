class Shape:

    def __init__(self, h, w):
        if self._validate(h):
            self._h = h
        else:
            self._h = 0
        if self._validate(w):
            self._w = w
        else:
            self._w = 0

    @property
    def h(self):
        return self._h

    @property
    def w(self):
        return self._w

    @h.setter
    def h(self, h):
        if self._validate(h):
            self._h = h

    @w.setter
    def w(self, w):
        if self._validate(w):
            self._w = w

    def __str__(self):
        return f'Shape h={self._h} w={self._w}'

    def _validate(self, val):
        return True if 0 < val < 10 else False

