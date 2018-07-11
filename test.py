#!/usr/bin/python

import ansible_runner
import argparse
import os

#global parser var
parser = argparse.ArgumentParser(description='gluster-ansible-runner')

def setup_args():
    parser.add_argument('-p', '--playbook', required=True, help='Specify the playbook you want ansible to use')
    #--playbook brick_setup.yml

    parser.add_argument('-i', '--inventory', required=True, help='Specify the inventory you want ansible to use. Check code for format examples')
    #inventory input examples
    #--inventory [vdos:192.168.122.158,192.168.122.159,192.168.122.160],[other:192.168.122.158,192.168.122.159],[more:192.168.122.158]
    #--inventory [vdos:192.168.122.158,192.168.122.158,192.168.122.158],[other:192.168.122.158]
    #--inventory [vdos:192.168.122.158,192.168.122.158,192.168.122.158]

    #infra
    parser.add_argument('--gluster_infra_fw_state', help='Enable or disable a setting. For ports: Should this port accept(enabled) or reject(disabled) connections. The states "present" and "absent" can only be used in zone level operations (i.e. when no other parameters but zone and state are set).')
    parser.add_argument('--gluster_infra_fw_ports', help='A list of ports in the format PORT/PROTO. For example 111/tcp. This is a list value.')
    parser.add_argument('--gluster_infra_fw_permanent', help='Whether to make the rule permanenet.')
    parser.add_argument('--gluster_infra_fw_zone', help='The firewalld zone to add/remove to/from')
    parser.add_argument('--gluster_infra_fw_services', help='Name of a service to add/remove to/from firewalld - service must be listed in output of firewall-cmd --get-services. This is a list variable')
    parser.add_argument('--gluster_infra_vdo_state', help='Optional variable, default is taken as present.')
    parser.add_argument('--gluster_infra_vdo', help='Mandatory argument if vdo has to be setup. Key/Value pairs have to be given. name and device are the keys, see examples for syntax.')
    parser.add_argument('--gluster_infra_disktype', help='Backend disk type.')
    parser.add_argument('--gluster_infra_diskcount	', help='RAID diskcount, can be ignored if disktype is JBOD')
    parser.add_argument('--gluster_infra_vg_name', help='Optional variable, if not provided glusterfs_vg is used as vgname.')
    parser.add_argument('--gluster_infra_pvs', help='Comma-separated list of physical devices. If vdo is used this variable can be omitted.')
    parser.add_argument('--gluster_infra_stripe_unit_size', help="Stripe unit size (KiB). DO NOT including trailing 'k' or 'K'")
    parser.add_argument('--gluster_infra_lv_poolmetadatasize', help='Metadata size for LV, recommended value 16G is used by default. That value can be overridden by setting the variable. Include the unit [G|M|K]')
    parser.add_argument('--gluster_infra_lv_thinpoolname', help='Optional variable. If omitted glusterfs_thinpool is used for thinpoolname.')
    parser.add_argument('--gluster_infra_lv_thinpoolsize', help='Thinpool size, if not set, entire disk is used. Include the unit [G|M|K]')
    parser.add_argument('--gluster_infra_lv_logicalvols', help='This is a list of hash/dictionary variables, with keys, lvname and lvsize.')
    parser.add_argument('--gluster_infra_lv_thicklvname', help='Optional. Needed only if thick volume has to be created. The variable will have default name gluster_infra_lv_thicklvname if thicklvsize is defined.')
    parser.add_argument('--gluster_infra_lv_thicklvsize', help='Optional. Needed only if thick volume has to be created. Include the unit [G|M|K]')
    parser.add_argument('--gluster_infra_mount_devices', help='This is a dictionary with mount values. path, and lv are the keys.')
    parser.add_argument('--gluster_infra_ssd_disk', help='SSD disk for cache setup, specific to HC setups. Should be absolute path. e.g /dev/sdc')
    parser.add_argument('--gluster_infra_lv_cachelvname', help='Optional variable, if omitted glusterfs_ssd_cache is used by default.')
    parser.add_argument('--gluster_infra_lv_cachelvsize', help='Size of the cache logical volume. Used only while setting up cache.')
    parser.add_argument('--gluster_infra_lv_cachemetalvname', help='Optional. Cache metadata volume name.')
    parser.add_argument('--gluster_infra_lv_cachemetalvsize', help='Optional. Cache metadata volume size.')
    parser.add_argument('--gluster_infra_cachemode', help='Optional. If omitted writethrough is used.')

    #cluster
    parser.add_argument('--gluster_cluster_arbiter_count', help='Number of arbiter bricks to use (Only for arbiter volume types).')
    parser.add_argument('--gluster_cluster_bricks', help='Bricks that form the GlusterFS volume. The format of the bricks would be hostname:mountpoint/brick_dir alternatively user can provide just mountpoint/birck_dir, in such a case gluster_hosts variable has to be set')
    parser.add_argument('--gluster_cluster_disperse_count', help='Disperse count for the volume. If this value is specified, a dispersed volume will be created')
    parser.add_argument('--gluster_cluster_force', help='Force option will be used while creating a volume, any warnings will be suppressed.')
    parser.add_argument('--gluster_cluster_hosts', help='Contains the list of hosts that have to be peer probed.')
    parser.add_argument('--gluster_cluster_redundancy_count', help='Specifies the number of redundant bricks while creating a disperse volume. If redundancy count is missing an optimal value is computed.')
    parser.add_argument('--gluster_cluster_replica_count', help='Replica count while creating a volume. Currently replica 2 and replica 3 are supported.')
    parser.add_argument('--gluster_cluster_state', help='If value is present volume will be created. If value is absent, volume will be deleted. If value is started, volume will be started. If value is stopped, volume will be stopped.')
    parser.add_argument('--gluster_cluster_transport', help='The transport type for the volume.')
    parser.add_argument('--gluster_cluster_volume', help='Name of the volume. Refer GlusterFS documentation for valid characters in a volume name.')
    parser.add_argument('--gluster_cluster_new_bricks', help='Contains the list of bricks along with the new bricks to be added to the GlusterFS volume. The format of the bricks is mountpoint/brick_dir')
    parser.add_argument('--gluster_cluster_remove_bricks', help='Contains the list of bricks to be removed.')

    #features
    parser.add_argument('--gluster_features_ganesha_haname', help='Name of the NFS Ganesha cluster.')
    parser.add_argument('--gluster_features_ganesha_volume', help='An existing GlusterFS volume which will be exported through NFS Ganesha')
    parser.add_argument('--gluster_features_ganesha_hostnames	', help='A comma separated list of hostnames, these are subset of nodes of the Gluster Trusted Pool that form the ganesha HA cluster')
    parser.add_argument('--gluster_features_ganesha_viplist', help='A comma separated list of virtual IPs for each of the nodes specified above.')
    parser.add_argument('--gluster_features_ganesha_masternode', help="One of the nodes from the Trusted Storage Pool, gluster commands will be run on this node. gluster_features_ganesha_masternode: {{ groups['ganesha_nodes'][0] }} - the first node of the inventory section ganesha_nodes will be used.")
    parser.add_argument('--gluster_features_ganesha_clusternodes', help="List of the nodes in the Trusted Storage Pool. gluster_features_ganesha_clusternodes: {{ groups['ganesha_nodes'] }} - The nodes listed in section ganesha_nodes in the inventory.")
    parser.add_argument('--gluster_features_hci_cluster', help="The cluster ip/hostnames. Can be set by gluster_hci_cluster: {{ groups['hc-nodes'] }}, where hc-nodes is from the inventory file.")
    parser.add_argument('--gluster_features_hci_volumes', help='This is a dictionary setting the volume information. See below for further explanation and variables.')
    parser.add_argument('--gluster_features_hci_packages', help='List of packages to be installed. User need not set this, picked up from defaults.')
    parser.add_argument('--gluster_features_hci_volume_options', help='This is not needed to be set by user, defaults are picked up. Set to override defaults. For default values see Gluster HCI documentation.')

    #repositores
    parser.add_argument('--gluster_repos_activationkey', help='Activation key for enabling the repositories')
    parser.add_argument('--gluster_repos_attach', help='Whether to auto-attach the available repositories')
    parser.add_argument('--gluster_repos_username', help='Username for the subscription-manager command')
    parser.add_argument('--gluster_repos_password', help='Password for the subscription-manager command')
    parser.add_argument('--gluster_repos_force', help='If set to yes, subscription-manager registers by force even if already registerd')
    parser.add_argument('--gluster_repos_pools', help='List of pool ids to attach')
    parser.add_argument('--gluster_repos_disable_all', help='Disable all the repositories before attaching to new repositories')
    parser.add_argument('--gluster_repos_rhsmrepos', help='List of repositories to enable')
    parser.add_argument('--gluster_repos_hci_subscribe', help='Attach to HCI repositories')
    parser.add_argument('--gluster_repos_nfsganesha_subscribe', help='Attach to list of NFS Ganesha repositories')
    parser.add_argument('--gluster_repos_smb_subscribe', help='Attach to list of SMB repositores')

def parse_args():
    args = parser.parse_args()
    vars = {}

    if args.gluster_infra_fw_state:
        print args.gluster_infra_fw_state

    return vars

def main():
    setup_args()

    vars = parse_args()

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
                           #extravars = vars,
                           verbosity = 3,
                           settings = settings)

if __name__ == "__main__":
    main()
