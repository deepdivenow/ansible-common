#!/usr/bin/python
class FilterModule(object):
    def filters(self):
        return {
            'ipv4_is_local': self.ipv4_is_local
        }

    def IP2Int(self,ip):
        lst = [int(item) for item in ip.split('.')]
        int_ip = lst[3] | lst[2] << 8 | lst[1] << 16 | lst[0] << 24
        return int_ip

    def ipv4_is_local(self,ipv4):

        ipv4_binary=self.IP2Int(ipv4)
        ipv_192_mask=self.IP2Int("255.255.0.0")
        ipv_172_mask=self.IP2Int('255.240.0.0')
        ipv_10_mask=self.IP2Int('255.0.0.0')

        if ipv4_binary & ipv_192_mask == self.IP2Int('192.168.0.0'):
            return True
        if ipv4_binary & ipv_172_mask == self.IP2Int('172.16.0.0'):
            return True
        if ipv4_binary & ipv_10_mask == self.IP2Int('10.0.0.0'):
            return True
        if ipv4_binary & ipv_10_mask == self.IP2Int('127.0.0.0'):
            return True
        return False

