import pytest
import sys

sys.path.append("C:\\Users\\Kfir\\Documents\\program\\Pytest\\src\\Conf")
sys.path.append("C:\\Users\\Kfir\\Documents\\program\\Pytest\\src\\Pages")
sys.path.append("C:\\Users\\Kfir\\Documents\\program\\Pytest\\src\\Tests")

#From Conf
import config

#From Pages
import LoginPage
import MainPage
import CartPage
import DetailsPage
import PaymentPage

###################################################
#This class is intended for the recognition of several functions and functionalities that transfer from page to page
###################################################

class  Functions():
    
    def go_to_main_page(self,username):
     self.loginPage=LoginPage.LoginPage(self.driver)
     return self.loginPage.do_login(username,config.TestData.PASSWORD)  

    def go_to_cart_page(self,username):
      mainPage=Functions.go_to_main_page(self,username)
      return  mainPage.go_to_cart_page()     
    
    def go_to_info_page(self,username,product):
     mainPage=Functions.go_to_main_page(self,username)
     return mainPage.go_to_info_page(product)
    
    def go_to_details_page(self,username):
     cartPage=Functions.go_to_cart_page(self,username)
     return cartPage.go_to_details_page()


    def go_to_payment_page_with_products(self,username):
        mainPage= Functions.go_to_main_page(self,username)
        mainPage.remove_from_cart()
        mainPage.add_to_cart_specific_product("Bike")
        mainPage.add_to_cart_specific_product("Jacket")
        cartPage=mainPage.go_to_cart_page()
        detailsPage= cartPage.go_to_details_page()
        detailsPage.fill_details(config.TestData.FIRST_NAME,config.TestData.LAST_NAME,config.TestData.ZIP)
        return detailsPage.go_to_payment_summery_page()

   
    def go_to_finish_page(self,username):
        paymentPage = Functions.go_to_payment_page_with_products(self,username)
        return  paymentPage.finish_the_purchase()       



    def assert_one_function_without_param_with_comparison(self,username,func1,comparison,error):
     try: 
      assert func1() == comparison 
     except Exception:
      error =error 
      pytest.fail(f"Failed for user '{username}':{error}")
    

    def assert_move_from_page(self,username, func1,titleOfNextPage,object):
     try:  
        assert func1() == titleOfNextPage 
     except Exception:
         error="Didn't reach the desire page"
         pytest.fail(f"Failed for user '{username}':{error}")


    def assert_one_function_without_param(self,username, func1,error):
     try: 
        assert func1() == True 
     except Exception:
         print(error)
         print(func1())
         pytest.fail(f"Failed for user '{username}'")



    def assert_one_function_with_param(self,username, func1,param, error):
     try: 
        assert func1(param) == True 
     except Exception:
         print(error)
         print(func1(param))
         pytest.fail(f"Failed for user '{username}'")




    def assert_three_functions_with_one_param(self, username, func1,func2,func3,param1,error1,error2):
       try: 
         if func1(param1) == True :
             func2(param1)
             assert func3(param1)
         else:
             print(error2)
             pytest.fail(f"Failed for user '{username}'")    
       except Exception:
                print(error1)
                pytest.fail(f"Failed for user '{username}'") 
                

    def assert_two_functions_with_param_for_func1(self, username, func1,func2,param1,error1,error2):
        try: 
         if func1(param1) == True :
             assert func2()
         else:
             print(error2)
             pytest.fail(f"Failed for user '{username}'")    
        except Exception:
                print(error1)
                pytest.fail(f"Failed for user '{username}'") 