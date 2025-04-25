/**
 * Main JavaScript file for the Mentally application
 */

document.addEventListener('DOMContentLoaded', function() {
    // Initialize mobile navigation with enhanced functionality
    initMobileNav();
    
    // Initialize tab functionality if present on page
    initTabs();
    
    // Initialize tooltips
    initTooltips();
});

/**
 * Initialize mobile navigation menu with improved animation and accessibility
 */
function initMobileNav() {
    const menuToggle = document.querySelector('.menu-toggle');
    const navMenu = document.querySelector('nav ul');
    
    if (menuToggle && navMenu) {
        // Add aria attributes for accessibility
        menuToggle.setAttribute('aria-expanded', 'false');
        menuToggle.setAttribute('aria-controls', 'navigation-menu');
        navMenu.setAttribute('id', 'navigation-menu');
        
        menuToggle.addEventListener('click', function() {
            const isExpanded = navMenu.classList.contains('active');
            navMenu.classList.toggle('active');
            
            // Update aria-expanded attribute
            this.setAttribute('aria-expanded', isExpanded ? 'false' : 'true');
            
            // Animate hamburger to X with smoother transitions
            const spans = this.querySelectorAll('span');
            if (spans.length === 3) {
                if (navMenu.classList.contains('active')) {
                    spans[0].style.transform = 'rotate(45deg) translate(5px, 5px)';
                    spans[1].style.opacity = '0';
                    spans[2].style.transform = 'rotate(-45deg) translate(5px, -5px)';
                    
                    // Add overlay to darken background when menu is open
                    addMobileOverlay();
                } else {
                    spans[0].style.transform = 'none';
                    spans[1].style.opacity = '1';
                    spans[2].style.transform = 'none';
                    
                    // Remove overlay when menu is closed
                    removeMobileOverlay();
                }
            }
        });
        
        // Close menu when clicking on menu items
        navMenu.addEventListener('click', function(event) {
            if (event.target.tagName === 'A') {
                navMenu.classList.remove('active');
                menuToggle.setAttribute('aria-expanded', 'false');
                
                // Reset hamburger icon
                const spans = menuToggle.querySelectorAll('span');
                spans[0].style.transform = 'none';
                spans[1].style.opacity = '1';
                spans[2].style.transform = 'none';
                
                // Remove overlay
                removeMobileOverlay();
            }
        });
        
        // Close menu when clicking elsewhere
        document.addEventListener('click', function(event) {
            if (!event.target.closest('nav') && !event.target.closest('.menu-toggle') && navMenu.classList.contains('active')) {
                navMenu.classList.remove('active');
                menuToggle.setAttribute('aria-expanded', 'false');
                
                // Reset hamburger icon
                const spans = menuToggle.querySelectorAll('span');
                spans[0].style.transform = 'none';
                spans[1].style.opacity = '1';
                spans[2].style.transform = 'none';
                
                // Remove overlay
                removeMobileOverlay();
            }
        });
        
        // Handle escape key to close menu
        document.addEventListener('keydown', function(event) {
            if (event.key === 'Escape' && navMenu.classList.contains('active')) {
                navMenu.classList.remove('active');
                menuToggle.setAttribute('aria-expanded', 'false');
                
                // Reset hamburger icon
                const spans = menuToggle.querySelectorAll('span');
                spans[0].style.transform = 'none';
                spans[1].style.opacity = '1';
                spans[2].style.transform = 'none';
                
                // Remove overlay
                removeMobileOverlay();
            }
        });
    }
}

/**
 * Add overlay behind mobile menu for better contrast
 */
function addMobileOverlay() {
    // Check if overlay already exists
    if (!document.querySelector('.mobile-overlay')) {
        const overlay = document.createElement('div');
        overlay.className = 'mobile-overlay';
        document.body.appendChild(overlay);
        
        // Animate overlay
        setTimeout(() => {
            overlay.style.opacity = '1';
        }, 10);
    }
}

/**
 * Remove mobile menu overlay
 */
function removeMobileOverlay() {
    const overlay = document.querySelector('.mobile-overlay');
    if (overlay) {
        // Fade out then remove
        overlay.style.opacity = '0';
        setTimeout(() => {
            overlay.remove();
        }, 300);
    }
}

/**
 * Initialize tab functionality on pages that use tabs
 */
function initTabs() {
    const tabButtons = document.querySelectorAll('.tab-btn');
    
    if (tabButtons.length > 0) {
        tabButtons.forEach(button => {
            button.addEventListener('click', function() {
                // Remove active class from all tabs and content
                document.querySelectorAll('.tab-btn').forEach(tab => tab.classList.remove('active'));
                document.querySelectorAll('.tab-content').forEach(content => content.classList.remove('active'));
                
                // Add active class to clicked tab
                this.classList.add('active');
                
                // Show corresponding content
                const tabId = this.getAttribute('data-tab');
                const tabContent = document.getElementById(tabId);
                if (tabContent) {
                    tabContent.classList.add('active');
                }
            });
        });
    }
}

/**
 * Initialize tooltips for elements with data-tooltip attribute
 */
function initTooltips() {
    const tooltipElements = document.querySelectorAll('[data-tooltip]');
    
    if (tooltipElements.length > 0) {
        tooltipElements.forEach(element => {
            element.addEventListener('mouseenter', function() {
                const tooltipText = this.getAttribute('data-tooltip');
                const tooltip = document.createElement('div');
                tooltip.className = 'tooltip';
                tooltip.textContent = tooltipText;
                document.body.appendChild(tooltip);
                
                // Position tooltip
                const rect = this.getBoundingClientRect();
                tooltip.style.left = rect.left + (rect.width / 2) - (tooltip.offsetWidth / 2) + 'px';
                tooltip.style.top = rect.top - tooltip.offsetHeight - 10 + 'px';
                
                // Store tooltip reference
                this.tooltip = tooltip;
            });
            
            element.addEventListener('mouseleave', function() {
                if (this.tooltip) {
                    document.body.removeChild(this.tooltip);
                    this.tooltip = null;
                }
            });
        });
    }
}

// Fix for scroll behavior on hash navigation
if (window.location.hash) {
    const targetElement = document.querySelector(window.location.hash);
    if (targetElement) {
        setTimeout(() => {
            window.scrollTo({
                top: targetElement.offsetTop - 100,
                behavior: 'smooth'
            });
        }, 100);
    }
}

// Add smooth scrolling for anchor links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
        const targetId = this.getAttribute('href');
        if (targetId !== '#') {
            const targetElement = document.querySelector(targetId);
            if (targetElement) {
                e.preventDefault();
                window.scrollTo({
                    top: targetElement.offsetTop - 100,
                    behavior: 'smooth'
                });
            }
        }
    });
});
