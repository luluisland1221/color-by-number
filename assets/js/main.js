// Mobile Navigation Toggle
const hamburger = document.querySelector('.hamburger');
const navMenu = document.querySelector('.nav-menu');

hamburger.addEventListener('click', () => {
    navMenu.classList.toggle('active');
    
    // Animate hamburger
    hamburger.classList.toggle('active');
});

// Close mobile menu when clicking on a link
document.querySelectorAll('.nav-menu a').forEach(link => {
    link.addEventListener('click', () => {
        navMenu.classList.remove('active');
        hamburger.classList.remove('active');
    });
});

// Newsletter Form Handling
const newsletterForm = document.querySelector('.newsletter-form');
if (newsletterForm) {
    newsletterForm.addEventListener('submit', async (e) => {
        e.preventDefault();
        
        const email = e.target.querySelector('input[type="email"]').value;
        const button = e.target.querySelector('button');
        const originalText = button.textContent;
        
        // Show loading state
        button.innerHTML = '<span class="loading"></span> Subscribing...';
        button.disabled = true;
        
        try {
            // Here you would integrate with your email service
            // For now, we'll simulate an API call
            await new Promise(resolve => setTimeout(resolve, 1500));
            
            // Show success message
            showNotification('Thank you for subscribing! Check your email for confirmation.', 'success');
            e.target.reset();
            
        } catch (error) {
            showNotification('Something went wrong. Please try again.', 'error');
        } finally {
            button.textContent = originalText;
            button.disabled = false;
        }
    });
}

// Smooth Scrolling for Anchor Links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            target.scrollIntoView({
                behavior: 'smooth',
                block: 'start'
            });
        }
    });
});

// Lazy Loading Images
const images = document.querySelectorAll('img[loading="lazy"]');
const imageObserver = new IntersectionObserver((entries, observer) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            const img = entry.target;
            img.src = img.dataset.src || img.src;
            img.classList.remove('lazy');
            observer.unobserve(img);
        }
    });
});

images.forEach(img => imageObserver.observe(img));

// Download Button Tracking
function trackDownload(filename, category) {
    // Track download for analytics
    console.log(`Download tracked: ${filename} from ${category}`);
    
    // Here you would integrate with your analytics service
    // Example: gtag('event', 'download', { filename, category });
}

// Add event listeners to download buttons
document.querySelectorAll('.download-btn').forEach(btn => {
    btn.addEventListener('click', (e) => {
        const filename = btn.dataset.filename || 'unknown';
        const category = btn.dataset.category || 'unknown';
        trackDownload(filename, category);
    });
});

// Notification System
function showNotification(message, type = 'info') {
    const notification = document.createElement('div');
    notification.className = `notification notification-${type}`;
    notification.textContent = message;
    
    // Add styles
    Object.assign(notification.style, {
        position: 'fixed',
        top: '20px',
        right: '20px',
        padding: '1rem 2rem',
        borderRadius: '8px',
        color: 'white',
        fontWeight: '600',
        zIndex: '10000',
        transform: 'translateX(100%)',
        transition: 'transform 0.3s ease',
        boxShadow: '0 4px 12px rgba(0,0,0,0.15)'
    });
    
    // Set colors based on type
    const colors = {
        success: '#4caf50',
        error: '#f44336',
        info: '#2196f3',
        warning: '#ff9800'
    };
    
    notification.style.backgroundColor = colors[type] || colors.info;
    
    document.body.appendChild(notification);
    
    // Animate in
    setTimeout(() => {
        notification.style.transform = 'translateX(0)';
    }, 100);
    
    // Remove after 4 seconds
    setTimeout(() => {
        notification.style.transform = 'translateX(100%)';
        setTimeout(() => {
            document.body.removeChild(notification);
        }, 300);
    }, 4000);
}

// Search Functionality
function initializeSearch() {
    const searchInput = document.querySelector('.search-input');
    const searchResults = document.querySelector('.search-results');
    
    if (!searchInput || !searchResults) return;
    
    let searchTimeout;
    
    searchInput.addEventListener('input', (e) => {
        clearTimeout(searchTimeout);
        const query = e.target.value.trim().toLowerCase();
        
        searchTimeout = setTimeout(() => {
            if (query.length > 2) {
                performSearch(query);
            } else {
                searchResults.innerHTML = '';
                searchResults.classList.add('hidden');
            }
        }, 300);
    });
}

function performSearch(query) {
    // This would connect to your search API
    const mockResults = [
        { title: 'Lion Color by Number', url: '/color-by-number/animals/lion.html', category: 'Animals' },
        { title: 'Christmas Tree Color by Number', url: '/color-by-number/holidays/christmas-tree.html', category: 'Holidays' }
    ].filter(item => item.title.toLowerCase().includes(query));
    
    displaySearchResults(mockResults);
}

function displaySearchResults(results) {
    const searchResults = document.querySelector('.search-results');
    
    if (results.length === 0) {
        searchResults.innerHTML = '<p>No results found</p>';
    } else {
        searchResults.innerHTML = results.map(result => `
            <div class="search-result-item">
                <a href="${result.url}">
                    <h4>${result.title}</h4>
                    <span class="category-tag">${result.category}</span>
                </a>
            </div>
        `).join('');
    }
    
    searchResults.classList.remove('hidden');
}

// Print Functionality
function setupPrintButtons() {
    document.querySelectorAll('.print-btn').forEach(btn => {
        btn.addEventListener('click', () => {
            window.print();
        });
    });
}

// Newsletter Popup (optional)
function setupNewsletterPopup() {
    if (localStorage.getItem('newsletterPopupShown')) return;
    
    setTimeout(() => {
        showNewsletterPopup();
        localStorage.setItem('newsletterPopupShown', 'true');
    }, 30000); // Show after 30 seconds
}

function showNewsletterPopup() {
    const popup = document.createElement('div');
    popup.className = 'newsletter-popup';
    popup.innerHTML = `
        <div class="popup-content">
            <span class="close-popup">&times;</span>
            <h3>Get Free Printables!</h3>
            <p>Join our newsletter and get the latest free color by number worksheets delivered to your inbox.</p>
            <form class="popup-newsletter-form">
                <input type="email" placeholder="Enter your email" required>
                <button type="submit">Subscribe</button>
            </form>
        </div>
    `;
    
    // Add styles
    Object.assign(popup.style, {
        position: 'fixed',
        top: 0,
        left: 0,
        width: '100%',
        height: '100%',
        backgroundColor: 'rgba(0,0,0,0.5)',
        display: 'flex',
        justifyContent: 'center',
        alignItems: 'center',
        zIndex: '10000'
    });
    
    document.body.appendChild(popup);
    
    // Close popup
    popup.querySelector('.close-popup').addEventListener('click', () => {
        document.body.removeChild(popup);
    });
    
    popup.addEventListener('click', (e) => {
        if (e.target === popup) {
            document.body.removeChild(popup);
        }
    });
    
    // Handle form submission
    popup.querySelector('.popup-newsletter-form').addEventListener('submit', (e) => {
        e.preventDefault();
        showNotification('Thank you for subscribing!', 'success');
        document.body.removeChild(popup);
    });
}

// Initialize all functionality
document.addEventListener('DOMContentLoaded', () => {
    initializeSearch();
    setupPrintButtons();
    
    // Uncomment to enable newsletter popup
    // setupNewsletterPopup();
});

// Performance monitoring
if ('performance' in window) {
    window.addEventListener('load', () => {
        const loadTime = performance.timing.loadEventEnd - performance.timing.navigationStart;
        console.log(`Page load time: ${loadTime}ms`);
    });
}

// Service Worker registration (for PWA support)
if ('serviceWorker' in navigator) {
    window.addEventListener('load', () => {
        navigator.serviceWorker.register('/sw.js')
            .then(registration => console.log('SW registered'))
            .catch(registrationError => console.log('SW registration failed'));
    });
}

// Export functions for testing
if (typeof module !== 'undefined' && module.exports) {
    module.exports = {
        showNotification,
        trackDownload,
        performSearch
    };
}