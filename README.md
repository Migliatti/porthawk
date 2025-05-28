# PortHawk 🦅

[![Python Version](https://img.shields.io/badge/python-3.6+-blue.svg)](https://python.org)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![GitHub Stars](https://img.shields.io/github/stars/seuusuario/PortHawk.svg)](https://github.com/seuusuario/PortHawk/stargazers)

> **PortHawk** é um scanner TCP rápido e educacional desenvolvido em Python para descobrir portas abertas e identificar serviços em execução. Ideal para aprender sobre networking, sockets e segurança de redes.

## ✨ Características

- 🚀 **Multi-threaded** - Escaneamento rápido e eficiente
- 🎯 **Portas específicas** - Escaneia portas exatas ou ranges
- 🔍 **Detecção de serviços** - Identifica serviços comuns automaticamente
- 🏷️ **Banner grabbing** - Captura informações dos serviços
- 🌐 **Suporte a hostname** - Resolve DNS automaticamente
- ⚙️ **Configurável** - Timeout e threads ajustáveis
- 📊 **Relatório detalhado** - Resultados organizados e informativos

## 🚀 Instalação Rápida

```bash
# Clone o repositório
git clone https://github.com/seuusuario/PortHawk.git
cd PortHawk

# Execute diretamente (Python 3.6+ necessário)
python src/porthawk.py -h
```

## 📖 Uso Básico

### Exemplos rápidos:

```bash
# Escanear portas comuns
python src/porthawk.py -t google.com -p 80,443,8080

# Escanear range de portas
python src/porthawk.py -t 192.168.1.1 -p 1-1000

# Scan rápido com mais threads
python src/porthawk.py -t example.com -p 20-25 -th 200 -T 0.5
```

### Parâmetros disponíveis:

| Parâmetro | Descrição | Exemplo |
|-----------|-----------|---------|
| `-t, --target` | IP ou hostname do alvo | `-t 192.168.1.1` |
| `-p, --ports` | Portas (range ou específicas) | `-p 1-1000` ou `-p 80,443` |
| `-T, --timeout` | Timeout em segundos | `-T 2` |
| `-th, --threads` | Número de threads | `-th 100` |

## 🎯 Exemplos Detalhados

### 1. Scan básico de um servidor web
```bash
python src/porthawk.py -t www.example.com -p 80,443,8080,8443
```

### 2. Descoberta de serviços em rede local
```bash
python src/porthawk.py -t 192.168.1.1 -p 1-65535 -th 500 -T 1
```

### 3. Teste rápido de portas específicas
```bash
python src/porthawk.py -t target.com -p 22,23,25,53,80,110,143,443,993,995
```

## 📊 Exemplo de Saída

```

         

 ██▓███   ▒█████   ██▀███  ▄▄▄█████▓ ██░ ██  ▄▄▄       █     █░██ ▄█▀
▓██░  ██▒▒██▒  ██▒▓██ ▒ ██▒▓  ██▒ ▓▒▓██░ ██▒▒████▄    ▓█░ █ ░█░██▄█▒ 
▓██░ ██▓▒▒██░  ██▒▓██ ░▄█ ▒▒ ▓██░ ▒░▒██▀▀██░▒██  ▀█▄  ▒█░ █ ░█▓███▄░ 
▒██▄█▓▒ ▒▒██   ██░▒██▀▀█▄  ░ ▓██▓ ░ ░▓█ ░██ ░██▄▄▄▄██ ░█░ █ ░█▓██ █▄ 
▒██▒ ░  ░░ ████▓▒░░██▓ ▒██▒  ▒██▒ ░ ░▓█▒░██▓ ▓█   ▓██▒░░██▒██▓▒██▒ █▄
▒▓▒░ ░  ░░ ▒░▒░▒░ ░ ▒▓ ░▒▓░  ▒ ░░    ▒ ░░▒░▒ ▒▒   ▓▒█░░ ▓░▒ ▒ ▒ ▒▒ ▓▒
░▒ ░       ░ ▒ ▒░   ░▒ ░ ▒░    ░     ▒ ░▒░ ░  ▒   ▒▒ ░  ▒ ░ ░ ░ ░▒ ▒░
░░       ░ ░ ░ ▒    ░░   ░   ░       ░  ░░ ░  ░   ▒     ░   ░ ░ ░░ ░ 
             ░ ░     ░               ░  ░  ░      ░  ░    ░   ░  ░   
                                                                     
              
2025-05-28 10:43:05 
============================================================
[INFO] Resolvendo google.com -> 172.217.28.142
[ALVO] IP: 172.217.28.142
[RANGE] Portas: 80-450
[INFO] Escaneando range de portas 80-450
[INFO] Total de portas: 371
[INFO] Usando 100 threads com timeout de 1s
--------------------------------------------------
[ABERTA] Porta 80 - HTTP
[ABERTA] Porta 443 - HTTPS
--------------------------------------------------
[RESUMO] Scan finalizado em 4.07 segundos
[RESULTADO] 2 porta(s) aberta(s) encontrada(s):

Porta    80 - HTTP           
Banner
HTTP/1.1 301 Moved Permanently
Location: http://www.google.com/
Content-Type: text/html; charset=U

Porta   443 - HTTPS          
```

## 🧠 Conceitos Demonstrados

Este projeto é uma excelente ferramenta educacional que demonstra:

- **Sockets TCP**: Uso da biblioteca `socket` do Python
- **Threading**: Paralelização para melhor performance
- **Network Programming**: Conexões, timeouts e tratamento de erros
- **Service Detection**: Identificação de serviços por porta
- **Banner Grabbing**: Captura de informações de serviços
- **Command Line Interface**: Uso do `argparse`

## ⚠️ Uso Responsável

Este projeto foi desenvolvido para fins **educacionais e de teste**. Use apenas em:

- ✅ Redes próprias
- ✅ Ambientes de teste autorizados
- ✅ Sistemas que você possui ou tem permissão explícita

**Não use para:**
- ❌ Scan de redes sem autorização
- ❌ Atividades maliciosas
- ❌ Violação de termos de serviço

## 🛠️ Desenvolvimento

### Executar testes
```bash
python -m pytest tests/
```

### Contribuir
1. Fork o projeto
2. Crie uma branch para sua feature (`git checkout -b feature/nova-feature`)
3. Commit suas mudanças (`git commit -am 'Adiciona nova feature'`)
4. Push para a branch (`git push origin feature/nova-feature`)
5. Abra um Pull Request

## 🤝 Contribuições

Contribuições são bem-vindas! Veja como você pode ajudar:

- 🐛 Reportar bugs
- 💡 Sugerir novas features
- 📖 Melhorar a documentação
- 🧪 Adicionar testes
- 🔧 Otimizar o código

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## 👨‍💻 Autor

Desenvolvido com ❤️ para aprendizado e educação em segurança de redes.

---

⭐ Se este projeto foi útil para você, considere dar uma estrela no GitHub!

## 🔗 Links Úteis

- [Documentação do Python Socket](https://docs.python.org/3/library/socket.html)
- [Network Programming with Python](https://realpython.com/python-sockets/)
- [TCP/IP Fundamentals](https://en.wikipedia.org/wiki/Transmission_Control_Protocol)
