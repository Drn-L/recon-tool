Recon Tool - Análisis de IP

Herramienta desarrollada en Python para el análisis de direcciones IP, combinando escaneo de puertos y obtención de información mediante API.

🚀 Características

Escaneo de puertos con Nmap
Consulta de información de IP (país, ciudad, ISP)
Generación de reportes automáticos
Manejo de errores
Soporte para IPs públicas y privadas

🛠 Tecnologías

Python 3
Nmap
Requests
Argparse

▶️ Uso

python3 recon_tool_final.py --ip 8.8.8.8

📄 Ejemplo de salida

[INFO IP]
País: United States
Ciudad: Mountain View
ISP: Google LLC

[ESCANEO]
53/tcp open domain
443/tcp open https

📁 Salida

Se genera un archivo:

reporte_8.8.8.8.txt

⚠️ Nota

Las IPs privadas no devuelven información en la API, pero sí permiten escaneo de puertos.

👨‍💻 Autor

DRN
