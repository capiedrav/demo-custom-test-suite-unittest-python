from unittest import TestCase, main, TextTestRunner, TestSuite


class BaseTest(TestCase):

    @classmethod
    def setUpClass(cls):

        cls.setting = None
        
    def test_setting_is_not_None(self):
    
        self.assertIsNotNone(self.setting)

class Test1(BaseTest):
    
    @classmethod
    def setUpClass(cls):
        super().setUpClass()

        cls.setting = "hello"

    def test_setting_is_hello(self):

        self.assertEqual(self.setting, "hello")

class Test2(BaseTest):
    
    @classmethod
    def setUpClass(cls):
        super().setUpClass()

        cls.setting = "good bye"

    def test_setting_is_good_bye(self):

        self.assertEqual(self.setting, "good bye")


def suite():
    suite = TestSuite()
    
    suite.addTest(Test1("test_setting_is_not_None"))
    suite.addTest(Test1("test_setting_is_hello"))

    suite.addTest(Test2("test_setting_is_not_None"))
    suite.addTest(Test2("test_setting_is_good_bye"))
    
    return suite

if __name__ == '__main__':
    runner = TextTestRunner(verbosity=2)
    runner.run(suite())

