import argparse
import subprocess

def run_command(hosts, ports, arguments, superuser):
    command = ["nmap"]
    command.extend(hosts)
    command.extend(["-p", ",".join(ports)])
    command.extend(arguments)

    if superuser:
        command.insert(0, "sudo")

    print("Running command:", " ".join(command))
    subprocess.run(command)

def main():
    parser = argparse.ArgumentParser(description="Custom Nmap Command Runner")
    parser.add_argument("hosts", nargs="+", help="Hosts to scan")
    parser.add_argument("-p", "--ports", nargs="+", default=["1-1000"], help="Ports to scan")
    parser.add_argument("-a", "--arguments", nargs="+", default=[], help="Additional arguments for Nmap")
    parser.add_argument("--superuser", action="store_true", help="Run command as superuser (sudo)")

    args = parser.parse_args()

    run_command(args.hosts, args.ports, args.arguments, args.superuser)

if __name__ == "__main__":
    main()
