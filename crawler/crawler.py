ip = input()
address = input()


def isIn(ip, address):
    ip_range = ip.split('.')
    address_header_range, address_body_range = address.split(r'/')
    address_header = address_header_range.split('.')
    for i in range(3):
        if ip_range[i] != address_header[i]:
            return 0
    return 1


if __name__ == "__main__":
    ip = input()
    address = input()
    print(isIn(ip, address))