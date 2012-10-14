import unittest
import poke


class TestPoke(unittest.TestCase):
    def test_string_peek(self):
        s = 'rather_unlikely'
        q = poke.peek(id(s), 128)
        assert s in q

    def test_string(self):
        s = 'rather_unlikely'
        q = poke.peek(id(s), 128)

        i = q.find(s)
        assert i >= 0

        poke.poke(id(s) + i, 'abomination...!')
        assert s == 'abomination...!'


if __name__ == '__main__':
    unittest.main()
