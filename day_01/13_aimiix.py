class LogMixin:
    def log(self):
        return "logging..."
class RetryMixin(LogMixin):
    def retry(self):
        return super.log() + " retrying..."
class AIService(RetryMixin):
    @classmethod
    def run(cls):
        return super.retry()
    
print(AIService.run())  # This will call the run method of AIService, which in turn calls the retry method of RetryMixin, and finally the log method of LogMixin.