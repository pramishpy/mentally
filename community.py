class CommunityManager:
    """
    Manages community features like resource locator and support networks
    """
    def __init__(self):
        # Sample local resources database
        self.local_resources = {
            "new york": [
                {
                    "name": "NYC Well",
                    "description": "Free, confidential mental health support, crisis intervention, and information and referral service.",
                    "address": "Available 24/7 via phone, text, or chat",
                    "phone": "1-888-NYC-WELL",
                    "website": "https://nycwell.cityofnewyork.us",
                    "services": ["Crisis Intervention", "Peer Support", "Referrals"],
                    "coordinates": [40.7128, -74.0060]
                },
                {
                    "name": "National Alliance on Mental Illness (NAMI) NYC",
                    "description": "Provides support groups, education programs, and advocacy for people with mental illness.",
                    "address": "505 Eighth Avenue, Suite 1103, New York, NY 10018",
                    "phone": "(212) 684-3264",
                    "website": "https://www.naminycmetro.org",
                    "services": ["Support Groups", "Education", "Advocacy"],
                    "coordinates": [40.7535, -73.9922]
                }
            ],
            "los angeles": [
                {
                    "name": "Los Angeles County Department of Mental Health",
                    "description": "Provides mental health services to those in need throughout LA County.",
                    "address": "550 S. Vermont Avenue, Los Angeles, CA 90020",
                    "phone": "(800) 854-7771",
                    "website": "https://dmh.lacounty.gov",
                    "services": ["Clinical Services", "Crisis Response", "Rehabilitation"],
                    "coordinates": [34.0631, -118.2912]
                },
                {
                    "name": "Open Path Psychotherapy Collective",
                    "description": "Affordable psychotherapy for individuals, couples, and families in need.",
                    "address": "Available throughout Los Angeles",
                    "phone": "N/A - Online resource",
                    "website": "https://openpathcollective.org",
                    "services": ["Affordable Therapy", "Mental Health Referrals"],
                    "coordinates": [34.0522, -118.2437]
                }
            ]
        }
        
        # Featured resources (non-location specific)
        self.featured_resources = [
            {
                "name": "Crisis Text Line",
                "description": "24/7 crisis support via text message.",
                "contact": "Text HOME to 741741",
                "website": "https://www.crisistextline.org",
                "services": ["Crisis Support", "Referrals"]
            },
            {
                "name": "National Suicide Prevention Lifeline",
                "description": "24/7, free and confidential support for people in distress.",
                "contact": "1-800-273-8255",
                "website": "https://suicidepreventionlifeline.org",
                "services": ["Crisis Support", "Mental Health Services"]
            },
            {
                "name": "Psychology Today Therapist Finder",
                "description": "Search for therapists in your area who match your needs and preferences.",
                "contact": "N/A - Online resource",
                "website": "https://www.psychologytoday.com/us/therapists",
                "services": ["Therapist Directory", "Mental Health Information"]
            }
        ]
        
        # Community support groups
        self.virtual_support_groups = [
            {
                "id": "group1",
                "name": "Anxiety Support Circle",
                "description": "Weekly virtual meetup for people managing anxiety.",
                "meeting_time": "Wednesdays, 7:00 PM EST",
                "facilitator": "Dr. Sarah Johnson",
                "max_participants": 12,
                "current_participants": 8,
                "upcoming_topics": ["Coping with Work Anxiety", "Managing Physical Symptoms", "Supporting Loved Ones"]
            },
            {
                "id": "group2",
                "name": "Depression Recovery Group",
                "description": "Supportive community for those navigating depression.",
                "meeting_time": "Mondays, 6:30 PM EST",
                "facilitator": "Michael Chen, LCSW",
                "max_participants": 10,
                "current_participants": 7,
                "upcoming_topics": ["Building a Self-Care Routine", "Communicating with Family", "Managing Low Energy"]
            }
        ]
    
    def get_community_data(self):
        """Return general community data"""
        return {
            "support_groups": self.virtual_support_groups,
            "featured_resources": self.featured_resources
        }
    
    def get_local_resources(self, location):
        """Return mental health resources for a specific location"""
        location_lower = location.lower()
        if location_lower in self.local_resources:
            return {
                "location": location,
                "resources": self.local_resources[location_lower]
            }
        return {
            "location": location,
            "resources": [],
            "message": "No specific resources found for this location. Please consider these general resources:",
            "general_resources": self.featured_resources
        }
    
    def get_featured_resources(self):
        """Return featured (non-location specific) mental health resources"""
        return {
            "resources": self.featured_resources
        }
    
    def get_support_groups(self):
        """Return virtual support groups"""
        return self.virtual_support_groups
