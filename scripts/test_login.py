import allure


class TestLogin:

    @allure.step(title="小吴是猪")
    def test_login_001(self):
        assert 1

    @allure.step(title="小吴是dog")
    def test_login_002(self):
        assert 1

    @allure.step(title="小吴是feipig")
    def test_login_003(self):
        assert 1
