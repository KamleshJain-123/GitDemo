import pytest


@pytest.fixture(scope="class")
def setup():
    print("this will execute first")
    yield
    print("this will be execute in last after test")


@pytest.fixture()
def testdata():
    print("this using testdata fixture ")
    return ["Kamlesh", "jain", "Sandeep"]


@pytest.fixture(params=[("Chrome", "Rahul"), ("kamlesh", "Jain"), ("krishna","singh")])
def dataparametrization(request):
    return request.param
