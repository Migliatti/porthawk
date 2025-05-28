#!/usr/bin/env python3
"""
TCP Port Scanner Simples
Ferramenta educacional para entender sockets e escaneamento de portas
"""

import socket
import threading
import argparse
import sys
from datetime import datetime
import ipaddress

class TCPScanner:
    def __init__(self, target, port_list, timeout=1, threads=100):
        self.target = target
        self.port_list = port_list  # Agora pode ser uma lista ou tupla (start, end)
        self.timeout = timeout
        self.threads = threads
        self.open_ports = []
        self.lock = threading.Lock()
        
        # Dicionário com serviços comuns por porta
        self.common_ports = {
            21: "FTP", 22: "SSH", 23: "Telnet", 25: "SMTP", 53: "DNS",
            80: "HTTP", 110: "POP3", 143: "IMAP", 443: "HTTPS", 993: "IMAPS",
            995: "POP3S", 1433: "MSSQL", 3306: "MySQL", 3389: "RDP", 5432: "PostgreSQL",
            6379: "Redis", 27017: "MongoDB", 8080: "HTTP-Alt", 8443: "HTTPS-Alt"
        }

    def resolve_hostname(self, hostname):
        """Resolve hostname para IP"""
        try:
            ip = socket.gethostbyname(hostname)
            print(f"[INFO] Resolvendo {hostname} -> {ip}")
            return ip
        except socket.gaierror:
            print(f"[ERRO] Não foi possível resolver o hostname: {hostname}")
            return None

    def validate_ip(self, ip):
        """Valida se o IP é válido"""
        try:
            ipaddress.ip_address(ip)
            return True
        except ValueError:
            return False

    def scan_port(self, target_ip, port):
        """Escaneia uma porta específica"""
        try:
            # Cria socket TCP
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(self.timeout)
            
            # Tenta conectar na porta
            result = sock.connect_ex((target_ip, port))
            
            if result == 0:
                # Porta está aberta
                service = self.common_ports.get(port, "Unknown")
                
                with self.lock:
                    self.open_ports.append((port, service))
                    print(f"[ABERTA] Porta {port} - {service}")
            
            sock.close()
            
        except socket.error:
            pass
        except Exception as e:
            pass

    def scan_ports(self, target_ip, ports_to_scan):
        """Escaneia uma lista de portas usando threading"""
        threads = []
        
        if isinstance(ports_to_scan, list):
            print(f"[INFO] Escaneando portas específicas: {', '.join(map(str, ports_to_scan))}")
            port_list = ports_to_scan
        else:
            # É um range (tupla)
            start_port, end_port = ports_to_scan
            print(f"[INFO] Escaneando range de portas {start_port}-{end_port}")
            port_list = list(range(start_port, end_port + 1))
        
        print(f"[INFO] Total de portas: {len(port_list)}")
        print(f"[INFO] Usando {self.threads} threads com timeout de {self.timeout}s")
        print("-" * 50)
        
        for port in port_list:
            # Controla o número de threads ativas
            while len(threads) >= self.threads:
                for t in threads[:]:
                    if not t.is_alive():
                        threads.remove(t)
            
            # Cria nova thread para escanear a porta
            thread = threading.Thread(target=self.scan_port, args=(target_ip, port))
            thread.daemon = True
            thread.start()
            threads.append(thread)
        
        # Aguarda todas as threads terminarem
        for thread in threads:
            thread.join()

    def banner_grab(self, target_ip, port):
        """Tenta capturar banner do serviço"""
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(3)
            sock.connect((target_ip, port))
            
            # Envia requisição HTTP básica para portas web
            if port in [80, 8080]:
                sock.send(b"GET / HTTP/1.1\r\nHost: " + target_ip.encode() + b"\r\n\r\n")
            
            banner = sock.recv(1024).decode('utf-8', errors='ignore').strip()
            sock.close()
            return banner[:100] if banner else None
            
        except:
            return None

    def run_scan(self):
        """Executa o scan completo"""
        print(f"""
         

 ██▓███   ▒█████   ██▀███  ▄▄▄█████▓ ██░ ██  ▄▄▄       █     █░██ ▄█▀
▓██░  ██▒▒██▒  ██▒▓██ ▒ ██▒▓  ██▒ ▓▒▓██░ ██▒▒████▄    ▓█░ █ ░█░██▄█▒ 
▓██░ ██▓▒▒██░  ██▒▓██ ░▄█ ▒▒ ▓██░ ▒░▒██▀▀██░▒██  ▀█▄  ▒█░ █ ░█▓███▄░ 
▒██▄█▓▒ ▒▒██   ██░▒██▀▀█▄  ░ ▓██▓ ░ ░▓█ ░██ ░██▄▄▄▄██ ░█░ █ ░█▓██ █▄ 
▒██▒ ░  ░░ ████▓▒░░██▓ ▒██▒  ▒██▒ ░ ░▓█▒░██▓ ▓█   ▓██▒░░██▒██▓▒██▒ █▄
▒▓▒░ ░  ░░ ▒░▒░▒░ ░ ▒▓ ░▒▓░  ▒ ░░    ▒ ░░▒░▒ ▒▒   ▓▒█░░ ▓░▒ ▒ ▒ ▒▒ ▓▒
░▒ ░       ░ ▒ ▒░   ░▒ ░ ▒░    ░     ▒ ░▒░ ░  ▒   ▒▒ ░  ▒ ░ ░ ░ ░▒ ▒░
░░       ░ ░ ░ ▒    ░░   ░   ░       ░  ░░ ░  ░   ▒     ░   ░ ░ ░░ ░ 
             ░ ░     ░               ░  ░  ░      ░  ░    ░   ░  ░   
                                                                     
              """)
        print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} ")
        print("=" * 60)
        
        # Resolve hostname se necessário
        if not self.validate_ip(self.target):
            target_ip = self.resolve_hostname(self.target)
            if not target_ip:
                return
        else:
            target_ip = self.target
        
        print(f"[ALVO] IP: {target_ip}")
        
        if isinstance(self.port_list, list):
            print(f"[PORTAS] Específicas: {', '.join(map(str, self.port_list))}")
        else:
            print(f"[RANGE] Portas: {self.port_list[0]}-{self.port_list[1]}")
        
        start_time = datetime.now()
        
        # Executa o scan
        self.scan_ports(target_ip, self.port_list)
        
        end_time = datetime.now()
        duration = end_time - start_time
        
        print("-" * 50)
        print(f"[RESUMO] Scan finalizado em {duration.total_seconds():.2f} segundos")
        
        if self.open_ports:
            print(f"[RESULTADO] {len(self.open_ports)} porta(s) aberta(s) encontrada(s):")
            print()
            
            # Ordena as portas
            self.open_ports.sort(key=lambda x: x[0])
            
            # Exibe resultados detalhados
            for port, service in self.open_ports:
                banner = self.banner_grab(target_ip, port)
                banner_info = f"Banner\n{banner}" if banner else ""
                print(f"Porta {port:5d} - {service:15s}\n{banner_info}\n")
        else:
            print("[RESULTADO] Nenhuma porta aberta encontrada no range especificado")

def main():
    parser = argparse.ArgumentParser(
        description="TCP Port Scanner - Ferramenta educacional para scan de portas",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Exemplos de uso:
  python tcp_scanner.py -t 192.168.1.1 -p 1-1000
  python tcp_scanner.py -t google.com -p 80,443,8080
  python tcp_scanner.py -t 10.0.0.1 -p 20-25 -T 2 -th 50
        """
    )
    
    parser.add_argument('-t', '--target', required=True,
                       help='IP ou hostname do alvo')
    
    parser.add_argument('-p', '--ports', required=True,
                       help='Range de portas (ex: 1-1000) ou portas específicas (ex: 80,443,8080)')
    
    parser.add_argument('-T', '--timeout', type=float, default=1,
                       help='Timeout para conexão em segundos (padrão: 1)')
    
    parser.add_argument('-th', '--threads', type=int, default=100,
                       help='Número de threads (padrão: 100)')
    
    args = parser.parse_args()
    
    # Parse do range de portas
    try:
        if '-' in args.ports:
            # Range de portas (ex: 1-1000)
            start, end = map(int, args.ports.split('-'))
            port_list = (start, end)  # Tupla para range
        elif ',' in args.ports:
            # Portas específicas (ex: 80,443,8080)
            port_list = list(map(int, args.ports.split(',')))  # Lista para portas específicas
        else:
            # Porta única
            port = int(args.ports)
            port_list = [port]  # Lista com uma porta
    except ValueError:
        print("[ERRO] Formato de porta inválido. Use: 1-1000 ou 80,443,8080")
        sys.exit(1)
    
    # Validações
    if isinstance(port_list, list):
        # Validação para portas específicas
        for port in port_list:
            if port < 1 or port > 65535:
                print(f"[ERRO] Porta {port} inválida. Portas devem estar entre 1 e 65535")
                sys.exit(1)
    else:
        # Validação para range
        if port_list[0] < 1 or port_list[1] > 65535:
            print("[ERRO] Portas devem estar entre 1 e 65535")
            sys.exit(1)
    
    if args.threads < 1 or args.threads > 1000:
        print("[ERRO] Número de threads deve estar entre 1 e 1000")
        sys.exit(1)
    
    # Cria e executa o scanner
    scanner = TCPScanner(args.target, port_list, args.timeout, args.threads)
    
    try:
        scanner.run_scan()
    except KeyboardInterrupt:
        print("\n[INFO] Scan interrompido pelo usuário")
        sys.exit(0)
    except Exception as e:
        print(f"[ERRO] Erro durante o scan: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
