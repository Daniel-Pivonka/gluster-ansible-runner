import argparse

parser = argparse.ArgumentParser(description='gluster-ansible-runner')

parser.add_argument('-i', '--inventory', required=True, help='Specifc the inventory you want ansible to use check code for format examples')
#inventory input examples
#--inventory [vdos:192.168.122.158,192.168.122.159,192.168.122.160],[other:192.168.122.158,192.168.122.159],[more:192.168.122.158]
#--inventory [vdos:192.168.122.158,192.168.122.158,192.168.122.158],[other:192.168.122.158]
#--inventory [vdos:192.168.122.158,192.168.122.158,192.168.122.158]


args = parser.parse_args()


input = args.inventory


inventory = {}

groups = input.split('],[')

for group in groups:
    group = group.replace('[', '')
    group = group.replace(']', '')
    split = group.split(':')
    hosts = {}
    ips = {}
    ip_list = split[1].split(',')
    for ip in ip_list:
        ips[ip] = ''
    inventory[split[0]] = ips

print inventory
