"""
core/ai_client.py
Modular AI Client connector for BizAssist AI.

Supports:
1. Groq Cloud (Meta Llama 3.3 70B / Llama 3.1 8B) - Primary free tier choice.
2. Graceful offline/demonstration fallback when no API key is provided,
   ensuring the application never crashes during beginner testing or capstone evaluation.
"""

import os
from typing import Optional, Tuple
from dotenv import load_dotenv

# Load local .env variables if present
load_dotenv()


class AIClient:
    """
    Modular wrapper for Generative AI API calls.
    Allows easy switching of models or providers without touching application UI code.
    """

    def __init__(self, api_key: Optional[str] = None, model: str = "llama-3.3-70b-versatile"):
        self.api_key = api_key or os.getenv("GROQ_API_KEY", "").strip()
        self.model = model
        self.provider = "Groq (Meta Llama 3.3)"

    def is_configured(self) -> bool:
        """Returns True if a non-placeholder API key is available."""
        return bool(self.api_key and not self.api_key.startswith("your_"))

    def generate(self, system_prompt: str, user_prompt: str) -> Tuple[str, bool]:
        """
        Sends the prompts to the Generative AI model and returns (response_text, is_live_api).
        If no API key is configured, provides a high-quality demonstration fallback.
        """
        if self.is_configured():
            try:
                from groq import Groq

                client = Groq(api_key=self.api_key)
                completion = client.chat.completions.create(
                    model=self.model,
                    messages=[
                        {"role": "system", "content": system_prompt},
                        {"role": "user", "content": user_prompt},
                    ],
                    temperature=0.7,
                    max_tokens=1024,
                )
                generated_text = completion.choices[0].message.content
                return generated_text, True

            except Exception as e:
                # Capture and explain errors clearly for beginners
                error_msg = str(e)
                if "authentication" in error_msg.lower() or "api_key" in error_msg.lower():
                    return (
                        "❌ API Key Error: Your Groq API key appears to be invalid or expired. "
                        "Please verify your key at https://console.groq.com/keys and update it in the sidebar or .env file.",
                        False,
                    )
                elif "rate_limit" in error_msg.lower():
                    return (
                        "⚠️ Rate Limit: You have made too many requests in a short period. "
                        "Please wait 30 seconds and try again.",
                        False,
                    )
                else:
                    return f"❌ Connection Error: Unable to reach AI service ({error_msg}). Please check your internet connection.", False

        # Demonstration Fallback Mode when no key has been supplied yet
        demo_response = self._generate_demo_response(user_prompt)
        return demo_response, False

    def _generate_demo_response(self, user_prompt: str) -> str:
        """
        Provides a realistic, structured sample response when the user hasn't set an API key yet.
        Helps beginners preview the app before getting their API key.
        """
        if "WhatsApp Sales Message" in user_prompt:
            return (
                "🟢 *SHORT VERSION (WhatsApp Status / Quick Story)*\n"
                "✨ Craving something sweet and freshly baked? 🎂\n"
                "Treat yourself and your loved ones to our signature custom celebration cakes! Made with 100% real dairy butter and zero preservatives. 🧁\n"
                "👉 Tap reply now to book your weekend slot!\n\n"
                "───────────────────────────────\n\n"
                "🔵 *DETAILED VERSION (Broadcast / Direct Message)*\n"
                "Hello beautiful people! 👋 Are you planning a birthday, anniversary, or special get-together this month? 🎉\n\n"
                "At *Sweet Crumbs Confectionery*, we believe every milestone deserves an unforgettable centerpiece cake:\n"
                "• 🎂 *Ultra-moist & fresh:* Baked from scratch strictly on order\n"
                "• 🧈 *Pure Quality:* 100% real butter, decadent fillings, and no artificial aftertaste\n"
                "• 🎨 *Tailored to you:* Custom designs to match your party theme\n\n"
                "💰 *Special Offer:* Book at least 3 days in advance and receive a complimentary 6-piece cupcake box!\n\n"
                "📲 *How to Order:* Reply directly to this message or send us a WhatsApp DM with your event date and desired flavor. Slots fill up fast, so reserve yours today!\n\n"
                "— *Sweet Crumbs Confectionery, Wuse 2, Abuja*"
            )
        elif "Product / Service Description" in user_prompt or "Product Description" in user_prompt:
            return (
                "🌟 *PowerMax 20,000mAh Ultra-Fast Power Bank — Reliable Power On The Go!*\n\n"
                "🔍 *What It Is & Why You'll Love It*\n"
                "Never get caught stranded with a dead battery again. The PowerMax 20,000mAh combines high-speed 22.5W two-way fast charging with a sleek, pocket-friendly metallic body. Whether you're commuting, working remotely during power outages, or shooting content on the move, this power bank keeps all your essential devices powered throughout the day.\n\n"
                "💎 *Key Highlights:*\n"
                "• ⚡ *22.5W Two-Way Fast Charging:* Rapidly recharges your smartphone and recharges itself quickly.\n"
                "• 🔋 *Triple Device Charging:* Power up to 3 devices simultaneously with dual USB and Type-C outputs.\n"
                "• 📊 *Smart LED Digital Display:* Real-time numeric battery percentage indicator—no guessing remaining charge.\n"
                "• 🛡️ *Durable Metal Housing:* Premium build that resists drops and overheating.\n\n"
                "🎯 *Who It's Perfect For:*\n"
                "Busy professionals, remote workers, students, frequent travelers, and content creators who need dependable, all-day power.\n\n"
                "🛒 *How to Order:*\n"
                "Send us a direct message now with your delivery location to order your authentic PowerMax unit today!"
            )
        elif "Social Media" in user_prompt or "Instagram" in user_prompt:
            return (
                "🎣 *HOOK:*\n"
                "Stop letting bad hair days ruin your plans! ✨ Who else agrees that fresh knotless braids hit different? 😍\n\n"
                "📝 *CAPTION BODY:*\n"
                "Look at this flawless, painless bohemian knotless braid transformation on our gorgeous client! Done with precision on natural 4C hair with ZERO scalp tension. 🙌\n\n"
                "At Glitz Beauty Bar & Salon, your hair health comes first. Every braiding appointment comes with our complimentary herbal scalp oil treatment so your edges stay protected and your style stays fresh for weeks.\n\n"
                "👉 *CALL TO ACTION:*\n"
                "Our weekend calendar is filling up quickly! Click the link in our bio or tap the WhatsApp button to book your braiding slot today.\n\n"
                "🏷️ *TAGS:*\n"
                "#PortHarcourtHair #KnotlessBraidsPH #NaijaHairStylist #ProtectiveStyles #GlitzBeautyBar #PHCityVendors #HealthyHairJourney"
            )
        else:
            return (
                "💬 *RECOMMENDED REPLY:*\n"
                "Hello, thank you for reaching out to us! 😊\n\n"
                "We appreciate your interest in our products. Regarding your enquiry, our 8-inch chocolate birthday cake is ₦18,000.\n\n"
                "For same-day delivery, we typically require at least 4 hours notice to prepare and package your order fresh. Could you kindly let us know your exact delivery location so we can confirm the logistics fee and time for you?\n\n"
                "Looking forward to hearing from you!\n\n"
                "💡 *Note for Business Owner:* Confirm the rider's availability before finalizing the order with the customer."
            )
