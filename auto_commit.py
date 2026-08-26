import os
import random
import subprocess
import datetime
import time
import argparse

LOG_FILE = "activity.txt"

COMMIT_MESSAGES = [
    "docs: update activity log",
    "chore: daily sync update",
    "feat: record routine automated telemetry",
    "fix: minor syntax and log formatting",
    "refactor: optimize routine tracking data",
    "style: format tracking history",
    "ci: routine activity check",
    "test: update automated test logs",
    "perf: optimize background log entry",
    "build: routine build timestamp update",
]

def run_git_command(cmd_list):
    """Menjalankan perintah Git melalui subprocess."""
    result = subprocess.run(
        cmd_list,
        capture_output=True,
        text=True,
        check=False
    )
    if result.returncode != 0:
        print(f"[Error Git] {' '.join(cmd_list)}:\n{result.stderr}")
    else:
        if result.stdout.strip():
            print(result.stdout.strip())
    return result.returncode == 0

def update_activity_file():
    """Menambahkan timestamp ke file activity.txt."""
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(f"Updated at: {now} - random hash: {os.urandom(4).hex()}\n")

def make_commit(custom_message=None):
    """Membuat 1 commit tanpa push."""
    update_activity_file()
    message = custom_message or random.choice(COMMIT_MESSAGES)
    
    print(f"[*] Melakukan commit: '{message}'...")
    if not run_git_command(["git", "add", LOG_FILE]):
        return False
    
    if not run_git_command(["git", "commit", "-m", message]):
        return False
    return True

def make_commit_and_push(custom_message=None):
    """Membuat 1 commit dan push ke remote."""
    if make_commit(custom_message):
        print("[*] Melakukan push ke GitHub...")
        return run_git_command(["git", "push"])
    return False

def run_batch(min_commits=3, max_commits=10, push=True):
    """Membuat beberapa commit sekaligus (3 - 10 commit) dan push."""
    total = random.randint(min_commits, max_commits)
    print(f"[*] Menjalankan batch commit: Total {total} commit akan dibuat.")
    
    for i in range(1, total + 1):
        update_activity_file()
        msg = f"{random.choice(COMMIT_MESSAGES)} (#{i}/{total})"
        run_git_command(["git", "add", LOG_FILE])
        run_git_command(["git", "commit", "-m", msg])
        time.sleep(1)
        
    if push:
        print(f"[*] Mendorong {total} commit ke GitHub...")
        run_git_command(["git", "push"])
    print("[✓] Selesai!")

def run_daemon(min_commits=3, max_commits=10):
    """
    Mode background / daemon:
    Berjalan seharian dan menyebarkan 3 - 10 commit dalam waktu 24 jam.
    """
    print(f"[*] Mode Daemon aktif. Menghasilkan {min_commits}-{max_commits} commit secara berkala setiap hari...")
    while True:
        target_today = random.randint(min_commits, max_commits)
        print(f"[*] Hari baru: Target {target_today} commit hari ini.")
        
        seconds_in_day = 86400
        avg_interval = seconds_in_day // target_today
        
        for i in range(target_today):
            delay = random.randint(int(avg_interval * 0.5), int(avg_interval * 1.5))
            print(f"[*] Commit berikutnya dalam {delay // 60} menit...")
            time.sleep(delay)
            make_commit_and_push()
            
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Auto Commit & Push ke GitHub")
    parser.add_argument("--mode", choices=["single", "batch", "daemon"], default="single",
                        help="Mode: 'single' (1 commit), 'batch' (3-10 commit sekaligus), 'daemon' (berjalan sepanjang hari)")
    parser.add_argument("--min", type=int, default=3, help="Jumlah minimal commit (default: 3)")
    parser.add_argument("--max", type=int, default=10, help="Jumlah maksimal commit (default: 10)")
    parser.add_argument("--no-push", action="store_true", help="Hanya buat commit tanpa push (cocok untuk GitHub Actions)")
    
    args = parser.parse_args()
    
    if args.mode == "single":
        if args.no_push:
            make_commit()
        else:
            make_commit_and_push()
    elif args.mode == "batch":
        run_batch(args.min, args.max, push=not args.no_push)
    elif args.mode == "daemon":
        run_daemon(args.min, args.max)
