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
import DetailsPage
import PaymentPage
import CartPage
import InfoPage
import FinishPage

#From Tests
from test_base import BaseTest
from Tests.Func import Functions 


class Test_PaymentPage(BaseTest):
            
   @pytest.fixture(params=[
              config.TestData.STANDARD_USER_NAME,
              config.TestData.VISUAL_USER_NAME,
              config.TestData.GLITCH_USER_NAME,
              config.TestData.ERROR_USER_NAME,
          ])

   def username(self, request):
              return request.param

   def test_go_to_info_page(self,username):
          paymentPage= Functions.go_to_payment_page_with_products(self,username)
          infoPage=paymentPage.go_to_info_page("Bike")
          Functions.assert_move_from_page(self,username,infoPage.get_title,config.TestData.INFO_PAGE_TITLE,InfoPage.InfoPage(self.driver))

   def test_correct_total_price(self,username):
          paymentPage=Functions.go_to_payment_page_with_products(self,username)
          Functions.assert_one_function_without_param(self, username, paymentPage.verify_correct_total_price,"Inccorect price")
        

   def test_correct_payment_information(self,username):
          paymentPage=Functions.go_to_payment_page_with_products(self,username)
          Functions.assert_one_function_without_param_with_comparison(self,username,paymentPage.get_shipping_info,config.TestData.SHIPPING_INFO,"Worng shipping information")
      

   def test_finish_the_purchase(self,username):
          paymentPage=Functions.go_to_payment_page_with_products(self,username)
          finishPage=paymentPage.finish_the_purchase()
          Functions.assert_move_from_page(self,username,finishPage.get_title,config.TestData.FINISH_PAGE_TITLE,FinishPage.FinishPage(self.driver))