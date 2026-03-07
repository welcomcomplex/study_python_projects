import json

def load_config(filepath: str):
    try:
        with open(filepath) as f:
            return json.load(f)  # ← 在这里捕获并重新抛出
    except Exception as e:
        raise RuntimeError(f"Failed to load config from {filepath}") from e  
    
class APIRateLimitError(Exception):
    def __init__(self, user_id, limit):
        self.user_id = user_id
        self.limit = limit
        super().__init__(f"Rate limit exceeded for user {user_id}, limit {limit}")
api_rate_limits = APIRateLimitError(user_id=1001, limit=10)
try:
    def check_rate_limit(user_id):
        if user_id == 1001:
            raise api_rate_limits
    check_rate_limit(1001)
except APIRateLimitError as e:
    print(f"Caught API rate limit error: {e}")
    