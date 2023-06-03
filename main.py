from services import rss, tts
from config import elevenlabs_key


rss_service = rss.RSS()
tts_service = tts.TTS(api_key=elevenlabs_key)

summaries = rss_service.get_summaries()
tts_service.generate_save_audio(summaries[0], 'summaries0')