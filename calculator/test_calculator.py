from calculator.calculator import Calculator

class TestCalculator: 
    def test_add(self):
        # arrange
        a = 4
        b = 2
        cal = Calculator()

        # act
        result = cal.div(a, b)

        # assert
        expected = 2
        assert result == expected

