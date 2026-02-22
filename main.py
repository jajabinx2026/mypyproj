import argparse
import socket


def is_open(host: str, port: int, timeout: float = 0.5) -> bool:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(timeout)
        return s.connect_ex((host, port)) == 0


def main() -> None:
    parser = argparse.ArgumentParser(description="Simple port checker")
    parser.add_argument("host", help="Target host (IP or domain)")
    parser.add_argument("--port", type=int, default=80, help="Port to check (default: 80)")
    parser.add_argument("--timeout", type=float, default=0.5, help="Timeout seconds (default: 0.5)")
    args = parser.parse_args()

    ok = is_open(args.host, args.port, args.timeout)
    if ok:
        print(f"✅ {args.host}:{args.port} is OPEN")
    else:
        print(f"❌ {args.host}:{args.port} is CLOSED or FILTERED")


if __name__ == "__main__":
    main()
