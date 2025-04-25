document.addEventListener('DOMContentLoaded', function () {
    const arExperienceContent = document.getElementById('ar-experience-content');
    const arContentDiv = document.getElementById('ar-content');
    const arInfoOverlay = document.getElementById('ar-info-overlay');
    const closeInfoButton = document.getElementById('close-info');
    const continueExploringButton = document.getElementById('continue-exploring');
    const userPromptInput = document.getElementById('user-prompt');
    const arSubmitButton = document.getElementById('ar-submit');
    const suggestionButtons = document.querySelectorAll('.suggestion-buttons .btn');
    const tourButtons = document.querySelectorAll('.start-tour');
    const stopArButton = document.getElementById('stop-ar');

    // --- Configuration: Map topics/tours to AR assets and info ---
    const arExperiencesConfig = {
        "anxiety stigma": {
            type: "single-marker",
            markerUrl: "static/assets/markers/pattern-anxiety-stigma.patt",
            contentHtml: `
                <a-marker preset="custom" type="pattern" url="static/assets/markers/pattern-anxiety-stigma.patt">
                    <a-entity
                        position="0 0.5 0"
                        rotation="-90 0 0"
                        text="value: Anxiety is a medical condition,\nnot a sign of weakness.; color: #ffffff; align: center; width: 2">
                    </a-entity>
                    <a-entity
                        position="0 0 0"
                        rotation="-90 0 0"
                        gltf-model="static/assets/models/brain_activity.glb"
                        scale="0.5 0.5 0.5"
                        animation="property: rotation; to: -90 360 0; loop: true; dur: 10000; easing: linear">
                    </a-entity>
                </a-marker>
                <a-entity camera></a-entity>
            `,
            info: {
                title: "Understanding Anxiety Stigma",
                description: "Anxiety disorders are one of the most common mental health conditions, affecting millions of people. Yet many still face stigma when seeking help.",
                fact: "Nearly 60% of people with anxiety disorders do not receive treatment, with stigma being a significant barrier."
            },
            instructions: "Point your camera at the anxiety stigma marker to see an interactive visualization of anxiety's impact on the brain."
        },
        "depression reality": {
            type: "single-marker",
            markerUrl: "static/assets/markers/pattern-depression.patt",
            contentHtml: `
                <a-marker preset="custom" type="pattern" url="static/assets/markers/pattern-depression.patt">
                    <a-entity
                        position="0 0.3 0"
                        rotation="-90 0 0"
                        gltf-model="static/assets/models/brain_simplified.glb"
                        scale="0.5 0.5 0.5"
                        animation="property: position; to: 0 0.5 0; dir: alternate; dur: 2000; loop: true; easing: easeInOutQuad">
                    </a-entity>
                    <a-entity
                        position="0 0.8 0"
                        rotation="-90 0 0"
                        text="value: Depression affects brain chemistry\nand is not a character flaw.; color: #ffffff; align: center; width: 2">
                    </a-entity>
                </a-marker>
                <a-entity camera></a-entity>
            `,
            info: {
                title: "The Reality of Depression",
                description: "Depression is a complex condition affecting brain chemistry, thought patterns, and emotions. This visualization shows how depression can physically impact brain function.",
                fact: "Depression is the leading cause of disability worldwide, affecting more than 264 million people of all ages."
            },
            instructions: "Point your camera at the depression marker to see how depression affects the brain."
        },
        "breaking stereotypes": {
            type: "multi-marker",
            markers: [
                {
                    markerUrl: "static/assets/markers/pattern-stereotype1.patt",
                    contentHtml: `
                        <a-marker preset="custom" type="pattern" url="static/assets/markers/pattern-stereotype1.patt">
                            <a-entity
                                position="0 0.5 0"
                                rotation="-90 0 0"
                                text="value: 'Mental illness isn't real.'\nHarmful stereotype; color: #ff0000; align: center; width: 2">
                            </a-entity>
                            <a-box position="0 0.2 0" rotation="-90 0 0" color="#ff0000" depth="0.2" height="0.2" width="1.5"></a-box>
                        </a-marker>
                    `
                },
                {
                    markerUrl: "static/assets/markers/pattern-stereotype2.patt",
                    contentHtml: `
                        <a-marker preset="custom" type="pattern" url="static/assets/markers/pattern-stereotype2.patt">
                            <a-entity
                                position="0 0.5 0"
                                rotation="-90 0 0"
                                text="value: Mental illnesses are REAL\nmedical conditions; color: #00ff00; align: center; width: 2">
                            </a-entity>
                            <a-cylinder position="0 0.2 0" rotation="-90 0 0" color="#00ff00" height="0.2" radius="0.5"
                                        animation="property: rotation; to: -90 360 0; loop: true; dur: 5000; easing: linear">
                            </a-cylinder>
                        </a-marker>
                    `
                }
            ],
            info: {
                title: "Breaking Stereotypes",
                description: "Compare harmful stereotypes with the reality of mental health conditions to see how stigma can harm and how accurate information can help.",
                fact: "Stigma causes many people to delay seeking help for an average of 11 years from the onset of mental health symptoms."
            },
            instructions: "This experience uses multiple markers. Start by pointing your camera at the red stereotype marker, then switch to the green reality marker."
        },
        "anxiety visualization": {
            type: "multi-marker",
            markers: [
                {
                    markerUrl: "static/assets/markers/pattern-anxiety-tour1.patt",
                    contentHtml: `
                        <a-marker preset="custom" type="pattern" url="static/assets/markers/pattern-anxiety-tour1.patt">
                            <a-torus-knot position="0 0.5 0" rotation="-90 0 0" color="#aa0000" 
                                        radius="0.5" radius-tubular="0.05" p="2" q="3" segments-tubular="128"
                                        animation="property: rotation; to: -90 360 360; loop: true; dur: 5000; easing: linear">
                            </a-torus-knot>
                            <a-entity
                                position="0 1 0"
                                rotation="-90 0 0"
                                text="value: The tangled, complex nature\nof anxious thoughts; color: #ffffff; align: center; width: 2">
                            </a-entity>
                        </a-marker>
                    `
                },
                {
                    markerUrl: "static/assets/markers/pattern-anxiety-tour2.patt",
                    contentHtml: `
                        <a-marker preset="custom" type="pattern" url="static/assets/markers/pattern-anxiety-tour2.patt">
                            <a-entity 
                                position="0 0.5 0" 
                                rotation="-90 0 0" 
                                text="value: What if...?\nI can't...\nThey think...!; color: #ffff00; align: center; width: 2"
                                animation="property: position; to: 0 0.8 0; dir: alternate; dur: 2000; loop: true; easing: easeInOutQuad">
                            </a-entity>
                            <a-sphere position="0 0.2 0" radius="0.3" color="#ffff00" opacity="0.5"
                                    animation="property: scale; to: 1.2 1.2 1.2; dir: alternate; dur: 1000; loop: true; easing: easeInOutQuad">
                            </a-sphere>
                        </a-marker>
                    `
                }
            ],
            isTour: true,
            info: {
                title: "Understanding Anxiety Visualization",
                description: "This guided tour helps visualize the experience of anxiety through AR visualizations of racing thoughts and physical sensations.",
                fact: "Anxiety disorders are highly treatable, yet only 36.9% of those affected receive treatment."
            },
            instructions: "This is a multi-marker tour. Start with the first marker, then move to the second marker to explore different aspects of anxiety."
        }
    };

    let currentExperienceConfig = null;
    
    // --- Event Listeners ---
    
    // Handle User Prompt Submit
    arSubmitButton.addEventListener('click', function () {
        const userPrompt = userPromptInput.value.trim().toLowerCase();
        if (userPrompt) {
            startARExperience(userPrompt);
        } else {
            alert('Please enter a topic to explore');
        }
    });

    // Handle Suggested Buttons
    suggestionButtons.forEach(button => {
        button.addEventListener('click', function () {
            const topic = this.dataset.topic;
            userPromptInput.value = topic;
            startARExperience(topic);
        });
    });

    // Handle Guided Tour Buttons
    tourButtons.forEach(button => {
        button.addEventListener('click', function () {
            const tour = this.dataset.tour;
            userPromptInput.value = tour;
            startARExperience(tour);
        });
    });

    // Stop AR Experience
    stopArButton.addEventListener('click', function () {
        stopARExperience();
    });

    // Close Info Overlay
    closeInfoButton.addEventListener('click', function () {
        arInfoOverlay.classList.add('hidden');
    });

    // Continue Exploring (within current AR scene)
    continueExploringButton.addEventListener('click', function () {
        arInfoOverlay.classList.add('hidden');
    });

    // --- AR Experience Functions ---

    function startARExperience(topicOrTour) {
        // Show loading state
        arContentDiv.innerHTML = `
            <div class="loading-indicator">
                <div class="loading-spinner"></div>
                <p>Loading AR Experience...</p>
            </div>
        `;
        arContentDiv.classList.remove('hidden');
        arExperienceContent.classList.add('hidden');

        // Find matching AR experience configuration
        currentExperienceConfig = arExperiencesConfig[topicOrTour.toLowerCase()];

        if (currentExperienceConfig) {
            // Create AR scene
            setTimeout(() => {  // Timeout to allow loading indicator to display
                try {
                    createARScene();
                    showARInformation();
                } catch (error) {
                    console.error('Error creating AR scene:', error);
                    arContentDiv.innerHTML = `
                        <div class="error-message">
                            <p>Sorry, there was an error creating the AR experience.</p>
                            <button class="btn secondary" onclick="window.location.reload()">Try Again</button>
                        </div>
                    `;
                }
            }, 500);
        } else {
            // Handle unrecognized topics
            arContentDiv.innerHTML = `
                <div class="error-message">
                    <p>Sorry, we don't have an AR experience for "${topicOrTour}" yet.</p>
                    <p>Please try one of our suggested topics or check back later.</p>
                    <button class="btn secondary" onclick="stopARExperience()">Go Back</button>
                </div>
            `;
        }
    }

    function stopARExperience() {
        arContentDiv.classList.add('hidden');
        arInfoOverlay.classList.add('hidden');
        arExperienceContent.classList.remove('hidden');
        
        // Clean up AR scene
        arContentDiv.innerHTML = '';
        currentExperienceConfig = null;
    }

    function createARScene() {
        if (!currentExperienceConfig) return;

        // Clear previous content first
        arContentDiv.innerHTML = '';

        // Create A-Frame scene with better camera handling
        let sceneHtml = `
            <a-scene embedded arjs="sourceType: webcam; debugUIEnabled: false; detectionMode: mono_and_matrix; cameraParametersUrl: static/assets/camera_para.dat;">
        `;

        if (currentExperienceConfig.type === "single-marker") {
            // Add single marker content
            sceneHtml += currentExperienceConfig.contentHtml;
        } else if (currentExperienceConfig.type === "multi-marker") {
            // Add all markers content
            currentExperienceConfig.markers.forEach(marker => {
                sceneHtml += marker.contentHtml;
            });
        }

        // Adding a custom camera entity with specific setup
        sceneHtml += `
            <a-entity camera></a-entity>
            </a-scene>
        `;

        // Add AR instructions based on the experience type
        const instructionsHtml = `
            <div class="ar-instructions">
                <p>${currentExperienceConfig.instructions}</p>
                <div class="marker-container">
                    <p>Need a marker? Download and print:</p>
                    <a href="static/assets/markers/marker-template.png" download class="marker-download">Download Marker</a>
                </div>
            </div>
        `;

        // Add scene and instructions to AR content div
        arContentDiv.insertAdjacentHTML('beforeend', sceneHtml);
        arContentDiv.insertAdjacentHTML('beforeend', instructionsHtml);
        
        // Ensure we have camera permissions
        if (navigator.mediaDevices && navigator.mediaDevices.getUserMedia) {
            navigator.mediaDevices.getUserMedia({ video: true })
                .catch(function(err) {
                    console.error('Camera access error:', err);
                    arContentDiv.innerHTML = `
                        <div class="error-message">
                            <p>Camera access is required for AR. Please allow camera access and try again.</p>
                            <button class="btn secondary" onclick="window.location.reload()">Try Again</button>
                        </div>
                    `;
                });
        }
    }

    function showARInformation() {
        if (!currentExperienceConfig) return;

        // Populate overlay with information
        document.getElementById('ar-title').textContent = currentExperienceConfig.info.title;
        document.getElementById('ar-description').textContent = currentExperienceConfig.info.description;
        document.getElementById('ar-fact').textContent = currentExperienceConfig.info.fact;

        // Show the info overlay after a delay
        setTimeout(() => {
            arInfoOverlay.classList.remove('hidden');
        }, 2000);
    }

    // Make functions available globally if needed
    window.stopARExperience = stopARExperience;
});
