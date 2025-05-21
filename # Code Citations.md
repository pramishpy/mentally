# Code Citations

This document contains citations for code segments used in the Mentally application.

## HTML Templates

### Basic HTML Structure
Source: https://github.com/CelineLind/celinelind.github.io/blob/278862eae9c3f0c1ac989f5ae8b50b951b1f7e44/coding/ai/learn.html
License: Unknown
Used in: Multiple template files including learn.html, index.html
Description: Basic HTML5 document structure including DOCTYPE, meta tags, and viewport settings.

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
```

### Flask Template Integration
Source: https://github.com/martincalvert/GAE-Flask/blob/c069b342ac60ea00139b3dd619002bd6f767dec0/templates/layout.html
License: Unknown
Used in: All template files
Description: Integration of Flask's template engine with static file loading.

```html
    <link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">
</head>
<body>
    <header>
        <div class="container">
```

## JavaScript Functions

### Time Formatting Functions
Source: https://github.com/viaacode/avo2-client/blob/2ac5a5804677bd274edc7e0f02d377f0bd64662a/src/shared/helpers/formatters/duration.ts
License: Unknown
Used in: simulation_viewer.html
Description: Functions for formatting time durations.

```javascript
const mins = Math.floor(seconds / 60);
const secs = seconds % 60;
return `${mins.toString().padStart(2, '0')}:${secs.toString().padStart(2, '0')}`;
```

## AR Implementation

### AR.js Integration
Source: https://github.com/valtech-sd/spyglass/blob/480bd900f071c18d980edbf0de6dd6cc5036845a/samples/scenario-1-template/index.html
License: Unknown
Used in: ar_experience.html, simulation_viewer.html
Description: Integration of AR.js library for augmented reality experiences.

```html
<!-- AR.js for marker-based AR -->
<script src="https://raw.githack.com/AR-js-org/AR.js/master/aframe/build/aframe-ar.js"></script>
</head>
<body>
```

## Design Elements

### Basic Layout Components
Source: https://github.com/Tencent/omi/blob/d0328754f34f4b3cda8fd828a9516e86f66a1438/test.html
License: Unknown
Used in: Multiple template files
Description: Basic layout structure for HTML pages.

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
```

## Additional Credits

The Mentally application integrates various open-source libraries and resources:

1. A-Frame - Used for AR experiences (https://aframe.io) - MIT License
2. AR.js - Used for marker-based AR (https://ar-js-org.github.io) - MIT License
3. Leaflet - Used for maps on resource finder (https://leafletjs.com) - BSD-2-Clause License
4. AOS - Used for scroll animations (https://michalsnik.github.io/aos/) - MIT License

All code has been adapted and modified to fit the specific needs of the Mentally application.

