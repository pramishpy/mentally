class SimulationManager:
    """
    Manages AR simulations that help users understand various mental health experiences
    """
    def __init__(self):
        self.simulations = {
            "auditory-hallucination": {
                "id": "auditory-hallucination",
                "title": "Auditory Hallucination Simulation",
                "description": "Experience what it might be like to hear voices, similar to some experiences of schizophrenia.",
                "duration": "3 minutes",
                "warning": "This simulation may be distressing. Stop immediately if you feel uncomfortable.",
                "type": "audio",
                "scenario": "coffee-shop",
                "audio_files": ["ambient_voices.mp3", "critical_voices.mp3", "command_voices.mp3"],
                "youtube_video": {
                    "id": "0vvU-Ajwbok",
                    "title": "Auditory Hallucinations Simulation",
                    "description": "This video simulates what auditory hallucinations might sound like for someone experiencing them."
                },
                "instructions": "Put on headphones. When ready, press start. You'll hear ambient coffee shop sounds mixed with simulated auditory hallucinations.",
                "educational_content": "Auditory hallucinations affect approximately 70% of people with schizophrenia. They often involve hearing voices that others don't hear.",
                "coping_strategies": ["Focus on real external sounds", "Use grounding techniques", "Seek support from others"],
                "ar_elements": {
                    "visual_distortions": False,
                    "interactive_objects": [],
                    "environment": "coffee_shop.glb"
                }
            },
            "anxiety-simulation": {
                "id": "anxiety-simulation",
                "title": "Social Anxiety Simulation",
                "description": "Experience aspects of social anxiety in a simulated public speaking scenario.",
                "duration": "5 minutes",
                "warning": "This simulation may trigger anxiety. Stop immediately if you feel uncomfortable.",
                "type": "visual-audio",
                "scenario": "presentation-room",
                "audio_files": ["heartbeat.mp3", "murmuring.mp3", "inner_critic.mp3"],
                "instructions": "Use headphones and hold your phone up as if you're viewing the room. You'll experience visual and auditory effects similar to social anxiety.",
                "educational_content": "Social anxiety disorder affects about 15 million adults in the U.S. It involves intense fear of being judged or rejected in social situations.",
                "coping_strategies": ["Controlled breathing", "Cognitive reframing", "Gradual exposure"],
                "ar_elements": {
                    "visual_distortions": True,
                    "distortion_effects": ["tunnel_vision", "blur", "pulsing"],
                    "interactive_objects": [
                        {"id": "audience1", "position": [0, 0, -2], "animation": "judgmental_looking"},
                        {"id": "audience2", "position": [1, 0, -2], "animation": "whispering"},
                        {"id": "audience3", "position": [-1, 0, -2], "animation": "checking_phone"}
                    ],
                    "environment": "presentation_room.glb"
                }
            },
            "depression-simulation": {
                "id": "depression-simulation",
                "title": "Depression Perception Simulation",
                "description": "Experience how depression can alter perception and energy levels through this educational video.",
                "duration": "4 minutes",
                "warning": "This simulation may evoke feelings of sadness. Stop if you feel uncomfortable.",
                "type": "video-only",
                "scenario": "depression-video",
                "audio_files": [],
                "youtube_video": {
                    "id": "TEXACMOrZQw",
                    "title": "Depression Perception Simulation",
                    "description": "This video demonstrates how depression can alter perception, making the world appear less vibrant and tasks feel more difficult."
                },
                "instructions": "Watch this educational video to gain insight into how depression can alter one's perception of the world.",
                "educational_content": "Depression can alter how people perceive their environment, often making things appear less vibrant and tasks feel more difficult.",
                "coping_strategies": ["Behavioral activation", "Social connection", "Professional support"],
                "ar_elements": {
                    "visual_distortions": False,
                    "interactive_objects": [],
                    "environment": ""
                }
            },
            "panic-attack": {
                "id": "panic-attack",
                "title": "Panic Attack Simulation",
                "description": "Experience some sensory aspects of a panic attack with guided recovery techniques.",
                "duration": "6 minutes",
                "warning": "This simulation includes intense sensory effects. Stop immediately if distressed.",
                "type": "full-sensory",
                "scenario": "public-transport",
                "audio_files": ["racing_heart.mp3", "heavy_breathing.mp3", "crowd_noise.mp3"],
                "youtube_video": {
                    "id": "_VIuaqUMfWk",
                    "title": "Panic Attack Simulation",
                    "description": "This video demonstrates what experiencing a panic attack might feel like, including the physical and emotional sensations."
                },
                "instructions": "Find a quiet space where you can sit comfortably. The simulation will progress through stages of a panic attack, followed by guided recovery.",
                "educational_content": "Panic attacks involve sudden, intense fear with physical symptoms like racing heart, shortness of breath, and dizziness.",
                "coping_strategies": ["Deep breathing", "5-4-3-2-1 grounding technique", "Progressive muscle relaxation"],
                "ar_elements": {
                    "visual_distortions": True,
                    "distortion_effects": ["pulsing", "tunnel_vision", "brightness_fluctuation"],
                    "interactive_objects": [],
                    "environment": "subway_car.glb",
                    "recovery_guide": {
                        "model": "calm_guide.glb",
                        "audio": "guided_recovery.mp3",
                        "appears_at": 180  # Seconds into simulation
                    }
                }
            }
        }
    
    def get_all_simulations(self):
        """Return all available simulations"""
        return list(self.simulations.values())
    
    def get_simulation(self, simulation_id):
        """Return a specific simulation by ID"""
        if simulation_id in self.simulations:
            return self.simulations[simulation_id]
        return None
    
    def get_simulations_by_type(self, sim_type):
        """Return simulations filtered by type"""
        return [sim for sim in self.simulations.values() if sim["type"] == sim_type]
