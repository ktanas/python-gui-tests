import pytest
from fixture.application import Application


@pytest.fixture(scope="session")
def app(request):
    fixture = Application("c:\\Users\\ktana\\addressbook\\AddressBook.exe")
    request.addfinalizer(fixture.destroy)
    return fixture

