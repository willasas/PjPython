from imp import reload
from faker import Faker

fake = Faker()

# locale参数指定语言，不带参数则默认为英语
fake = Faker(locale='zh_CN')

# 生成姓名和地址
name = fake.name()
address = fake.address()


print(name)
print(address)
