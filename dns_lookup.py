#!/usr/bin/env python3
import argparse
import dns.resolver

def dns_lookup(hostnames, record_type, server):
    resolver = dns.resolver.Resolver()
    if server:
        resolver.nameservers = [server]

    results = {}
    for host in hostnames:
        host = host.strip()
        if not host:
            continue
        try:
            answers = resolver.resolve(host, record_type)
            results[host] = [r.to_text() for r in answers]
        except Exception as e:
            results[host] = [f"Error: {e}"]
    return results

def main():
    parser = argparse.ArgumentParser(
        description="DNS lookup tool (nslookup-style) for multiple hostnames."
    )
    parser.add_argument(
        "--file", "-f", required=True,
        help="File containing list of hostnames (one per line)"
    )
    parser.add_argument(
        "--server", "-s",
        help="DNS server to query (default: system default)"
    )
    parser.add_argument(
        "--type", "-t", default="A",
        help="Record type (A, AAAA, CNAME, MX, TXT, etc.)"
    )
    args = parser.parse_args()

    with open(args.file, "r") as f:
        hostnames = f.read().splitlines()

    results = dns_lookup(hostnames, args.type, args.server)
    for host, records in results.items():
        print(f"{host} ({args.type}):")
        for r in records:
            print(f"  {r}")
        print()

if __name__ == "__main__":
    main()
