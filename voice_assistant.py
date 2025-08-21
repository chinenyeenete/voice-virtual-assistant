import os
from dotenv import load_dotenv

load_dotenv()

# getting agent ID and elevenlabs api
AGENT_ID = os.getenv("AGENT_ID")
API_KEY = os.getenv("API_KEY")

# importing elevenlabs dependencies
from elevenlabs.client import ElevenLabs
from elevenlabs.conversational_ai.conversation import Conversation
from elevenlabs.conversational_ai.default_audio_interface import DefaultAudioInterface
from elevenlabs.types import ConversationConfig

# Creating first prompt
user_name = "Chinenye"
schedule = "Project due at 5:00pm; Date at 7:00pm."
prompt = f"Hey assistant. Your interlocutor has the following schedule: {schedule}"
first_message = f"Hello {user_name}, how can I assist you today?"

# Conversation configuration override