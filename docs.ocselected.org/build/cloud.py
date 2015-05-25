#!/bin/python
# This file is used to generate the "out/static/js/cloud_ec2.js" file used the get-fedora-options#cloud tab
# You should only edit
# - the bellow dictionnary containing the AMI ID (get them on the wiki)
# - the python list ec2_fXX_regions
# - the template call at the end of file near "noscript" and "if JS enabled" (data/template/)

import os

OUTPUT = 'out/static/js/cloud_ec2.js'

# Returns a sorted list of unique available regions from the array
def sorted_region(arr):
	list = []
	for i in arr:
		list.append(i['region'])
	return(sorted(set(list), key=lambda  item: (int(item.partition(' ')[0]) if item[0].isdigit() else float('inf'), item)))

# Generated using the following:
# :%s#^\(ami-[0-9a-z]*\) : \([a-zA-Z0-9-]*\) image for \([xi].*\)#{'region':'\2', 'arch':'\3', 'store':'\EBS-Backed', 'id': '\1'},#g
# :%s/us-east-1/US East (Northern Virginia)/g
# :%s/us-west-1/US West (Northern California)/g
# :%s/us-west-2/US West (Oregon)/g
# :%s/eu-west-1/EU (Ireland)/g
# :%s/ap-southeast-1/Asia Pacific (Singapore)/g
# :%s/ap-southeast-2/Asia Pacific (Sydney)/g
# :%s/ap-northeast-1/Asia Pacific (Tokyo)/g
# :%s/sa-east-1/South America (Sao Paulo)/g

# Get the list at: https://dl.fedoraproject.org/pub/alt/stage/20-Beta-RC2/Images/x86_64/
ec2_f21_Alpha_Base = [
                        {'region':'US East (Northern Virginia)', 'arch':'x86_64', 'store':'EBS-Backed', 'id':'ami-20268848'},
#                        {'region':'US East (Northern Virginia)', 'arch':'i386', 'store':'EBS-Backed', 'id':'ami-8b4219e2'},
                        {'region':'Asia Pacific (Singapore)', 'arch':'x86_64', 'store':'EBS-Backed', 'id':'ami-820f2bd0'},
#                        {'region':'Asia Pacific (Singapore)', 'arch':'i386', 'store':'EBS-Backed', 'id':'ami-0eb2e75c'},
                        {'region':'Asia Pacific (Sydney)', 'arch':'x86_64', 'store':'EBS-Backed', 'id':'ami-7b6c0f41'},
#                        {'region':'Asia Pacific (Sydney)', 'arch':'i386', 'store':'EBS-Backed', 'id':'ami-db63ffe1'},
                        {'region':'Asia Pacific (Tokyo)', 'arch':'x86_64', 'store':'EBS-Backed', 'id':'ami-cf644bce'},
#                        {'region':'Asia Pacific (Tokyo)', 'arch':'i386', 'store':'EBS-Backed', 'id':'ami-e15135e0'},
                        {'region':'US West (Northern California)', 'arch':'x86_64', 'store':'EBS-Backed', 'id':'ami-b58b82f0'},
#                        {'region':'US West (Northern California)', 'arch':'i386', 'store':'EBS-Backed', 'id':'ami-00d0e645'},
                        {'region':'US West (Oregon)', 'arch':'x86_64', 'store':'EBS-Backed', 'id':'ami-af57179f'},
#                        {'region':'US West (Oregon)', 'arch':'i386', 'store':'EBS-Backed', 'id':'ami-48ca5178'},
                        {'region':'EU (Ireland)', 'arch':'x86_64', 'store':'EBS-Backed', 'id':'ami-bac760cd'},
#                        {'region':'EU (Ireland)', 'arch':'i386', 'store':'EBS-Backed', 'id':'ami-897b99fe'},
                        {'region':'South America (Sao Paulo)', 'arch':'x86_64', 'store':'EBS-Backed', 'id':'ami-ab9f35b6'}
#                        {'region':'South America (Sao Paulo)', 'arch':'i386', 'store':'EBS-Backed', 'id':'ami-4b5cfa56'}
]

ec2_f21_Alpha_Atomic = [
                        {'region':'Asia Pacific (Tokyo)', 'arch':'x86_64', 'store':'BS-Backed', 'id':'ami-ebfe80ea'},
                        {'region':'Asia Pacific (Singapore)', 'arch':'x86_64', 'store':'BS-Backed', 'id':'ami-deeebe8c'},
                        {'region':'Asia Pacific (Sydney)', 'arch':'x86_64', 'store':'BS-Backed', 'id':'ami-27a1391d'},
                        {'region':'EU (Ireland)', 'arch':'x86_64', 'store':'BS-Backed', 'id':'ami-29a2595e'},
                        {'region':'South America (Sao Paulo)', 'arch':'x86_64', 'store':'BS-Backed', 'id':'ami-8145e79c'},
                        {'region':'US East (Northern Virginia)', 'arch':'x86_64', 'store':'BS-Backed', 'id':'ami-f525389c'},
                        {'region':'US West (Northern California)', 'arch':'x86_64', 'store':'BS-Backed', 'id':'ami-46f3ca03'},
                        {'region':'US West (Oregon)', 'arch':'x86_64', 'store':'BS-Backed', 'id':'ami-9682e9a6'}
]

ec2_f21_Base = [
                        {'region':'Asia Pacific (Tokyo)', 'arch':'x86_64', 'store':'BS-Backed', 'id':'ami-9583fd94'},
                        {'region':'Asia Pacific (Singapore)', 'arch':'x86_64', 'store':'BS-Backed', 'id':'ami-6ceebe3e'},
                        {'region':'Asia Pacific (Sydney)', 'arch':'x86_64', 'store':'BS-Backed', 'id':'ami-eba038d1'},
                        {'region':'EU (Ireland)', 'arch':'x86_64', 'store':'BS-Backed', 'id':'ami-a5ad56d2'},
                        {'region':'South America (Sao Paulo)', 'arch':'x86_64', 'store':'BS-Backed', 'id':'ami-2345e73e'},
                        {'region':'US East (Northern Virginia)', 'arch':'x86_64', 'store':'BS-Backed', 'id':'ami-21362b48'},
                        {'region':'US West (Northern California)', 'arch':'x86_64', 'store':'BS-Backed', 'id':'ami-f8f1c8bd'},
                        {'region':'US West (Oregon)', 'arch':'x86_64', 'store':'BS-Backed', 'id':'ami-cc8de6fc'},
                        {'region':'Asia Pacific (Tokyo)', 'arch':'i386', 'store':'BS-Backed', 'id':'ami-db83fdda'},
                        {'region':'Asia Pacific (Singapore)', 'arch':'i386', 'store':'BS-Backed', 'id':'ami-30eebe62'},
                        {'region':'Asia Pacific (Sydney)', 'arch':'i386', 'store':'BS-Backed', 'id':'ami-d9a038e3'},
                        {'region':'EU (Ireland)', 'arch':'i386', 'store':'BS-Backed', 'id':'ami-0bac577c'},
                        {'region':'South America (Sao Paulo)', 'arch':'i386', 'store':'BS-Backed', 'id':'ami-4b45e756'},
                        {'region':'US East (Northern Virginia)', 'arch':'i386', 'store':'BS-Backed', 'id':'ami-81302de8'},
                        {'region':'US West (Northern California)', 'arch':'i386', 'store':'BS-Backed', 'id':'ami-a0f1c8e5'},
                        {'region':'US West (Oregon)', 'arch':'i386', 'store':'BS-Backed', 'id':'ami-768ce746'}
]

ec2_f21_Atomic = [
                        {'region':'Asia Pacific (Tokyo)', 'arch':'i386', 'store':'BS-Backed', 'id':'ami-5bff815a'},
                        {'region':'Asia Pacific (Singapore)', 'arch':'i386', 'store':'BS-Backed', 'id':'ami-e2eebeb0'},
                        {'region':'Asia Pacific (Sydney)', 'arch':'i386', 'store':'BS-Backed', 'id':'ami-7fa13945'},
                        {'region':'EU (Ireland)', 'arch':'i386', 'store':'BS-Backed', 'id':'ami-e7a25990'},
                        {'region':'South America (Sao Paulo)', 'arch':'i386', 'store':'BS-Backed', 'id':'ami-ad45e7b0'},
                        {'region':'US East (Northern Virginia)', 'arch':'i386', 'store':'BS-Backed', 'id':'ami-812439e8'},
                        {'region':'US West (Northern California)', 'arch':'i386', 'store':'BS-Backed', 'id':'ami-1cf3ca59'},
                        {'region':'US West (Oregon)', 'arch':'i386', 'store':'BS-Backed', 'id':'ami-e882e9d8'},
                        {'region':'Asia Pacific (Tokyo)', 'arch':'x86_64', 'store':'BS-Backed', 'id':'ami-ebfe80ea'},
                        {'region':'Asia Pacific (Singapore)', 'arch':'x86_64', 'store':'BS-Backed', 'id':'ami-deeebe8c'},
                        {'region':'Asia Pacific (Sydney)', 'arch':'x86_64', 'store':'BS-Backed', 'id':'ami-27a1391d'},
                        {'region':'EU (Ireland)', 'arch':'x86_64', 'store':'BS-Backed', 'id':'ami-29a2595e'},
                        {'region':'South America (Sao Paulo)', 'arch':'x86_64', 'store':'BS-Backed', 'id':'ami-8145e79c'},
                        {'region':'US East (Northern Virginia)', 'arch':'x86_64', 'store':'BS-Backed', 'id':'ami-f525389c'},
                        {'region':'US West (Northern California)', 'arch':'x86_64', 'store':'BS-Backed', 'id':'ami-46f3ca03'},
                        {'region':'US West (Oregon)', 'arch':'x86_64', 'store':'BS-Backed', 'id':'ami-9682e9a6'}
]

# The idea is to get something similar to http://jsfiddle.net/shaiton/wChSv/5/
# But we have to generate it in order to have to maintain only one list of AMI ID
# Simply read the output at "out/static/js/cloud_ec2.js"
def gen_js(*args):
	js="// File generated from cloud-tab.html.\n"
	js+="addEventListener('DOMContentLoaded', function(){\n"

	for release in args:
		js+="\tvar element = document.getElementById('cloud_options_" + release[0] + "');\n"
		js+="\tif (element != null)\n"
		js+="\t\telement.style.visibility='visible';\n"
		js+="\telement = document.getElementById('amihref_" + release[0] + "');\n"
		js+="\tif (element != null)\n"
		js+="\t\telement.style.visibility='hidden';\n"
	js+="});\n"

	js+="\nfunction getval() {\n"
	js+="\t// We get the number of regions, and define a two dimensional array (region,arch) to store the AMI ID\n"
	js+="\t// We limit to i > 1 as we don't need the first null entry'\n"
	js+="\t// For each release providen. '\n"
	js+="\tvar region_name = {\n"
 	js+="\t  'Asia Pacific (Tokyo)': 'ap-northeast-1',\n"
	js+="\t  'Asia Pacific (Singapore)': 'ap-southeast-1',\n"
	js+="\t  'Asia Pacific (Sydney)': 'ap-southeast-2',\n"
	js+="\t  'EU (Ireland)': 'eu-west-1',\n"
	js+="\t  'South America (Sao Paulo)': 'sa-east-1',\n"
	js+="\t  'US East (Northern Virginia)': 'us-east-1',\n"
	js+="\t  'US West (Northern California)': 'us-west-1',\n"
	js+="\t  'US West (Oregon)': 'us-west-2'\n"
	js+="\t}\n"
	for release in args:
		js+="\n\tvar form_" + release[0] + " = document.forms['cloud_options_" + release[0] + "'];\n"
		js+="\n\tvar is_form_" + release[0] + " = typeof form_" + release[0] + ";\n"
		js+="\tif (is_form_" + release[0] + " != 'undefined' && form_" + release[0] + ".region_" + release[0] + ".value != 'null') {\n"
		js+="\t\tfor (var i = form_" + release[0] + ".region_" + release[0] + ".options.length, id_" + release[0] + " = new Array(form_" + release[0] + ".region_" + release[0] + ".options.length); i > 1; i--)\n"
		js+="\t\t\tid_" + release[0] + "[form_" + release[0] + ".region_" + release[0] + ".options[i - 1].value] = new Array(2);\n\n"

		for img in release[1]:
			js+="\t\tid_" + release[0] + "['" + img['region'] + "']['" + img['arch'] + "'] = '" + img['id'] + "';\n"
		js+="\t}\n"
	for release in args:
		js+="\n\tif (is_form_" + release[0] + " != 'undefined') {\n"
		js+="\n\t\tif (form_" + release[0] + ".region_" + release[0] + ".value != 'null') {\n"
		js+="\t\t\tvar ami_id = id_" + release[0] + "[form_" + release[0] + ".region_" + release[0] + ".value][form_" + release[0] + ".arch_" + release[0] + ".value];\n"
		js+="\t\t\tvar url = 'https://console.aws.amazon.com/ec2/v2/home?region=' + region_name[form_" + release[0] + ".region_" + release[0] + ".value] + '#LaunchInstanceWizard:ami=' + ami_id;\n"
		js+="\t\t\tdocument.getElementById('amihref_" + release[0] + "').href = url;\n"
		js+="\t\t\tdocument.getElementById('amihref_" + release[0] + "').style.visibility='visible';\n"
		js+="\t\t\tdocument.getElementById('label_" + release[0] + "').innerHTML = ami_id;\n"
		js+="\t\t} else {\n"
		js+="\t\t\tdocument.getElementById('amihref_" + release[0] + "').href = '';\n"
		js+="\t\t\tdocument.getElementById('amihref_" + release[0] + "').style.visibility='hidden';\n"
		js+="\t\t\tdocument.getElementById('label_" + release[0] + "').innerHTML = '';\n"
		js+="\t\t}\n"
		js+="\t}\n"
	js+="}\n"
	f = open(OUTPUT, 'w+')
	f.write(js)
	f.close()

def get_amis():
    ec2_f21_Alpha_Base_regions = sorted_region(ec2_f21_Alpha_Base)
    ec2_f21_Alpha_Atomic_regions = sorted_region(ec2_f21_Alpha_Atomic)
    ec2_f21_Base_regions = sorted_region(ec2_f21_Base)
    ec2_f21_Atomic_regions = sorted_region(ec2_f21_Atomic)

    if not os.path.exists(OUTPUT):
        gen_js(
        	['21_Base',ec2_f21_Base],
            ['21_Atomic',ec2_f21_Atomic],
            ['21_Alpha_Base',ec2_f21_Alpha_Base],
            ['21_Alpha_Atomic',ec2_f21_Alpha_Atomic])

    return {
        'f21_Base':ec2_f21_Base, 'f21_Base_regions':ec2_f21_Base_regions,
        'f21_Atomic':ec2_f21_Atomic, 'f21_Atomic_regions':ec2_f21_Atomic_regions,
        'f21_Alpha_Base':ec2_f21_Alpha_Base, 'f21_Alpha_Base_regions':ec2_f21_Alpha_Base_regions,
        'f21_Alpha_Atomic':ec2_f21_Alpha_Atomic, 'f21_Alpha_Atomic_regions':ec2_f21_Alpha_Atomic_regions
           }

