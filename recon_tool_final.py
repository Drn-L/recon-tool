import argparse
import subprocess
import requests

#- - - - - - - - - - - - - - -
#FUNCIONES
#- - - - - - - - - - - - - - -

def obtener_info_ip(ip):
    url = "http://ip-api.com/json/" + ip

    try:
        respuesta = requests.get(url)
        data = respuesta.json()

        if data.get("status") == "fail":
            return None

        return {
            "pais": data.get("country"),
            "ciudad": data.get("city"),
            "isp": data.get("isp")
        }

    except Exception as e:
        print("Error al consultar API:", e)
        return None


def escanear_puertos(ip):
    try:
        resultado = subprocess.run(
            ["nmap", "-p", "1-1000", ip],
            capture_output=True,
            text=True
        )
        return resultado.stdout

    except Exception as e:
        print("Error en escaneo:", e)
        return ""


def guardar_reporte(ip, info, escaneo):
    nombre_archivo = "reporte_" + ip + ".txt"

    with open(nombre_archivo, "w") as archivo:
        archivo.write("IP: " + ip + "\n")

        if info:
            archivo.write("Pais: " + info["pais"] + "\n")
            archivo.write("Ciudad: " + info["ciudad"] + "\n")
            archivo.write("ISP: " + info["isp"] + "\n")
        else:
            archivo.write("Sin informacion de API\n")

        archivo.write("\n--- ESCANEO ---\n")
        archivo.write(escaneo)


#- - - - - - - - - - - - - -
# MAIN
#- - - - - - - - - - - - - -

def main():
    parser = argparse.ArgumentParser(description="Herramienta de reconocimiento")
    parser.add_argument("--ip", required=True, help="IP objetivo")

    args = parser.parse_args()
    ip = args.ip.strip()

    print("Analizando IP:", ip)

    info = obtener_info_ip(ip)

    if info:
        print("\n[INFO IP]")
        print("Pais:", info["pais"])
        print("Ciudad:", info["ciudad"])
        print("ISP:", info["isp"])
    else:
        print("\n[!] No hay informacion disponible (IP privada o invalidad)")


    escaneo = escanear_puertos(ip)

    print("\n[ESCANEO]")
    print(escaneo)

    guardar_reporte(ip, info, escaneo)

    print("\n[/] Reporte generado")


if __name__ == "__main__":
    main()
