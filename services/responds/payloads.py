
class Payloads:

    @staticmethod
    def valid_responds_params():
        return {
            "page": 1,
            "limit": 10,
            "sort": "date",
            "order": "desc"
        }

    @staticmethod
    def invalid_responds_params():
        return {
            "page": -1,
            "limit": 0,
            "sort": "invalid_sort",
            "order": "invalid_order"
        }

    @staticmethod
    def valid_pagination_params():
        return {
            "page": faker.random_int(min=1, max=10),
            "limit": faker.random_int(min=5, max=50)
        }

    @staticmethod
    def valid_sort_params():
        return {
            "sort": faker.random_element(["date", "name", "status"]),
            "order": faker.random_element(["asc", "desc"])
        }