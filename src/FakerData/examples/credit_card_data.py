from faker import Faker

fake = Faker(locale='zh_CN')
print('Card Number:', fake.credit_card_number(card_type=None))
print('Card Provider:', fake.credit_card_provider(card_type=None))
print('Card Security Code:', fake.credit_card_security_code(card_type=None))
print('Card Expire:', fake.credit_card_expire())
