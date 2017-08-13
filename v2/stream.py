class Stream(object):

    def __init__(self, func):
        self._func = func
        self._next = {}
        self._data = None
        self._is_running = False

    def run(self, value):
        self._is_running = True
        self._data = value
        self._func(self)

    def on(self, channel, stream):
        if self._is_running:
            raise Exception('Stream is running.')
        if channel not in self._next:
            self._next[channel] = []
        self._next[channel].append(stream)
        return self

    def write(self, channel, value):
        if channel in self._next:
            for stream in  self._next[channel]:
                stream.run(value)

    def read(self):
        return self._data