import pytest
import sys


sys.path.append("C:\\Users\\Kfir\\Documents\\program\\Pytest\\src\\Conf")
sys.path.append("C:\\Users\\Kfir\\Documents\\program\\Pytest\\src\\Pages")
sys.path.append("C:\\Users\\Kfir\\Documents\\program\\Pytest\\src\\Tests")

#From Config
import config

#From Pages
import MainPage
import LoginPage
import CartPage
import PaymentPage

#From Tests
from test_base import BaseTest
from  Tests.Func import Functions


class Test_DetailsPage(BaseTest):

          
   @pytest.fixture(params=[
          config.TestData.STANDARD_USER_NAME,
          config.TestData.VISUAL_USER_NAME,
          config.TestData.GLITCH_USER_NAME,
          config.TestData.ERROR_USER_NAME,
          config.TestData.PROBLEMATIC_USER_NAME,
      ])

   def username(self, request):
          return request.param

   def test_go_to_cart_page(self,username):
        detailsPage=Functions.go_to_details_page(self,username)
        cartPage=detailsPage.go_to_cart_page()
        Functions.assert_move_from_page(self,username,cartPage.get_title,config.TestData.CART_PAGE_TITLE,CartPage.CartPage(self.driver))


   def test_go_to_payment_summery_page(self,username):
        detailsPage=Functions.go_to_details_page(self,username)
        detailsPage.fill_details(config.TestData.FIRST_NAME,config.TestData.LAST_NAME,config.TestData.ZIP)
        paymentPage=detailsPage.go_to_payment_summery_page()
        Functions.assert_move_from_page(self,username,paymentPage.get_title,config.TestData.PAYMENT_PAGE_TITLE,PaymentPage.PaymentPage(self.driver))


   @pytest.mark.parametrize(
        "firstName,lastName,zip",
        [
        (config.TestData.FIRST_NAME,config.TestData.LAST_NAME,config.TestData.ZIP),
        (config.TestData.FIRST_NAME,config.TestData.ZIP,config.TestData.ZIP),
        (config.TestData.ZIP,config.TestData.LAST_NAME,config.TestData.ZIP),
        (config.TestData.FIRST_NAME,config.TestData.LAST_NAME,config.TestData.FIRST_NAME),
      ])

   def test_fill_details(self,firstName,lastName,zip):
        detailsPage=Functions.go_to_details_page(self,config.TestData.STANDARD_USER_NAME)
        detailsPage.fill_details(firstName,lastName,zip)
        Functions.assert_one_function_without_param(self, config.TestData.STANDARD_USER_NAME, detailsPage.verifiy_details,"First and last names must contain letters, while zip codes must contain only numbers")
      

#     # # Check all users error massages 
        
   @pytest.mark.parametrize(
        "firstName,lastName,zip",
        [
        (config.TestData.FIRST_NAME,config.TestData.LAST_NAME,config.TestData.ZIP),
        (config.TestData.FIRST_NAME,config.TestData.EMPTY,config.TestData.ZIP),
        (config.TestData.EMPTY,config.TestData.LAST_NAME,config.TestData.ZIP),
        (config.TestData.FIRST_NAME,config.TestData.LAST_NAME,config.TestData.EMPTY),
      ])

   def test_errors_of_unfill_fileds(self,firstName,lastName,zip):
        detailsPage=Functions.go_to_details_page(self,config.TestData.STANDARD_USER_NAME)
        detailsPage.fill_details(firstName,lastName,zip)
        paymentPage=detailsPage.go_to_payment_summery_page()  
        try:
          assert paymentPage.get_title() == config.TestData.PAYMENT_PAGE_TITLE
        except Exception:
          error =detailsPage.get_error_massage()
          pytest.fail(f"Failed for user '{config.TestData.STANDARD_USER_NAME}':{error}") 

  