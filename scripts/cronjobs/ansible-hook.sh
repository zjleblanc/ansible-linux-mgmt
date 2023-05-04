#!/bin/sh

ipv4=$(ifconfig eth0 | grep 192 | awk '{$1=$1};1' | cut -d ' ' -f 2)
mac=$(ifconfig | grep ether | awk '{$1=$1};1' | cut -d ' ' -f 2)
mac_short=$(echo $mac | sed '/s/://g')

echo '{"name": "rhel-guest-'$mac_short'", "inventory": 7, "description": "provisioned via ansible", "variables": "---\nansible_host: '$ipv4'\nansible_user: cloud_user\nguest_mac_address: '$mac'\n"}' > host.json

if test -f "/.aap"; then
    token=$(cat /.aap)
	curl -v -X POST -H "Content-Type: application/json" -H "Authorization: Bearer $token" -d @host.json https://controller.autodotes.com/api/v2/hosts/
	rm -f /.aap
fi