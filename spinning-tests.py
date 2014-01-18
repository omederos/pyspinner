import spinning
import unittest


class SpinningTestCase(unittest.TestCase):
    def test_unique_not_nested(self):
        unique = spinning.unique('The {quick|fast} fox...')
        for x in ['The quick fox...', 'The fast fox...']:
            if unique == x:
                return
        self.fail('The returned sentence was incorrect: {0}'.format(unique))

    def test_unique_nested(self):
        unique = spinning.unique('The {{quick|fast}|{black|red}} fox...')
        for x in ['The quick fox...',
                  'The fast fox...',
                  'The black fox...',
                  'The red fox...']:
            if unique == x:
                return
        self.fail('The returned sentence was incorrect: {0}'.format(unique))


if __name__ == '__main__':
    unittest.main()