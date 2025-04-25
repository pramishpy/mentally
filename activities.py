class ActivityManager:
    """
    Manages interactive activities designed to reduce mental health stigma
    """
    def __init__(self):
        self.activities = {
            "myth-buster": {
                "id": "myth-buster",
                "title": "Mental Health Myth Buster",
                "description": "An interactive quiz to test your knowledge about mental health and bust common myths.",
                "duration": "5-10 minutes",
                "type": "quiz",
                "questions": [
                    {
                        "question": "Mental health problems are uncommon.",
                        "options": ["True", "False"],
                        "correct": "False",
                        "explanation": "Mental health problems affect 1 in 4 people worldwide each year."
                    },
                    {
                        "question": "People with mental illness rarely recover.",
                        "options": ["True", "False"],
                        "correct": "False",
                        "explanation": "With proper treatment and support, many people recover fully or learn to manage their conditions effectively."
                    },
                    {
                        "question": "Mental illness is a sign of personal weakness.",
                        "options": ["True", "False"],
                        "correct": "False",
                        "explanation": "Mental illnesses are medical conditions, not character flaws or signs of weakness."
                    },
                    {
                        "question": "Children don't experience mental health problems.",
                        "options": ["True", "False"],
                        "correct": "False",
                        "explanation": "Mental health problems can affect people of any age, including children and adolescents."
                    },
                    {
                        "question": "Therapy and medication are effective treatments for many mental health disorders.",
                        "options": ["True", "False"],
                        "correct": "True",
                        "explanation": "Evidence-based treatments like therapy and medication have proven effective for many mental health conditions."
                    }
                ],
                "completion_message": "Great job! You've taken an important step in understanding mental health better. Knowledge is key to reducing stigma."
            },
            "conversation-starter": {
                "id": "conversation-starter",
                "title": "AR Conversation Starters",
                "description": "Place virtual conversation starter objects in your environment and share them to spark mental health discussions.",
                "duration": "Flexible",
                "type": "ar-sharing",
                "ar_objects": [
                    {
                        "id": "ally-badge",
                        "name": "Mental Health Ally Badge",
                        "model": "ally_badge.glb",
                        "message": "I'm a mental health ally. Let's talk."
                    },
                    {
                        "id": "speech-bubble",
                        "name": "Thought Bubble",
                        "model": "thought_bubble.glb",
                        "customizable": True,
                        "default_message": "Mental health matters because..."
                    },
                    {
                        "id": "green-ribbon",
                        "name": "Mental Health Awareness Ribbon",
                        "model": "green_ribbon.glb",
                        "message": "Breaking the stigma one conversation at a time."
                    }
                ],
                "sharing_platforms": ["Instagram", "Facebook", "Twitter", "TikTok"],
                "hashtags": ["#MentalHealthAwareness", "#BreakTheStigma", "#MentallyApp"]
            },
            "empathy-bridge": {
                "id": "empathy-bridge",
                "title": "Empathy Bridge",
                "description": "Interactive scenarios that help build empathy for various mental health experiences.",
                "duration": "15-20 minutes",
                "type": "interactive-scenarios",
                "scenarios": [
                    {
                        "id": "workplace-anxiety",
                        "title": "Workplace Anxiety",
                        "description": "Navigate a day at work while experiencing anxiety.",
                        "ar_scene": "office_environment.glb",
                        "character": "alex.glb",
                        "decision_points": [
                            {
                                "situation": "Your manager asks you to present in a meeting with little notice.",
                                "options": [
                                    "Try to get out of it by making an excuse.",
                                    "Agree but ask if you can present later in the meeting to have more time to prepare.",
                                    "Panic and go to the restroom."
                                ],
                                "consequences": [
                                    "You avoid the immediate anxiety but feel guilty and worry about future requests.",
                                    "Your manager appreciates your honesty and gives you time to prepare.",
                                    "You feel temporary relief but the anxiety returns stronger when you return."
                                ]
                            },
                            {
                                "situation": "A colleague notices you seem stressed and asks if you're okay.",
                                "options": [
                                    "Dismiss their concern and say you're fine.",
                                    "Briefly acknowledge you're feeling anxious but say you're managing it.",
                                    "Share honestly about your anxiety."
                                ],
                                "consequences": [
                                    "You maintain your privacy but miss an opportunity for support.",
                                    "You maintain boundaries while acknowledging your feelings and receive some support.",
                                    "Your colleague shares that they've had similar experiences and offers helpful suggestions."
                                ]
                            }
                        ],
                        "reflection_questions": [
                            "How did it feel to navigate these situations with anxiety?",
                            "Did any of the character's experiences resonate with your own experiences?",
                            "What did you learn about supporting someone with anxiety in the workplace?"
                        ]
                    }
                ],
                "completion_message": "Thank you for walking in someone else's shoes. Building empathy is one of the most powerful ways to reduce mental health stigma."
            }
        }
        
        self.scavenger_hunt = {
            "id": "stigma-busters-hunt",
            "title": "Stigma Busters AR Scavenger Hunt",
            "description": "An interactive scavenger hunt that challenges misconceptions about mental health through AR clues and tasks.",
            "instructions": "Follow the clues and scan your environment to find AR markers. Each found marker will reveal information and a task related to mental health awareness.",
            "locations": [
                {
                    "id": "location1",
                    "clue": "Look for a place where knowledge flows freely (like a bookshelf or desk).",
                    "ar_marker": "book_marker.png",
                    "ar_content": {
                        "model": "floating_brain.glb",
                        "fact": "Mental health conditions are medical conditions, not character flaws.",
                        "task": "Write down one way that language can inadvertently stigmatize mental health."
                    }
                },
                {
                    "id": "location2",
                    "clue": "Find something that represents connection (like a phone or computer).",
                    "ar_marker": "connection_marker.png",
                    "ar_content": {
                        "model": "support_network.glb",
                        "fact": "Strong social connections can be protective factors for mental health.",
                        "task": "Send a supportive message to someone you care about."
                    }
                },
                {
                    "id": "location3",
                    "clue": "Locate something that helps you relax or find comfort.",
                    "ar_marker": "comfort_marker.png",
                    "ar_content": {
                        "model": "self_care_kit.glb",
                        "fact": "Self-care is not selfish—it's essential for mental wellbeing.",
                        "task": "Take a moment to practice a brief mindfulness exercise."
                    }
                }
            ],
            "completion_reward": {
                "title": "Stigma Buster Badge",
                "description": "You've earned a digital Stigma Buster badge for completing the scavenger hunt!",
                "ar_model": "stigma_buster_badge.glb",
                "shareable": True
            }
        }
    
    def get_all_activities(self):
        """Return all available activities"""
        return list(self.activities.values())
    
    def get_activity(self, activity_id):
        """Return a specific activity by ID"""
        if activity_id in self.activities:
            return self.activities[activity_id]
        return None
    
    def get_scavenger_hunt(self):
        """Return the scavenger hunt data"""
        return self.scavenger_hunt
