with open("error.log", "a", encoding="utf-8") as f:
    f.write("ERROR: Failed to connect to DB\n")

##import json, os
#new_config = {"debug": True, "timeout": 30}
##with open("config.json.tmp", "x", encoding="utf-8") as f:
#    json.dump(new_config, f, indent=2)
 #   os.replace("config.json.tmp", "config.json")
#    raise RuntimeError("Simulated error after writing config.json.tmp")

import json, os, tempfile

def safe_write_json(filepath: str, data: dict):
    # 创建临时文件（自动命名，避免冲突）
    tmp_fd, tmp_path = tempfile.mkstemp(suffix=".json", dir=os.path.dirname(filepath))
    try:
        with os.fdopen(tmp_fd, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        
        # 原子替换（Linux/macOS 安全；Windows 上用 shutil.move）
        if os.name == 'nt':  # Windows
            import shutil
            shutil.move(tmp_path, filepath)
        else:
            os.replace(tmp_path, filepath)
    except Exception:
        # 清理临时文件（无论成功失败）
        try:
            os.unlink(tmp_path)
        except OSError:
            pass
        raise

# 使用：
new_config = {"debug": True, "timeout": 30}
safe_write_json("config.json", new_config)



def init_once(filepath: str) -> bool:
    try:
        with open(filepath, "x", encoding="utf-8") as f:
            f.write("initialized")
    except FileExistsError:
        return False
    return True