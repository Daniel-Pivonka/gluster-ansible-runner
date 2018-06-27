import ansible_runner
import argparse

parser = argparse.ArgumentParser(description='gluster-ansible-runner')

parser.add_argument('-p', '--playbook', required=True, help='Specify the playbook you want ansible to use')
#--playbook brick_setup.yml

parser.add_argument('-i', '--inventory', required=True, help='Specify the inventory you want ansible to use. Check code for format examples')
#inventory input examples
#--inventory [vdos:192.168.122.158,192.168.122.159,192.168.122.160],[other:192.168.122.158,192.168.122.159],[more:192.168.122.158]
#--inventory [vdos:192.168.122.158,192.168.122.158,192.168.122.158],[other:192.168.122.158]
#--inventory [vdos:192.168.122.158,192.168.122.158,192.168.122.158]

args = parser.parse_args()

#create inventroy
inventory = {}
#break up groups
groups = args.inventory.split('],[')
#go thru groups
for group in groups:
    #remove extra '[' & ']'
    group = group.replace('[', '')
    group = group.replace(']', '')
    #split group name from ips
    split = group.split(':')
    #creat inner dicts
    hosts = {}
    ips = {}
    #split ips
    ip_list = split[1].split(',')
    #fill ip dict with ips
    for ip in ip_list:
        ips[ip] = ''
    #put ip dict in host dict
    hosts['hosts'] = ips
    #put host in group in inventory dict
    inventory[split[0]] = hosts

#playbook
playbook = args.playbook

#variables
vars = {"gluster_infra_pvs": "/dev/vdb",
		"gluster_infra_lv_logicalvols": [
			{"lvname": "thin_lv1",
			 "lvsize": "25G"},
			{"lvname": "thin_lv2",
			 "lvsize": "25G"}
		],
		"gluster_infra_mount_devices": [
			{"path": "/mnt/thinv1",
			 "lv": "thin_lv1"},
			{"path": "/mnt/thinv2",
			 "lv": "thin_lv2"}
		]
}

settings = {"suppress_ansible_output": False}

#run playbook wiht inventory
r = ansible_runner.run(private_data_dir = '/home/dpivonka/Documents/gluster-ansible-runner/ansible',
                       playbook = playbook,
                       inventory = inventory,
                       extravars = vars,
                       settings = settings)
