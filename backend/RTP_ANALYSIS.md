# RTP (Return to Player) Analysis

## Question 1: What RTP is achieved with the original odds?

**Original Odds** (from test_rtp_simple.py):
- Pair: **1.5x**
- Straight: **2.0x**
- Full House: **3.0x**
- Balut: **10.0x**

**Answer: The RTP achieved with these odds is approximately 122.75%**

This was calculated by simulating 1,000,000 games. The high RTP (>100%) means players would win more money than they bet on average, which is not sustainable for a casino or game operator.

## Question 2: New odds for 95% RTP

To achieve a target RTP of exactly **95%**, the following odds should be used:

| Combination | Original Odds | New Odds for 95% RTP |
|-------------|--------------|---------------------|
| Pair        | 1.5x         | **1.1609x**         |
| Straight    | 2.0x         | **1.5479x**         |
| Full House  | 3.0x         | **2.3218x**         |
| Balut       | 10.0x        | **7.7394x**         |

### How were these calculated?

The new odds were calculated by applying a scaling factor to the original odds:

```
Scaling Factor = Target RTP / Current RTP = 95.0 / 122.75 = 0.7739
New Odds = Original Odds × Scaling Factor
```

This ensures the theoretical RTP is exactly **95.00%**, which is a standard RTP for casino games.

### Verification

You can verify these calculations by running:
```bash
python test_rtp_simple.py
```

The script simulates 1,000,000 games and shows:
- Current RTP with original odds (~122.75%)
- Adjusted odds for 95% RTP
- Theoretical RTP calculation (exactly 95.00%)

**Note:** Due to randomness in simulation, the verified RTP may vary slightly (e.g., 94.8% - 95.2%), but the theoretical mathematical value is exactly 95%.
