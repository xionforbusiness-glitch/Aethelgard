import os
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

# Verify BOM and Margin Calculations
bom = {
    'text_post': 0.01901,
    'carousel_7slide': 0.08950,
    'video_20s': 0.84925,
    'landing_page_min': 0.4482,
    'landing_page_max': 0.7852,
    'whatsapp_conv': 0.03575
}

credit_weights = {
    'text_post': 1,
    'carousel_7slide': 5,
    'video_20s': 25,
    'landing_page': 50
}

# Cost per credit for each deliverable
cost_per_credit = {
    'text_post': bom['text_post'] / credit_weights['text_post'],
    'carousel_7slide': bom['carousel_7slide'] / credit_weights['carousel_7slide'],
    'video_20s': bom['video_20s'] / credit_weights['video_20s'],
    'landing_page_max': bom['landing_page_max'] / credit_weights['landing_page']
}

print("Cost per credit by deliverable:")
for k, v in cost_per_credit.items():
    print(f"  {k}: ${v:.5f} / credit")

worst_case_cogs_per_credit = cost_per_credit['video_20s']
print(f"\nWorst-case COGS per credit (100% video): ${worst_case_cogs_per_credit:.5f}")

# Verify Top-Up packs margin under worst-case
top_ups = [
    ('Starter', 50, 49.00),
    ('Growth', 175, 149.00),
    ('Scale', 450, 349.00),
    ('Enterprise', 1300, 899.00),
    ('Surge Alt 1', 50, 29.00),
    ('Surge Alt 2', 200, 99.00),
    ('Surge Alt 3', 500, 219.00),
    ('Surge Alt 4', 1500, 549.00)
]

print("\nVerifying Top-Up Pack Margins (Requirement: >70%):")
all_top_ups_pass = True
for name, credits, price in top_ups:
    price_per_credit = price / credits
    worst_case_margin = (price_per_credit - worst_case_cogs_per_credit) / price_per_credit * 100
    passes = worst_case_margin > 70.0
    if not passes:
        all_top_ups_pass = False
    print(f"  {name:12} | {credits:5} cr | ${price:6.2f} | ${price_per_credit:.4f}/cr | Worst Margin: {worst_case_margin:.2f}% | Pass: {passes}")

print(f"\nAll Top-Up Packs exceed 70% threshold in worst-case: {all_top_ups_pass}")

# Verify Geo-Launch Weighted Score Formula:
# Geo Score = 0.25 * S_SaaS + 0.20 * S_density + 0.20 * S_social + 0.20 * S_compliance + 0.15 * S_gtm_ease
geo_scores = {
    'US': (9.8, [10, 10, 9.5, 9.5, 10]),
    'UK': (9.1, [9.0, 9.5, 9.0, 9.0, 9.0]),
    'UAE': (8.6, [8.5, 8.5, 9.5, 8.5, 8.0]),
    'Singapore': (8.4, [8.5, 9.0, 8.0, 8.5, 8.0]),
    'Germany': (6.5, [8.5, 8.0, 6.0, 4.0, 6.0])
}

weights = [0.25, 0.20, 0.20, 0.20, 0.15]
print("\nVerifying Geo-Launch Scores:")
for country, (claimed, factors) in geo_scores.items():
    calculated = sum(w * f for w, f in zip(weights, factors))
    diff = abs(claimed - calculated)
    print(f"  {country:10} | Claimed: {claimed:.1f} | Calculated: {calculated:.2f} | Diff: {diff:.2f}")

