from faker import Faker

faker = Faker()


class Payloads:
#     @staticmethod
#     def recruiter_register_params():
#         person_type = faker.random_element(elements=["Физлицо", "Организация"])
#
#         payload = {
#             "phone": "+7" + faker.numerify("98########"),
#             "fio": faker.name(),
#             "guid": faker.uuid4(),
#             "email": faker.email(domain="api-autofake.ru"),
#             "person_type": person_type,
#         }
#
#         if person_type == "Организация":
#             payload["legal_inn"] = faker.random_int(1000000000, 9999999999, 9)
#             payload["legal_name"] = faker.company()
#
#         return payload

    @staticmethod
    def recruiter_register_params():
        person_type = faker.random_element(elements=["Физлицо", "Организация"])

        # Если организация — создаём список с одним словарём
        if person_type == "Организация":
            legal_data = [{
                "inn": str(faker.random_int(min=1000000000, max=9999999999)),
                "name": faker.company()
            }]
        else:
            legal_data = [{"inn": "str", "name": "str"}]  # Пустой словарь для физлица

        return {
            "phone": "+7" + faker.numerify("98########"),
            "fio": faker.name(),
            "guid": faker.uuid4(),
            "email": faker.email(),
            "person_type": person_type,
            "legal_data": legal_data  # Список с одним словарём или пустой
            }

print(Payloads.recruiter_register_params())