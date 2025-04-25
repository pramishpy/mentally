class MentalHealthContent:
    """
    Provides educational content about mental health to reduce stigma.
    """
    def __init__(self):
        self.content = {
            "facts": [
                "Mental health problems affect 1 in 4 people worldwide.",
                "Depression is the leading cause of disability worldwide.",
                "Stigma is one of the main reasons people don't seek help for mental health conditions.",
                "Most people with mental health problems recover completely, or are able to live with and manage them.",
                "Therapy and medication are effective treatments for many mental health disorders."
            ],
            "myths": [
                {"myth": "Mental health problems are rare.", 
                 "fact": "Mental health problems affect millions of people worldwide."},
                {"myth": "People with mental illness are violent and dangerous.", 
                 "fact": "Most people with mental health problems are no more likely to be violent than anyone else."},
                {"myth": "People with mental health problems cannot work.", 
                 "fact": "Many people with mental health problems are successful employees and leaders."},
                {"myth": "Mental health problems are a sign of weakness.", 
                 "fact": "Mental health problems are medical conditions, not character flaws."},
                {"myth": "You can't recover from mental health problems.", 
                 "fact": "With proper treatment and support, many people recover completely."}
            ],
            "resources": [
                {"name": "National Alliance on Mental Illness (NAMI)", 
                 "url": "https://www.nami.org", 
                 "description": "Largest grassroots mental health organization dedicated to building better lives for Americans affected by mental illness."},
                {"name": "Mental Health America", 
                 "url": "https://www.mhanational.org", 
                 "description": "Nation's leading community-based nonprofit dedicated to addressing the needs of those living with mental illness."},
                {"name": "National Institute of Mental Health (NIMH)", 
                 "url": "https://www.nimh.nih.gov", 
                 "description": "Lead federal agency for research on mental disorders."},
                {"name": "Crisis Text Line", 
                 "url": "https://www.crisistextline.org", 
                 "description": "24/7 text-based mental health support and crisis intervention."},
                {"name": "Psychology Today", 
                 "url": "https://www.psychologytoday.com", 
                 "description": "Find mental health professionals in your area."}
            ]
        }
        
        # Educational topics with detailed content
        self.educational_topics = {
            "depression": {
                "title": "Understanding Depression",
                "overview": "Depression is more than just feeling sad. It's a serious mental health condition that affects how a person thinks, feels, and handles daily activities.",
                "symptoms": ["Persistent sad or empty mood", "Loss of interest in activities", "Changes in appetite or weight", "Sleep disturbances", "Fatigue", "Feelings of worthlessness or guilt", "Difficulty concentrating", "Thoughts of death or suicide"],
                "treatments": ["Psychotherapy", "Medication", "Lifestyle changes", "Support groups", "Brain stimulation therapies"],
                "ar_visualizations": ["brain_chemistry.glb", "support_network.glb"],
                "videos": ["understanding_depression.mp4", "treatment_options.mp4"],
                "infographics": ["depression_stats.jpg", "depression_cycle.jpg"]
            },
            "anxiety": {
                "title": "Anxiety Disorders",
                "overview": "Anxiety disorders involve excessive worry or fear that interferes with daily activities. They are the most common mental health concern in the United States.",
                "symptoms": ["Excessive worry", "Restlessness", "Fatigue", "Difficulty concentrating", "Irritability", "Muscle tension", "Sleep disturbances", "Panic attacks"],
                "treatments": ["Cognitive Behavioral Therapy", "Medication", "Mindfulness practices", "Stress management techniques", "Support groups"],
                "ar_visualizations": ["anxiety_response.glb", "calming_techniques.glb"],
                "videos": ["understanding_anxiety.mp4", "coping_strategies.mp4"],
                "infographics": ["anxiety_types.jpg", "stress_response.jpg"]
            },
            "schizophrenia": {
                "title": "Understanding Schizophrenia",
                "overview": "Schizophrenia is a serious mental disorder in which people interpret reality abnormally. It may result in hallucinations, delusions, and extremely disordered thinking.",
                "symptoms": ["Hallucinations", "Delusions", "Disorganized thinking", "Abnormal motor behavior", "Negative symptoms (reduced emotional expression)"],
                "treatments": ["Antipsychotic medications", "Psychosocial interventions", "Coordinated specialty care", "Family support and education"],
                "ar_visualizations": ["neural_pathways.glb", "hallucination_simulation.glb"],
                "videos": ["schizophrenia_explained.mp4", "supporting_loved_ones.mp4"],
                "infographics": ["schizophrenia_facts.jpg", "early_intervention.jpg"]
            },
            "bipolar": {
                "title": "Bipolar Disorder",
                "overview": "Bipolar disorder causes unusual shifts in mood, energy, activity levels, concentration, and the ability to carry out day-to-day tasks.",
                "symptoms": ["Manic episodes", "Depressive episodes", "Mood changes", "Sleep disturbances", "Impulsive behavior", "Racing thoughts", "Grandiose ideas"],
                "treatments": ["Mood stabilizers", "Psychotherapy", "Lifestyle management", "Support networks"],
                "ar_visualizations": ["mood_cycles.glb", "stabilization_techniques.glb"],
                "videos": ["bipolar_explained.mp4", "managing_bipolar.mp4"],
                "infographics": ["bipolar_types.jpg", "mood_tracking.jpg"]
            }
        }
        
        # Assessment questions for personalized learning
        self.assessment_questions = [
            {
                "id": "q1",
                "text": "Which mental health topic are you most interested in learning about?",
                "options": ["Depression", "Anxiety", "Schizophrenia", "Bipolar Disorder", "PTSD", "Other"]
            },
            {
                "id": "q2",
                "text": "What aspect of mental health do you want to understand better?",
                "options": ["Symptoms & Diagnosis", "Treatment Options", "Supporting Others", "Self-Care Strategies", "Science & Research"]
            },
            {
                "id": "q3",
                "text": "How do you prefer to learn new information?",
                "options": ["Reading Articles", "Watching Videos", "Interactive Experiences", "Visual Infographics", "Personal Stories"]
            },
            {
                "id": "q4",
                "text": "What is your primary goal for using this application?",
                "options": ["Personal Education", "Supporting a Loved One", "Professional Development", "Reducing Societal Stigma", "General Interest"]
            }
        ]
        
        # Personal stories for empathy building
        self.personal_stories = [
            {
                "id": "story1",
                "title": "Living with Anxiety - Sarah's Story",
                "person": "Sarah, 32",
                "summary": "Sarah shares her journey of living with generalized anxiety disorder and how she learned to manage it through therapy and mindfulness.",
                "content": "I've always been a worrier, but in my late twenties, it started to take over my life...",
                "ar_elements": {
                    "character_model": "sarah_character.glb",
                    "environment": "calm_park.glb",
                    "interactive_points": [
                        {"title": "First Panic Attack", "position": [0, 1, -3], "content": "I was grocery shopping when suddenly..."},
                        {"title": "Finding Help", "position": [2, 1, -2], "content": "My therapist taught me that anxiety is..."},
                        {"title": "Coping Strategies", "position": [-2, 1, -2], "content": "Deep breathing has become my go-to..."}
                    ]
                },
                "media": ["sarah_photo.jpg", "anxiety_journal.jpg"]
            },
            {
                "id": "story2",
                "title": "My Experience with Depression - Miguel's Journey",
                "person": "Miguel, 45",
                "summary": "Miguel discusses his battle with depression, including his initial resistance to treatment and how he eventually found healing.",
                "content": "For years, I thought I could just 'tough it out' and that asking for help would make me weak...",
                "ar_elements": {
                    "character_model": "miguel_character.glb",
                    "environment": "cozy_home.glb",
                    "interactive_points": [
                        {"title": "Rock Bottom", "position": [0, 1, -3], "content": "I barely got out of bed for weeks..."},
                        {"title": "Reaching Out", "position": [2, 1, -2], "content": "Calling that helpline was the hardest..."},
                        {"title": "Recovery Path", "position": [-2, 1, -2], "content": "Each day got a little brighter..."}
                    ]
                },
                "media": ["miguel_photo.jpg", "support_group.jpg"]
            }
        ]
        
        # Mindfulness exercises
        self.mindfulness_exercises = [
            {
                "id": "mindful1",
                "title": "Grounding Breathing Exercise",
                "duration": "5 minutes",
                "description": "A simple breathing technique to help ground yourself in moments of anxiety or stress.",
                "instructions": "Find a comfortable position. Begin to focus on your breath...",
                "ar_visualization": "breathing_visualization.glb"
            },
            {
                "id": "mindful2",
                "title": "Body Scan Meditation",
                "duration": "15 minutes",
                "description": "A guided meditation that helps you bring awareness to each part of your body.",
                "instructions": "Lie down in a comfortable position. Start by bringing awareness to your toes...",
                "ar_visualization": "body_scan.glb"
            },
            {
                "id": "mindful3",
                "title": "Mindful Walking",
                "duration": "10 minutes",
                "description": "Practice mindfulness while walking to combine mental and physical wellness.",
                "instructions": "Find a quiet place to walk. Begin walking slowly, paying attention to each step...",
                "ar_visualization": "mindful_path.glb"
            }
        ]

    def get_content(self):
        """Return all basic mental health content"""
        return self.content
    
    def get_facts(self):
        """Return mental health facts"""
        return self.content["facts"]
    
    def get_myths(self):
        """Return mental health myths and facts"""
        return self.content["myths"]
    
    def get_resources(self):
        """Return mental health resources"""
        return self.content["resources"]
    
    def get_educational_topics(self):
        """Return all educational topics"""
        return self.educational_topics
    
    def get_topic_content(self, topic_id):
        """Return content for a specific topic"""
        if topic_id in self.educational_topics:
            return self.educational_topics[topic_id]
        return None
    
    def get_assessment_questions(self):
        """Return assessment questions for personalized learning"""
        return self.assessment_questions
    
    def get_personalized_recommendations(self, responses):
        """Generate personalized topic recommendations based on assessment responses"""
        # Simple recommendation logic - in a real app this would be more sophisticated
        recommendations = []
        
        # Extract the user's primary interest from q1
        if "q1" in responses:
            primary_interest = responses["q1"].lower()
            if primary_interest in ["depression", "anxiety", "schizophrenia", "bipolar disorder", "ptsd"]:
                for topic_id, topic in self.educational_topics.items():
                    if primary_interest in topic_id:
                        recommendations.append({
                            "id": topic_id,
                            "title": topic["title"],
                            "overview": topic["overview"],
                            "relevance": "High - Matches your primary interest"
                        })
        
        # Add some secondary recommendations
        for topic_id, topic in self.educational_topics.items():
            if len(recommendations) < 3:  # Ensure we have at least 3 recommendations
                if not any(r["id"] == topic_id for r in recommendations):
                    recommendations.append({
                        "id": topic_id,
                        "title": topic["title"],
                        "overview": topic["overview"],
                        "relevance": "Suggested to broaden your understanding"
                    })
                    
        return recommendations
    
    def get_personal_stories(self):
        """Return all personal stories"""
        return self.personal_stories
    
    def get_story(self, story_id):
        """Return a specific personal story"""
        for story in self.personal_stories:
            if story["id"] == story_id:
                return story
        return None
    
    def get_mindfulness_exercises(self):
        """Return mindfulness exercises"""
        return self.mindfulness_exercises
