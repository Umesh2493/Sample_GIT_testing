import pytest

from PageObject.Login_page import SwaglabsLogin

def test_start():
    assert SwaglabsLogin().start() == True
    print("Success Automation started")

def test_login():
    assert SwaglabsLogin().Login() == True
    print("Success Login")

def test_shutdown():
    assert SwaglabsLogin().shutdown() == None
    print ("Success Shutdown")

