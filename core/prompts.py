"""
core/prompts.py
Prompt Engineering Module for BizSabi AI.

Defines carefully engineered system prompts and task-specific prompt templates.
Ensures zero-hallucination of prices, stock, delivery dates, or policies,
and maintains authentic Nigerian business communication standards.
"""

from typing import Dict, Any, Optional

# System Persona shared across all tasks
SYSTEM_PROMPT = """You are BizSabi AI, an expert digital marketing consultant and professional customer communication assistant built specifically for Nigerian small business owners and micro-enterprises.

YOUR CORE PRINCIPLES:
1. CONTEXTUAL RELEVANCE: Communicate in clear, natural, engaging Nigerian English that resonates with local customers (warm, respectful, polite, and persuasive without unnecessary corporate jargon).
2. STRICT TRUTHFULNESS & GROUNDING:
   - NEVER invent or hallucinate product specifications, prices, discounts, delivery dates, guarantees, certifications, or stock availability.
   - Use the Nigerian Naira symbol (₦) ONLY when a price or budget has been explicitly provided in the input.
   - If essential information (like delivery fees or delivery timeframes) is missing, do NOT guess. Either politely ask the customer for their location or provide a placeholder bracket like '[Insert Delivery Fee]' so the owner can fill it in.
3. ETHICAL MARKETING: Never generate deceptive, spammy, or manipulative claims.
4. ACTIONABLE & READY-TO-USE: Output clean, beautifully formatted text with appropriate emojis, persuasive hooks, and clear Calls to Action (CTAs).
5. EDITABLE DRAFTS: Provide high quality drafts that the business owner can review, edit, and send with confidence.
"""


def build_whatsapp_prompt(business_profile: Dict[str, Any], task_input: Dict[str, Any]) -> str:
    """
    Constructs the prompt for Feature 2: WhatsApp Sales Message Generator.
    Produces both a Short Status Version and a Detailed Broadcast Version.
    """
    focus = task_input.get("focus", "").strip()
    price_offer = task_input.get("price_offer", "").strip()
    message_type = task_input.get("message_type", "WhatsApp Status / Promo")
    custom_cta = task_input.get("custom_cta", "").strip()

    return f"""TASK: Generate high-converting WhatsApp Sales Messages for this Nigerian business.

--- BUSINESS CONTEXT ---
Business Name: {business_profile.get('name', 'N/A')}
Industry: {business_profile.get('industry', 'N/A')}
Location: {business_profile.get('location', 'Nigeria')}
Products/Services: {business_profile.get('products_services', 'N/A')}
Target Customers: {business_profile.get('target_customers', 'N/A')}
Unique Selling Proposition (USP): {business_profile.get('usp', 'N/A')}
Preferred Tone: {business_profile.get('tone', 'Warm & Friendly')}

--- CAMPAIGN DETAILS ---
Message Type: {message_type}
What is being promoted / Focus: {focus}
Price or Special Offer: {price_offer if price_offer else 'None provided (Do NOT make up any price)'}
Specific Call-to-Action requested: {custom_cta if custom_cta else 'Standard WhatsApp call to action (e.g. DM to order)'}

--- INSTRUCTIONS ---
Please generate TWO versions:
1. 🟢 SHORT VERSION (Ideal for WhatsApp Status updates or quick stories):
   - Catchy opening hook with emoji
   - 2-3 concise lines explaining the value
   - Clear Call to Action (e.g., "Tap reply to order", "Send a DM")

2. 🔵 DETAILED VERSION (Ideal for WhatsApp Broadcast lists, promotional groups, or direct 1-on-1 chats):
   - Engaging greeting & hook
   - Bulleted breakdown of key benefits
   - Clear pricing / offer details (ONLY mention prices explicitly stated above)
   - Urgency or ordering instructions
   - Warm sign-off with business name

Formatting requirements: Use WhatsApp bolding with asterisks (*bold*) where appropriate. Keep emojis natural and visually balanced.
"""


def build_product_description_prompt(business_profile: Dict[str, Any], task_input: Dict[str, Any]) -> str:
    """
    Constructs the prompt for Feature 3: Product Description Generator.
    Creates structured, compelling product/service descriptions without fabricating claims.
    """
    product_name = task_input.get("product_name", "").strip()
    product_details = task_input.get("product_details", "").strip()
    target_buyer = task_input.get("target_buyer", "").strip()
    price_info = task_input.get("price_info", "").strip()

    return f"""TASK: Write a compelling, customer-centric Product / Service Description for an online catalog, website, or social media showcase.

--- BUSINESS CONTEXT ---
Business Name: {business_profile.get('name', 'N/A')}
Industry: {business_profile.get('industry', 'N/A')}
Location: {business_profile.get('location', 'Nigeria')}
Preferred Tone: {business_profile.get('tone', 'Professional & Persuasive')}

--- PRODUCT/SERVICE DETAILS ---
Product/Service Name: {product_name}
Raw Details & Specifications: {product_details}
Target Buyer / Who it is for: {target_buyer if target_buyer else business_profile.get('target_customers', 'Everyday customers')}
Price / Package: {price_info if price_info else 'Not provided (Do NOT invent prices)'}

--- INSTRUCTIONS ---
Write a structured, persuasive description containing:
1. 🌟 Headline / Catchy Title: An enticing summary that hooks the ideal buyer.
2. 🔍 What It Is & Why You'll Love It: A brief, captivating overview transforming features into real lifestyle benefits.
3. 💎 Key Highlights / Features: Clean bullet points highlighting why it stands out, based ONLY on the supplied details.
4. 🎯 Who It's Perfect For: Clearly stating who gets the most value from this product or service.
5. 🛒 How To Order / Inquire: A straightforward call-to-action guiding the customer on how to purchase or book.

STRICT RULE: Do NOT fabricate features, battery life, fabric quality, guarantees, or certifications not explicitly provided.
"""


def build_social_media_prompt(business_profile: Dict[str, Any], task_input: Dict[str, Any]) -> str:
    """
    Constructs the prompt for Feature 4: Social Media Caption Generator.
    Customizes format, tone, and hashtags for Instagram, Facebook, TikTok, or WhatsApp Status.
    """
    platform = task_input.get("platform", "Instagram")
    caption_focus = task_input.get("caption_focus", "").strip()
    caption_goal = task_input.get("caption_goal", "Engage & Drive Sales")
    tone_override = task_input.get("tone_override", business_profile.get("tone", "Friendly & Engaging"))

    return f"""TASK: Generate a high-performing {platform} caption for this Nigerian business.

--- BUSINESS CONTEXT ---
Business Name: {business_profile.get('name', 'N/A')}
Industry: {business_profile.get('industry', 'N/A')}
Location: {business_profile.get('location', 'Nigeria')}
Unique Selling Proposition: {business_profile.get('usp', 'N/A')}
Default Brand Tone: {tone_override}

--- POST DETAILS ---
Target Platform: {platform}
Post Topic / Visual Focus: {caption_focus}
Primary Goal of the Post: {caption_goal} (e.g., engagement, sales, educate, booking)

--- PLATFORM GUIDELINES ---
- If Instagram: Strong opening hook in line 1 (before 'see more'), clean spacing, compelling CTA, and 6-9 highly targeted Nigerian hashtags (e.g. #LagosFashion #AbujaBakers #NaijaVendors).
- If Facebook: Conversational storytelling, relatable tone, clear direct CTA.
- If TikTok: Snappy, catchy video caption, punchy hook, trending audio cue suggestion, 4-6 concise hashtags.
- If WhatsApp Status: Short, punchy, emoji-rich, immediate tap-to-reply prompt.

--- INSTRUCTIONS ---
Provide:
1. 🎣 Hook (The first line that stops the scroll).
2. 📝 Caption Body (Engaging storytelling or product highlight).
3. 👉 Clear Call-to-Action (Comment, DM, click link in bio, or WhatsApp).
4. 🏷️ Curated Hashtags (Relevant, tasteful, avoid hashtag spamming).
"""


def build_customer_reply_prompt(business_profile: Dict[str, Any], task_input: Dict[str, Any]) -> str:
    """
    Constructs the prompt for Feature 5: Professional Customer Reply Generator.
    Ensures safe, polite, and unhallucinated replies to customer messages and inquiries.
    """
    scenario = task_input.get("scenario", "General Inquiry")
    customer_message = task_input.get("customer_message", "").strip()
    response_style = task_input.get("response_style", "Polite & Professional")
    known_facts = task_input.get("known_facts", "").strip()

    return f"""TASK: Draft a professional, courteous, and effective reply to a customer message.

--- BUSINESS CONTEXT ---
Business Name: {business_profile.get('name', 'N/A')}
Industry: {business_profile.get('industry', 'N/A')}
Location: {business_profile.get('location', 'Nigeria')}
Products/Services: {business_profile.get('products_services', 'N/A')}

--- CUSTOMER CONVERSATION DETAILS ---
Scenario Type: {scenario}
Customer's Exact Message:
\"\"\"{customer_message}\"\"\"

Desired Response Style: {response_style}
Known Facts / Instructions from Owner:
{known_facts if known_facts else 'None provided. (CRITICAL: Do NOT invent prices, delivery fees, delivery times, or refund promises).'}

--- SAFETY & GROUNDING RULES ---
1. If the customer asks for a price, delivery date, or stock availability that is NOT in the 'Known Facts', do NOT invent numbers. Instead, provide a courteous placeholder like '[Insert price here]' or gently ask the customer for their delivery location / size needed.
2. If handling a complaint: Always acknowledge their feeling politely, apologize for the inconvenience without making unauthorized financial promises, and offer a clear next step (e.g. 'Kindly share your order number so we can resolve this right away').
3. Keep the greeting warm, respectful, and natural for Nigerian customer relations (e.g., 'Hello [Customer Name]', 'Good day', 'Thank you for reaching out to us').

--- OUTPUT FORMAT ---
1. 💬 Recommended Reply: (Ready to copy-paste directly into WhatsApp or Instagram DM).
2. 💡 Note for Business Owner: (A quick tip on what details to confirm or customize before hitting send).
"""

