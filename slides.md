---
layout: cover
class: text-center
title: Who Survives AI ?
#theme: academic
titleTemplate: '%s'
favicon: ./images/defiicon.png
author: Fayçal Drissi
themeConfig:
  paginationX: disabled
  paginationY: disabled
  paginationPagesDisabled: [1]
fonts:
  local: Montserrat, Roboto Mono, Roboto Slab # local fonts are used for legal reasons for deployment to https://slidev-theme-academic.alexeble.de and only set up for the example project, remove this line for your project to automatically have fonts imported from Google

theme: frankfurt
infoLine: true # on by default, can be turned off
#author: 'Your name here' # shows in infoLine
#title: 'Title' # shows in infoLine
date: '26/06/2026' # shows in infoLine, defaults to the current date

mdc: true
---


<br>

# Who Survives AI ?

## Fayçal Drissi

### *University of Oxford*
<br>

### joint work with Fahad Saleh (University of Florida)

<!--These slides: [https://www.faycaldrissi.com/siam2025](https://www.faycaldrissi.com/siam2025)
[my scholar](https://scholar.google.com/citations?user=njvyriQAAAAJ&hl=fr), 
[my website](https://www.faycaldrissi.com/), [my github](https://github.com/FDR0903)-->


---
section: AI economy
---

# "Wrapper" AI companies

### Startups that do not train their own models

- they are on top of foundation models (GPT, Claude)
- they add prompts, workflows, and integrations to offer a full specialized product
- easiest way for many people to experience generative AI for the first time

<br>

<v-click>

### Evidence

- **coding**: Windsurf and Cursor replaced by integrated offerings (OpenAI Codex, Anthropic's Claude Code, Google's Jules)

<v-click>

- **design**: Anthropic launched products against their own customers (Figma)

<v-click>

- others: **science, security, law, financial analysis**

<v-click>

<br>

$\implies$ a firm which relies exclusively on an AI model has a competitive edge that the model supplier can reproduce easily

</v-click>
</v-click>
</v-click>
</v-click>

---

# Models learn from usage

### RLHF: the new standard approach for aligning LLMs with human preferences

- InstructGPT (Ouyang et al., 2022)<br>
user-submitted prompts from the OpenAI API + human rankings $\to$ reward model $\to$ fine-tuning
- real user behavior and feedback are central to improving the model

<br>

<v-click>

### Multi-turn RLHF (2024): alignment over entire conversations, not individual turns

- models internalize the scope of discussions, workflows, and their next steps (GPT-5, recent iterations of Claude Code)

<br>

<v-click>

### Training on usage is now the default

- Anthropic (August 2025): consumer chats and coding sessions train the models
- a continuous learning loop

<v-click>

- July 2026: Claude Cowork: record your screen while you do a task, talk through it as you go, and Claude turns it into a skill it can run again

</v-click>
</v-click>
</v-click>


---

# What firms give away

<v-click>

### Firms can protect themselves ...

- contracts: enterprise no-training clauses, Zero Data Retention (ZDR), Data Processing Agreements (DPA)

<br>

<v-click>

### ... but there are always leaks

- routing proprietary data, operating procedures, and processes through black boxes
<v-click>

- incentives to improve models (OpenAI / Google)
<v-click>

- "Shadow AI": 
  - employees using unapproved AI tools: creates major risks of sensitive data leaks
  - April 2026: Samsung employees leak internal meeting notes and source code into ChatGPT $\implies$ many companies (JPMorgan, Verizon) block AI chatbots from corporate systems
<v-click>

- June 2026: pharmaceutical companies restrict or completely ban AI with their proprietary R&D and clinical data

<v-click>

<br>

$\implies$ the model learns from what firms do with the model



</v-click>
</v-click>
</v-click></v-click>
</v-click>
</v-click>


---

# Providers become specialised

### The economics of AI favor providers moving up the stack

- selling API tokens: a low-margin, volume-driven business
- domain-specific solutions: offer higher margins +  ownership of customer value

<v-click>

<br>

### Evidence

- OpenAI:
  - **Jobs Platform** & AI-driven hiring and matchmaking
- Anthropic: 
  - **Claude for Financial Services** (Bloomberg, S&P integrations)

<v-click>

<br>

$\implies$ the option to enter customers' markets is being exercised

</v-click>
</v-click>



---

# Motivation

### Summary

-  AI models are an input that a growing share of production needs
- providers sell that input, and price it unilaterally
-  **AI models learn from their customers' usage** of the model
- they hold an **option to enter their customers' markets**


<v-click>

<br>

$\implies$ AI / firms relationship shapes **growth and incentives to create** $\implies$ important to study


<v-click>
<br>

$\implies$ **this paper**: a model of the relationship


</v-click>

</v-click>

---
section: Model
---

# The model

### An AI-based economy: two strategic players, and demand for a product

<v-click>

**1. A firm** 
- the firm sells a product to buyers
- the firm has a **private competitive advantage** in the market
- producing the product requires the provider's AI model **tokens** 

<br>

<v-click>

**2. An AI model provider** 
- provider sells tokens to the firm
- it holds the option to enter, competitively, the firm's market

<br>

<v-click>

**3. Buyers** 
- buyers purchase the product from the firm
- if the provider enters the firm's market, buyers can also purchase from the provider

</v-click>
</v-click>
</v-click>

---

# The firm

- the firm sells a product that requires an AI model

<v-click>

- it holds a **private advantage** $x(t) \geq 0$ that the provider cannot (yet) reproduce (proprietary data, workflows, know-how)

<v-click>

- buyers value the advantage: they buy the product at
  $$
  D\big(Q(t)\big) + x(t)
  $$

  - $D(\cdot)$ is an inverse demand function
  -  $Q(t)$ the available quantity of product at $t$
<v-click>

<br>

- if $Q(t)$ includes the provider's product $\implies$ the firm sells less, at a lower price

</v-click>
</v-click>
</v-click>

---

# The firm's advantage

- the advantage evolves through two forces, creation and absorption:

  $$
  dx(t) = \Big( \underbrace{\iota(t)}_{\text{innovation effort}} \; - \underbrace{\lambda\, \tau_F(t)\, x(t)}_{\text{absorption}} \ \ \ \Big)\, dt \; + \underbrace{\sigma\, x(t) \sqrt{\tau_F(t)}\; dW(t)}_{\text{risk}}
  $$

  - $\lambda > 0$ is the absorption speed per token 
  - $\tau_F(t) \geq 0$ is the firm's token usage
<br>


<v-click>
<br>

- without innovation ($\iota = 0$):

$$
x(t) = x(0)\, \exp\!\Big(\! -\big(\lambda + \tfrac{\sigma^2}{2}\big) \int_0^t \tau_F(s)\, ds \; + \; \sigma \int_0^t \sqrt{\tau_F(s)}\; dW(s) \Big)
$$

$\implies$ the advantage decays with **cumulative usage**

</v-click>


---

# The firm's production

- the firm owns an infrastructure stock $S_F$

$$
dS_F(t) = \Big( \underbrace{I_F(t)}_{\text{investment}} - \underbrace{\delta\, S_F(t)}_{\text{depreciation}} \Big)\, dt
$$

<v-click>

- **production technology:** the firm produces with tokens $\tau_F$ and with the stock $S_F$ (**constant elasticity of substitution**):

  $$
  q_F = G(\tau_F, S_F) = \Big[ \omega\, \tau_F^{\theta} + (1-\omega)\, S_F^{\theta} \Big]^{1/\theta}
  $$

  <v-click>

  - the elasticity of substitution between tokens and stock is $\varsigma = 1/(1-\theta)$: increasing in $\theta$
    - if $\theta > 0$: each input can produce without the other ($\theta = 1$: perfect substitutes)
    - if $\theta \leq 0$: both inputs are essential ($\theta \to -\infty$: fixed proportions)

  </v-click>
</v-click>

---

# The firm's problem

<v-click>

- producing has costs
  - tokens cost the price $p$ per unit
  - investment cost $h_F(I_F(t))$: increasing, convex
  - innovation cost $\kappa(\iota(t))$: strictly convex

<v-click>

<br>

- the firm has instantaneous profit:

$$
\pi_F = \underbrace{\big[ D(Q) + x \big]\, q_F}_{\text{revenue at the premium}} \; - \underbrace{p\, \tau_F}_{\text{token bill}} \; - \underbrace{h_F(I_F)}_{\text{investment}} \; - \underbrace{\kappa(\iota)}_{\text{innovation}}
$$

<br>

<v-click>

- the firm maximizes

$$
\max_{\tau_F,\; I_F,\; \iota} \;\; \mathbb{E}\left[ \int_0^\infty e^{-r_F\, t}\, \pi_F(t)\, dt \right]
$$

</v-click>

</v-click>

</v-click>

---

# The AI model provider

- the provider sells tokens to the firm
  - it posts the token price $p(t)$ continuously
  - it bears a token serving cost $\Gamma(\cdot)$: increasing, convex



<v-click>
<br>

- **the provider can enter (irreversibly) the firm's market**
  - it pays a fixed entry cost $E > 0$ 
  - it then produces with the same CES technology $G$
    - it uses its own tokens $\tau_P$ (for free)
    - it builds its own infrastructure $S_P$ with investment $I_P$ (if needed)

</v-click>

---

# The provider's problem

- the provider has instantaneous profit:

$$
\small
\pi_P = \underbrace{p\, \tau_F - \Gamma(\tau_F)}_{\text{revenue from tokens}} \; + \; \underbrace{\mathbf{1}\{t \geq e\}}_\text{if provider enters market} \Big[ \underbrace{D(Q)\, q_P - h_P(I_P)}_{\text{revenue from product}} \; - \underbrace{\big( \Gamma(\tau_F + \tau_P) - \Gamma(\tau_F) \big)}_{\text{token serving cost adjustment}} \Big]
$$

<br>

<v-click>

- the provider maximizes

$$
\max_{p,\; e,\; \tau_P,\; I_P} \;\; \mathbb{E}\left[ \int_0^\infty e^{-r_P\, t}\, \pi_P(t)\, dt \; - \; e^{-r_P\, e}\, E \right]
$$

<v-click>

<br>

- the objective has two components
  - the **token business**: the firm is a customer worth keeping
  - the **product business**: the firm is a rival worth displacing

</v-click>
</v-click>

---
section: Results
---

# Model solution

### Very hard in the general case


<v-click>

<br>

### The linear case

- linear inverse demand 
$$D(Q) = a - b\, Q$$
- linear investment costs 

$$h_F(I) = \chi_F\, I \qquad \text{and} \qquad h_P(I) = \chi_P\, I$$

- quadratic innovation cost 
$$\kappa(\iota) = \kappa_0\, \iota + \dfrac{\kappa_1}{2}\, \iota^2$$ 

- linear token serving cost 
$$\Gamma(\tau) = \gamma_s\, \tau$$

</v-click>


---

# The equilibrium system in the linear case

- effective token price, and the CES unit cost:

$$\footnotesize
\tilde{p} = \underbrace{p}_{\text{token price}} + \underbrace{\lambda\, x\, \partial_x V_F - \tfrac{1}{2}\, \sigma^2 x^2\, \partial_{xx} V_F}_{\text{shadow cost of absorption}},
\qquad\qquad 
c_F(\tilde{p}) = \Big[ \omega^{\varsigma}\, \tilde{p}^{\,1-\varsigma} + (1-\omega)^{\varsigma}\, \zeta_F^{\,1-\varsigma} \Big]^{\frac{1}{1-\varsigma}}
$$

<v-click>

- before entry, on $(\bar{x}, \infty)$:

$$\footnotesize
r_F V_F^0 = \frac{\big( a + x - c_F(\tilde{p}) \big)^2}{4b} + \frac{\big( \max\{0,\; \partial_x V_F^0 - \kappa_0\} \big)^2}{2 \kappa_1}
$$

$$\footnotesize
r_P V_P^0 = \iota\, \partial_x V_P^0 + \max_{p \, \geq\, 0}\; \tau_F(x, p) \Big( p - \gamma_s - \lambda\, x\, \partial_x V_P^0 + \tfrac{1}{2}\, \sigma^2 x^2\, \partial_{xx} V_P^0 \Big)
$$



- after entry, similar ODE system in $V_F^1$ and $V_P^1$

<v-click>

- entry is a **threshold rule**: enter the first time $x(t) < \bar{x}$

<v-click>

- at the boundary $\bar{x}$: value matching, and smooth pasting for the provider, which chooses the boundary

$$\footnotesize
V_F^0 = V_F^1, \qquad V_P^0 = V_P^1 - E, \qquad \partial_x V_P^0 = \partial_x V_P^1
$$

$\implies$ equilibrium $\equiv$ system of second-order ODEs with a free boundary

<small>$\tau_F(x, p)$: the firm's token demand at the posted price; $\iota$: the innovation rule; $V^0 / V^1$: values before / after entry; $\varsigma = 1/(1-\theta)$: elasticity of substitution.</small>

</v-click>
</v-click>
</v-click>

---

# Result 1: firms restrict their use of the model

### Every token produces output today + transfers part of the advantage

<v-click>

- the firm's marginal revenue from tokens stays **strictly above** the token price:

$$\small
\underbrace{\frac{\partial}{\partial \tau_F} \Big[ \big( D(Q) + x \big)\, q_F \Big]}_{\text{marginal revenue from each token}} - \;\, \underbrace{p}_\text{token price}
\;\; = \; \underbrace{\lambda\, x\, \partial_x V_F}_{\text{destroyed exclusivity}} \; - \underbrace{\tfrac{1}{2}\, \sigma^2 x^2\, \partial_{xx} V_F}_{\text{price of the uncertainty}} \;\; > \;\, 0
$$

 $q_F = G(\tau_F, S_F)$ is output 

<v-click>

- marginal revenue from tokens falls with usage $\implies$ a firm using tokens optimally today would buy them until marginal revenue $=$ token price

- a **positive** difference $\implies$ the firm gives up tokens today because it adjusts token prices to account for destroyed exclusivity 
<v-click>

$\implies$ restraint is **equilibrium self-defense**

$\implies$ adoption of AI can be low where AI is productive 

</v-click>
</v-click>
</v-click>

---

# Result 2: the price of tokens

### <u>Before entry</u>, the posted price balances two motives for the provider

$$\small
\underbrace{\frac{\partial}{\partial p} \Big[ \big( p - \gamma_s \big)\, \tau_F(x, p) \Big]}_{\text{marginal instantaneous profit from tokens}}
\;\; = \;\;
\underbrace{\big(\partial_p \tau_F\big) \Big( \lambda\, x\, \partial_x V_P^0 - \tfrac{1}{2}\, \sigma^2 x^2\, \partial_{xx} V_P^0 \Big)}_{\text{learning motive}}
$$

<v-click>

- a provider extracting everything from token sales today would set the price where marginal current profit $= 0$

- the provider prices **off** that optimum on purpose: it trades instantaneous token profit against what usage teaches the model

<v-click>

- the sign of the learning motive is the provider's **posture** toward its customer

<v-click>

- when the **option to enter** dominates:
  - the provider prices **below** the price that maximizes its instantaneous token profit, possibly **below cost**, to accelerate absorption

<v-click>

- when the **token business** dominates:
  - the provider prices **above** the price that maximizes its current token profit, to slow learning

</v-click>
</v-click>
</v-click>
</v-click>

---

# Result 2: the price of tokens

### <u> After entry </u>, the price serves a second purpose:

$$\small
\underbrace{\frac{\partial}{\partial p} \Big[ \big( p - \gamma_s \big)\, \tau_F(x, p) \Big]}_{\text{marginal instantaneous profit from tokens}}\;\; = \;\;
\underbrace{\big(\partial_p \tau_F\big) \Big( \lambda\, x\, \partial_x V_P^1 - \tfrac{1}{2}\, \sigma^2 x^2\, \partial_{xx} V_P^1 \Big)}_{\text{learning motive}} \ -\ \underbrace{\tfrac{2}{3}\, q_P\, \partial_{\tilde{p}} c_F}_{\text{raising the rival's cost}}

$$ 

term $\tfrac{2}{3}\, q_P\, \partial_{\tilde{p}} c_F$ is nonnegative
$\implies$ the provider gives up token revenue with higher token prices $\implies$ higher price raises firm's production cost $\implies$ firm competes less 

<v-click>

<br>

### Token price

- **high** if the token business dominates
- **low** if the provider wants to accumulate its customer's advantage
- **higher** after entry to raise the rival's cost

<v-click>

<br>


$\implies$ pricing of model access is strategic

</v-click>
</v-click>


---

# Result 3: coexistence regimes

### Any equilibrium is one of three regimes

<v-click>

**1. No entry, no defense**: the firm's market is not worth taking



<v-click>

**2. Deterrence by perpetual innovation**: the firm keeps the advantage above the threshold $\bar{x}$ at all dates

- Deterrence is a permanent running cost

<v-click>

**3. Entry**: the advantage falls below $\bar{x}$, and the provider enters at that moment


</v-click>
</v-click>
</v-click>

---

# Result 4: who survives AI?

Depends on the production technology !

<v-click>

- Case 1: stock and AI are **substitutes** ($\theta > 0$)
  - the firm can shift production onto its non-AI capacity
  - the provider produces from tokens alone after (if) entry

<v-click>
<br>

- Case 2: stock and AI are **complements** ($\theta \leq 0$)
  - the firm cannot produce without tokens
  - it transfers its advantage $\implies$ defense is expensive for firms that use the model most

<v-click>

<br>

$\implies$ which regime a firm faces is a property of its **production technology**

$\implies$ most exposed: the firms that **must** use the model to operate

</v-click>
</v-click>
</v-click>

---
layout: end
---

Thank you !
