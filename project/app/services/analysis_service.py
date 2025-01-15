from scapy.all import rdpcap, IP, TCP, UDP, DNS, HTTPRequest
from collections import Counter
from typing import Dict, Any
import logging

# Настройка логирования
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def analyze_pcap(file_path: str) -> Dict[str, Any]:
    """
    Анализирует PCAP-файл, извлекая информацию о протоколах, IP-адресах, HTTP-запросах и DNS-запросах.

    Args:
        file_path (str): Путь к PCAP-файлу.

    Returns:
        dict: Словарь с результатами анализа, включая общее количество пакетов, протоколы,
              IP-адреса, HTTP-запросы и DNS-запросы.
    """
    logger.info(f"Начинается анализ файла: {file_path}")
    try:
        packets = rdpcap(file_path)
        logger.info(f"Успешно прочитано {len(packets)} пакетов.")
    except Exception as e:
        logger.error(f"Ошибка при чтении файла: {e}")
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
            method = packet[HTTPRequest].Method.decode() if packet[HTTPRequest].Method else "UNKNOWN"
            host = packet[HTTPRequest].Host.decode() if packet[HTTPRequest].Host else "UNKNOWN"
            path = packet[HTTPRequest].Path.decode() if packet[HTTPRequest].Path else "/"
            http_requests.append({
                "method": method,
                "host": host,
                "path": path,
            })

        if packet.haslayer(DNS) and packet[DNS].qd:
            query_name = packet[DNS].qd.qname.decode() if packet[DNS].qd.qname else "UNKNOWN"
            dns_queries.append(query_name)

    result = {
        "total_packets": total_packets,
        "protocols": dict(protocols.most_common(10)),  # Топ-10 протоколов
        "ip_addresses": dict(ip_addresses.most_common(10)),  # Топ-10 IP-адресов
        "http_requests": http_requests[:10],  # Топ-10 HTTP-запросов
        "dns_queries": dns_queries[:10],  # Топ-10 DNS-запросов
    }

    logger.info(f"Анализ завершен. Результат: {result}")
    return result

