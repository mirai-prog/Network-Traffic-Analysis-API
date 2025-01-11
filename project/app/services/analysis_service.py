from scapy.all import rdpcap, IP, TCP, UDP, DNS, HTTPRequest, HTTPResponse
from collections import Counter

def analyze_pcap(file_path: str) -> dict:
    try:
        packets = rdpcap(file_path)
    except Exception as e:
        raise ValueError(f"Ошибка при чтении файла: {e}")

    total_packets = len(packets)
    protocols = Counter(packet.__class__.__name__ for packet in packets)

    ip_addresses = Counter()
    http_requests = []
    dns_queries = []

    for packet in packets:
        if hasattr(packet, "src") and hasattr(packet, "dst"):
            ip_addresses[packet.src] += 1
            ip_addresses[packet.dst] += 1

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

