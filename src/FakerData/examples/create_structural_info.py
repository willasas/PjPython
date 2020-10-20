from faker import Faker

fake = Faker(locale='zh_CN')
print('生成Python字典: {}'.format(fake.pydict(
    nb_elements=10, variable_nb_elements=True)))  # Python字典
print('生成Python可迭代对象:{}.'.format(fake.pyiterable(
    nb_elements=10, variable_nb_elements=True)))   # Python可迭代对象
print('生成Python结构：{}'.format(fake.pystruct(count=1)))  # Python结构
