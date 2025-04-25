"""
AR Educational Module for Mental Health Stigma Reduction
"""
class AREducation:
    """
    Provides educational AR content specifically designed to reduce mental health stigma
    through immersive learning experiences.
    """
    def __init__(self):
        self.educational_modules = {
            "stigma_basics": {
                "title": "Understanding Mental Health Stigma",
                "description": "Learn about the types and impacts of mental health stigma through interactive AR visualization.",
                "ar_scenes": [
                    {
                        "id": "public_stigma",
                        "title": "Public Stigma",
                        "description": "Visualize how public stigma creates barriers in everyday situations",
                        "model": "public_stigma_visualization.glb",
                        "interaction_points": [
                            {"position": [0, 0, -1], "title": "Workplace", "content": "49% of employees wouldn't discuss mental health with their supervisor"},
                            {"position": [1, 0, -1], "title": "Healthcare", "content": "Many people avoid seeking treatment due to fear of being labeled"},
                            {"position": [-1, 0, -1], "title": "Media", "content": "Media portrayals often reinforce negative stereotypes"}
                        ],
                        "audio": "public_stigma_narration.mp3"
                    },
                    {
                        "id": "self_stigma",
                        "title": "Self-Stigma",
                        "description": "Experience how internalized stigma affects self-perception and help-seeking",
                        "model": "self_stigma_visualization.glb",
                        "interaction_points": [
                            {"position": [0, 0, -1], "title": "Self-Image", "content": "Self-stigma can lead to decreased self-esteem and self-efficacy"},
                            {"position": [0.5, 0, -1], "title": "Help-Seeking", "content": "Self-stigma reduces likelihood of seeking treatment by 60%"},
                            {"position": [-0.5, 0, -1], "title": "Recovery", "content": "Overcoming self-stigma is a key part of the recovery process"}
                        ],
                        "audio": "self_stigma_narration.mp3"
                    }
                ],
                "quizzes": [
                    {
                        "question": "Which of the following is NOT a common form of mental health stigma?",
                        "options": ["Public stigma", "Self-stigma", "Economic stigma", "Structural stigma"],
                        "correct_answer": "Economic stigma"
                    },
                    {
                        "question": "How can media portrayals contribute to mental health stigma?",
                        "options": [
                            "By accurately depicting treatment options", 
                            "By reinforcing stereotypes of violence and unpredictability",
                            "By showing diverse recovery journeys", 
                            "By focusing on the biological basis of mental health conditions"
                        ],
                        "correct_answer": "By reinforcing stereotypes of violence and unpredictability"
                    }
                ]
            },
            "language_matters": {
                "title": "The Language of Mental Health",
                "description": "Explore how language shapes perceptions of mental health through AR word clouds and interactive dialogs.",
                "ar_scenes": [
                    {
                        "id": "stigmatizing_language",
                        "title": "Stigmatizing Language",
                        "description": "Visualize how certain terms and phrases perpetuate stigma",
                        "model": "stigmatizing_language.glb",
                        "interaction_points": [
                            {"position": [0, 0, -1], "title": "Person-First Language", "content": "Say 'person with schizophrenia' not 'schizophrenic'"},
                            {"position": [0.7, 0, -1], "title": "Avoid Defining by Condition", "content": "People are more than their diagnosis"},
                            {"position": [-0.7, 0, -1], "title": "Casual Misuse", "content": "Terms like 'OCD' or 'bipolar' shouldn't be used casually"}
                        ],
                        "audio": "language_matters_narration.mp3"
                    },
                    {
                        "id": "empowering_language",
                        "title": "Empowering Language",
                        "description": "Learn how supportive language can reduce stigma and encourage help-seeking",
                        "model": "empowering_language.glb",
                        "interaction_points": [
                            {"position": [0, 0, -1], "title": "Recovery-Oriented", "content": "Focus on hope and possibility rather than limitations"},
                            {"position": [0.7, 0, -1], "title": "Normalize Help-Seeking", "content": "Phrases that validate seeking support and treatment"},
                            {"position": [-0.7, 0, -1], "title": "Strength-Based", "content": "Language that acknowledges resilience and capability"}
                        ],
                        "audio": "empowering_language_narration.mp3"
                    }
                ],
                "conversation_simulator": {
                    "title": "Stigma-Free Conversations",
                    "scenarios": [
                        {
                            "setup": "A coworker discloses they're taking time off for mental health",
                            "options": [
                                {"text": "You don't look sick to me.", "feedback": "This invalidates their experience and reinforces stigma."},
                                {"text": "Thank you for sharing that with me. How can I support you?", "feedback": "This response is supportive and non-judgmental.", "is_correct": True},
                                {"text": "Have you tried exercise instead of medication?", "feedback": "This could undermine their treatment choices and implies they haven't explored options."}
                            ]
                        },
                        {
                            "setup": "Someone mentions they have anxiety",
                            "options": [
                                {"text": "Everyone gets anxious sometimes. Just relax.", "feedback": "This minimizes their experience and fails to acknowledge anxiety as a mental health condition."},
                                {"text": "I know anxiety can be really challenging. How are you managing?", "feedback": "This validates their experience and shows interest in their wellbeing.", "is_correct": True},
                                {"text": "What do you have to be anxious about?", "feedback": "This question implies they need a 'reason' to have anxiety, which misunderstands the condition."}
                            ]
                        }
                    ]
                }
            },
            "representation_reality": {
                "title": "Representation vs. Reality",
                "description": "Compare media portrayals of mental health conditions with real experiences through AR visualizations.",
                "ar_scenes": [
                    {
                        "id": "media_stereotypes",
                        "title": "Media Stereotypes",
                        "description": "Examine common media depictions of mental health conditions",
                        "model": "media_stereotypes.glb",
                        "interaction_points": [
                            {"position": [0, 0, -1], "title": "Film Portrayals", "content": "Characters with mental illness are often portrayed as dangerous or unpredictable"},
                            {"position": [0.7, 0, -1], "title": "News Coverage", "content": "Media often links mental illness to violence despite contrary evidence"},
                            {"position": [-0.7, 0, -1], "title": "Dramatic Exaggeration", "content": "Symptoms are often exaggerated for dramatic effect"}
                        ],
                        "audio": "media_portrayal_narration.mp3"
                    },
                    {
                        "id": "lived_experiences",
                        "title": "Lived Experiences",
                        "description": "Explore the diverse reality of living with mental health conditions",
                        "model": "diverse_experiences.glb",
                        "interaction_points": [
                            {"position": [0, 0, -1], "title": "Recovery Journeys", "content": "Many people effectively manage symptoms and lead fulfilling lives"},
                            {"position": [0.7, 0, -1], "title": "Treatment Success", "content": "70-90% of individuals see reduction in symptoms with proper treatment"},
                            {"position": [-0.7, 0, -1], "title": "Everyday Heroes", "content": "People with mental health conditions contribute valued work across all fields"}
                        ],
                        "audio": "lived_experiences_narration.mp3"
                    }
                ],
                "media_comparison": [
                    {
                        "condition": "Schizophrenia",
                        "media_portrayal": "Violent, unpredictable, unable to function in society",
                        "reality": "Most people with schizophrenia are not violent. Many live independently, work, and have families with proper treatment."
                    },
                    {
                        "condition": "OCD",
                        "media_portrayal": "Quirky neat freaks who like organization",
                        "reality": "OCD involves distressing, intrusive thoughts and compulsive behaviors that interfere with daily life."
                    },
                    {
                        "condition": "Depression",
                        "media_portrayal": "Just sadness that can be overcome with positive thinking",
                        "reality": "Clinical depression is a serious medical condition affecting mood, cognition, and physical health, often requiring treatment."
                    }
                ]
            }
        }
        
    def get_all_modules(self):
        """Return list of all available AR educational modules"""
        return [{
            "id": module_id,
            "title": data["title"],
            "description": data["description"]
        } for module_id, data in self.educational_modules.items()]
    
    def get_module(self, module_id):
        """Return specific educational module by ID"""
        if module_id in self.educational_modules:
            return self.educational_modules[module_id]
        return None
    
    def get_ar_scene(self, module_id, scene_id):
        """Return specific AR scene from a module"""
        if module_id in self.educational_modules:
            module = self.educational_modules[module_id]
            for scene in module.get("ar_scenes", []):
                if scene["id"] == scene_id:
                    return scene
        return None
    
    def get_conversation_simulator(self, module_id):
        """Return conversation simulator for practicing stigma-free conversations"""
        if module_id in self.educational_modules and "conversation_simulator" in self.educational_modules[module_id]:
            return self.educational_modules[module_id]["conversation_simulator"]
        return None
