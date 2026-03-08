#Author: Kasiemobi Ojiaku
#Date: 3-05-2026
#Data last updated: 3-05-2026
# Log Analyzer Project

from pathlib import Path
def read_log_file(path: str):
    log_path = Path(path)
    if not log_path.exists():
        print (f"[!] Log file not found: {log_path}")
        return
    with log_path.open("r", encoding="utf-8") as f:
        for line in f:
            line = line.rstrip("\n")
            print(line)
def main():
    sample_path = Path(__file__).parent.parent / "SampleLogs" / "example.log"
    print(f"[+] Reading: {sample_path}")
    read_log_file(str(sample_path))

if __name__ == "__main__":
    main()
