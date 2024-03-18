from env_config import ExpectedData

def test_get_all_stores(stores_route):
    stores_route.get_stores(expected_data=ExpectedData.STORES)