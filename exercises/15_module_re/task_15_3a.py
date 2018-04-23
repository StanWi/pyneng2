# -*- coding: utf-8 -*-
'''
Задание 15.3a

Переделать функцию parse_cfg из задания 15.3 таким образом, чтобы она возвращала словарь:
* ключ: имя интерфейса
* значение: кортеж с двумя строками:
  * IP-адрес
  * маска

Например (взяты произвольные адреса):
{'FastEthernet0/1':('10.0.1.1', '255.255.255.0'),
 'FastEthernet0/2':('10.0.2.1', '255.255.255.0')}

Для получения такого результата, используйте регулярные выражения.

Проверить работу функции на примере файла config_r1.txt.

Обратите внимание, что в данном случае, можно не проверять корректность IP-адреса,
диапазоны адресов и так далее, так как обрабатывается вывод команды, а не ввод пользователя.

'''
#not complete
import re
from pprint import pprint

def parse_cfg(file: str) -> list:
    regex = ('^interface (?P<interface>\S+)'
             '| ip address (?P<ip>\d+\.\d+\.\d+\.\d+) (?P<mask>\d+\.\d+\.\d+\.\d+)')
    result = {}
    with open(file) as f:
        for line in f:
            match = re.search(regex, line)
            if match:
                if match.lastgroup == 'interface':
                    interface = match.group(match.lastgroup)
                    result[interface] = {}
                elif interface:
                    result[interface] = match.groups()
    return result

if __name__ == '__main__':
    pprint(parse_cfg('config_r1.txt'))
