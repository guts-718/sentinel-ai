from dotenv import load_dotenv
from src.utils.env import get_env
from src.utils.alert_manager import AlertManager
import datetime
# Load env
load_dotenv()

# Get credentials
token = get_env("TELEGRAM_TOKEN")
chat_id = get_env("TELEGRAM_CHAT_ID")

# Create alert manager
alert = AlertManager(token, chat_id)
message = f"✅ SentinelAI Test Alert\nTime: {datetime.datetime.now()}"

# Send test message
alert.send_alert(message)

print("Message sent (check Telegram)")