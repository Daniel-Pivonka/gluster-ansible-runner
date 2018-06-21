import ansible_runner

#playbook
playbook = 'brick_setup.yml'


#hosts
ip_1 = '192.168.122.158'
ip_2 = '192.168.122.18'
ip_3 = '192.168.122.145'

#create ip list from raw data
ip_list = []
ip_list.append(ip_1)
ip_list.append(ip_2)
ip_list.append(ip_3)

#create ips dict from list of ips
ip_dict = {}
for i in ip_list:
    ip_dict[i] = ''

#create hosts from ips
hosts = {}
hosts['hosts'] = ip_dict

#creat test group and fill with hosts
inventory = {}
inventory['vdos'] = hosts


#variables
vars = {
	"vars": {
		"gluster_infra_pvs": "/dev/vdb",
		"gluster_infra_lv_logicalvols": [
			{
				"lvname": "thin_lv1",
				"lvsize": "25G"
			},
			{
				"lvname": "thin_lv2",
				"lvsize": "25G"
			}
		],
		"gluster_infra_mount_devices": [
			{
				"path": "/mnt/thinv1",
				"lv": "thin_lv1"
			},
			{
				"path": "/mnt/thinv2",
				"lv": "thin_lv2"
			}
		]
	}
}

#run playbook wiht inventory
r = ansible_runner.run(private_data_dir = '/home/dpivonka/Documents/gluster_ansible_runner/ansible',
                       playbook = playbook,
                       inventory = inventory,
                       extravars = vars)
