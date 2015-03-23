#!/usr/bin/python
# -*- coding: utf-8 -*-
# This file defines all variable needed to be edited during the release cycle (alpha, beta...).
release={
    'prev_id':     '20',
    'curr_id':     '21',
    'next_id':     '22',
    'curr_name':   '',
    'next_name':   '',
    'curr_state':  'Alpha',        # either 'Alpha', 'Beta' or '' (i.e empty)
    'curr_arm_state':  'Alpha',         # either 'Alpha', 'Beta' or '' (i.e empty)
    'curr_ppc64_state':  'Alpha',       # either 'Alpha', 'Beta' or '' (i.e empty)
    'curr_s390_state':  'Alpha',        # either 'Alpha', 'Beta' or '' (i.e empty)
    'curr_cloud_state':  'Alpha',       # either 'Alpha', 'Beta' or '' (i.e empty)
    'prev_arm_id': '20',
    'prev_ppc64_id': '20',
    'prev_s390_id': '20',
    'prev_cloud_id': '20',
    'curr_arm_id': '21',
    'curr_ppc64_id': '21',
    'curr_s390_id': '21',
    'curr_cloud_id': '21',
    'next_arm_id': '22',
    'next_ppc64_id': '22',
    'next_s390_id': '22',
    'next_cloud_id': '22',
    'composedate': '20141203',
    'pre_cloud_composedate': '20150305',
    'RC_gold': '5',              # insert the number of the RC version declared GOLD
    'RC_pre_gold': '3'           # insert the number of the prerelease RC version declared GOLD
}

path={
    'torrent':         'http://torrent.fedoraproject.org/torrents',
    'torrent_spins':   'http://torrent.fedoraproject.org/torrents',
    'download':        'http://download.fedoraproject.org/pub/fedora/linux/releases',
    'dl':              'http://download.fedoraproject.org/pub/fedora/linux/updates',
    'download_spins':  'http://download.fedoraproject.org/pub/alt/releases',
    'download_arch':   'http://download.fedoraproject.org/pub/fedora-secondary/releases',
    'mirrors':         'http://mirrors.fedoraproject.org/metalink?path=pub/fedora/linux/releases',
    'checksums':       './static/checksums',
    'doc':             'http://docs.fedoraproject.org/en-US/Fedora'
}

iso_size={
    # Legacy
    'x86_64_DVD':          '4.3',       # In GB
    'i386_DVD':            '4.4',       # In GB
    'source_DVD':          '9.2',       # In GB
    'i686_Live_Desktop':   '922',       # In MB
    'x86_64_Live_Desktop': '953',       # In MB
    'i386_Netinstall':     '357',       # In MB
    'x86_64_Netinstall':   '321',       # In MB
    'PPC64_DVD':           '4.3',       # In GB
    'PPC64_Netinstall':    '340',       # In MB
    's390_DVD':            '4.6',       # In GB
    'i686_sda.qcow2':      '212',       # In MB
    'x86_64_sda.qcow2':    '207',       # In MB
    'i686_raw':            '122',       # In MB
    'x86_64_raw':          '117',       # In MB
    # Lives
    'i686_Live_KDE':       '937',       # In MB
    'x86_64_Live_KDE':     '953',       # In MB
    'i686_Live_LXDE':      '819',       # In MB
    'x86_64_Live_LXDE':    '869',       # In MB
    'i686_Live_Xfce':      '852',       # In MB
    'x86_64_Live_Xfce':    '892',       # In MB
    'i686_Live_Mate':      '1.0',       # In GB
    'x86_64_Live_Mate':    '916',       # In MB
    'i686_Live_Soas':      '713',       # In MB
    'x86_64_Live_Soas':    '755',       # In MB
    # Lives prerelease
    'pre_i686_Live_KDE':    '1.1',       # In GB
    'pre_x86_64_Live_KDE':  '1.1',       # In GB
    'pre_i686_Live_LXDE':   '870',       # In MB
    'pre_x86_64_Live_LXDE': '778',       # In MB
    'pre_i686_Live_Xfce':   '818',       # In MB
    'pre_x86_64_Live_Xfce': '850',       # In MB
    'pre_i686_Live_Mate':   '1.1',       # In GB
    'pre_x86_64_Live_Mate': '1.1',       # In GB
    'pre_i686_Live_Soas':   '721',       # In MB
    'pre_x86_64_Live_Soas': '662',       # In MB
    # Spins
    'i686_Live_Security':  '855',       # In MB
    'x86_64_Live_Security':'890',       # In MB
    'i686_Live_Games':     '3.9',       # In GB
    'x86_64_Live_Games':   '3.9',       # In GB
    'i686_Live_Elab':      '2.5',       # In GB
    'x86_64_Live_Elab':    '2.5',       # In GB
    'i686_Live_Design':    '1.5',       # In GB
    'x86_64_Live_Design':  '1.5',       # In GB
    'i686_Live_Sci-kde':   '3.3',       # In GB
    'x86_64_Live_Sci-kde': '3.3',       # In GB
    'i686_Live_Robotics':  '2.3',       # In GB
    'x86_64_Live_Robotics':'2.4',       # In GB
    'i686_Live_Jam':       '1.5',       # In GB
    'x86_64_Live_Jam':     '1.5',       # In GB
    # Spins prerelease
    'pre_i686_Live_Security':  '877',   # In MB
    'pre_x86_64_Live_Security':'910',   # In MB
    'pre_i686_Live_Games':     '3.8',   # In GB
    'pre_x86_64_Live_Games':   '3.8',   # In GB
    'pre_i686_Live_Elab':      '2.5',   # In GB
    'pre_x86_64_Live_Elab':    '2.5',   # In GB
    'pre_i686_Live_Design':    '1.6',   # In GB
    'pre_x86_64_Live_Design':  '1.7',   # In GB
    'pre_i686_Live_Sci-kde':   '3.0',   # In GB
    'pre_x86_64_Live_Sci-kde': '3.0',   # In GB
    'pre_i686_Live_Robotics':  '2.4',   # In GB
    'pre_x86_64_Live_Robotics':'2.5',   # In GB
    'pre_i686_Live_Jam':       '1.6',   # In GB
    'pre_x86_64_Live_Jam':     '1.7',   # In GB
    # Server
    'x86_64_server_DVD':   '2.1',       # In GB
    'i386_server_DVD':     '2.2',       # In GB
    'x86_64_server_net':   '441',       # In MB
    'i386_server_net':     '504',       # In MB
    # Server prerelease
    'pre_x86_64_server_DVD': '1.9',     # In GB
    'pre_i386_server_DVD':   '2.0',     # In GB
    'pre_x86_64_server_net': '424',     # In MB
    'pre_i386_server_net':   '482',     # In MB
    # Workstation
    'x86_64_workstation':  '1.4',       # In GB
    'i386_workstation':    '1.2',       # In GB
    # Workstation prerelease
    'pre_x86_64_workstation':  '1.4',   # In GB
    'pre_i386_workstation':    '1.1',   # In GB
    # ARM
    'ARM_Workstation':     '1.1',       # In GB
    'ARM_Minimal':         '272',       # In MB
    'ARM_KDE':             '1.0',       # In GB
    'ARM_Xfce':            '756',       # In MB
    'ARM_LXDE':            '700',       # In MB
    'ARM_Mate':            '939',       # In MB
    'ARM_SoaS':            '553',       # In MB
    # ARM prerelease
    'pre_ARM_Workstation': '1.1',       # In GB
    'pre_ARM_Minimal':     '293',       # In MB
    'pre_ARM_KDE':         '1.0',       # In GB
    'pre_ARM_Xfce':        '784',       # In MB
    'pre_ARM_LXDE':        '727',       # In MB
    'pre_ARM_Mate':        '1.0',       # In GB
    'pre_ARM_SoaS':        '522',       # In MB
    # Cloud
    'raw_x86_64_cloud':    '100',       # In MB
    'raw_i386_cloud':      '105',       # In MB
    'qcow2_x86_64_cloud':  '151',       # In MB
    'qcow2_i386_cloud':    '166',       # In MB
    'atomic_raw_cloud':    '232',       # In MB
    'atomic_qcow2_cloud':  '342',       # In MB
    'x86_64_docker':       '90',        # In MB
    'x86_64_cloud_net':    '400',       # In MB
    'i386_cloud_net':      '460',       # In MB
    # Cloud prerelease
    'pre_raw_x86_64_cloud':    '151',   # In MB
    'pre_raw_i386_cloud':      '139',   # In MB
    'pre_qcow2_x86_64_cloud':  '220',   # In MB
    'pre_qcow2_i386_cloud':    '208',   # In MB
    'pre_atomic_raw_cloud':    '333',   # In MB
    'pre_atomic_qcow2_cloud':  '440',   # In MB
    'pre_atomic_VBvag_cloud':  '435',   # In MB
    'pre_atomic_libvag_cloud': '425',   # In MB
    'pre_x86_64_docker':        '89',   # In MB
    'pre_x86_64_cloud_net':    '400',   # In MB
    'pre_i386_cloud_net':      '460'    # In MB
}

# Redirect EC2 images

path_ec2_base={
    'virginia':    'https://redirect.fedoraproject.org/console.aws.amazon.com/ec2/v2/home?region=us-east-1#LaunchInstanceWizard:ami=ami-acd999c4',
    'oregon':      'https://redirect.fedoraproject.org/console.aws.amazon.com/ec2/v2/home?region=us-west-2#LaunchInstanceWizard:ami=ami-15326925',
    'california':  'https://redirect.fedoraproject.org/console.aws.amazon.com/ec2/v2/home?region=us-west-1#LaunchInstanceWizard:ami=ami-dce3fb99',
    'ireland':     'https://redirect.fedoraproject.org/console.aws.amazon.com/ec2/v2/home?region=eu-west-1#LaunchInstanceWizard:ami=ami-b7c846c0',
    'frankfurt':   'https://redirect.fedoraproject.org/console.aws.amazon.com/ec2/v2/home?region=eu-central-1#LaunchInstanceWizard:ami=ami-5cd9ea41',
    'singapore':   'https://redirect.fedoraproject.org/console.aws.amazon.com/ec2/v2/home?region=ap-southeast-1#LaunchInstanceWizard:ami=ami-06edc754',
    'tokyo':       'https://redirect.fedoraproject.org/console.aws.amazon.com/ec2/v2/home?region=ap-northeast-1#LaunchInstanceWizard:ami=ami-20d6cd21',
    'sydney':      'https://redirect.fedoraproject.org/console.aws.amazon.com/ec2/v2/home?region=ap-southeast-2#LaunchInstanceWizard:ami=ami-ddf480e7',
    'saopaolo':    'https://redirect.fedoraproject.org/console.aws.amazon.com/ec2/v2/home?region=sa-east-1#LaunchInstanceWizard:ami=ami-650cb078'
}

path_ec2_PV={
    'virginia':    'https://redirect.fedoraproject.org/console.aws.amazon.com/ec2/v2/home?region=us-east-1#LaunchInstanceWizard:ami=ami-d2d999ba',
    'oregon':      'https://redirect.fedoraproject.org/console.aws.amazon.com/ec2/v2/home?region=us-west-2#LaunchInstanceWizard:ami=ami-13326923',
    'california':  'https://redirect.fedoraproject.org/console.aws.amazon.com/ec2/v2/home?region=us-west-1#LaunchInstanceWizard:ami=ami-d0e3fb95',
    'ireland':     'https://redirect.fedoraproject.org/console.aws.amazon.com/ec2/v2/home?region=eu-west-1#LaunchInstanceWizard:ami=ami-cdc846ba',
    'frankfurt':   'https://redirect.fedoraproject.org/console.aws.amazon.com/ec2/v2/home?region=eu-central-1#LaunchInstanceWizard:ami=ami-5ed9ea43',
    'singapore':   'https://redirect.fedoraproject.org/console.aws.amazon.com/ec2/v2/home?region=ap-southeast-1#LaunchInstanceWizard:ami=ami-02edc750',
    'tokyo':       'https://redirect.fedoraproject.org/console.aws.amazon.com/ec2/v2/home?region=ap-northeast-1#LaunchInstanceWizard:ami=ami-22d6cd23',
    'sydney':      'https://redirect.fedoraproject.org/console.aws.amazon.com/ec2/v2/home?region=ap-southeast-2#LaunchInstanceWizard:ami=ami-e5f480df',
    'saopaolo':    'https://redirect.fedoraproject.org/console.aws.amazon.com/ec2/v2/home?region=sa-east-1#LaunchInstanceWizard:ami=ami-690cb074'
}

path_ec2_atomic={
    'virginia':    'https://redirect.fedoraproject.org/console.aws.amazon.com/ec2/v2/home?region=us-east-1#LaunchInstanceWizard:ami=ami-78bafa10',
    'oregon':      'https://redirect.fedoraproject.org/console.aws.amazon.com/ec2/v2/home?region=us-west-2#LaunchInstanceWizard:ami=ami-fd075ccd',
    'california':  'https://redirect.fedoraproject.org/console.aws.amazon.com/ec2/v2/home?region=us-west-1#LaunchInstanceWizard:ami=ami-7cedf539',
    'ireland':     'https://redirect.fedoraproject.org/console.aws.amazon.com/ec2/v2/home?region=eu-west-1#LaunchInstanceWizard:ami=ami-dd3fb0aa',
    'frankfurt':   'https://redirect.fedoraproject.org/console.aws.amazon.com/ec2/v2/home?region=eu-central-1#LaunchInstanceWizard:ami=ami-7adae967',
    'singapore':   'https://redirect.fedoraproject.org/console.aws.amazon.com/ec2/v2/home?region=ap-southeast-1#LaunchInstanceWizard:ami=ami-02e9c350',
    'tokyo':       'https://redirect.fedoraproject.org/console.aws.amazon.com/ec2/v2/home?region=ap-northeast-1#LaunchInstanceWizard:ami=ami-34243f35',
    'sydney':      'https://redirect.fedoraproject.org/console.aws.amazon.com/ec2/v2/home?region=ap-southeast-2#LaunchInstanceWizard:ami=ami-6388fc59',
    'saopaolo':    'https://redirect.fedoraproject.org/console.aws.amazon.com/ec2/v2/home?region=sa-east-1#LaunchInstanceWizard:ami=ami-d516aac8'
}

# Redirect EC2 prerelease images

path_pre_ec2_base={
    'virginia':    'https://redirect.fedoraproject.org/console.aws.amazon.com/ec2/v2/home?region=us-east-1#LaunchInstanceWizard:ami=ami-268fd54e',
    'oregon':      'https://redirect.fedoraproject.org/console.aws.amazon.com/ec2/v2/home?region=us-west-2#LaunchInstanceWizard:ami=ami-bfddfe8f',
    'california':  'https://redirect.fedoraproject.org/console.aws.amazon.com/ec2/v2/home?region=us-west-1#LaunchInstanceWizard:ami=ami-b9a047fd',
    'ireland':     'https://redirect.fedoraproject.org/console.aws.amazon.com/ec2/v2/home?region=eu-west-1#LaunchInstanceWizard:ami=ami-1170e366',
    'frankfurt':   'https://redirect.fedoraproject.org/console.aws.amazon.com/ec2/v2/home?region=eu-central-1#LaunchInstanceWizard:ami=ami-9a96a487',
    'singapore':   'https://redirect.fedoraproject.org/console.aws.amazon.com/ec2/v2/home?region=ap-southeast-1#LaunchInstanceWizard:ami=ami-ec3c0abe',
    'tokyo':       'https://redirect.fedoraproject.org/console.aws.amazon.com/ec2/v2/home?region=ap-northeast-1#LaunchInstanceWizard:ami=ami-ab648dab',
    'sydney':      'https://redirect.fedoraproject.org/console.aws.amazon.com/ec2/v2/home?region=ap-southeast-2#LaunchInstanceWizard:ami=ami-8d91e0b7',
    'saopaolo':    'https://redirect.fedoraproject.org/console.aws.amazon.com/ec2/v2/home?region=sa-east-1#LaunchInstanceWizard:ami=ami-f93089e4'
}

path_pre_ec2_atomic={
    'virginia':    'https://redirect.fedoraproject.org/console.aws.amazon.com/ec2/v2/home?region=us-east-1#LaunchInstanceWizard:ami=ami-f48fd59c',
    'oregon':      'https://redirect.fedoraproject.org/console.aws.amazon.com/ec2/v2/home?region=us-west-2#LaunchInstanceWizard:ami=ami-83ddfeb3',
    'california':  'https://redirect.fedoraproject.org/console.aws.amazon.com/ec2/v2/home?region=us-west-1#LaunchInstanceWizard:ami=ami-79af483d',
    'ireland':     'https://redirect.fedoraproject.org/console.aws.amazon.com/ec2/v2/home?region=eu-west-1#LaunchInstanceWizard:ami=ami-f970e38e',
    'frankfurt':   'https://redirect.fedoraproject.org/console.aws.amazon.com/ec2/v2/home?region=eu-central-1#LaunchInstanceWizard:ami=ami-9296a48f',
    'singapore':   'https://redirect.fedoraproject.org/console.aws.amazon.com/ec2/v2/home?region=ap-southeast-1#LaunchInstanceWizard:ami=ami-b23c0ae0',
    'tokyo':       'https://redirect.fedoraproject.org/console.aws.amazon.com/ec2/v2/home?region=ap-northeast-1#LaunchInstanceWizard:ami=ami-bd648dbd',
    'sydney':      'https://redirect.fedoraproject.org/console.aws.amazon.com/ec2/v2/home?region=ap-southeast-2#LaunchInstanceWizard:ami=ami-8591e0bf',
    'saopaolo':    'https://redirect.fedoraproject.org/console.aws.amazon.com/ec2/v2/home?region=sa-east-1#LaunchInstanceWizard:ami=ami-eb3089f6'
}

path_pre_ec2_PV={
    'virginia':    'https://redirect.fedoraproject.org/console.aws.amazon.com/ec2/v2/home?region=us-east-1#LaunchInstanceWizard:ami=ami-488fd520',
    'oregon':      'https://redirect.fedoraproject.org/console.aws.amazon.com/ec2/v2/home?region=us-west-2#LaunchInstanceWizard:ami=ami-b5ddfe85',
    'california':  'https://redirect.fedoraproject.org/console.aws.amazon.com/ec2/v2/home?region=us-west-1#LaunchInstanceWizard:ami=ami-81a047c5',
    'ireland':     'https://redirect.fedoraproject.org/console.aws.amazon.com/ec2/v2/home?region=eu-west-1#LaunchInstanceWizard:ami=ami-2770e350',
    'frankfurt':   'https://redirect.fedoraproject.org/console.aws.amazon.com/ec2/v2/home?region=eu-central-1#LaunchInstanceWizard:ami=ami-9096a48d',
    'singapore':   'https://redirect.fedoraproject.org/console.aws.amazon.com/ec2/v2/home?region=ap-southeast-1#LaunchInstanceWizard:ami=ami-ea3c0ab8',
    'tokyo':       'https://redirect.fedoraproject.org/console.aws.amazon.com/ec2/v2/home?region=ap-northeast-1#LaunchInstanceWizard:ami=ami-a9648da9',
    'sydney':      'https://redirect.fedoraproject.org/console.aws.amazon.com/ec2/v2/home?region=ap-southeast-2#LaunchInstanceWizard:ami=ami-8991e0b3',
    'saopaolo':    'https://redirect.fedoraproject.org/console.aws.amazon.com/ec2/v2/home?region=sa-east-1#LaunchInstanceWizard:ami=ami-fd3089e0'
}
