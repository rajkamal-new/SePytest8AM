import pytest

from base.driver_init import driver_init


@pytest.fixture(scope="session", autouse=True)
def init_driver(request):
    driver = driver_init()
    session = request.node
    for item in session.items:
        cls = item.getparent(pytest.Class)
        setattr(cls.obj, "driver", driver)
    yield
    driver.close()
