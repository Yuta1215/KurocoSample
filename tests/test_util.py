from chalicelib.controllers import UserController


class TestSample:
    def test_sample(self, mocker):
        ret_val = [
            {
                'id': 1,
                'name': 'test1'
            }
        ]
        expect = [
            {
                'id': 1,
                'name': 'test1'
            }
        ]
        result = mocker.patch('chalicelib.controllers.UserController.list', ret_val)
        assert expect == result
