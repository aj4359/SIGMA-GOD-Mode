# SIGMA Market Intention Lab — research prototype

**Research only; no real exchange connections or real capital used.**

An initial standard-library Python experiment was built and tested locally on 6 November 2026. It simulates 3,200 time-ordered market periods with behavioural demand, attention, wallet activity, liquidity, hype manipulation, regime changes and occasional crashes. Price-only and market-intention classifiers are trained on the first 60%, validated on the next 20%, and tested on the final 20%. Trading friction is modelled.

### Synthetic holdout test (640 periods)

| Metric | Price-only | Market-intention |
| --- | ---: | ---: |
| Directional accuracy | 42.81% | 65.78% |
| Brier score (lower better) | 0.2624 | 0.2099 |
| Simulated final equity multiple | 0.861x | 1.837x |
| Simulated maximum drawdown | -29.0% | -12.3% |

**These numbers do NOT show a real trading edge.** The synthetic market incorporates the behavioural features into its price-generation rules. A richer model is therefore expected to have an advantage. The model must first be tested against *actual historically timestamped* data without lookahead or survivorship bias. Three local automated tests passed.

### Next acceptance gates

1. Import real timestamped crypto prices/order flow and sentiment, attention, wallet data where legally usable. Preserve arrival times rather than hindsight revisions.
2. Chronological walk-forward testing by asset and market regime; price-only, buy-and-hold and random baselines.
3. Detect false social hype, wash trades and illiquidity; account for fees, slippage, market impact, exchange outages and extreme crashes.
4. Keep all trading in **simulation/paper mode** until independently validated.
5. Build explainable probabilities and scenario ranges, never mystical certainty.

This repository tracks the research programme. Initial runnable source and reports were generated in the ChatGPT conversation; they are not yet committed here.
