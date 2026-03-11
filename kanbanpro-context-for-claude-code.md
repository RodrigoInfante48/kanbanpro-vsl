# KanbanPro — Full Business Context for Claude Code Skills Analysis

## What is KanbanPro?

KanbanPro is a **Notion-based project management product** sold under the brand **DailyDuty**. It is a mobile-first system built entirely inside Notion that combines **Kanban boards**, **Six Sigma DMAIC methodology** (Define, Measure, Analyze, Improve, Control), and **Kaizen continuous improvement** into a single workspace. It targets professionals, small business owners, and operations teams who need structured process improvement without enterprise software costs.

## Product Architecture

- **Platform:** Notion (duplicated template). No custom code — the product IS a Notion workspace.
- **Delivery:** Digital product sold via Hotmart (one-time payment of $22 USD). Customer receives a Notion template link after purchase.
- **Components included:**
  1. **Dynamic Kanban Board** — Adaptive columns that scale with project complexity, optimized for Notion mobile.
  2. **DMAIC Roadmap** — Step-by-step templates for each Six Sigma phase (Define → Measure → Analyze → Improve → Control).
  3. **Kaizen Logs** — Quick-capture system for micro-improvements on the go.
  4. **Visual Workspace** (Bonus) — Custom dashboard with drag-and-drop analytics views.
  5. **Notion Blueprint** (Bonus) — Full organizational template syncing mobile data to desktop.
- **Key Differentiator in Measure Phase:** The DMAIC Measure phase explicitly includes a **free ETL stack** (PostgreSQL + Python + Power BI local) as a tangible, zero-cost data pipeline — positioned against expensive licensed tools like Tableau, Minitab, or JMP.

## Target Market & Go-to-Market

- **Primary audience:** Small business owners in Bogotá, Colombia (priority neighborhoods: Chapinero and Usaquén), expanding to English-speaking and international markets.
- **Languages:** VSL (Video Sales Letter) landing page translated into 7 languages: EN, ES, PT, ZH, FR, DE, JP, KR.
- **Sales funnel:** Social media → Linktree → Carrd-hosted VSL landing page → Hotmart checkout. Also WhatsApp-based free 8-day trial activation.
- **Outreach method:** Manual Google Maps prospecting → Airtable lead database → WhatsApp/email/phone contact. Target: ~28 contacts/week.
- **Pricing:** One-time $22 USD (positioned against $124.90/mo anchor price). 8-day money-back guarantee. Limited to 28 units/month (scarcity mechanic).

## Current Sales Infrastructure

- **Landing page (VSL):** Single-page HTML site (the `index.html` attached). Dark theme, teal (#00e6c7) + gold (#FFB800) color scheme. Mobile-first responsive design using Tailwind CSS. Includes:
  - Hero section with phone mockup
  - 4 testimonials (Marcus Reed, Sarah Chen, David Okoro, Elena Vasi)
  - Benefits checklist (PDCA, DMAIC, Kanban, Six Sigma)
  - Feature cards for the 3 core modules + 2 bonuses
  - Pricing section with countdown timer (30 min), animated gradient borders
  - Payment methods marquee (Cards, Efecty, Nequi, PSE, PayPal — Colombian + international)
  - WhatsApp CTA for free trial activation
  - Sticky bottom CTA bar
  - Google Analytics (G-M08G3EFVMM)
- **Checkout:** Hotmart payment link with tracking parameters.
- **WhatsApp:** +57 320 997 4750 (business number for trial activation and sales).
- **Links hub:** Linktree (linktr.ee/DailyDuty).
- **FAQ:** Hosted on Notion (public page).

## Tech Stack (Product Creator's Background)

The creator (Rod) is a data analyst/engineer with deep expertise in:
- **Data:** PostgreSQL, Python, dbt, Power BI, Power Query M, Amazon Redshift
- **Portfolio project:** World Bank ETL pipeline (GitHub: RodrigoInfante48/ETL) — Python + PostgreSQL + dbt + matplotlib/seaborn automated email reports + materialized views (country profiles, global trends, Z-score outlier detection)
- **AI workflow:** Uses Claude as a "translator" for Python — prefers complete executable code over conceptual explanations
- **Learning style:** Project-based, AI-assisted, prefers working code and actionable outputs

## Business Objectives

1. **Scale KanbanPro sales** — Increase conversion rate on the VSL landing page, expand outreach automation, improve the sales funnel.
2. **Professionalize marketing assets** — Create polished pitch decks, proposals, one-pagers, and sales documents for B2B outreach.
3. **Automate outreach operations** — Streamline the Google Maps → Airtable → WhatsApp/email pipeline.
4. **International expansion** — Leverage the 7-language VSL to reach markets beyond Colombia.
5. **Position as a data guru** — Build authority content (LinkedIn posts, case studies, blog posts) connecting Six Sigma + data engineering.

---

## YOUR TASK

You have access to Anthropic's Skills repository. Analyze every available skill and tell me:

1. **Which skills are directly applicable** to KanbanPro's business needs listed above? For each one, explain specifically HOW it would help (not generic — tied to my actual product, funnel, and operations).
2. **Which skills could I combine** to build compound workflows? (e.g., a skill that generates a pitch deck + a skill that creates a PDF proposal = automated B2B outreach package).
3. **What custom skills should I create** (using the skill-creator skill if available) that don't exist yet but would directly serve KanbanPro's go-to-market?
4. **Priority ranking:** Order everything by impact on revenue generation, from highest to lowest.

Be specific. Reference my actual product name, price point, target market, color scheme, tech stack, and sales channels. I don't want generic advice — I want an actionable skills deployment plan for KanbanPro.
