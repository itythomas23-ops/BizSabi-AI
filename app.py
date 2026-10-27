"""
app.py
BizSabi AI  - Web Application
Streamlit user interface for the 3MTT Meta Generative AI Capstone Project.
"""

import streamlit as st
from core.prompts import (
    SYSTEM_PROMPT,
    build_whatsapp_prompt,
    build_product_description_prompt,
    build_social_media_prompt,
    build_customer_reply_prompt,
)
from core.ai_client import AIClient
from data.samples import SAMPLE_BUSINESSES, TEST_SCENARIOS

# Page configuration
st.set_page_config(
    page_title="BizSabi AI - Small Business Assistant",
    page_icon="💼",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Custom CSS for polished typography and badges
st.markdown(
    """
    <style>
    .main-title {
        font-size: 2.2rem;
        font-weight: 700;
        color: #1E3A8A;
        margin-bottom: 0.2rem;
    }
    .sub-title {
        font-size: 1.1rem;
        color: #4B5563;
        margin-bottom: 1.5rem;
    }
    .badge-live {
        background-color: #DEF7EC;
        color: #03543F;
        padding: 4px 10px;
        border-radius: 9999px;
        font-weight: 600;
        font-size: 0.85rem;
        display: inline-block;
    }
    .badge-demo {
        background-color: #FEF08A;
        color: #713F12;
        padding: 4px 10px;
        border-radius: 9999px;
        font-weight: 600;
        font-size: 0.85rem;
        display: inline-block;
    }
    .result-box {
        background-color: #F9FAFB;
        border-left: 5px solid #2563EB;
        padding: 18px;
        border-radius: 8px;
        margin-top: 15px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Initialize Session State
if "business_profile" not in st.session_state:
    st.session_state.business_profile = SAMPLE_BUSINESSES["Baker (Sweet Crumbs, Abuja)"].copy()

if "generated_result" not in st.session_state:
    st.session_state.generated_result = ""

if "is_live" not in st.session_state:
    st.session_state.is_live = False

if "last_task" not in st.session_state:
    st.session_state.last_task = ""


# ==========================================
# SIDEBAR: Business Profile & API Settings
# ==========================================
with st.sidebar:
    st.header("⚙️ Configuration")

    # API Key Input
    with st.expander("🔑 AI Model & API Key", expanded=False):
        st.markdown(
            "Powered by **Meta Llama 3.3 (70B)** via Groq Cloud. "
            "Get your 100% free key at [console.groq.com/keys](https://console.groq.com/keys)."
        )
        api_key_input = st.text_input(
            "Groq API Key (Optional):",
            type="password",
            placeholder="gsk_...",
            help="Leave empty to test in Demonstration Mode, or enter your key to call live Meta Llama 3.",
        )
        if api_key_input:
            ai_client = AIClient(api_key=api_key_input)
        else:
            ai_client = AIClient()  # Picks up from .env if present, else demo mode

        if ai_client.is_configured():
            st.markdown('<span class="badge-live">🟢 Live Meta Llama 3 Connected</span>', unsafe_allow_html=True)
        else:
            st.markdown('<span class="badge-demo">🟡 Demo Mode (No API key needed)</span>', unsafe_allow_html=True)

    st.markdown("---")
    st.header("🏢 Business Profile")
    st.caption("This information personalizes all generated messages.")

    # Quick Sample Profile Loader
    selected_sample = st.selectbox(
        "Load Sample Nigerian Business:",
        options=["(Custom Profile)"] + list(SAMPLE_BUSINESSES.keys()),
        index=1,  # Default to Baker
        help="Quickly populate the business profile for demonstration.",
    )

    if selected_sample != "(Custom Profile)":
        if st.button("Apply Selected Profile", use_container_width=True):
            st.session_state.business_profile = SAMPLE_BUSINESSES[selected_sample].copy()
            st.rerun()

    # Profile Editing Form
    with st.form("business_profile_form"):
        biz_name = st.text_input("Business Name:", value=st.session_state.business_profile.get("name", ""))
        biz_industry = st.text_input("Industry / Category:", value=st.session_state.business_profile.get("industry", ""))
        biz_location = st.text_input("Location:", value=st.session_state.business_profile.get("location", ""))
        biz_products = st.text_area(
            "Products / Services Offered:",
            value=st.session_state.business_profile.get("products_services", ""),
            height=70,
)
        biz_target = st.text_area(
            "Target Customers:",
            value=st.session_state.business_profile.get("target_customers", ""),
            height=70,
)

        biz_usp = st.text_area(
            "Unique Selling Proposition (USP):",
            value=st.session_state.business_profile.get("usp", ""),
            height=70,
            help="What makes your business special? (e.g. fresh daily, free delivery, neat stitching)",
    )
        biz_tone = st.selectbox(
            "Preferred Brand Tone:",
            options=[
                "Warm, Friendly & Welcoming",
                "Polite, Professional & Elegant",
                "Trendy, Friendly & Enthusiastic",
                "Warm, Energetic & Persuasive",
                "Professional, Direct & Reassuring",
            ],
            index=0,
        )

        update_profile_btn = st.form_submit_button("Save Business Profile", use_container_width=True)
        if update_profile_btn:
            st.session_state.business_profile = {
                "name": biz_name,
                "industry": biz_industry,
                "location": biz_location,
                "products_services": biz_products,
                "target_customers": biz_target,
                "usp": biz_usp,
                "tone": biz_tone,
            }
            st.success("Business Profile updated successfully!")


# ==========================================
# MAIN INTERFACE
# ==========================================
st.markdown('<div class="main-title">💼 BizSabi AI</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="sub-title">Your AI-powered partner for smarter business communication. '
    'Tailored for Nigerian MSMEs, online vendors, and entrepreneurs.</div>',
    unsafe_allow_html=True,
)

# Quick Status Bar
col_stat1, col_stat2, col_stat3 = st.columns([2, 2, 2])
with col_stat1:
    st.info(f"🏢 **Active Business:** {st.session_state.business_profile.get('name', 'Not set')}")
with col_stat2:
    st.info(f"📍 **Location:** {st.session_state.business_profile.get('location', 'Nigeria')}")
with col_stat3:
    if ai_client.is_configured():
        st.success("🤖 **AI Model:** Meta Llama 3.3 (Live)")
    else:
        st.warning("🤖 **AI Model:** Demo Mode (Offline Preview)")


# Feature Selection Tabs
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "📱 WhatsApp Sales Message",
    "🏷️ Product Description",
    "📸 Social Media Caption",
    "💬 Professional Customer Reply",
    "🧪 10 Capstone Test Scenarios",
])


# ------------------------------------------
# TAB 1: WhatsApp Sales Message Generator
# ------------------------------------------
with tab1:
    st.subheader("📱 WhatsApp Sales Message Generator")
    st.caption("Generate high-converting messages for WhatsApp Status, broadcast lists, or direct customer chats.")

    with st.form("whatsapp_form"):
        col_w1, col_w2 = st.columns(2)
        with col_w1:
            msg_type = st.selectbox(
                "Message Format:",
                options=[
                    "WhatsApp Status / Promo",
                    "Promotional Broadcast",
                    "Individual Customer / Direct Message",
                ],
            )
            price_offer = st.text_input(
                "Price or Special Offer (Optional):",
                placeholder="e.g. Starts at ₦25,000 / Buy 2 get free delivery",
                help="Only enter a price if you want it included. BizSabi AI will never invent prices.",
            )
        with col_w2:
            custom_cta = st.text_input(
                "Call to Action (Optional):",
                placeholder="e.g. Reply 'YES' to order, or tap link in bio",
            )
            msg_focus = st.text_area(
                "What are you promoting? (Required):",
                placeholder="e.g. Promoting our fresh 2-tier celebration birthday cakes for weekend orders...",
               height=70,
            )

        generate_wa_btn = st.form_submit_button("🚀 Generate WhatsApp Message", use_container_width=True)

    if generate_wa_btn:
        if not msg_focus.strip():
            st.error("Please specify what you are promoting.")
        else:
            task_input = {
                "message_type": msg_type,
                "price_offer": price_offer,
                "custom_cta": custom_cta,
                "focus": msg_focus,
            }
            with st.spinner("BizSabi AI is crafting your WhatsApp sales message..."):
                prompt = build_whatsapp_prompt(st.session_state.business_profile, task_input)
                result, is_live = ai_client.generate(SYSTEM_PROMPT, prompt)
                st.session_state.generated_result = result
                st.session_state.is_live = is_live
                st.session_state.last_task = "WhatsApp Sales Message"


# ------------------------------------------
# TAB 2: Product Description Generator
# ------------------------------------------
with tab2:
    st.subheader("🏷️ Product & Service Description Generator")
    st.caption("Craft attractive, honest descriptions that highlight benefits without fabricating features.")

    with st.form("product_form"):
        prod_col1, prod_col2 = st.columns(2)
        with prod_col1:
            product_name = st.text_input(
                "Product or Service Name (Required):",
                placeholder="e.g. PowerMax 20,000mAh Fast Power Bank / Bespoke Ankara Gown",
            )
            price_info = st.text_input(
                "Price / Package (Optional):",
                placeholder="e.g. ₦18,500 with nationwide dispatch",
            )
        with prod_col2:
            target_buyer = st.text_input(
                "Who is this ideal for? (Optional):",
                placeholder="e.g. Busy office workers, students, travelers",
            )
            product_details = st.text_area(
                "Features & Raw Details (Required):",
                placeholder="e.g. 22.5W two-way fast charging, LED percentage display, charges 3 devices simultaneously, type-C port...",
                height=70,
            )

        generate_prod_btn = st.form_submit_button("🚀 Generate Product Description", use_container_width=True)

    if generate_prod_btn:
        if not product_name.strip() or not product_details.strip():
            st.error("Please provide both the product name and its key details.")
        else:
            task_input = {
                "product_name": product_name,
                "price_info": price_info,
                "target_buyer": target_buyer,
                "product_details": product_details,
            }
            with st.spinner("BizSabi AI is creating your product description..."):
                prompt = build_product_description_prompt(st.session_state.business_profile, task_input)
                result, is_live = ai_client.generate(SYSTEM_PROMPT, prompt)
                st.session_state.generated_result = result
                st.session_state.is_live = is_live
                st.session_state.last_task = "Product Description"


# ------------------------------------------
# TAB 3: Social Media Caption Generator
# ------------------------------------------
with tab3:
    st.subheader("📸 Social Media Caption Generator")
    st.caption("Generate platform-optimized captions with strong hooks, calls to action, and targeted hashtags.")

    with st.form("social_form"):
        soc_col1, soc_col2 = st.columns(2)
        with soc_col1:
            platform = st.selectbox(
                "Target Social Platform:",
                options=["Instagram", "Facebook", "TikTok", "WhatsApp Status"],
            )
            caption_goal = st.selectbox(
                "Goal of this Post:",
                options=[
                    "Drive Sales & Direct Orders",
                    "Boost Engagement & Comments",
                    "Book Appointments / Slots",
                    "Educate & Build Trust",
                ],
            )
        with soc_col2:
            tone_override = st.selectbox(
                "Caption Tone:",
                options=[
                    "Friendly & Engaging",
                    "Polite, Professional & Classy",
                    "Energetic & Fun (Naija Style)",
                    "Inspirational & Storytelling",
                ],
            )
            caption_focus = st.text_area(
                "Visual Content / Topic of the Post (Required):",
                placeholder="e.g. Showcasing painless knotless bohemian braids on 4C hair with free scalp treatment...",
                height=70,
            )

        generate_soc_btn = st.form_submit_button("🚀 Generate Social Media Caption", use_container_width=True)

    if generate_soc_btn:
        if not caption_focus.strip():
            st.error("Please specify what your post is about.")
        else:
            task_input = {
                "platform": platform,
                "caption_goal": caption_goal,
                "tone_override": tone_override,
                "caption_focus": caption_focus,
            }
            with st.spinner(f"BizSabi AI is generating your {platform} caption..."):
                prompt = build_social_media_prompt(st.session_state.business_profile, task_input)
                result, is_live = ai_client.generate(SYSTEM_PROMPT, prompt)
                st.session_state.generated_result = result
                st.session_state.is_live = is_live
                st.session_state.last_task = f"{platform} Caption"


# ------------------------------------------
# TAB 4: Professional Customer Reply Generator
# ------------------------------------------
with tab4:
    st.subheader("💬 Professional Customer Reply Generator")
    st.caption("Draft respectful, professional customer replies for WhatsApp, DMs, complaints, or inquiries.")

    with st.form("reply_form"):
        rep_col1, rep_col2 = st.columns(2)
        with rep_col1:
            scenario = st.selectbox(
                "Customer Conversation Scenario:",
                options=[
                    "Product / Price Enquiry",
                    "Delivery & Shipping Arrangements",
                    "Order & Payment Acknowledgment",
                    "Complaint Resolution (Polite & Constructive)",
                    "Follow-up with Interested Customer",
                    "Product Unavailable / Out of Stock",
                    "Thank You for Purchase & Review Request",
                ],
            )
            response_style = st.selectbox(
                "Desired Response Style:",
                options=[
                    "Polite & Professional",
                    "Warm & Friendly",
                    "Apologetic & Solution-Focused",
                    "Gentle, Encouraging & Helpful",
                ],
            )
        with rep_col2:
            known_facts = st.text_area(
                "Known Facts / Actual Details (Crucial to prevent guesswork):",
                placeholder="e.g. Price is ₦18,000. Interstate delivery takes 2-3 days via GIG Logistics (₦3,500 fee)...",
                height=70,
                help="Supply true prices, delivery dates, or policies so the AI never has to invent them.",
            )

        customer_message = st.text_area(
            "Customer's Message or Question (Required):",
            placeholder="e.g. Hi, how much is your 8-inch chocolate cake? Can I get it today in Maitama?",
           height=100,
        )

        generate_reply_btn = st.form_submit_button("🚀 Generate Customer Reply", use_container_width=True)

    if generate_reply_btn:
        if not customer_message.strip():
            st.error("Please paste the customer's message or question.")
        else:
            task_input = {
                "scenario": scenario,
                "customer_message": customer_message,
                "response_style": response_style,
                "known_facts": known_facts,
            }
            with st.spinner("BizSabi AI is drafting your professional customer reply..."):
                prompt = build_customer_reply_prompt(st.session_state.business_profile, task_input)
                result, is_live = ai_client.generate(SYSTEM_PROMPT, prompt)
                st.session_state.generated_result = result
                st.session_state.is_live = is_live
                st.session_state.last_task = f"Customer Reply ({scenario})"


# ------------------------------------------
# TAB 5: 10 Capstone Test Scenarios
# ------------------------------------------
with tab5:
    st.subheader("🧪 10 Realistic Capstone Test Scenarios")
    st.caption("Demonstrate the complete versatility of BizSabi AI across 10 distinct Nigerian business situations.")

    selected_test_id = st.selectbox(
        "Choose a Test Scenario to inspect or run:",
        options=[s["id"] for s in TEST_SCENARIOS],
        format_func=lambda x: f"Scenario #{x}: {next(s['description'] for s in TEST_SCENARIOS if s['id'] == x)}",
    )

    current_test = next(s for s in TEST_SCENARIOS if s["id"] == selected_test_id)

    st.markdown(f"**Business Involved:** `{current_test['business']}`")
    st.markdown(f"**Target Feature:** `{current_test['feature']}`")
    st.json(current_test["task_input"])

    if st.button(f"⚡ Execute Scenario #{selected_test_id} Now", use_container_width=True):
        # Match sample business profile
        matched_biz = None
        for key, biz in SAMPLE_BUSINESSES.items():
            if biz["name"].lower() in current_test["business"].lower():
                matched_biz = biz
                break

        if not matched_biz:
            matched_biz = st.session_state.business_profile

        with st.spinner(f"Running Scenario #{selected_test_id}..."):
            feature_name = current_test["feature"]
            t_input = current_test["task_input"]

            if "WhatsApp" in feature_name:
                prompt = build_whatsapp_prompt(matched_biz, t_input)
            elif "Product" in feature_name:
                prompt = build_product_description_prompt(matched_biz, t_input)
            elif "Social" in feature_name:
                prompt = build_social_media_prompt(matched_biz, t_input)
            else:
                prompt = build_customer_reply_prompt(matched_biz, t_input)

            result, is_live = ai_client.generate(SYSTEM_PROMPT, prompt)
            st.session_state.generated_result = result
            st.session_state.is_live = is_live
            st.session_state.last_task = f"Scenario #{selected_test_id} ({current_test['description']})"


# ==========================================
# RESULT DISPLAY & OUTPUT ACTIONS
# ==========================================
if st.session_state.generated_result:
    st.markdown("---")
    res_header_col1, res_header_col2 = st.columns([4, 2])
    with res_header_col1:
        st.subheader(f"📋 Generated Output: {st.session_state.last_task}")
    with res_header_col2:
        if st.session_state.is_live:
            st.markdown('<span class="badge-live">Generated with Live Meta Llama 3.3</span>', unsafe_allow_html=True)
        else:
            st.markdown('<span class="badge-demo">Generated in Demonstration Mode</span>', unsafe_allow_html=True)

    # Clean display
    st.markdown(st.session_state.generated_result)

    # Convenient copy code block
    with st.expander("📄 Raw Text (Click to easily select & copy)", expanded=True):
        st.code(st.session_state.generated_result, language="markdown")

    # Action buttons
    action_col1, action_col2 = st.columns([1, 1])
    with action_col1:
        if st.button("🔄 Clear Output"):
            st.session_state.generated_result = ""
            st.rerun()
    with action_col2:
        st.caption("💡 *Tip: You can edit or tweak any details before posting to WhatsApp or Social Media.*")

