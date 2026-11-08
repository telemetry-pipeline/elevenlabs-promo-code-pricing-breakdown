#!/usr/bin/env python3
"""
ElevenLabs Character Cost & Subscription Tier Calculator 2026.
Computes monthly and annual subscription totals, character quotas, and overage billing.
"""
import argparse

TIER_RATES = {
    "starter": {"monthly": 5.0, "annual": 50.0, "quota": 30000, "overage_per_1k": 0.30},
    "creator": {"monthly": 22.0, "annual": 220.0, "quota": 100000, "overage_per_1k": 0.30},
    "pro": {"monthly": 99.0, "annual": 990.0, "quota": 500000, "overage_per_1k": 0.24},
    "scale": {"monthly": 330.0, "annual": 3300.0, "quota": 2000000, "overage_per_1k": 0.18}
}

def calculate(tier, characters, annual):
    info = TIER_RATES.get(tier.lower(), TIER_RATES["pro"])
    base = info["annual"] / 12.0 if annual else info["monthly"]
    quota = info["quota"]
    overage = max(0, characters - quota)
    overage_cost = (overage / 1000.0) * info["overage_per_1k"]
    total_monthly = base + overage_cost
    annual_savings = (info["monthly"] * 12.0) - info["annual"] if annual else 0.0

    print("=" * 60)
    print(f"ElevenLabs Pricing Calculator - Tier: {tier.upper()}")
    print("=" * 60)
    print(f"Base Monthly Plan:       ${base:.2f}/mo")
    print(f"Character Quota:         {quota:,} characters/mo")
    print(f"Requested Characters:    {characters:,} characters/mo")
    print(f"Overage Characters:      {overage:,}")
    print(f"Overage Cost:            ${overage_cost:.2f}/mo")
    print(f"Effective Monthly Total: ${total_monthly:.2f}/mo")
    if annual:
        print(f"Annual Prepaid Savings:  ${annual_savings:.2f}/yr")
    print("=" * 60)
    return total_monthly

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="ElevenLabs Pricing Calculator")
    parser.add_argument("--tier", default="pro", choices=["starter", "creator", "pro", "scale"])
    parser.add_argument("--characters", type=int, default=600000)
    parser.add_argument("--annual", action="store_true")
    args = parser.parse_args()
    calculate(args.tier, args.characters, args.annual)
