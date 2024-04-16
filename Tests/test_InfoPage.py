import pytest
import sys

sys.path.append("C:\\Users\\Kfir\\Documents\\program\\Pytest\\src\\Conf")
sys.path.append("C:\\Users\\Kfir\\Documents\\program\\Pytest\\src\\Pages")
sys.path.append("C:\\Users\\Kfir\\Documents\\program\\Pytest\\src\\Tests")

#From Conf
import config

#From Pages
import MainPage
import LoginPage
import InfoPage
import CartPage

#From Tests
from test_base import BaseTest
from  Tests.Func import Functions


class Test_InfoPage(BaseTest):

    @pytest.fixture(params=[
            config.TestData.STANDARD_USER_NAME,
            config.TestData.VISUAL_USER_NAME,
            config.TestData.GLITCH_USER_NAME,
            config.TestData.ERROR_USER_NAME,
            config.TestData.PROBLEMATIC_USER_NAME,
        ])

    def username(self, request):
            return request.param

    def test_add_to_cart(self,username):
     infoPage=Functions.go_to_info_page(self,username,"Jacket")
     infoPage.remove_from_cart()
     infoPage.add_to_cart()
     Functions.assert_two_functions_with_param_for_func1(self,username,infoPage.verify_right_product,infoPage.verify_added_to_cart,"Jacket","Didn't reach the desire page","The product has not been added to the cart")


    def test_remove_from_cart(self,username):
     infoPage=Functions.go_to_info_page(self,username,"Jacket")
     infoPage.remove_from_cart()
     infoPage.add_to_cart()
     infoPage.remove_from_cart()
     Functions.assert_two_functions_with_param_for_func1(self,username,infoPage.verify_right_product,infoPage.verify_removed_from_cart,"Jacket","Didn't reach the desire page","The product has not been removed from cart")


    def test_check_image(self,username):
     infoPage=Functions.go_to_info_page(self,username,"Bike")
     Functions.assert_two_functions_with_param_for_func1(self,username,infoPage.verify_right_product,infoPage.verify_right_image,"Bike","Didn't reach the desire page","The image and the prodcut are no coordinated") 


    def test_go_to_main_page(self,username):
     infoPage=Functions.go_to_info_page(self,username,"Jacket")
     mainPage=infoPage.go_to_main_page()
     Functions.assert_move_from_page(self,username,mainPage.get_title,config.TestData.MAIN_PAGE_TITLE,MainPage.MainPage(self.driver))

    def test_go_to_cart_page(self,username):
     infoPage=Functions.go_to_info_page(self,username,"Jacket")
     cartPage=infoPage.go_to_cart_page()
     Functions.assert_move_from_page(self,username,cartPage.get_title,config.TestData.CART_PAGE_TITLE,CartPage.CartPage(self.driver))