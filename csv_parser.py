import csv
import ipaddress

#FILE = 'file\Test_Python.csv'
NET_MASKS = {'0.0.0.0': '0',
             '128.0.0.0': '1',
             '192.0.0.0': '2',
             '224.0.0.0': '3',
             '240.0.0.0': '4',
             '248.0.0.0': '5',
             '252.0.0.0': '6',
             '254.0.0.0': '7',
             '255.0.0.0': '8',
             '255.128.0.0': '9',
             '255.192.0.0': '10',
             '255.224.0.0': '11',
             '255.240.0.0': '12',
             '255.248.0.0': '13',
             '255.252.0.0': '14',
             '255.254.0.0': '15',
             '255.255.0.0': '16',
             '255.255.128.0': '17',
             '255.255.192.0': '18',
             '255.255.224.0': '19',
             '255.255.240.0': '20',
             '255.255.248.0': '21',
             '255.255.252.0': '22',
             '255.255.254.0': '23',
             '255.255.255.0': '24',
             '255.255.255.128': '25',
             '255.255.255.192': '26',
             '255.255.255.224': '27',
             '255.255.255.240': '28',
             '255.255.255.248': '29',
             '255.255.255.252': '30',
             '255.255.255.254': '31',
             '255.255.255.255': '32'
             }


def validate_ip_address(address: str):
    """Проверка что ip адрес валидный"""
    try:
        ipaddress.ip_address(address)
        return True
    except ValueError:
        return False


def validate_ip_mask(mask: str):
    """Проверка что маска сети валидная"""
    if mask in NET_MASKS:
        return True
    else:
        return False


def calculate_net_addr(address: str, mask: str):
    """Вычисление адреса сети"""
    if not validate_ip_mask(mask) or not validate_ip_address(address):
        return ''
    mask_prefix = NET_MASKS[mask]
    some_net = ipaddress.ip_network('0.0.0.0/{}'.format(mask_prefix))
    count_hosts = some_net.num_addresses
    address = ipaddress.ip_address(address)
    net_address = address - (int(address) % count_hosts)
    return net_address


def validate_num(num: str):
    """Проверка на порядковый номер"""
    try:
        num = int(num)
        if num > 1:
            return True
        else:
            return False
    except ValueError:
        return False


def parse_file(file: str):
    """Основная логика парсинга csv"""
    result = []
    previous_num = 0
    with open(file, 'r') as f:
        reader = csv.reader(f, delimiter=';')
        for row in reader:
            errors = []
            address, mask, subnet, num, fio = row
            # Если IP-адрес имеет формат, отличный от стандартного, в столбец ошибки вносится отметка «IP err».
            if not validate_ip_address(address):
                errors.append("IP err")
            # Если маска подсети имеет формат, отличный от стандартного, в столбец ошибки вносится отметка «Mask err».
            if not validate_ip_mask(mask):
                errors.append("Mask err")
            # Если адрес подсети имеет формат, отличный от стандартного, в столбец ошибки вносится отметка «Subnet err».
            if not validate_ip_address(subnet):
                errors.append("Subnet err")
            # Если подсеть указана неверно, в столбец ошибки вносится отметка «Subnet incorrect».
            else:
                real_subnet = calculate_net_addr(address, mask)
                if real_subnet != subnet:
                    errors.append("Subnet incorrect")
            # Если подсеть не указана, то она вычисляется и вносится в соответствующий столбец.
            if subnet == '':
                row[2] = calculate_net_addr(address,mask)
            # Если номер компьютера отсутствует, то он должен быть присвоен в порядке возрастания.
            if num == '':
                num = previous_num + 1
                row[3] = num
            # Если номер компьютера имеет формат, отличный от стандартного, в столбец ошибки вносится отметка «Num err»
            elif not validate_num(num):
                errors.append("Num err")
            else:
                num = int(num)
                # Если номер компьютера повторяется, то он должен быть заменён на очередной в порядке возрастания.
                if num <= previous_num:
                    num = previous_num + 1
                    row[3] = num
                previous_num = int(num)
            row.append(' '.join(errors))
            result.append(row)
    with open(file, 'w', newline='') as f:
        writer = csv.writer(f, delimiter=';')
        writer.writerows(result)


if __name__ == '__main__':
    parse_file(FILE)
