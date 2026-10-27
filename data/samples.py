"""
data/samples.py
Sample Nigerian business profiles and test scenarios for BizAssist AI.
These fictional profiles help non-technical users quickly test all features
without typing everything from scratch.
"""

SAMPLE_BUSINESSES = {
    "Baker (Sweet Crumbs, Abuja)": {
        "name": "Sweet Crumbs Confectionery",
        "industry": "Bakery & Catering",
        "products_services": "Custom birthday cakes, cupcakes, bridal dessert tables, fresh meat pies, and party small chops.",
        "description": "A boutique bakery in Wuse 2, Abuja, crafting freshly baked, visually stunning celebration cakes and pastries.",
        "target_customers": "Party planners, busy parents, brides, and corporate event organizers looking for premium celebration treats.",
        "location": "Wuse 2, Abuja",
        "usp": "Baked fresh on order using 100% real dairy butter, no artificial preservatives, and same-day express delivery for select treats.",
        "tone": "Warm, Friendly & Welcoming",
    },
    "Fashion Designer (Oma Stitches, Lagos)": {
        "name": "Oma Stitches & Couture",
        "industry": "Fashion & Tailoring",
        "products_services": "Bespoke female native wear, ready-to-wear corporate gowns, boubou dresses, and Aso-Ebi tailoring.",
        "description": "Contemporary African fashion brand blending traditional Ankara and crepe fabrics into modern everyday and event styles.",
        "target_customers": "Working-class women, wedding guests, and young stylish professionals aged 22-45 across Lagos and nationwide.",
        "location": "Surulere, Lagos",
        "usp": "Perfect fitting guarantee, neatly finished seams, and 7-day turnaround time for bespoke stitching.",
        "tone": "Polite, Professional & Elegant",
    },
    "Hairdresser (Glitz Beauty, Port Harcourt)": {
        "name": "Glitz Beauty Bar & Salon",
        "industry": "Hair & Beauty",
        "products_services": "Knotless braids, wig revamping, lace frontal installation, pedicures, and natural hair treatments.",
        "description": "Full-service beauty salon offering relaxing haircare experiences and modern protective hairstyles.",
        "target_customers": "Students, working ladies, brides, and mothers who prioritize neat, long-lasting hairstyles and scalp care.",
        "location": "Peter Odili Road, Port Harcourt",
        "usp": "Zero scalp tension, clean and serene environment, with free hair oil treatment for every braiding session.",
        "tone": "Trendy, Friendly & Enthusiastic",
    },
    "Food Vendor (Mama Put Express, Ibadan)": {
        "name": "Mama Put & Grills Express",
        "industry": "Food & Restaurant",
        "products_services": "Smoky party Jollof rice, peppered goat meat (Asun), fried plantain, Egusi soup bowls, and cold Chapman.",
        "description": "Authentic Nigerian fast-casual kitchen serving hot, flavorful local dishes and lunch packs.",
        "target_customers": "Office workers, university students, and families wanting home-style meals delivered fast to their doorstep.",
        "location": "Bodija, Ibadan",
        "usp": "Signature firewood smoky aroma, generous food portions, and fast 45-minute lunch delivery.",
        "tone": "Warm, Energetic & Persuasive",
    },
    "Online Retailer (TechNova Hub, Kano)": {
        "name": "TechNova Gadgets Hub",
        "industry": "Electronics & Mobile Accessories",
        "products_services": "Fast charging power banks, wireless earbuds, ring lights, phone tripods, and smart watches.",
        "description": "Trusted online electronics merchant delivering affordable, authentic mobile phone accessories and creator tools.",
        "target_customers": "Smartphone users, content creators, students, and remote workers who need reliable gadgets.",
        "location": "Farm Centre, Kano (Nationwide Delivery)",
        "usp": "100% original manufacturer warranty, 24-hour dispatch, and pay-on-delivery available in select cities.",
        "tone": "Professional, Direct & Reassuring",
    },
}

# 10 Detailed Capstone Test Scenarios required for verification
TEST_SCENARIOS = [
    {
        "id": 1,
        "business": "Sweet Crumbs Confectionery",
        "feature": "WhatsApp Sales Message",
        "task_input": {
            "focus": "Promoting custom 2-tier whipped cream birthday cakes for weekend parties",
            "price_offer": "Starts at ₦25,000. Book 3 days ahead for free 6-piece cupcake box.",
            "message_type": "WhatsApp Status / Promo",
        },
        "description": "A baker promoting a birthday cake on WhatsApp Status."
    },
    {
        "id": 2,
        "business": "Oma Stitches & Couture",
        "feature": "WhatsApp Sales Message",
        "task_input": {
            "focus": "New 'Elegance Boubou' collection release in silk crepe and rich Ankara prints",
            "price_offer": "₦18,500 each. Free delivery within Lagos for orders of 2 or more.",
            "message_type": "Promotional Broadcast",
        },
        "description": "A fashion designer advertising new clothing."
    },
    {
        "id": 3,
        "business": "Mama Put & Grills Express",
        "feature": "WhatsApp Sales Message",
        "task_input": {
            "focus": "Special Friday Lunch combo: Smoky party jollof, grilled chicken quarter, fried plantain, and chilled drink",
            "price_offer": "₦3,800 per pack. Order cut-off time is 11:30 AM.",
            "message_type": "Individual Customer / Direct Message",
        },
        "description": "A food vendor writing a WhatsApp sales message."
    },
    {
        "id": 4,
        "business": "Glitz Beauty Bar & Salon",
        "feature": "Social Media Caption",
        "task_input": {
            "focus": "Showcasing painless knotless bohemian braids done on natural 4C hair",
            "platform": "Instagram",
            "caption_goal": "Drive booking appointments via WhatsApp DM for the upcoming weekend",
        },
        "description": "A hairdresser creating an Instagram caption."
    },
    {
        "id": 5,
        "business": "TechNova Gadgets Hub",
        "feature": "Product Description",
        "task_input": {
            "product_name": "PowerMax 20,000mAh Ultra-Fast Power Bank",
            "product_details": "22.5W two-way fast charging, LED percentage display, charges 3 devices simultaneously, type-C input/output, pocket-sized metal casing.",
            "target_buyer": "Busy professionals, travelers, and students needing power during outages.",
        },
        "description": "An online retailer describing a tech product."
    },
    {
        "id": 6,
        "business": "Sweet Crumbs Confectionery",
        "feature": "Customer Reply",
        "task_input": {
            "scenario": "Price Enquiry",
            "customer_message": "Hi, how much is your 8-inch chocolate birthday cake? Do you do same-day delivery?",
            "response_style": "Friendly & Informative",
            "known_facts": "8-inch chocolate cake is ₦18,000. Same day delivery requires at least 4 hours notice depending on location.",
        },
        "description": "A customer asking about product prices."
    },
    {
        "id": 7,
        "business": "TechNova Gadgets Hub",
        "feature": "Customer Reply",
        "task_input": {
            "scenario": "Delivery Enquiry",
            "customer_message": "Good day, I stay in Port Harcourt. How many days will it take for my power bank to arrive and how much is shipping?",
            "response_style": "Professional & Reassuring",
            "known_facts": "Interstate delivery to Port Harcourt takes 2-3 business days via GIG Logistics. Delivery fee is ₦3,500.",
        },
        "description": "A customer asking about delivery arrangements."
    },
    {
        "id": 8,
        "business": "Mama Put & Grills Express",
        "feature": "Customer Reply",
        "task_input": {
            "scenario": "Complaint Resolution",
            "customer_message": "I ordered 2 packs of jollof and beef an hour ago. The food just arrived cold and one drink is missing! This is disappointing.",
            "response_style": "Apologetic & Solution-Focused",
            "known_facts": "Apologize sincerely, immediately dispatch the rider with the missing chilled drink and a complimentary dessert, or offer an instant refund for the drink.",
        },
        "description": "A business owner responding politely to a customer complaint."
    },
    {
        "id": 9,
        "business": "Oma Stitches & Couture",
        "feature": "Customer Reply",
        "task_input": {
            "scenario": "Order Acknowledgment",
            "customer_message": "Hello, I just sent ₦37,000 for 2 Boubou dresses to your GTBank account. Receipt attached. When will I get them?",
            "response_style": "Warm & Professional",
            "known_facts": "Payment received with thanks. Production/dispatch takes 3 working days. Tracking info will be sent via WhatsApp.",
        },
        "description": "A business owner acknowledging an order and payment."
    },
    {
        "id": 10,
        "business": "Glitz Beauty Bar & Salon",
        "feature": "Customer Reply",
        "task_input": {
            "scenario": "Follow-up with Interested Customer",
            "customer_message": "I asked about the wig revamping service 3 days ago. Still thinking about it.",
            "response_style": "Gentle, Encouraging & Helpful",
            "known_facts": "Current promo gives 15% off wig washing and deep conditioning if brought in before Saturday.",
        },
        "description": "A business owner following up with an interested customer."
    },
]
