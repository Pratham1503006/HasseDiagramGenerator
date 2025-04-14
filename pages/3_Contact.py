import streamlit as st
import requests

def main():
    st.title("Contact Us")
    
    # Custom CSS
    st.markdown("""
    <style>
        /* Main container and background */
        .main {
            background: linear-gradient(135deg, #1E1E1E, #2D2D2D);
        }
        
        /* Headers */
        h1, h2, h3 {
            background: linear-gradient(90deg, #4a90e2, #357abd);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            font-weight: 700;
            margin-bottom: 1.5rem;
        }
        
        /* Contact form styling */
        .stForm {
            background: rgba(45, 45, 45, 0.7);
            backdrop-filter: blur(10px);
            padding: 2rem;
            border-radius: 15px;
            border: 1px solid rgba(74, 144, 226, 0.3);
            box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
        }
        
        /* Input fields */
        .stTextInput > div > div > input,
        .stTextArea > div > div > textarea,
        .stSelectbox > div > div > div {
            background-color: rgba(30, 30, 30, 0.6) !important;
            border: 1px solid rgba(74, 144, 226, 0.3) !important;
            color: white !important;
            border-radius: 8px !important;
            padding: 12px !important;
            transition: all 0.3s ease;
        }
        
        .stTextInput > div > div > input:focus,
        .stTextArea > div > div > textarea:focus {
            border-color: #4a90e2 !important;
            box-shadow: 0 0 0 2px rgba(74, 144, 226, 0.2) !important;
        }
        
        /* Submit button */
        .stButton > button {
            width: 100%;
            background: linear-gradient(90deg, #4a90e2, #357abd) !important;
            color: white !important;
            border: none !important;
            padding: 15px 30px !important;
            border-radius: 8px !important;
            font-weight: bold !important;
            transition: all 0.3s ease !important;
        }
        
        .stButton > button:hover {
            transform: translateY(-2px);
            box-shadow: 0 4px 12px rgba(74, 144, 226, 0.3) !important;
        }
        
        /* Contact info cards */
        .contact-info-card {
            background: rgba(45, 45, 45, 0.7);
            backdrop-filter: blur(10px);
            padding: 20px;
            border-radius: 10px;
            border: 1px solid rgba(74, 144, 226, 0.3);
            margin-bottom: 20px;
            transition: transform 0.3s ease;
        }
        
        .contact-info-card:hover {
            transform: translateY(-5px);
        }

        /* Icon container */
        .icon-container {
            background: linear-gradient(135deg, #4a90e2, #357abd);
            width: 80px;
            height: 80px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            margin: 0 auto 20px auto;
            font-size: 2.5em;
            color: white;
            box-shadow: 0 4px 15px rgba(74, 144, 226, 0.3);
        }
        
        /* Social media links */
        .social-links {
            display: flex;
            gap: 15px;
            margin-top: 20px;
            justify-content: center;
        }
        
        .social-link {
            background: rgba(74, 144, 226, 0.1);
            color: #4a90e2;
            text-decoration: none;
            padding: 10px 20px;
            border-radius: 20px;
            transition: all 0.3s ease;
            border: 1px solid rgba(74, 144, 226, 0.3);
        }
        
        .social-link:hover {
            background: rgba(74, 144, 226, 0.2);
            transform: translateY(-2px);
        }
        
        /* Footer */
        .footer {
            text-align: center;
            padding: 20px;
            background: rgba(45, 45, 45, 0.7);
            backdrop-filter: blur(10px);
            border-top: 1px solid rgba(74, 144, 226, 0.3);
            margin-top: 50px;
        }
        
        /* Animation classes */
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(20px); }
            to { opacity: 1; transform: translateY(0); }
        }
        
        .animate-fade-in {
            animation: fadeIn 0.8s ease-out forwards;
        }

        /* Stats container */
        .stats-container {
            display: flex;
            justify-content: space-around;
            margin: 30px 0;
            text-align: center;
        }

        .stat-item {
            background: rgba(45, 45, 45, 0.7);
            padding: 15px 25px;
            border-radius: 10px;
            border: 1px solid rgba(74, 144, 226, 0.3);
        }

        .stat-number {
            font-size: 1.8em;
            color: #4a90e2;
            font-weight: bold;
        }

        .stat-label {
            font-size: 0.9em;
            color: #ffffff;
            opacity: 0.8;
        }
    </style>
    """, unsafe_allow_html=True)

    # Main content
    col1, col2 = st.columns([3, 2])

    with col1:
        st.markdown('<div class="animate-fade-in" style="animation-delay: 0.2s">', unsafe_allow_html=True)
        st.header("Get in Touch")
        st.markdown("""
        We're here to help! Whether you have questions about the Hasse Diagram Explorer,
        need technical support, or want to share your feedback, we'd love to hear from you.
        """)
        
        # Contact form with enhanced styling
        with st.form("contact_form", clear_on_submit=True):
            col_name, col_email = st.columns(2)
            with col_name:
                name = st.text_input("Your Name", placeholder="John Doe")
            with col_email:
                email = st.text_input("Your Email", placeholder="john@example.com")
            
            subject = st.selectbox(
                "Subject",
                ["General Inquiry", "Feature Request", "Bug Report", "Feedback", "Other"]
            )
            
            message = st.text_area(
                "Your Message",
                height=150,
                placeholder="Tell us how we can help..."
            )
            
            submitted = st.form_submit_button("Send Message 📤")
            if submitted:
                st.success("✅ Thank you for reaching out! We'll get back to you within 24 hours.")
        st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="animate-fade-in" style="animation-delay: 0.4s">', unsafe_allow_html=True)
        
        # Stats section
        st.markdown("""
        <div class="stats-container">
            <div class="stat-item">
                <div class="stat-number">24/7</div>
                <div class="stat-label">Support</div>
            </div>
            <div class="stat-item">
                <div class="stat-number">1hr</div>
                <div class="stat-label">Avg Response</div>
            </div>
            <div class="stat-item">
                <div class="stat-number">99%</div>
                <div class="stat-label">Satisfaction</div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Contact Information Cards
        st.markdown("""
        <div class="contact-info-card">
            <div class="icon-container">📧</div>
            <h3 style="text-align: center;">Email Support</h3>
            <p style="text-align: center;">support@hassediagramexplorer.com</p>
            <p style="text-align: center;">Response time: Within 24 hours</p>
        </div>
        
        <div class="contact-info-card">
            <div class="icon-container">🕒</div>
            <h3 style="text-align: center;">Office Hours</h3>
            <p style="text-align: center;">Monday - Friday: 9:00 AM - 5:00 PM (EST)</p>
            <p style="text-align: center;">Weekend support available for urgent matters</p>
        </div>
        
        <div class="contact-info-card">
            <div class="icon-container">🌐</div>
            <h3 style="text-align: center;">Connect With Us</h3>
            <div class="social-links">
                <a href="https://twitter.com/hassediagram" class="social-link">Twitter</a>
                <a href="https://github.com/hassediagramexplorer" class="social-link">GitHub</a>
                <a href="https://linkedin.com/company/hassediagramexplorer" class="social-link">LinkedIn</a>
            </div>
        </div>
        """, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    # FAQ Section
    st.markdown('<div class="animate-fade-in" style="animation-delay: 0.6s">', unsafe_allow_html=True)
    st.header("Frequently Asked Questions")
    
    faq_data = [
        ("How do I use the Hasse Diagram Generator?", 
         "Our generator is designed to be intuitive. Simply input your poset relations in the format 'a b' (meaning a ≤ b) and click 'Generate'. The tool will create a visual representation of your Hasse diagram."),
        ("Can I export my generated diagrams?",
         "Yes! You can download your diagrams in various formats including PNG, SVG, and PDF. Look for the download button near your generated diagram."),
        ("Is there a limit to the size of posets?",
         "While there's no strict limit, we recommend keeping your posets to a reasonable size (under 50 elements) for optimal performance and visualization clarity."),
        ("Do you offer premium features?",
         "Currently, all features are available for free. We're working on premium features that will include advanced analysis tools and batch processing capabilities.")
    ]
    
    for question, answer in faq_data:
        with st.expander(question):
            st.write(answer)
    st.markdown('</div>', unsafe_allow_html=True)

    # Footer
    st.markdown("""
    <div class="footer">
        <p>Hasse Diagram Explorer v1.0 | © 2024 All rights reserved</p>
        <p style="font-size: 0.8em;">Made with ❤️ for mathematics enthusiasts</p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
