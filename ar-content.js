/**
 * Handles AR content creation and interaction for the Mentally application
 */

class ARContentManager {
    constructor() {
        this.sceneCreated = false;
        this.models = {
            anxiety: {
                path: 'anxiety_visualization.glb',
                scale: '0.5 0.5 0.5',
                position: '0 0 -3',
                rotation: '0 0 0'
            },
            depression: {
                path: 'depression_visualization.glb',
                scale: '0.7 0.7 0.7',
                position: '0 0.5 -3',
                rotation: '0 45 0'
            },
            stigma: {
                path: 'breaking_stigma.glb',
                scale: '0.5 0.5 0.5',
                position: '0 0 -2.5',
                rotation: '0 0 0'
            },
            general: {
                path: 'mental_health_awareness.glb',
                scale: '0.6 0.6 0.6',
                position: '0 0.3 -3',
                rotation: '0 30 0'
            }
        };
        
        // Text information to display with models
        this.infoTexts = {
            anxiety: "Anxiety disorders affect 40 million adults in the United States.",
            depression: "Depression is one of the most common mental disorders, affecting over 264 million people worldwide.",
            stigma: "Mental health stigma prevents 60% of people with mental health issues from seeking help.",
            general: "1 in 5 adults experience mental illness each year."
        };
    }
    
    /**
     * Create AR scene based on content type
     * @param {string} contentType - Type of content to display (anxiety, depression, stigma, general)
     * @param {HTMLElement} container - Container element for the AR scene
     */
    createARScene(contentType, container) {
        if (!container) return;
        
        // Clear previous content
        container.innerHTML = '';
        this.sceneCreated = false;
        
        // Default to general if content type doesn't exist
        const modelInfo = this.models[contentType] || this.models.general;
        
        // Create A-Frame scene
        const scene = document.createElement('a-scene');
        scene.setAttribute('embedded', '');
        scene.setAttribute('arjs', 'sourceType: webcam; debugUIEnabled: false;');
        
        // Create marker
        const marker = document.createElement('a-marker');
        marker.setAttribute('preset', 'hiro');
        marker.setAttribute('raycaster', 'objects: .clickable');
        marker.setAttribute('emitevents', 'true');
        marker.setAttribute('cursor', 'fuse: false; rayOrigin: mouse;');
        
        // Create 3D model entity
        const model = document.createElement('a-entity');
        model.setAttribute('gltf-model', `../static/models/${modelInfo.path}`);
        model.setAttribute('scale', modelInfo.scale);
        model.setAttribute('position', modelInfo.position);
        model.setAttribute('rotation', modelInfo.rotation);
        model.setAttribute('class', 'clickable');
        model.setAttribute('animation__rotate', 'property: rotation; to: 0 360 0; loop: true; dur: 15000; easing: linear');
        
        // Create text entity for information
        const infoText = document.createElement('a-text');
        infoText.setAttribute('value', this.infoTexts[contentType] || this.infoTexts.general);
        infoText.setAttribute('position', '0 -1 0');
        infoText.setAttribute('align', 'center');
        infoText.setAttribute('width', '4');
        infoText.setAttribute('color', '#ffffff');
        infoText.setAttribute('font', 'https://cdn.aframe.io/fonts/Exo2Bold.fnt');
        
        // Add event listener to model for interactivity
        model.addEventListener('click', function() {
            // Toggle animation pause/play
            const animState = model.getAttribute('animation__rotate').enabled;
            if (animState) {
                model.setAttribute('animation__rotate', 'enabled', false);
            } else {
                model.setAttribute('animation__rotate', 'enabled', true);
            }
        });
        
        // Assemble the scene
        marker.appendChild(model);
        marker.appendChild(infoText);
        scene.appendChild(marker);
        
        // Add camera
        const camera = document.createElement('a-entity');
        camera.setAttribute('camera', '');
        scene.appendChild(camera);
        
        // Add scene to container
        container.appendChild(scene);
        this.sceneCreated = true;
        
        // Add instructions
        const instructions = document.createElement('div');
        instructions.className = 'ar-instructions';
        instructions.innerHTML = `
            <p>Point your camera at a Hiro marker to view the AR experience.</p>
            <div class="marker-image">
                <img src="../static/images/hiro-marker.png" alt="Hiro Marker">
            </div>
            <p class="hint">Tap on the 3D model to interact with it.</p>
        `;
        container.appendChild(instructions);
        
        return scene;
    }
    
    /**
     * Check if device supports AR capabilities
     * @returns {boolean} Whether device supports AR
     */
    checkARSupport() {
        // Check for WebXR support
        const isWebXRSupported = 'xr' in navigator;
        
        // Check for AR.js compatibility (needs WebGL and camera access)
        const isWebGLSupported = (() => {
            try {
                const canvas = document.createElement('canvas');
                return !!(window.WebGLRenderingContext && 
                    (canvas.getContext('webgl') || canvas.getContext('experimental-webgl')));
            } catch (e) {
                return false;
            }
        })();
        
        // Check for camera access
        const isCameraSupported = 'mediaDevices' in navigator && 'getUserMedia' in navigator.mediaDevices;
        
        return isWebXRSupported || (isWebGLSupported && isCameraSupported);
    }
}
