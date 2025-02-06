from scapy.all import rdpcap
from scapy.layers.inet import IP, TCP, UDP
from scapy.layers.dns import DNS
from scapy.layers.http import HTTPRequest
from collections import Counter

def analyze_pcap(file_path: str, filter_ip: str = None, filter_protocol: str = None, filter_port: int = None) -> dict:
    try:
        packets = rdpcap(file_path)
    except Exception as e:
        raise ValueError(f"Ошибка при чтении файла: {e}")

    total_packets = len(packets)
    protocols = Counter()
    ip_addresses = Counter()
    http_requests = []
    dns_queries = []

    for packet in packets:
        if filter_protocol and not packet.haslayer(filter_protocol):
            continue

        if packet.haslayer(IP):
            src_ip, dst_ip = packet[IP].src, packet[IP].dst
            if filter_ip and filter_ip not in (src_ip, dst_ip):
                continue
            ip_addresses[src_ip] += 1
            ip_addresses[dst_ip] += 1

        if packet.haslayer(TCP) or packet.haslayer(UDP):
            sport = packet.sport
            dport = packet.dport
            if filter_port and filter_port not in (sport, dport):
                continue

        protocols.update([layer.__class__.__name__ for layer in packet.layers()])

        if packet.haslayer(HTTPRequest):
            http_requests.append({
                "method": packet[HTTPRequest].Method.decode(),
                "host": packet[HTTPRequest].Host.decode(),
                "path": packet[HTTPRequest].Path.decode(),
            })

        if packet.haslayer(DNS) and packet[DNS].qd:
            dns_queries.append(packet[DNS].qd.qname.decode())

    return {
        "total_packets": total_packets,
        "protocols": dict(protocols),
        "ip_addresses": dict(ip_addresses),
        "http_requests": http_requests,
        "dns_queries": dns_queries,
    }
