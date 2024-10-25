import json
import requests
requests.packages.urllib3.disable_warnings()

# Router IP Address is 10.0.15.181-184
api_url = "https://10.0.15.182/restconf"

# the RESTCONF HTTP headers, including the Accept and Content-Type
# Two YANG data formats (JSON and XML) work with RESTCONF 
headers = {
    "Accept": "application/yang-data+json",
    "Content-Type": "application/yang-data+json"
}
basicauth = ("admin", "cisco")


def create():
    yangConfig = {
        "ietf-interfaces:interface": {
            "name": "Loopback65070115",
            "description": "created loopback(RESTCONF)",
            "type": "iana-if-type:softwareLoopback",
            "enabled": True,
            "ietf-ip:ipv4": {
                "address": [
                    {
                        "ip": "172.30.115.1",
                        "netmask": "255.255.255.0"
                    }
                ]
            },
            "ietf-ip:ipv6": {}
        }
    } # Add

    # check = get()
    check = status()
    if check == True:
        return "Cannot create: Interface loopback65070115"
    else:
        resp = requests.put(
            api_url + "/data/ietf-interfaces:interfaces/interface=Loopback65070115",
            data=json.dumps(yangConfig),
            auth=basicauth, 
            headers=headers, 
            verify=False
            )

        if(resp.status_code >= 200 and resp.status_code <= 299):
            print("STATUS OK: {}".format(resp.status_code))
            return "Interface Loopback65070115 created."
        else:
            print('Error. Status Code: {}'.format(resp.status_code))
            return "Cannot create: Interface loopback65070115" # Add


def delete():
    resp = requests.delete(
        api_url + "/data/ietf-interfaces:interfaces/interface=Loopback65070115", # Add
        auth=basicauth, 
        headers=headers, # Add
        verify=False
        )

    if(resp.status_code >= 200 and resp.status_code <= 299):
        print("STATUS OK: {}".format(resp.status_code))
        return "Interface loopback65070115 is deleted successfully"
    else:
        print('Error. Status Code: {}'.format(resp.status_code))
        return "Cannot delete: Interface loopback65070115" # Add


def enable():
    yangConfig = {
        "ietf-interfaces:interface": {
            "name": "Loopback65070115",
            "type": "iana-if-type:softwareLoopback",
            "enabled": True,
        } # Add
    }

    resp = requests.patch(
        api_url + "/data/ietf-interfaces:interfaces/interface=Loopback65070115", # Add
        data=json.dumps(yangConfig), # Add
        auth=basicauth, 
        headers=headers, # Add
        verify=False
        )

    if(resp.status_code >= 200 and resp.status_code <= 299):
        print("STATUS OK: {}".format(resp.status_code))
        return "Interface loopback65070115 is enabled successfully" # Add
    else:
        print('Error. Status Code: {}'.format(resp.status_code))
        return "Cannot enable: Interface loopback65070115" # Add
        

def disable():
    yangConfig = yangConfig = {
        "ietf-interfaces:interface": {
            "name": "Loopback65070115",
            "type": "iana-if-type:softwareLoopback",
            "enabled": False,
        } # Add
    }

    resp = requests.patch(
        api_url + "/data/ietf-interfaces:interfaces/interface=Loopback65070115", # Add
        data=json.dumps(yangConfig), # Add
        auth=basicauth, 
        headers=headers, # Add
        verify=False
        )

    if(resp.status_code >= 200 and resp.status_code <= 299):
        print("STATUS OK: {}".format(resp.status_code))
        return "Interface loopback65070115 is shutdowned successfully" # Add
    else:
        print('Error. Status Code: {}'.format(resp.status_code))
        return "Cannot shutdown: Interface loopback65070115" # Add


def status():
    resp = requests.get(
            api_url + "/data/ietf-interfaces:interfaces-state/interface=Loopback65070115",
            auth=basicauth, 
            headers=headers, # Add
            verify=False
        )
    
    if(resp.status_code >= 200 and resp.status_code <= 299):
        print("STATUS OK: {}".format(resp.status_code))
        response_json = resp.json()
        print(json.dumps(response_json, indent=4))
        interface_name = response_json["ietf-interfaces:interface"]["name"]
        admin_status = response_json["ietf-interfaces:interface"]["admin-status"]
        oper_status = response_json["ietf-interfaces:interface"]["oper-status"]
        if(admin_status == 'up' and oper_status == 'up' and interface_name == 'Loopback65070115'):
            return "Interface loopback65070115 is enabled"
        elif(admin_status == 'down' and oper_status == 'down' and interface_name == 'Loopback65070115'):
            return "Interface loopback65070115 is disabled"
        elif(interface_name != 'Loopback65070115'):
            return "No Interface loopback65070115"
        
    else:
        return "No Interface loopback 65070115"
