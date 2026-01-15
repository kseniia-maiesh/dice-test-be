import random
from main import WINNING_ODDS, check_combination


def roll_dice():
    return [random.randint(1, 6) for _ in range(5)]


def simulate_with_current_odds(num_games):
    total_bets = total_wins = 0
    counts = {"Pair": 0, "Straight": 0, "Full House": 0, "Balut": 0, "None": 0}

    for _ in range(num_games):
        total_bets += 10
        dice = roll_dice()
        combo = check_combination(dice)
        if combo:
            total_wins += 10 * WINNING_ODDS[combo]
            counts[combo] += 1
        else:
            counts["None"] += 1

    return (total_wins / total_bets) * 100, counts


print("=" * 60)
print("VERIFYING CURRENT RTP IN main.py")
print("=" * 60)
print(f"\nCurrent WINNING_ODDS in main.py:")
for combo, odds in WINNING_ODDS.items():
    print(f"  {combo}: {odds}x")

print(f"\nSimulating 1,000,000 games...")
current_rtp, counts = simulate_with_current_odds(1000000)

print(f"\nResults:")
print(f"  Current RTP: {current_rtp:.2f}%")
print(f"  Target RTP: 95.00%")
print(f"  Difference: {current_rtp - 95.0:.2f}%")

print(f"\nCombination frequencies:")
total = sum(counts.values())
for combo, count in counts.items():
    pct = (count / total) * 100
    print(f"  {combo}: {count:,} ({pct:.2f}%)")

if 94.5 <= current_rtp <= 95.5:
    print(f"\nSUCCESS: RTP is approximately 95% (within acceptable range)")
else:
    print(f"\nFAILURE: RTP is {current_rtp:.2f}%, not close to 95%")
