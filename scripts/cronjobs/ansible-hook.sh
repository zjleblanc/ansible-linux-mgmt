#!/bin/sh

ipv4=$(ifconfig eth0 | grep 192 | awk '{$1=$1};1' | cut -d ' ' -f 2)
echo $ipv4 > ~/ip.txt

echo '{"name": "'$ipv4'", "inventory": 7, "description": "provisioned via ansible", "variables": "---\nansible_host: '$ipv4'\nansible_user: cloud_user\n"}' > host.json

if test -f "/.aap"; then
        token=$(cat /.aap)
	curl -v -X POST -H "Content-Type: application/json" -H "Authorization: Bearer $token" -d @host.json https://controller.autodotes.com/api/v2/hosts/

	rm -f /.aap
fi