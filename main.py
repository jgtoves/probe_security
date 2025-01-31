import argparse
from scapy.all import * 

ap_function = {
    "interface": raw_input()
     
}

parser = argparse.ArgumentParser(description="Get AP's clients.")
parser.add_argument("interface", type=str, help="This is my interface.")
parser.add_argument(
    "--request",
    action="store",
    help="Initial probe request operation.",
)
parser.add_argument(
    "--ap",
    action="store",
    help="This target Access Point.",
)

args = parser.parse_args()

interface = ap_function[args.interface]

interface = [interface]
probe_req = [request] 
ap_name = [ap]

def probesniff(fm): 
  if fm.haslayer(Dot11ProbeReq): 
    client_name = fm.info
    if client_name == ap_name :
			if fm.addr2 not in probe_req:
				print "New Probe Request: ", client_name 
				print "MAC ", fm.addr2
				probe_req.append(fm.addr2)
			
sniff(iface= interface,prn=probesniff)


    

// From here, code is totally 
// hypothetical by the way,  
// I want to as a step in detecting 
// a user has been connecting to a certain
// AP and how often, and what time. 
// A logger would be ideal, and maybe 
// an option to load in SSID to detect
// connections for real time based 
// tracking.
