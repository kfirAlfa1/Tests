import pytest
import sys

sys.path.append("C:\\Users\\Kfir\\Documents\\program\\Pytest\\src\\Conf")
sys.path.append("C:\\Users\\Kfir\\Documents\\program\\Pytest\\src\\Pages")
sys.path.append("C:\\Users\\Kfir\\Documents\\program\\Pytest\\src\\Tests")

#From Conf
import config

#From Pages
from Pages.LoginPage import LoginPage
from Pages.MainPage import MainPage
import InfoPage
import CartPage

#From Tests
from test_base import BaseTest
from Tests.Func import Functions

class Test_MainPage (BaseTest):

    def assert_right_order(self,checkFilterChanged,username):
     mainPage=MainPage(self.driver)
     if checkFilterChanged ==True:
       try:
         assert mainPage.verify_right_order()
       except Exception:
         error= "The order of the products is not coordinate to the filter"
         pytest.fail(f"Failed for user '{username}':{error}")
     else:
       error="The filter has not changed"
       pytest.fail(f"Failed for user '{username}':{error}") 


    @pytest.fixture(params=[
        config.TestData.STANDARD_USER_NAME,
        config.TestData.VISUAL_USER_NAME,
        config.TestData.GLITCH_USER_NAME,
        config.TestData.ERROR_USER_NAME,
        config.TestData.PROBLEMATIC_USER_NAME,
    ])

    def username(self, request):
        return request.param 

    def test_order_of_prices_low_to_high(self,username):
      mainPage=Functions.go_to_main_page(self,username)
      checkFilterChanged=mainPage.change_filter_and_verify(config.TestData.PRICES_FROM_LOW_TO_HIGH)
      self.assert_right_order(checkFilterChanged,username)
      
   
    def test_order_of_prices_high_to_low(self,username):
      mainPage=Functions.go_to_main_page(self,username)
      checkFilterChanged=mainPage.change_filter_and_verify(config.TestData.PRICES_FROM_HIGH_TO_LOW)
      self.assert_right_order(checkFilterChanged,username)


    def test_order_of_poductes_a_to_z(self,username):
     mainPage=Functions.go_to_main_page(self,username)
     checkFilterChanged=mainPage.change_filter_and_verify(config.TestData.PRODUCTS_FROM_A_TO_Z)
     self.assert_right_order(checkFilterChanged,username)    


    def test_order_of_poductes_z_to_a(self,username):
     mainPage=Functions.go_to_main_page(self,username)
     checkFilterChanged=mainPage.change_filter_and_verify(config.TestData.PRODUCTS_FROM_Z_TO_A)
     self.assert_right_order(checkFilterChanged,username)


    def test_coordinate_image_and_product(self,username):
     mainPage= Functions.go_to_main_page(self,username)
     Functions.assert_one_function_without_param(self,username,mainPage.verify_right_images,"The following products are not coordinate with their image")


    def test_add_to_cart(self,username):
      mainPage=Functions.go_to_main_page(self,username)        
      mainPage.remove_from_cart()#For cookies
      mainPage.add_to_cart()
      Functions.assert_one_function_without_param(self,username,mainPage.verify_all_prodcuts_added_to_cart,"The follwoing products didnt added to cart")


    def test_removed_from_cart(self,username):
      mainPage=Functions.go_to_main_page(self,username)
      mainPage.remove_from_cart()#For cookies
      mainPage.add_to_cart_specific_product("Bike")
      mainPage.add_to_cart_specific_product("Backpack")
      mainPage.add_to_cart_specific_product("Jacket")
      mainPage.remove_from_cart()
      Functions.assert_one_function_without_param(self,username,mainPage.verify_all_prodcuts_removed_from_cart,"The follwoing products didnt removed from cart")



    def test_add_specific_product_to_cart(self,username):
     mainPage=Functions.go_to_main_page(self,username)
     mainPage.remove_from_cart()#For cookies
     mainPage.add_to_cart_specific_product("Backpack")
     Functions.assert_one_function_with_param(self,username, mainPage.verify_specific_prodcut_added_to_cart,"Backpack","The product didnt added to cart")


    def test_removed_specific_product_from_cart(self,username):
     mainPage=Functions.go_to_main_page(self,username)
     mainPage.remove_from_cart()#For cookies
     mainPage.add_to_cart_specific_product("Bike")
     mainPage.add_to_cart_specific_product("Backpack")
     mainPage.remove_specific_product_from_cart("Backpack")
     Functions.assert_one_function_with_param(self,username, mainPage.verify_specific_prodcut_removed_from_cart,"Backpack","The product didnt removed from cart")        



    def test_from_main_page_to_info_page(self,username):
     mainPage=Functions.go_to_main_page(self,username)
     infoPage=mainPage.go_to_info_page("T-shirt red")
     if infoPage.verify_right_product("T-shirt red"):
      Functions.assert_move_from_page(self,username,infoPage.get_title,config.TestData.INFO_PAGE_TITLE,InfoPage.InfoPage(self.driver))
     else:
        error="Didn't reach the desire page"
        pytest.fail(f"Failed for user '{username}':{error}")

   
    def test_from_main_page_to_cart_page(self,username):
     mainPage=Functions.go_to_main_page(self,username)
     cartPage=mainPage.go_to_cart_page()
     Functions.assert_move_from_page(self,username,cartPage.get_title,config.TestData.CART_PAGE_TITLE,CartPage.CartPage(self.driver))
 
    def test_log_out(self,username):
     mainPage=Functions.go_to_main_page(self,username)
     loginPage=mainPage.do_log_out()
     Functions.assert_move_from_page(self,username,loginPage.get_title,config.TestData.LOGIN_PAGE_TITLE,LoginPage(self.driver))  