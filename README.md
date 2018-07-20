# Gluster Ansible Runner

gluster ansible runner is a proof of concept tool to automate user interaction with gluster ansible through command line arguments. The goal is to use this to build a tool that will automate WA's interation with gluster ansible.

# Command Line Arguments

*all command line arguments must be formated in a json style and wrapped in quotes to be parsed properly, True and False options must be capitalized*

#####  -p PLAYBOOK, --playbook PLAYBOOK
                        Specify the playbook you want ansible to use
                        infra.yml, cluster.yml, features.yml, repo.yml
#####  -i INVENTORY, --inventory INVENTORY
                        Specify the inventory you want ansible to use. Input format example below
                        "[vdos:192.168.122.158,192.168.122.159,192.168.122.160],[other:192.168.122.158,192.168.122.159],[more:192.168.122.158]"
                        "[vdos:192.168.122.158,192.168.122.158,192.168.122.158],[other:192.168.122.158]"
                        "[vdos:192.168.122.158,192.168.122.158,192.168.122.158]"
#####  --gluster_infra_fw_state GLUSTER_INFRA_FW_STATE
                        Enable or disable a setting. For ports: Should this
                        port accept(enabled) or reject(disabled) connections.
                        The states "present" and "absent" can only be used in
                        zone level operations (i.e. when no other parameters
                        but zone and state are set).
#####  --gluster_infra_fw_ports GLUSTER_INFRA_FW_PORTS
                        A list of ports in the format PORT/PROTO. For example
                        111/tcp. This is a list value.
#####  --gluster_infra_fw_permanent GLUSTER_INFRA_FW_PERMANENT
                        Whether to make the rule permanenet.
#####  --gluster_infra_fw_zone GLUSTER_INFRA_FW_ZONE
                        The firewalld zone to add/remove to/from
#####  --gluster_infra_fw_services GLUSTER_INFRA_FW_SERVICES
                        Name of a service to add/remove to/from firewalld -
                        service must be listed in output of firewall-cmd
                        --get-services. This is a list variable
#####  --gluster_infra_vdo_state GLUSTER_INFRA_VDO_STATE
                        Optional variable, default is taken as present.
#####  --gluster_infra_vdo GLUSTER_INFRA_VDO
                        Mandatory argument if vdo has to be setup. Key/Value
                        pairs have to be given. name and device are the keys,
                        see examples for syntax.
#####  --gluster_infra_disktype GLUSTER_INFRA_DISKTYPE
                        Backend disk type.
#####  --gluster_infra_diskcount	 GLUSTER_INFRA_DISKCOUNT
                        RAID diskcount, can be ignored if disktype is JBOD
#####  --gluster_infra_vg_name GLUSTER_INFRA_VG_NAME
                        Optional variable, if not provided glusterfs_vg is
                        used as vgname.
#####  --gluster_infra_pvs GLUSTER_INFRA_PVS
                        Comma-separated list of physical devices. If vdo is
                        used this variable can be omitted.
#####  --gluster_infra_stripe_unit_size GLUSTER_INFRA_STRIPE_UNIT_SIZE
                        Stripe unit size (KiB). DO NOT including trailing 'k'
                        or 'K'
#####  --gluster_infra_lv_poolmetadatasize GLUSTER_INFRA_LV_POOLMETADATASIZE
                        Metadata size for LV, recommended value 16G is used by
                        default. That value can be overridden by setting the
                        variable. Include the unit [G|M|K]
#####  --gluster_infra_lv_thinpoolname GLUSTER_INFRA_LV_THINPOOLNAME
                        Optional variable. If omitted glusterfs_thinpool is
                        used for thinpoolname.
#####  --gluster_infra_lv_thinpoolsize GLUSTER_INFRA_LV_THINPOOLSIZE
                        Thinpool size, if not set, entire disk is used.
                        Include the unit [G|M|K]
#####  --gluster_infra_lv_logicalvols GLUSTER_INFRA_LV_LOGICALVOLS
                        This is a list of hash/dictionary variables, with
                        keys, lvname and lvsize.
#####  --gluster_infra_lv_thicklvname GLUSTER_INFRA_LV_THICKLVNAME
                        Optional. Needed only if thick volume has to be
                        created. The variable will have default name
                        gluster_infra_lv_thicklvname if thicklvsize is
                        defined.
#####  --gluster_infra_lv_thicklvsize GLUSTER_INFRA_LV_THICKLVSIZE
                        Optional. Needed only if thick volume has to be
                        created. Include the unit [G|M|K]
#####  --gluster_infra_mount_devices GLUSTER_INFRA_MOUNT_DEVICES
                        This is a dictionary with mount values. path, and lv
                        are the keys.
#####  --gluster_infra_ssd_disk GLUSTER_INFRA_SSD_DISK
                        SSD disk for cache setup, specific to HC setups.
                        Should be absolute path. e.g /dev/sdc
#####  --gluster_infra_lv_cachelvname GLUSTER_INFRA_LV_CACHELVNAME
                        Optional variable, if omitted glusterfs_ssd_cache is
                        used by default.
#####  --gluster_infra_lv_cachelvsize GLUSTER_INFRA_LV_CACHELVSIZE
                        Size of the cache logical volume. Used only while
                        setting up cache.
#####  --gluster_infra_lv_cachemetalvname GLUSTER_INFRA_LV_CACHEMETALVNAME
                        Optional. Cache metadata volume name.
#####  --gluster_infra_lv_cachemetalvsize GLUSTER_INFRA_LV_CACHEMETALVSIZE
                        Optional. Cache metadata volume size.
#####  --gluster_infra_cachemode GLUSTER_INFRA_CACHEMODE
                        Optional. If omitted writethrough is used.
#####  --gluster_cluster_arbiter_count GLUSTER_CLUSTER_ARBITER_COUNT
                        Number of arbiter bricks to use (Only for arbiter
                        volume types).
#####  --gluster_cluster_bricks GLUSTER_CLUSTER_BRICKS
                        Bricks that form the GlusterFS volume. The format of
                        the bricks would be hostname:mountpoint/brick_dir
                        alternatively user can provide just
                        mountpoint/birck_dir, in such a case gluster_hosts
                        variable has to be set
#####  --gluster_cluster_disperse_count GLUSTER_CLUSTER_DISPERSE_COUNT
                        Disperse count for the volume. If this value is
                        specified, a dispersed volume will be created
#####  --gluster_cluster_force GLUSTER_CLUSTER_FORCE
                        Force option will be used while creating a volume, any
                        warnings will be suppressed.
#####  --gluster_cluster_hosts GLUSTER_CLUSTER_HOSTS
                        Contains the list of hosts that have to be peer
                        probed.
#####  --gluster_cluster_redundancy_count GLUSTER_CLUSTER_REDUNDANCY_COUNT
                        Specifies the number of redundant bricks while
                        creating a disperse volume. If redundancy count is
                        missing an optimal value is computed.
#####  --gluster_cluster_replica_count GLUSTER_CLUSTER_REPLICA_COUNT
                        Replica count while creating a volume. Currently
                        replica 2 and replica 3 are supported.
#####  --gluster_cluster_state GLUSTER_CLUSTER_STATE
                        If value is present volume will be created. If value
                        is absent, volume will be deleted. If value is
                        started, volume will be started. If value is stopped,
                        volume will be stopped.
#####  --gluster_cluster_transport GLUSTER_CLUSTER_TRANSPORT
                        The transport type for the volume.
#####  --gluster_cluster_volume GLUSTER_CLUSTER_VOLUME
                        Name of the volume. Refer GlusterFS documentation for
                        valid characters in a volume name.
#####  --gluster_cluster_new_bricks GLUSTER_CLUSTER_NEW_BRICKS
                        Contains the list of bricks along with the new bricks
                        to be added to the GlusterFS volume. The format of the
                        bricks is mountpoint/brick_dir
#####  --gluster_cluster_remove_bricks GLUSTER_CLUSTER_REMOVE_BRICKS
                        Contains the list of bricks to be removed.
#####  --gluster_features_ganesha_haname GLUSTER_FEATURES_GANESHA_HANAME
                        Name of the NFS Ganesha cluster.
#####  --gluster_features_ganesha_volume GLUSTER_FEATURES_GANESHA_VOLUME
                        An existing GlusterFS volume which will be exported
                        through NFS Ganesha
#####  --gluster_features_ganesha_hostnames	 GLUSTER_FEATURES_GANESHA_HOSTNAMES
                        A comma separated list of hostnames, these are subset
                        of nodes of the Gluster Trusted Pool that form the
                        ganesha HA cluster
#####  --gluster_features_ganesha_viplist GLUSTER_FEATURES_GANESHA_VIPLIST
                        A comma separated list of virtual IPs for each of the
                        nodes specified above.
#####  --gluster_features_ganesha_masternode GLUSTER_FEATURES_GANESHA_MASTERNODE
                        One of the nodes from the Trusted Storage Pool,
                        gluster commands will be run on this node.
                        gluster_features_ganesha_masternode: {{
                        groups['ganesha_nodes'][0] }} - the first node of the
                        inventory section ganesha_nodes will be used.
#####  --gluster_features_ganesha_clusternodes GLUSTER_FEATURES_GANESHA_CLUSTERNODES
                        List of the nodes in the Trusted Storage Pool.
                        gluster_features_ganesha_clusternodes: {{
                        groups['ganesha_nodes'] }} - The nodes listed in
                        section ganesha_nodes in the inventory.
#####  --gluster_features_hci_cluster GLUSTER_FEATURES_HCI_CLUSTER
                        The cluster ip/hostnames. Can be set by
                        gluster_hci_cluster: {{ groups['hc-nodes'] }}, where
                        hc-nodes is from the inventory file.
#####  --gluster_features_hci_volumes GLUSTER_FEATURES_HCI_VOLUMES
                        This is a dictionary setting the volume information.
                        See below for further explanation and variables.
#####  --gluster_features_hci_packages GLUSTER_FEATURES_HCI_PACKAGES
                        List of packages to be installed. User need not set
                        this, picked up from defaults.
#####  --gluster_features_hci_volume_options GLUSTER_FEATURES_HCI_VOLUME_OPTIONS
                        This is not needed to be set by user, defaults are
                        picked up. Set to override defaults. For default
                        values see Gluster HCI documentation.
#####  --gluster_repos_activationkey GLUSTER_REPOS_ACTIVATIONKEY
                        Activation key for enabling the repositories
#####  --gluster_repos_attach GLUSTER_REPOS_ATTACH
                        Whether to auto-attach the available repositories
#####  --gluster_repos_username GLUSTER_REPOS_USERNAME
                        Username for the subscription-manager command
#####  --gluster_repos_password GLUSTER_REPOS_PASSWORD
                        Password for the subscription-manager command
#####  --gluster_repos_force GLUSTER_REPOS_FORCE
                        If set to yes, subscription-manager registers by force
                        even if already registerd
#####  --gluster_repos_pools GLUSTER_REPOS_POOLS
                        List of pool ids to attach
#####  --gluster_repos_disable_all GLUSTER_REPOS_DISABLE_ALL
                        Disable all the repositories before attaching to new
                        repositories
#####  --gluster_repos_rhsmrepos GLUSTER_REPOS_RHSMREPOS
                        List of repositories to enable
#####  --gluster_repos_hci_subscribe GLUSTER_REPOS_HCI_SUBSCRIBE
                        Attach to HCI repositories
#####  --gluster_repos_nfsganesha_subscribe GLUSTER_REPOS_NFSGANESHA_SUBSCRIBE
                        Attach to list of NFS Ganesha repositories
#####  --gluster_repos_smb_subscribe GLUSTER_REPOS_SMB_SUBSCRIBE
                        Attach to list of SMB repositores


### Use examples

*copy your ssh key to the root user on all nodes prior or ansible will fail to connect*

./test.py --inventory "[vdos:192.168.122.79,192.168.122.121,192.168.122.249]" -p "infra.yml" --gluster_infra_pvs "/dev/vdb" --gluster_infra_lv_logicalvols "[{"lvname": "thin_lv1", "lvsize": "25G"}, {"lvname": "thin_lv2", "lvsize": "25G"}]" --gluster_infra_mount_devices "[{"path": "/mnt/thinv1", "lv": "thin_lv1"}, {"path": "/mnt/thinv2", "lv": "thin_lv2"}]"

./test.py --inventory "[vdos:192.168.122.79,192.168.122.121,192.168.122.249]" -p "infra.yml" --gluster_infra_fw_ports "["2049/tcp", "54321/tcp", "5900/tcp", "5900-6923/tcp", "5666/tcp", "16514/tcp"]" --gluster_infra_fw_permanent "True" --gluster_infra_fw_state "enabled" --gluster_infra_fw_zone "public" --gluster_infra_fw_services "["glusterfs"]"

./test.py --inventory "[rhsm:192.168.122.206]" -p "repo.yml" --gluster_repos_username "dpivonka@redhat.com" --gluster_repos_password "*******" --gluster_repos_disable_all "True" --gluster_repos_pools "8a85f98c617475400161756d571b1485" --gluster_repos_rhsmrepos "["rhel-7-server-rpms", "rhel-ha-for-rhel-7-server-rpms"]"

