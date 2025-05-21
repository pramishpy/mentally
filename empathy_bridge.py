class EmpathyBridgeManager:
    """
    Manages content and experiences for the Empathy Bridge feature.
    """
    def __init__(self):
        self.experiences = [
            {
                "id": "understanding_anxiety",
                "title": "Understanding Anxiety: A Day in the Life",
                "description": "Experience a simulated day through the eyes of someone living with an anxiety disorder.",
                "type": "perspective_simulation",
                "details_url": "/empathy_bridge/understanding_anxiety" 
            },
            {
                "id": "depression_dialogue",
                "title": "Depression Dialogue: The Weight of Words",
                "description": "Explore how different conversational approaches can impact someone experiencing depression.",
                "type": "interactive_dialogue",
                "details_url": "/empathy_bridge/depression_dialogue"
            },
            {
                "id": "stigma_stories",
                "title": "Stigma Stories: Voices Unheard",
                "description": "Listen to and reflect on personal stories of individuals who have faced mental health stigma.",
                "type": "story_collection",
                "details_url": "/empathy_bridge/stigma_stories"
            }
        ]

    def get_all_experiences(self):
        """
        Returns all available Empathy Bridge experiences.
        """
        return self.experiences

    def get_experience(self, experience_id):
        """
        Returns a specific Empathy Bridge experience by its ID.
        """
        for experience in self.experiences:
            if experience["id"] == experience_id:
                return experience
        return None
