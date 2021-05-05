class SubscriberOne(object):
    def __init__(self, name):
        self.name = name

    def update(self, message):
        print(f'{self.name}, {message}')


class SubscriberTwo(object):
    def __init__(self, name):
        self.name = name

    def receive(self, message):
        print(f'{self.name}, {message}')


class Publisher(object):
    def __init__(self):
        self.subscribers = dict()

    def register(self, who, callback=None):
        if callback is None:
            callback = getattr(who, 'update')
        self.subscribers[who] = callback

    def unregister(self, who):
        del self.subscribers[who]

    def dispatch(self, message):
        for _, callback in self.subscribers.items():
            callback(message)


if __name__ == "__main__":
    pub = Publisher()

    astin = SubscriberOne('아스틴')
    james = SubscriberTwo('제임스')
    jeff = SubscriberOne('제프')

    pub.register(astin, astin.update)
    pub.register(james, james.receive)
    pub.register(jeff)

    pub.dispatch('점심시간입니다.')
    pub.unregister(jeff)
    pub.dispatch('퇴근시간입니다.')
