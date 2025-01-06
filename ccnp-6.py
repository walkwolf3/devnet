import re

#pattern = r'\*?Dec 1[5-9]|21\s0?[9-12].*down.*'

#pattern = r'\*?Dec [1\[5-9\],21].*[0-1][1-9].*down*'

pattern = r'\*?Dec [1\[5-9\],21].*down.*'


string='''
*Dec 10 09:13:41.770: %LINEPROTO-5-UPDOWN: Line protocol on Interface VoIP-Null0, changed state to up
*Dec 10 09:13:41.770: %LINK-3-UPDOWN: Interface Ethernet0/0, changed state to up
*Dec 10 09:13:41.771: %LINK-3-UPDOWN: Interface Ethernet0/1, changed state to up
*Dec 10 09:13:41.771: %LINK-3-UPDOWN: Interface Ethernet0/2, changed state to up
*Dec 10 09:13:41.771: %LINK-3-UPDOWN: Interface Ethernet0/3, changed state to up
*Dec 10 09:13:42.778: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet0/0, changed state to up
*Dec 10 09:13:42.778: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet0/1, changed state to up
*Dec 10 09:13:42.778: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet0/2, changed state to up
Dec 10 09:13:42.779: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet0/3, changed state to up
*Dec 15 08:12:30.038: %LINK-5-CHANGED: Interface Ethernet0/0, changed state to administratively down
*Dec 15 09:14:30.038: %LINK-5-CHANGED: Interface Ethernet0/1, changed state to administratively down
Dec 15 09:14:30.038: %LINK-5-CHANGED: Interface Ethernet0/2, changed state to administratively down
*Dec 15 09:14:30.038: %LINK-5-CHANGED: Interface Ethernet0/3, changed state to administratively down
*Dec 16 09:14:31.041: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet0/0, changed state to down
Dec 16 08:00:31.041: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet0/1, changed state to down
*Dec 16 10:14:31.041: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet0/2, changed state to down
*Dec 16 09:14:31.041: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet0/3, changed state to down
*Dec 18 09:14:38.010: %CRYPTO-6-ISAKMP_ON_OFF: ISAKMP is OFF
Dec 18 09:14:38.010: %CRYPTO-6-GDOI_ON_OFF: GDOI is OFF
*Dec 18 09:14:46.915: %PNP-6-PNP_DISCOVERY_STOPPED: PnP Discovery stopped (Config Wizard)
Dec 19 09:15:12.188: %LINK-3-UPDOWN: Interface Ethernet0/0, changed state to up
*Dec 19 09:15:13.196: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet0/0, changed state to up
Dec 19 09:15:20.855: %LINK-3-UPDOWN: Interface Ethernet0/3, changed state to up
*Dec 19 09:15:21.855: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet0/3, changed state to up
*Dec 19 09:15:43.779: %LINEPROTO-5-UPDOWN: Line protocol on Interface Loopback0, changed state to up
Dec 19 09:16:13.515: %SYS-5-CONFIG_I: Configured from console by console
*Dec 20 09:15:13.196: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet0/0, changed state to down
*Dec 20 10:15:13.196: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet0/3, changed state to down
Dec 20 11:15:13.196: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet0/0, changed state to down
*Dec 21 08:15:13.196: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet0/0, changed state to up
*Dec 21 09:15:13.196: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet0/0, changed state to down
'''

result = re.findall(pattern=pattern,string=string)
for i in result:
    print(i)


#print(result)

#UPDOWN, down