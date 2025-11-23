"""
Random Password Generator using Streamlit
Author: Surendra Reddy
Enhanced with animations and improved UI/UX
"""

# Import necessary modules
import streamlit as st
import random
import string
import time
from streamlit_player import st_player
from PIL import Image

# Page Configuration
st.set_page_config(
    page_title='Password Generator',
    page_icon="🔑",
    layout="centered",
    initial_sidebar_state="expanded"
)

# Custom CSS for animations
st.markdown("""
<style>
    @keyframes fadeIn {
        from { opacity: 0; }
        to { opacity: 1; }
    }
    @keyframes slideDown {
        from { 
            opacity: 0;
            transform: translateY(-20px);
        }
        to { 
            opacity: 1;
            transform: translateY(0);
        }
    }
    @keyframes pulse {
        0%, 100% { opacity: 1; }
        50% { opacity: 0.7; }
    }
    .main-title {
        animation: slideDown 0.8s ease-out;
        text-align: center;
    }
    .info-box {
        animation: fadeIn 0.6s ease-in;
        padding: 1rem;
        border-radius: 10px;
    }
    .password-output {
        animation: pulse 2s ease-in-out;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 15px;
        border-radius: 8px;
        font-family: monospace;
        font-size: 16px;
    }
    .button-container {
        display: flex;
        justify-content: center;
        margin: 20px 0;
    }
</style>
""", unsafe_allow_html=True)

# Title with animation
st.markdown('<div class="main-title"><h1>🔐 Random Password Generator</h1></div>', unsafe_allow_html=True)

# Load and display image with animation
try:
    image = Image.open('password-generator.jpg')
    st.image(image, caption='🎯 Generate Secure Passwords', use_container_width=True)
except FileNotFoundError:
    st.warning("⚠️ Image file 'password-generator.jpg' not found. Skipping image display.")


# Main content layout with two columns
col1, col2 = st.columns(2)

with col1:
    with st.expander('📺 Demo Video'):
        st.markdown('<div class="info-box">', unsafe_allow_html=True)
        st_player("https://youtu.be/1VkPi33VQ6I")
        st.markdown('</div>', unsafe_allow_html=True)

with col2:
    with st.expander("❓ How Does It Work"):
        st.markdown("""
        <div class="info-box">
        <h4>🎯 Random Password Generator</h4>
        <p>Generate secure passwords using characters, letters, numbers, and symbols.</p>
        
        <h4>📝 Steps:</h4>
        <ol>
            <li>Select the <strong>desired length</strong> of the password (6-34)</li>
            <li>Click the <strong>Generate</strong> button</li>
            <li>Get a <strong>secure random password</strong> instantly</li>
        </ol>
        </div>
        """, unsafe_allow_html=True)

st.markdown("---")

# Password Generator Section
st.markdown("<h3>⚙️ Password Configuration</h3>", unsafe_allow_html=True)

# Configuration columns
config_col1, config_col2 = st.columns([2, 1])

with config_col1:
    input_markdown = "Minimum: 6 | Maximum: 34"
    password_length = int(st.slider(
        'Password Length',
        min_value=6,
        max_value=34,
        value=16,
        help=input_markdown
    ))

# Character set options
with st.expander("🔤 Character Options", expanded=True):
    opt_col1, opt_col2 = st.columns(2)
    
    with opt_col1:
        include_lowercase = st.checkbox("Lowercase (a-z)", value=True)
        include_numbers = st.checkbox("Numbers (0-9)", value=True)
    
    with opt_col2:
        include_uppercase = st.checkbox("Uppercase (A-Z)", value=True)
        include_symbols = st.checkbox("Symbols (!@#$...)", value=True)

st.markdown("---")

# Define character sets
def build_character_set():
    """Build character set based on user selections"""
    charset = ""
    if include_lowercase:
        charset += string.ascii_lowercase
    if include_uppercase:
        charset += string.ascii_uppercase
    if include_numbers:
        charset += string.digits
    if include_symbols:
        charset += string.punctuation
    return charset

# Generate password function with animation
def generate_password_animated(length, charset):
    """Generate password with animated effect"""
    if not charset:
        st.error("❌ Please select at least one character type!")
        return None
    
    if length > len(charset):
        st.warning(f"⚠️ Password length ({length}) is longer than available characters ({len(charset)}). Generating with repeated characters.")
    
    # Generate password
    temp = random.choices(charset, k=length)
    password = "".join(temp)
    return password

# Initialize session state for password
if 'password_result' not in st.session_state:
    st.session_state.password_result = ""
if 'regenerate_count' not in st.session_state:
    st.session_state.regenerate_count = 0

# Generate Button with animation
button_col1, button_col2, button_col3 = st.columns([1, 1, 1])

with button_col2:
    generate_clicked = st.button('✨ Generate Password', key='generate_btn', use_container_width=True)

# Generate password on button click
if generate_clicked:
    charset = build_character_set()
    password_result = generate_password_animated(password_length, charset)
    
    if password_result:
        st.session_state.password_result = password_result
        st.session_state.regenerate_count = 0

# Display password result
if st.session_state.password_result:
    import html
    password_result = st.session_state.password_result
    escaped_password = html.escape(password_result)
    
    # Animated password display
    with st.container():
        st.markdown(f'<div class="password-output">{escaped_password}</div>', unsafe_allow_html=True)
    
    # Text area for easy copying
    st.text_input("📋 Copy Password:", value=password_result, disabled=True, help="Click to select and copy the password")
    
    # Copy and additional actions
    action_col1, action_col2 = st.columns(2)
    
    with action_col1:
        st.info("✅ Password is ready to copy! Select the text above and use Ctrl+C (or Cmd+C on Mac)")
    
    with action_col2:
        if st.button("🔄 Regenerate New Password", key=f'regenerate_btn_{st.session_state.regenerate_count}', use_container_width=True):
            st.session_state.regenerate_count += 1
            charset = build_character_set()
            new_password = generate_password_animated(password_length, charset)
            if new_password:
                st.session_state.password_result = new_password
                st.rerun()

st.markdown("---")

# Share section
with st.expander('🔗 Share This Tool', expanded=False):
    URL = 'https://surendraredd-randompassword.streamlit.app/'
    st.markdown("""
    <div class="info-box">
    <h4>📤 Share with Others</h4>
    <p>Use the link below to share this tool with friends and colleagues.</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.code(URL, language="text")
    
    st.markdown(
        f"""<div style="text-align: center; margin-top: 1rem;">
        <a href="{URL}" target="_blank">
            <button style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
                           color: white; border: none; border-radius: 8px; 
                           padding: 12px 24px; font-size: 16px; font-weight: bold;
                           cursor: pointer; transition: transform 0.2s;">
                🔑 Open Tool
            </button>
        </a>
        </div>""",
        unsafe_allow_html=True
    )
    
    st.markdown("**🚀 Share this link with friends or colleagues!**")

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; margin-top: 2rem; color: #666;">
    <p>🔐 <strong>Generated passwords are random and secure</strong></p>
    <p><small>Built with Streamlit | Password Generator v2.0</small></p>
</div>
""", unsafe_allow_html=True)


