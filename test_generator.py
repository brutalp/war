from tests import exist_diameter


class TestGenerator(object):
    def test_generator(self):
        for i in range(10, 90, 10):
            yield self.check, i

    def check(self, arg):
        assert exist_diameter(arg) is True
