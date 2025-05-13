from flask import Flask, request, render_template
import nmap

app = Flask(__name__)

# Fonction pour scanner un réseau
def scan_network(target):
    scanner = nmap.PortScanner()
    scanner.scan(hosts=target, arguments='-sV')  # -sV pour scanner les versions des services
    results = []
    for host in scanner.all_hosts():
        result = {
            "host": host,
            "hostname": scanner[host].hostname(),
            "state": scanner[host].state(),
            "protocols": []
        }
        for proto in scanner[host].all_protocols():
            ports = []
            for port in scanner[host][proto].keys():
                ports.append({
                    "port": port,
                    "state": scanner[host][proto][port]['state']
                })
            result["protocols"].append({
                "protocol": proto,
                "ports": ports
            })
        results.append(result)
    return results

# Route pour la page d'accueil
@app.route('/')
def home():
    return render_template("index.html")

# Route pour lancer un scan
@app.route('/scan', methods=['POST'])
def scan():
    target = request.form['target']
    try:
        results = scan_network(target)
        return render_template("results.html", target=target, results=results)
    except Exception as e:
        return f"Erreur : {e}"

if __name__ == '__main__':
    app.run(debug=True)