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

#From Tests
from test_base import BaseTest
from Tests.Func import Functions


class Test_FinishPage (BaseTest):
   
   @pytest.fixture(params=[
          config.TestData.STANDARD_USER_NAME,
          config.TestData.VISUAL_USER_NAME,
          config.TestData.GLITCH_USER_NAME,
          ])
      
   def username(self, request):
              return request.param

   def test_messages_describe(self,username):
    finishPage=Functions.go_to_finish_page(self,username)
    Functions.assert_one_function_without_param_with_comparison(self,username,finishPage.get_description,config.TestData.DESCRIBE_MASSAGE,"The cart description is worng")

   def test_messages(self,username):
    finishPage=Functions.go_to_finish_page(self,username)
    Functions.assert_one_function_without_param_with_comparison(self,username,finishPage.get_thank_you_massage,config.TestData.MESSAGE_OF_COMPLETE,"The massage of thank you is worng")


   def test_messages(self,username):
    finishPage=Functions.go_to_finish_page(self,username)
    Functions.assert_one_function_without_param_with_comparison(self,username,finishPage.get_thank_you_massage,config.TestData.MESSAGE_OF_COMPLETE,"The massage of thank you is worng")


   def test_cart_is_empty(self,username):
    finishPage=Functions.go_to_finish_page(self,username)
    Functions.assert_one_function_without_param(self, username, finishPage.verify_cart_is_empty,"The cart is not empty after the purchase")


   def test_go_to_home_page(self,username):
    finishPage=Functions.go_to_finish_page(self,username)
    mainPage=finishPage.go_to_home_page()
    Functions.assert_move_from_page(self, username, mainPage.get_title,config.TestData.MAIN_PAGE_TITLE,MainPage.MainPage(self.driver))