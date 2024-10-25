from netmiko import ConnectHandler
from pprint import pprint

device_ip = "10.0.15.182"
username = "admin"
password = "cisco"

device = {
        'device_type': 'cisco_ios',
        'ip': '10.0.15.182',  
        'username': 'admin',  
        'password': 'cisco',
    }


def gigabit_status():
    ans = ""
    with ConnectHandler(**device) as ssh:
        up = 0
        down = 0
        admin_down = 0
        result = ssh.send_command("show ip interface brief", use_textfsm=True)
        for status in result:
            interface_status = status["status"]
            if interface_status:
                if interface_status == "up":
                    up += 1
                elif interface_status == "down":
                    down += 1
                elif interface_status == "administratively down":
                    admin_down += 1
        ans = f"Up: {up}, Down: {down}, Admin Down: {admin_down}"
        pprint(ans)
        return ans
