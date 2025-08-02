
class Payloads:
    @staticmethod
    def valid_tariff_id():
        return faker.random_int(min=1, max=10)

    @staticmethod
    def invalid_tariff_id():
        return faker.random_int(min=999, max=9999)

    @staticmethod
    def valid_payment_data():
        return {
            "tariff_id": faker.random_int(min=1, max=10),
            "payment_method": faker.random_element(["card", "bank_transfer"])
        }

    @staticmethod
    def invalid_payment_data():
        return {
            "tariff_id": faker.random_int(min=999, max=9999),
            "payment_method": "invalid_method"
        } 