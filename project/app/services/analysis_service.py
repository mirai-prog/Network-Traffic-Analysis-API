from scapy.all import rdpcap
from collections import Counter

def analyze_pcap(file_path: str) -> dict:
    """
    Анализ PCAP-файла.

    :param file_path: Путь к PCAP-файлу.
    :return: Сводная информация о пакете.
    """
    try:
        packets = rdpcap(file_path)  
    except Exception as e:
        raise ValueError(f"Ошибка при чтении файла: {e}")

    total_packets = len(packets)

    
    protocols = Counter(packet.__class__.__name__ for packet in packets)

    ip_addresses = Counter()
    for packet in packets:
        if hasattr(packet, "src") and hasattr(packet, "dst"):
            ip_addresses[packet.src] += 1
            ip_addresses[packet.dst] += 1

    return {
        "total_packets": total_packets,
        "protocols": dict(protocols),
        "ip_addresses": dict(ip_addresses),
    }

