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

# Overriding conversation
conversation_override = {
    "agent": {
        "prompt": {
            "prompt": prompt,
        },
        "first_message": first_message,
    },
}

config = ConversationConfig()
config = config.model_copy(update={
    "conversation_config_override": conversation_override,
    "extra_body": {},
    "dynamic_variables": {},
})

# printing transcripts in terminal

def  assistant_response(response):
    print(f"Assistant: {response}")

def assistant_interrupted_response(original, corrected):
    print(f"Assistant: {original} -> {corrected}")

def user_transcript(transcript):
    print(f"User: {transcript}")

client = ElevenLabs(api_key=API_KEY)

conversation = Conversation(client, AGENT_ID,
                            requires_auth=True,
                            audio_interface = DefaultAudioInterface(),
                            callback_agent_response = assistant_response,
                            callback_agent_response_correction = assistant_interrupted_response,
                            callback_user_transcript = user_transcript)

conversation.start_session()
