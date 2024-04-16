import os
import re

class Ping:
    def execute(self, ip_address: str) -> None:
        if not self.validate_ip(ip_address):
            print("La dirección IP no es válida.")
            return
        
        print(f"Haciendo ping a la dirección IP: {ip_address}")
        for _ in range(10):
            response = os.system(f"ping -c 1 {ip_address} > /dev/null 2>&1")
            if response == 0:
                print("Ping exitoso")
            else:
                print("Ping fallido")

    def executefree(self, ip_address: str) -> None:
        print(f"Haciendo ping libre a la dirección IP: {ip_address}")
        self.execute(ip_address)

    def validate_ip(self, ip_address: str) -> bool:
        parts = ip_address.split('.')
        if len(parts) != 4:
            return False
        for part in parts:
            if not part.isdigit():
                return False
            num = int(part)
            if num < 0 or num > 255:
                return False
        return parts[0] == '192'


class PingProxy:
    def __init__(self):
        self.ping = Ping()

    def execute(self, ip_address: str) -> None:
        if ip_address == "192.168.0.254":
            self.ping.executefree("www.google.com")
        else:
            self.ping.execute(ip_address)

if __name__ == "__main__":
    ping_proxy = PingProxy()

    print("Intentando ping a una dirección IP válida:")
    ping_proxy.execute("192.168.0.1")

    print("\nIntentando ping a una dirección IP inválida:")
    ping_proxy.execute("256.256.256.256")

    print("\nIntentando ping libre a una dirección IP válida:")
    ping_proxy.execute("192.168.1.1")

    print("\nIntentando ping proxy a una dirección IP especial:")
    ping_proxy.execute("192.168.0.254")