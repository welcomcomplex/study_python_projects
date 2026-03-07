import json
def load_json():
    try:
        with open("config.json", "r", encoding="utf-8") as f:
            config = json.load(f)
            return config
    except:
        raise RuntimeError
    return {}

import json, os
def safe_save_json(filepath: str, data: dict):
    tmp_path = filepath + ".tmp"
    try:
        with open(tmp_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
            os.replace(tmp_path, filepath)
    except Exception:
        if os.path.exists(tmp_path):
            try:
                os.unlink(tmp_path)
            except OSError:
                pass
        raise

def get_database_url() -> str:
    url = os.getenv("DATABASE_URL")
    if url is not None:
        return url
    try:
        with open("config.json") as f:
            josn_url = json.load(f)
            return josn_url.get("database_url")
    except(FileNotFoundError, json.JSONDecodeError, KeyError):
        # 文件不存在 / JSON 格式错误 / 缺少 database_url 字段
        return "sqlite:///default.db"

def __iter__(self):
    with open(self.filepath, encoding="utf-8") as f:
        for line in f: 
            yield json.loads(line)
    