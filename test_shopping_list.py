import unittest

from registered_user import user
from registered_user import shopping_list 

"""
this is a test case file that will be used to test if the implemntations made in registered user.py
are functioning as intended 

"""


class userTestCase(unittest.TestCase):
    """
        initualizing the user attributes 
    """
    def setUp(self):
        self.shopper =  user()

    def test_create_shopping_list(self):
        """
        this function tests if your new list was created 
        """
        self.shopper.create_shopping_list("holiday_list")
        self.assertEqual(self.shopper.shop_list,{'holiday_list':[]}, "List name not given")
    def test_delete_shopping_list(self):
        """
        test if an exsisting shopping list has been deleted
        """
        self.shopper.create_shopping_list("holiday_list")
        self.shopper.delete_shopping_list("holiday_list")
        self.assertEqual(self.shopper.shop_list,{})
    def test_view_shopping_list(self):
        """
        this will test if a user can view a shopping list
        """
        self.shopper.create_shopping_list("home_items")
        self.shopper.view_shopping_list("home_items")
        self.assertEqual(self.shopper.shop_list,{"home_items":[]})

class shoppinglistTestCase(unittest.TestCase):
    def setUp(self):
         self.shopper = shopping_list()

    def test_add_item(self):
        self.shopper.add_item("buy a shoe")
        self.assertEqual(self.shopper.items,["buy a shoe"])
    def test_remove_item(self):
        self.shopper.add_item("shoes")
        self.shopper.add_item("shorts")
        self.shopper.remove_item('shoes')
        self.assertEqual(self.shopper.items,["shorts"])

if __name__ == "__main__":
    unittest.main()
