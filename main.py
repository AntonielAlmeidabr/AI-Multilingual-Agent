class MultilingualAgent:
    def __init__(self):
        self.supported_languages = ["en", "fr", "es", "pt"]

    def triage_message(self, message: str, lang: str) -> dict:
        """
        Simula a triagem básica de mensagens recebidas.
        """
        if lang not in self.supported_languages:
            return {"error": "Language not supported"}
        
        return {
            "status": "success",
            "language": lang,
            "message_length": len(message),
            "priority": "normal"
        }

if __name__ == "__main__":
    agent = MultilingualAgent()
    sample = agent.triage_message("Bonjour, j'ai un problème avec ma réservation.", "fr")
    print("Agent Output:", sample)
