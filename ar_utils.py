import random

class ARProcessor:
    """
    Handles processing of AR content for mental health awareness and stigma reduction.
    """
    def __init__(self):
        self.ar_experiences = {
            "anxiety": {
                "models": ["anxiety_visualization.glb", "calming_exercise.glb"],
                "descriptions": ["Visual representation of anxiety and its effects", "Interactive calming exercise"],
                "info": "Anxiety disorders affect 40 million adults in the United States."
            },
            "depression": {
                "models": ["depression_visualization.glb", "mood_lifting.glb"],
                "descriptions": ["Visual metaphor for depression", "Interactive mood-lifting activity"],
                "info": "Depression is one of the most common mental disorders, affecting more than 264 million people worldwide."
            },
            "stigma": {
                "models": ["breaking_stigma.glb", "community_support.glb"],
                "descriptions": ["Breaking the chains of stigma visualization", "Building community support network"],
                "info": "Mental health stigma prevents 60% of people with mental health issues from seeking help."
            },
            # New stigma-focused AR experiences
            "anxiety-stigma": {
                "models": ["anxiety_misconceptions.glb", "anxiety_reality.glb"],
                "descriptions": ["Common misconceptions about anxiety disorders", "The reality of living with anxiety"],
                "info": "Many people mistakenly believe anxiety is just 'being nervous' when it's actually a serious medical condition.",
                "stigma_reduction": "This visualization contrasts public misconceptions with clinical realities of anxiety disorders."
            },
            "depression-reality": {
                "models": ["depression_stigma.glb", "depression_brain.glb"],
                "descriptions": ["Breaking myths about depression", "Neurological aspects of depression"],
                "info": "Depression is often incorrectly viewed as a choice or weakness, rather than a medical condition with biological factors.",
                "stigma_reduction": "By visualizing the biological aspects of depression, this AR experience helps viewers understand it's not a matter of willpower."
            },
            "breaking-stereotypes": {
                "models": ["mental_health_stereotypes.glb", "diverse_experiences.glb"],
                "descriptions": ["Common stereotypes about mental health", "Diverse experiences and recovery journeys"],
                "info": "Media portrayals often reinforce negative stereotypes about mental health conditions.",
                "stigma_reduction": "This experience challenges common media stereotypes by showcasing diverse individuals living with and managing mental health conditions."
            }
        }
        
        # Stigma-reduction specific prompts to guide user reflection
        self.reflection_prompts = {
            "anxiety-stigma": [
                "How might dismissing anxiety as 'just nerves' affect someone seeking help?",
                "What are ways you could respond supportively to someone with anxiety?"
            ],
            "depression-reality": [
                "How does understanding the biological basis of depression change your perspective?",
                "What common phrases might be harmful to someone experiencing depression?"
            ],
            "breaking-stereotypes": [
                "What mental health stereotypes have you encountered in media?",
                "How might these stereotypes affect someone's willingness to seek help?"
            ]
        }
    
    def process_input(self, user_input):
        """
        Process user input to generate relevant AR content focused on stigma reduction
        """
        # Simple keyword matching to determine relevant content
        user_input = user_input.lower()
        
        # Check for stigma-specific keywords first
        if "stigma" in user_input or "misconception" in user_input or "stereotype" in user_input:
            if "anxiety" in user_input:
                return self._prepare_ar_data("anxiety-stigma")
            elif "depression" in user_input or "sad" in user_input:
                return self._prepare_ar_data("depression-reality")
            else:
                return self._prepare_ar_data("breaking-stereotypes")
        
        # Fall back to general mental health topics
        elif "anxiety" in user_input or "stress" in user_input or "worry" in user_input:
            return self._prepare_ar_data("anxiety")
        elif "depression" in user_input or "sad" in user_input or "low" in user_input:
            return self._prepare_ar_data("depression")
        else:
            # Default to stigma reduction content if no specific match
            return self._prepare_ar_data("breaking-stereotypes")
    
    def _prepare_ar_data(self, category):
        """
        Prepare AR data package for the frontend, with emphasis on stigma reduction
        """
        experience = self.ar_experiences[category]
        model_index = random.randint(0, len(experience["models"]) - 1)
        
        data = {
            "type": category,
            "model": experience["models"][model_index],
            "description": experience["descriptions"][model_index],
            "info": experience["info"]
        }
        # Note for frontend: The AR experience page should render the live camera
        # feed as the background for the AR content. This is typically handled
        # by the frontend AR rendering engine (e.g., WebXR for web, 
        # ARKit/ARCore for native apps).
        
        # Add stigma reduction content if available
        if "stigma_reduction" in experience:
            data["stigma_reduction"] = experience["stigma_reduction"]
            
        # Add reflection prompts if available
        if category in self.reflection_prompts:
            data["reflection_prompts"] = self.reflection_prompts[category]
            
        return data
