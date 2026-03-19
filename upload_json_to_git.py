import subprocess
import os

def github_push():
    # เปลี่ยน Path ไปยังโฟลเดอร์ที่มีไฟล์ .git ของคุณ
    repo_path = r'Y:\runwrf\2026031900_6h_3TUMBON_t1\WRF\POST' 
    os.chdir(repo_path)
    
    try:
        # 1. Add เฉพาะไฟล์ JSON
        subprocess.run(["git", "add", "weather_data_locations.json"], check=True)
        
        # 2. Commit พร้อมใส่เวลาที่อัปเดต
        from datetime import datetime
        commit_message = f"Auto-update weather data: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
        subprocess.run(["git", "commit", "-m", commit_message], check=True)
        
        # 3. Push ขึ้น GitHub
        subprocess.run(["git", "push", "origin", "main"], check=True)
        
        print("✅ [GitHub] Data pushed successfully!")
    except subprocess.CalledProcessError as e:
        print(f"❌ [GitHub] Error occurred: {e}")

# เรียกใช้งานฟังก์ชันท้ายสคริปต์เดิมของคุณ
if __name__ == "__main__":
    # ... โค้ดเดิมของคุณที่สร้างไฟล์ JSON ...
    github_push()