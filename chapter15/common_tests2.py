import unittest
from chapter15 import common

class CommonTestCase(unittest.TestCase) :
    def test_email_validation_check_false(self) :
        # 단위테스트 대상 함수 호출 (False 기대)
        self.assertFalse(common.email_validation_check('##@gmail.com'))

    def test_email_validation_check_true(self) :
        # 단위테스트 대상 함수 호출 (True 기대)
        self.assertTrue(common.email_validation_check('isi.cho@gmail.com'))

