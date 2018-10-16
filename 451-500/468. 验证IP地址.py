class Solution:
    def validIPAddress(self, IP):
        IP=IP.lower()
        dic = "0123456789abcdef"
        ipv4=IP.split('.')
        if len(ipv4)==4:
            for ip in ipv4:
                if not ip.isdigit():
                    return "Neither"
                t=int(ip)
                if  t<0 or t>=256:
                    return "Neither"
                elif t==0 and len(ip)>1:
                    return "Neither"
                elif ip[0]=='0'and t!=0:
                    return "Neither"
            return "IPv4"
        else:
            ipv6=IP.split(":")
            if len(ipv6)>8:
                return "Neither"
            for ip in ipv6:
                if len(ip)==0 or len(ip)>4:
                    return "Neither"
                for i in ip:
                    if dic.find(i)<0:
                        return "Neither"
            return "IPv6"
s=Solution()
test=[
{"input": "0.0.0.01", "output":"IPv4"},
{"input": "192.0.0.1", "output":"IPv4"},
{"input": "20EE:FGb8:85a3:0:0:8A2E:0370:7334", "output":"Neither"},
{"input": "256.256.256.256", "output":"Neither"},
{"input": "A.a.aA.2", "output":"Neither"},
]

for t in test:
    r=s.validIPAddress(t['input'])
    if r!=t['output']:
        print("error:"+str(t)+" out:"+str(r))