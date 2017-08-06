# 测试代码

#11-1

import unittest
from city_functions import city_country

class test_city_country(unittest.TestCase):
    """测试city_function.py"""

    def test_cc(self):
        """能够正确处理city，country这样的对象"""
        test_name = city_country('chengdu','china')
        self.assertEqual(test_name, 'Chengdu China')
unittest.main()