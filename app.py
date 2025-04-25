from flask import Flask, render_template, request, jsonify, session, redirect, url_for
from mental_health import MentalHealthContent
from simulations import SimulationManager
from activities import ActivityManager
from ar_utils import ARProcessor
from ar_education import AREducation
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)  # For session management

# Initialize components
content = MentalHealthContent()
simulation_manager = SimulationManager()
activity_manager = ActivityManager()
ar_processor = ARProcessor()
ar_education = AREducation()

# Home and core routes
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/ar_experience')
def ar_experience():
    return render_template('ar_experience.html')

@app.route('/get_ar_content', methods=['POST'])
def get_ar_content():
    user_input = request.json.get('user_input')
    ar_data = ar_processor.process_input(user_input)
    return jsonify(ar_data)  # Return AR data as JSON

@app.route('/ar_resources')
def ar_resources():
    return render_template('ar_resources.html')

@app.route('/mental_health_content')
def mental_health_content():
    return render_template('mental_health_content.html', content=content.get_content())

# Educational Content Routes
@app.route('/learn')
def learn():
    topics = content.get_educational_topics()
    return render_template('learn.html', topics=topics)

@app.route('/learn/<topic>')
def learn_topic(topic):
    topic_content = content.get_topic_content(topic)
    return render_template('topic_detail.html', topic=topic_content)

# Perspective-Taking and Empathy Building Routes
@app.route('/simulations')
def simulations():
    all_simulations = simulation_manager.get_all_simulations()
    return render_template('simulations.html', simulations=all_simulations)

@app.route('/simulation/<sim_id>')
def run_simulation(sim_id):
    simulation = simulation_manager.get_simulation(sim_id)
    return render_template('simulation_viewer.html', simulation=simulation)

@app.route('/stories')
def stories():
    all_stories = content.get_personal_stories()
    return render_template('stories.html', stories=all_stories)

@app.route('/story/<story_id>')
def view_story(story_id):
    story = content.get_story(story_id)
    return render_template('story_detail.html', story=story)

# Stigma-Busting Activities Routes
@app.route('/activities')
def activities():
    all_activities = activity_manager.get_all_activities()
    return render_template('activities.html', activities=all_activities)

@app.route('/activity/<activity_id>')
def activity_detail(activity_id):
    activity = activity_manager.get_activity(activity_id)
    # Check if activity exists
    if activity is None:
        return render_template('error.html', message="Activity not found"), 404
    
    # Ensure all expected properties exist to prevent template errors
    if activity.get('type') == 'interactive-scenarios' and 'scenarios' not in activity:
        activity['scenarios'] = []
    
    return render_template('activity_detail.html', activity=activity)

@app.route('/scavenger_hunt')
def scavenger_hunt():
    hunt = activity_manager.get_scavenger_hunt()
    return render_template('scavenger_hunt.html', hunt=hunt)

@app.route('/mindfulness')
def mindfulness():
    exercises = content.get_mindfulness_exercises()
    return render_template('mindfulness.html', exercises=exercises)

@app.route('/local_resources')
def local_resources():
    location = request.args.get('location')
    if location:
        # Use the MentalHealthContent class to get local resources
        resources = content.get_local_resources(location) if hasattr(content, 'get_local_resources') else {
            "location": location,
            "message": "No specific resources found for this location.",
            "general_resources": content.get_resources() if hasattr(content, 'get_resources') else []
        }
    else:
        # Fall back to general resources
        resources = {
            "resources": content.get_resources() if hasattr(content, 'get_resources') else []
        }
    return render_template('local_resources.html', resources=resources)

# AR Educational Routes
@app.route('/ar_education')
def ar_education_modules():
    modules = ar_education.get_all_modules()
    return render_template('ar_education.html', modules=modules)

@app.route('/ar_education/<module_id>')
def ar_education_module_detail(module_id):
    module = ar_education.get_module(module_id)
    if module:
        return render_template('ar_module_detail.html', module=module)
    return render_template('error.html', message="Education module not found"), 404

@app.route('/ar_education/<module_id>/<scene_id>')
def ar_education_scene(module_id, scene_id):
    scene = ar_education.get_ar_scene(module_id, scene_id)
    if scene:
        return render_template('ar_education_scene.html', scene=scene, module_id=module_id)
    return render_template('error.html', message="AR scene not found"), 404

@app.route('/ar_conversation/<module_id>')
def ar_conversation_simulator(module_id):
    simulator = ar_education.get_conversation_simulator(module_id)
    if simulator:
        return render_template('ar_conversation_simulator.html', simulator=simulator, module_id=module_id)
    return render_template('error.html', message="Conversation simulator not found"), 404

if __name__ == '__main__':
    app.run(debug=True)