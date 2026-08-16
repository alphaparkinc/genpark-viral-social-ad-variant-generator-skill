from client import ViralSocialAdVariantGeneratorClient

def main():
    client = ViralSocialAdVariantGeneratorClient()
    usp = "Autonomous multi-agent cloud orchestration for developers"
    res = client.generate_ad_variants(usp, "LinkedIn")
    print(f"Predicted CTR Boost: +{res['predicted_ctr_boost_pct']}%")
    print(f"Variants Generated: {res['channel_variants_count']}")
    print("Winning Hook:")
    print(f"\"{res['winning_hook_copy']}\"")

if __name__ == "__main__":
    main()
