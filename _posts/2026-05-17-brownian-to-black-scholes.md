---
layout: post
title: From Brownian motion to Black-Scholes
math: true
---

Today I followed a thread from Brownian motion to stochastic calculus to Black-Scholes. Writing it down so I remember the chain.

## Brownian motion

A process $$W_t$$ with independent normal increments:

$$dW_t \sim \mathcal{N}(0, dt)$$

That is the whole object. Random walks in continuous time, with variance that grows like $$t$$.

## Stochastic calculus

Model a stock price as geometric Brownian motion:

$$dS = \mu S \, dt + \sigma S \, dW$$

If you hold a function $$V(t, S)$$ of that price (say, an option), how does $$V$$ move? Itô's lemma:

$$dV = \left( \frac{\partial V}{\partial t} + \mu S \frac{\partial V}{\partial S} + \tfrac{1}{2} \sigma^2 S^2 \frac{\partial^2 V}{\partial S^2} \right) dt + \sigma S \frac{\partial V}{\partial S} \, dW$$

The extra $$\tfrac{1}{2} \sigma^2 S^2 \, \partial^2 V / \partial S^2$$ term is the part that ordinary calculus misses. It comes from $$(dW)^2 = dt$$.

## Black-Scholes

Build a portfolio: long the option, short $$\partial V / \partial S$$ shares of the stock. The $$dW$$ terms cancel exactly. What remains is deterministic, so it must earn the risk-free rate $$r$$. Rearrange and you get the Black-Scholes PDE:

$$\frac{\partial V}{\partial t} + \tfrac{1}{2} \sigma^2 S^2 \frac{\partial^2 V}{\partial S^2} + r S \frac{\partial V}{\partial S} - r V = 0$$

Black-Scholes is a recipe for hedging away the randomness, share by share. Hold $$\Delta = \partial V / \partial S$$ units of the stock at every instant and the option's risk is gone. The price is whatever makes that hedge break even.

## Why this isn't free money

A risk-free portfolio has to earn the risk-free rate $$r$$, otherwise there is arbitrage. The hedged option grows at $$r$$, the same as a treasury bill. The option's price gets set at exactly the level that makes this true. Delta hedging turns a risky position into a boring one that yields the same as cash.

Where money actually gets made:

1. **Mispricing.** If the market sells the option below its Black-Scholes value, you buy it, hedge it, and earn more than $$r$$.
2. **Wrong volatility.** Black-Scholes takes $$\sigma$$ as an input. If you think true volatility is higher than what the market is pricing in, the option is cheap to you. Buy it, delta hedge, and you collect gamma profits as the stock moves around.
3. **Friction.** The model assumes continuous rebalancing with no transaction costs. In practice the hedge leaks, and market makers charge for that leakage.

If the option is fairly priced, you earn $$r$$. Mispriced, you earn $$r$$ plus the mispricing.

## The Greeks

Once you have $$V(t, S)$$, the partial derivatives have names. Each one is a sensitivity you might want to hedge:

- **Delta** $$\Delta = \partial V / \partial S$$: change in option value per dollar of stock. This is the one you hedge with shares.
- **Gamma** $$\Gamma = \partial^2 V / \partial S^2$$: how fast delta changes. Big gamma means you have to rebalance often.
- **Theta** $$\Theta = \partial V / \partial t$$: time decay.
- **Vega** $$\nu = \partial V / \partial \sigma$$: sensitivity to volatility.
- **Rho** $$\rho = \partial V / \partial r$$: sensitivity to the interest rate.

Delta hedging zeros out the first-order risk. The other Greeks tell you what risk is left.

## On the maths and proofs

Don't worry about it :P
