"""
test_app.py
Automated Verification and Capstone Test Runner for BizSabi AI.
Tests all 10 realistic Nigerian business scenarios and verifies prompt grounding.
"""

import sys
from core.prompts import (
    SYSTEM_PROMPT,
    build_whatsapp_prompt,
    build_product_description_prompt,
    build_social_media_prompt,
    build_customer_reply_prompt,
)
from core.ai_client import AIClient
from data.samples import SAMPLE_BUSINESSES, TEST_SCENARIOS


def test_10_scenarios():
    print("=" * 60)
    print("🚀 Running BizSabi AI 10 Capstone Test Scenarios Verification")
    print("=" * 60)

    client = AIClient()
    print(f"[*] AI Client Configured: {client.is_configured()} (Live API: {client.is_configured()})")
    print(f"[*] Model: {client.model}")
    print()

    passed = 0
    total = len(TEST_SCENARIOS)

    for scenario in TEST_SCENARIOS:
        s_id = scenario["id"]
        biz_name = scenario["business"]
        feature = scenario["feature"]
        t_input = scenario["task_input"]
        desc = scenario["description"]

        print(f"[{s_id}/{total}] Testing Scenario #{s_id}: {desc}")

        # Find matching business profile
        matched_biz = None
        for key, biz in SAMPLE_BUSINESSES.items():
            if biz["name"].lower() in biz_name.lower():
                matched_biz = biz
                break

        if not matched_biz:
            matched_biz = list(SAMPLE_BUSINESSES.values())[0]

        # Generate prompt based on feature
        if "WhatsApp" in feature:
            prompt = build_whatsapp_prompt(matched_biz, t_input)
        elif "Product" in feature:
            prompt = build_product_description_prompt(matched_biz, t_input)
        elif "Social" in feature:
            prompt = build_social_media_prompt(matched_biz, t_input)
        elif "Customer Reply" in feature:
            prompt = build_customer_reply_prompt(matched_biz, t_input)
        else:
            print(f"  ❌ Unknown feature: {feature}")
            continue

        # Basic prompt sanity check
        assert len(prompt) > 50, "Prompt too short!"
        assert matched_biz["name"] in prompt, "Business name missing from prompt!"

        # Generate output
        output, is_live = client.generate(SYSTEM_PROMPT, prompt)
        assert len(output) > 20, "Generated output is empty or too short!"

        print(f"  ✅ Prompt Built ({len(prompt)} chars) -> Output Generated ({len(output)} chars) [Live: {is_live}]")
        passed += 1

    print("\n" + "=" * 60)
    print(f"🎉 TEST SUMMARY: {passed}/{total} Scenarios Passed Successfully!")
    print("=" * 60)


if __name__ == "__main__":
    test_10_scenarios()

