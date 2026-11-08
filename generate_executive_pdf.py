import base64

with open('prof.jpeg', 'rb') as f:
    prof_b64 = base64.b64encode(f.read()).decode('utf-8')

def h(s):
    if not s:
        return ""
    return str(s).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;")

TOTAL_PAGES = 10

# All 19 highlighted projects with authentic, high-impact engineering bullets
projects_data = [
    # Page 3: Projects 1, 2, 3
    [
        {
            "num": "01",
            "title": "Volvexer — Global Multi-Ledger Accounting & Reconciliation Automation",
            "org": "Volvexer · Global Financial Services (USA, UK, Australia, Pakistan)",
            "date": "2024 – Present",
            "badge": "Enterprise Platform",
            "tags": "Multi-Ledger Sync · QuickBooks · Xero · NetSuite · Zoho Books · Python · OCR",
            "url": "https://www.volvexer.com/",
            "bullets": [
                "<strong>Multi-Ledger Integration:</strong> Engineered high-throughput bi-directional synchronization engines interfacing QuickBooks Online, Xero, NetSuite, and Zoho Books with automated currency rate updates and zero manual data entry.",
                "<strong>Intelligent OCR & Document Processing:</strong> Built multi-currency vendor bill and VAT invoice pipelines with automated classification, line-item splitting, and zero-leak document vaults — reducing month-end closing time by 75%.",
                "<strong>Compliance & Infrastructure:</strong> Deployed automated multi-tenant audit logging and cryptographic storage ensuring SOC 2 readiness and seamless multi-jurisdiction financial reporting across US, UK, AUS, and PK."
            ]
        },
        {
            "num": "02",
            "title": "Enterprise Operations Portal — Cloud & ERP Systems Architecture",
            "org": "Ambica International · United States (Remote)",
            "date": "2025 – 2026",
            "badge": "Production · Live",
            "tags": "GCP Cloud Run · FastAPI · NetSuite ERP · Claude LLM · DocuSign · Postgres 18 · Redis",
            "url": "https://github.com/tariqdreamstech",
            "bullets": [
                "<strong>Cloud Architecture:</strong> Architected multi-tenant operations portal on GCP Cloud Run using FastAPI (Python 3.12), PostgreSQL 18 (Cloud SQL), Celery Beat, Redis, and multi-stage Docker containers.",
                "<strong>Live NetSuite Sync:</strong> Engineered real-time SuiteQL synchronization pipeline mirroring employees, purchase orders, inventory, and customer records with sub-second change propagation via Celery Beat + Redis.",
                "<strong>AI Ops-Intelligence & Security:</strong> Built Claude LLM WhatsApp/Gmail intake classifier, DocuSign e-sign REST integrations, MS Entra ID SSO, and 3-layer OTP authentication with 10-minute expiry and attempt-limiting."
            ]
        },
        {
            "num": "03",
            "title": "Ranbval Secret Manager — Zero-Knowledge Cryptographic Secrets Vault",
            "org": "Ranbval Security Platform · Global Open-Source & Enterprise SaaS",
            "date": "2025 – Present",
            "badge": "NLnet Grant · Open Source",
            "tags": "Zero-Trust Architecture · Cryptographic Vaults · Repo-Bound Tokens · PyPI & npm SDKs",
            "url": "https://secret.ranbval.com/",
            "bullets": [
                "<strong>Zero-Trust Infrastructure:</strong> Engineered self-hostable control plane replacing plaintext .env files with AES-GCM-256 and ChaCha20Poly1305 encryption, offline verification, and repo-bound cryptographic tokens.",
                "<strong>Dual Runtime SDKs:</strong> Authored production verification libraries for Python (PyPI) and Node.js (npm) achieving 11,500+ global downloads with pure ASGI auto-decryption and sub-2ms latency.",
                "<strong>Grant & Academic Validation:</strong> Awarded NLnet Foundation (Netherlands · NGI Zero-Trust) research grant review and Ignite National Technology Fund for enterprise cryptographic validation at scale."
            ]
        }
    ],

    # Page 4: Projects 4, 5, 6
    [
        {
            "num": "04",
            "title": "Automated Candidate Screening & Device Intelligence System",
            "org": "Savvy Programmers · United States (Remote)",
            "date": "Apr 2026 – Oct 2026",
            "badge": "Enterprise Automation",
            "tags": "JotForm Enterprise · BAT Automation · Device Telemetry · Data Continuity",
            "url": "https://github.com/tariqdreamstech",
            "bullets": [
                "<strong>Multi-Step Candidate Pipeline:</strong> Designed high-volume screening architecture unifying application intake, live hardware vetting, and automated interview scheduling into unified profiles, cutting vetting time by 60%.",
                "<strong>Custom BAT Telemetry Engine:</strong> Built silent BAT automation collecting hardware specs (CPU cores, RAM, GPU, OS build) to verify remote engineering workstation compliance with zero user friction.",
                "<strong>Data Continuity & Email Mapping:</strong> Overcame third-party form pagination limits via dual-form schema architecture and email-keyed indexing, enabling reliable end-to-end candidate record unification."
            ]
        },
        {
            "num": "05",
            "title": "Chatbot Engineer — AI Sales Intelligence Backend",
            "org": "Enterprise Sales Infrastructure · Contract",
            "date": "2025 – 2026",
            "badge": "Commercial AI",
            "tags": "Voiceflow · N8N · Gemini 2.5 Flash · Explicit Context Caching · Postgres",
            "url": "https://github.com/tariqdreamstech",
            "bullets": [
                "<strong>Explicit Context Caching:</strong> Implemented Google Gemini <code>/v1beta/cachedContents</code> context caching on N8N, slashing LLM token ingestion costs by 85% and cutting response latency under 600ms.",
                "<strong>4-Case Routing Engine:</strong> Built automated cache lifecycle manager handling cache creation, refresh, TTL expiration, and cold fallback with database-level per-user session caps.",
                "<strong>Postgres Hydration Layer:</strong> Engineered single-query client data hydration delivering instantaneous multi-turn sales context across high-volume inbound prospect dialogues."
            ]
        },
        {
            "num": "06",
            "title": "AI-Powered Video to Shorts Autonomous Media Automation",
            "org": "TariqDreamsTech · Autonomous Media Pipeline",
            "date": "2025 – 2026",
            "badge": "Production System",
            "tags": "FastAPI · Celery · FFmpeg · OpenAI Whisper · Python 3.12 · YouTube API",
            "url": "https://github.com/tariqdreamstech",
            "bullets": [
                "<strong>Asynchronous Media Engine:</strong> Built FastAPI and Celery pipeline orchestrating FFmpeg dynamic cropping, OpenAI Whisper audio transcription, and 9:16 vertical re-framing for long-form video assets.",
                "<strong>Hook Detection & Animated Subtitles:</strong> Implemented semantic LLM hook discovery identifying high-retention segments and generating word-level animated subtitle overlays automatically.",
                "<strong>Autonomous Syndication:</strong> Integrated YouTube Data API v3 for zero-touch horizontal-to-vertical content repurposing, scheduling, and direct channel upload."
            ]
        }
    ],

    # Page 5: Projects 7, 8, 9
    [
        {
            "num": "07",
            "title": "AI Persona, CSR & Action Item Analysis System",
            "org": "Savvy Programmers · United States (Remote)",
            "date": "Feb 2026 – Oct 2026",
            "badge": "Enterprise AI",
            "tags": "N8N Orchestration · Gemini 2.5 Pro · Supabase · Multi-Agent State Graph",
            "url": "https://github.com/tariqdreamstech",
            "bullets": [
                "<strong>Automated Transcript Analysis:</strong> Architected N8N pipeline parsing raw call recordings, extracting friction points, and categorizing sentiment across a 5-tier behavioral scoring framework (L1–L5) within 45 seconds.",
                "<strong>Jira & Supabase Automation:</strong> Programmatically generated structured Jira action items with severity tagging, routing critical customer escalations to engineering teams — reducing manual QA review by 90%.",
                "<strong>LinkedIn Profile Enrichment:</strong> Built Scrapin.io API integration with exponential backoff retry logic, enriching corporate prospect profiles into versioned Supabase CRM analytics dashboards."
            ]
        },
        {
            "num": "08",
            "title": "Autonomous Content Generation & SEO Publishing Engine",
            "org": "Autonomous Publishing Network · Remote",
            "date": "Feb 2026 – Apr 2026",
            "badge": "Autonomous AI",
            "tags": "Multi-Agent AI · WordPress REST API · YouTube API · Schema (JSON-LD) · GHL",
            "url": "https://github.com/tariqdreamstech",
            "bullets": [
                "<strong>Multi-Agent Editorial Graph:</strong> Deployed LangGraph state graph with 5 specialized agents: Topic Discovery, Atomic Outline Planning, Draft Synthesis, Fact Validation, and JSON-LD schema generation.",
                "<strong>Programmatic WordPress REST API:</strong> Automated multi-site publishing with contextual internal linking, image prompt synthesis, and real-time Google Indexing API pings for immediate crawl submission.",
                "<strong>Answer-First Quality Standards:</strong> Produced 30+ comprehensive long-form articles per cycle with autonomous YouTube script generation and structured multimedia asset embedding."
            ]
        },
        {
            "num": "09",
            "title": "Merchant Onboarding & Underwriting Lifecycle Automation",
            "org": "Transact Ultd · Iris CRM Integration (United States, Remote)",
            "date": "Feb 2026 – May 2026",
            "badge": "FinTech Platform",
            "tags": "Iris CRM · N8N Enterprise · ISO AMP · SMTP · Paybright · Compliance",
            "url": "https://github.com/tariqdreamstech",
            "bullets": [
                "<strong>Iris CRM Lifecycle Automation:</strong> Built automated merchant lifecycle workflows on N8N Enterprise, polling CRM lead stage updates and managing required documentation pipelines end-to-end.",
                "<strong>Statement Analysis & Email Engine:</strong> Automated underwriting document requests via SMTP, parsing multi-page merchant processing statements and updating compliance records in real time.",
                "<strong>Processor Integrations:</strong> Connected ISO AMP, Paybright, and underwriting endpoints with resilient error logging, cutting onboarding cycle time from 5 days to under 24 hours."
            ]
        }
    ],

    # Page 6: Projects 10, 11, 12
    [
        {
            "num": "10",
            "title": "Digital Operations Transformation & ERP Workflow Modernization",
            "org": "Global Enterprise Operations · Remote",
            "date": "2025 – 2026",
            "badge": "Enterprise Ops",
            "tags": "NetSuite ERP · Celery Beat · SuiteQL · Redis · Automation Pipelines",
            "url": "https://github.com/tariqdreamstech",
            "bullets": [
                "<strong>Legacy Modernization:</strong> Replaced manual cross-department spreadsheets with centralized automated event-driven workflows connecting NetSuite ERP with operational databases and downstream analytics.",
                "<strong>SuiteQL Delta Extraction:</strong> Configured scheduled SuiteQL extractors with change-tracking, transforming raw relational financial records into actionable real-time dashboards.",
                "<strong>Schema Validation & Alerts:</strong> Reduced data entry errors by 90% by enforcing strict automated schema validation, Slack alert notifications, and transactional rollback mechanisms."
            ]
        },
        {
            "num": "11",
            "title": "AI-Driven Service Operations Ecosystem — Qira Project",
            "org": "Computer Vision & Autonomous Audio Systems · Lahore, Pakistan",
            "date": "2025 – 2026",
            "badge": "Vision & Audio AI",
            "tags": "MediaPipe (468-pt Mesh) · OpenCV · FastAPI · TTS Engine · Python",
            "url": "https://github.com/tariqdreamstech",
            "bullets": [
                "<strong>MediaPipe Facial Mesh Analysis:</strong> Engineered deep computer vision module using OpenCV and MediaPipe for granular extraction of 468+ facial landmark points in real-time mobile camera streams.",
                "<strong>Multilingual AI Backend:</strong> Developed asynchronous FastAPI services delivering low-latency audio processing and multi-language AI dialogue generation for context-aware mobile client responses.",
                "<strong>Edge Optimization:</strong> Applied model quantization and edge inference optimizations ensuring smooth real-time telemetry visualization on standard mobile hardware."
            ]
        },
        {
            "num": "12",
            "title": "Zero-Touch Service Business Operations Platform",
            "org": "Autonomous Business Systems · Remote",
            "date": "2025 – 2026",
            "badge": "Full-Stack Automation",
            "tags": "N8N Enterprise · OpenPhone · Housecall Pro · Twilio · Webhooks",
            "url": "https://github.com/ahsantariq7",
            "bullets": [
                "<strong>Omnichannel Intake Engine:</strong> Built AI intake automation capturing inbound customer leads from OpenPhone, Google, Angi, and Thumbtack, standardizing disparate inquiries into unified CRM records.",
                "<strong>Housecall Pro Dispatch:</strong> Connected intake pipelines directly to Housecall Pro API for automated job creation, technician scheduling, and instant quote generation.",
                "<strong>End-to-End Automation:</strong> Slashed administrative overhead by 80%, coordinating the complete customer lifecycle from initial contact through automated review collection."
            ]
        }
    ],

    # Page 7: Projects 13, 14, 15
    [
        {
            "num": "13",
            "title": "AI Proposal Generation Platform — LLHAM Project",
            "org": "LLHAM Project · Remote (USA)",
            "date": "2024 – 2025",
            "badge": "Multi-Agent AI",
            "tags": "LangGraph · Submodules · Multi-Agent State Graph · Streaming · Vector RAG",
            "url": "https://github.com/tariqdreamstech",
            "bullets": [
                "<strong>LangGraph Multi-Agent Architecture:</strong> Architected dual-repository system with <code>llham-agents</code> submodule running specialized agents: Master Agent, Business Analyst, and Technical Architect.",
                "<strong>Real-Time Token Streaming:</strong> Built stateful checkpointing streaming endpoints allowing users to watch structured technical proposals compile with live token-by-token output.",
                "<strong>Vector RAG for Grounding:</strong> Integrated dense vector retrieval over corporate case studies and historical proposal libraries for accurate pricing and grounded effort estimation."
            ]
        },
        {
            "num": "14",
            "title": "Vectorized Database & AI Email Intelligence Engine",
            "org": "InstaMailAI · United States (Remote)",
            "date": "Feb 2025 – Mar 2025",
            "badge": "Vector Search",
            "tags": "MongoDB Atlas Vector Search · LangChain · FastAPI · Python · Embeddings",
            "url": "https://github.com/tariqdreamstech",
            "bullets": [
                "<strong>MongoDB Atlas Vector Search:</strong> Built high-performance semantic search pipeline indexing millions of corporate email threads into high-dimensional embeddings with sub-50ms similarity retrieval.",
                "<strong>RAG Draft Synthesis:</strong> Implemented dense retrieval augmented generation providing contextually grounded, executive-ready draft suggestions with zero hallucinations.",
                "<strong>Scalable Architecture:</strong> Designed decoupled FastAPI ingestion endpoints handling asynchronous webhook payloads from enterprise email providers under heavy concurrent load."
            ]
        },
        {
            "num": "15",
            "title": "Enterprise Automation Workflows & CRM Architecture",
            "org": "hddisenos · Remote (Venezuela)",
            "date": "May 2025 – Dec 2025",
            "badge": "Enterprise N8N",
            "tags": "N8N Enterprise · REST/SOAP APIs · HubSpot · Zoho CRM · PostgreSQL",
            "url": "https://github.com/tariqdreamstech",
            "bullets": [
                "<strong>Cross-CRM Synchronization:</strong> Architected resilient N8N workflows bridging external REST/SOAP partner endpoints with HubSpot marketing funnels and regional Zoho CRM instances.",
                "<strong>Error Handling & Retry Queues:</strong> Built custom JavaScript transformation nodes and automated retry queues, reducing manual data synchronization effort by 60%.",
                "<strong>Database Pooling Optimization:</strong> Tuned PostgreSQL and NoSQL connection pooling to prevent pipeline timeouts during high-volume nocturnal batch processing runs."
            ]
        }
    ],

    # Page 8: Projects 16, 17, 18, 19
    [
        {
            "num": "16",
            "title": "Legal Interview Intelligence & Case Preparation System",
            "org": "Seanz Law Firm · United States (Remote)",
            "date": "June 2024 – Aug 2024",
            "badge": "Legal Tech",
            "tags": "OpenAI GPT-4 · Twilio · WhatsApp API · Google Looker Studio · Python",
            "url": "https://github.com/tariqdreamstech",
            "bullets": [
                "<strong>Bilingual Legal Assistant:</strong> Built multilingual (English/Spanish) AI-powered interview assistant on WhatsApp and Twilio for immigration law client intake.",
                "<strong>Compliance & Reporting:</strong> Enforced strict attorney-client privilege guidelines with zero-retention prompts and real-time paralegal tracking via Google Looker Studio."
            ]
        },
        {
            "num": "17",
            "title": "Secure Multi-Tenant SaaS & Role-Based Workflows",
            "org": "NVIT Project · United States (Remote)",
            "date": "Jan 2024 – May 2024",
            "badge": "Multi-Tenant SaaS",
            "tags": "Django · JWT Authentication · OpenAI GPT · PostgreSQL · JerichoAI.io",
            "url": "https://jerichoai.io",
            "bullets": [
                "<strong>Schema-Level Multi-Tenancy:</strong> Engineered multi-role Django backend (Customers, Engineers, Admins) with strict schema-level tenant isolation and JWT token authentication.",
                "<strong>AI Ticket Estimation:</strong> Integrated OpenAI GPT for automatic ticket scope estimation, effort prediction, and Jira-style hierarchy duplication."
            ]
        },
        {
            "num": "18",
            "title": "AI Workflow Automation Platform Backend",
            "org": "2456.ai · United States (Remote)",
            "date": "Aug 2023 – Dec 2023",
            "badge": "AI Microservices",
            "tags": "Django · FastAPI · PostgreSQL · Pinecone Vector DB · Stripe Billing",
            "url": "https://github.com/tariqdreamstech",
            "bullets": [
                "<strong>Hybrid Microservices:</strong> Architected Django core backend coupled with FastAPI microservices for high-frequency AI workflow computations under concurrent load.",
                "<strong>Dual Database & Billing:</strong> Managed relational state in PostgreSQL and semantic queries in Pinecone; integrated Stripe webhooks for granular tier-based billing."
            ]
        },
        {
            "num": "19",
            "title": "Data Engineering & Scalable ETL Analytics Architecture",
            "org": "QPharma Project · United States (Remote)",
            "date": "Mar 2022 – July 2022",
            "badge": "Cloud Data Eng",
            "tags": "AWS Glue · S3 Data Lake · AWS Lambda · Python Pandas · Excalidraw",
            "url": "https://github.com/tariqdreamstech",
            "bullets": [
                "<strong>Serverless Cloud Pipelines:</strong> Built ETL pipelines using AWS Glue, Amazon S3 data lakes, and Lambda functions to ingest high-volume pharmaceutical sales datasets.",
                "<strong>Automated Cleansing & Speed:</strong> Accelerated BI and market forecasting cycles by 70%, outputting sanitized analytical tables into Amazon Athena with Pandas-based transformation."
            ]
        }
    ]
]

html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Ahsan Tariq — AI Engineer · Forward Deployed Engineer Portfolio</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600;700&family=Outfit:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">
<style>
/* ─── RESET & A4 PAGE GEOMETRY ───────────────────── */
@page {{
    size: A4 portrait;
    margin: 0;
}}
*, *::before, *::after {{
    box-sizing: border-box;
    margin: 0;
    padding: 0;
    -webkit-print-color-adjust: exact !important;
    print-color-adjust: exact !important;
}}

:root {{
    --bg-dark: #08080d;
    --card-bg: #0f0e17;
    --card-surface: #141320;
    --accent: #ffba49;
    --accent-glow: rgba(255, 186, 73, 0.15);
    --cyan: #38bdf8;
    --emerald: #10b981;
    --purple: #a78bfa;
    --text-pure: #ffffff;
    --text-primary: #f1f5f9;
    --text-secondary: #cbd5e1;
    --text-muted: #94a3b8;
    --text-dim: #64748b;
    --border: rgba(255, 255, 255, 0.08);
    --border-accent: rgba(255, 186, 73, 0.35);
    --font-heading: 'Outfit', sans-serif;
    --font-body: 'Plus Jakarta Sans', sans-serif;
    --font-mono: 'JetBrains Mono', monospace;
}}

html, body {{
    background: #08080d;
    color: var(--text-primary);
    font-family: var(--font-body);
    font-size: 8.5px;
    line-height: 1.45;
    width: 210mm;
    margin: 0 auto;
}}

.pdf-page {{
    width: 210mm;
    height: 297mm;
    max-height: 297mm;
    padding: 10mm 12mm 10mm 12mm;
    page-break-after: always;
    page-break-inside: avoid;
    break-after: page;
    break-inside: avoid;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    position: relative;
    overflow: hidden;
    background: #08080d;
}}

/* Header & Footer */
.doc-header {{
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-bottom: 1px solid var(--border);
    padding-bottom: 2.2mm;
    margin-bottom: 3.5mm;
}}
.doc-header-left {{
    font-family: var(--font-heading);
    font-size: 8px;
    font-weight: 800;
    letter-spacing: 0.8px;
    color: var(--accent);
    text-transform: uppercase;
}}
.doc-header-left span {{
    color: var(--text-dim);
    margin: 0 4px;
}}
.doc-header-right {{
    font-family: var(--font-mono);
    font-size: 7.2px;
    color: var(--text-dim);
}}
.doc-footer {{
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-top: 1px solid var(--border);
    padding-top: 2.2mm;
    margin-top: 2.5mm;
    font-family: var(--font-mono);
    font-size: 7.2px;
    color: var(--text-dim);
}}
.doc-footer-left strong {{ color: var(--accent); }}
.doc-footer-link {{ color: inherit; text-decoration: none; }}

/* Page Titles */
.page-title-block {{ margin-bottom: 3mm; }}
.page-tag {{
    font-family: var(--font-mono);
    font-size: 7px;
    font-weight: 700;
    color: var(--accent);
    text-transform: uppercase;
    letter-spacing: 1px;
    display: block;
    margin-bottom: 0.8mm;
}}
.page-title {{
    font-family: var(--font-heading);
    font-size: 15px;
    font-weight: 900;
    color: var(--text-pure);
    line-height: 1.15;
    letter-spacing: -0.3px;
}}
.page-subtitle {{
    font-size: 8.5px;
    color: var(--text-muted);
    line-height: 1.4;
    margin-top: 0.8mm;
}}

/* Chips */
.chip {{
    display: inline-flex;
    align-items: center;
    font-family: var(--font-mono);
    font-size: 6.8px;
    font-weight: 600;
    padding: 1.2px 4.5px;
    border-radius: 4px;
    background: rgba(255, 255, 255, 0.04);
    border: 1px solid var(--border);
    color: var(--text-secondary);
    white-space: nowrap;
}}
.chip-accent {{
    background: rgba(255, 186, 73, 0.1);
    border-color: rgba(255, 186, 73, 0.3);
    color: var(--accent);
}}
.chip-cyan {{
    background: rgba(56, 189, 248, 0.1);
    border-color: rgba(56, 189, 248, 0.3);
    color: var(--cyan);
}}
.chip-emerald {{
    background: rgba(16, 185, 129, 0.1);
    border-color: rgba(16, 185, 129, 0.3);
    color: var(--emerald);
}}
.chip-purple {{
    background: rgba(167, 139, 250, 0.1);
    border-color: rgba(167, 139, 250, 0.3);
    color: var(--purple);
}}

/* ─── COVER PAGE (PAGE 1) ────────────────────────── */
.cover-page {{
    background: radial-gradient(circle at 50% 25%, #14131f 0%, #08080d 75%);
    justify-content: space-between;
    padding: 14mm 16mm;
}}
.cover-top {{
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-bottom: 1px solid rgba(255,255,255,0.08);
    padding-bottom: 3.5mm;
}}
.cover-brand {{
    font-family: var(--font-heading);
    font-size: 18px;
    font-weight: 900;
    color: var(--accent);
    letter-spacing: -0.5px;
}}
.cover-badge {{
    font-family: var(--font-mono);
    font-size: 7.2px;
    font-weight: 700;
    color: var(--accent);
    background: var(--accent-glow);
    border: 1px solid var(--border-accent);
    padding: 2px 7px;
    border-radius: 99px;
    text-transform: uppercase;
    letter-spacing: 0.5px;
}}
.cover-hero {{
    text-align: center;
    margin: 3mm 0;
}}
.cover-avatar-wrap {{
    width: 82px;
    height: 82px;
    margin: 0 auto 3mm;
    border-radius: 50%;
    padding: 2.5px;
    background: linear-gradient(135deg, var(--accent) 0%, rgba(255,186,73,0.15) 100%);
    box-shadow: 0 0 25px rgba(255,186,73,0.3);
}}
.cover-avatar {{
    width: 100%;
    height: 100%;
    border-radius: 50%;
    object-fit: cover;
    display: block;
}}
.cover-name {{
    font-family: var(--font-heading);
    font-size: 26px;
    font-weight: 900;
    color: var(--text-pure);
    letter-spacing: -0.5px;
    line-height: 1.1;
    margin-bottom: 1mm;
}}
.cover-role {{
    font-family: var(--font-heading);
    font-size: 11px;
    font-weight: 700;
    color: var(--accent);
    letter-spacing: 0.5px;
    margin-bottom: 2.5mm;
}}
.cover-quote {{
    max-width: 155mm;
    margin: 0 auto;
    font-size: 9px;
    line-height: 1.5;
    color: var(--text-secondary);
    background: rgba(255,255,255,0.02);
    border: 1px solid rgba(255,255,255,0.05);
    border-radius: 8px;
    padding: 2.8mm 4.5mm;
    font-style: italic;
}}
.cover-stats-grid {{
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 2.5mm;
    margin: 3.5mm 0;
}}
.cover-stat-card {{
    background: var(--card-bg);
    border: 1px solid rgba(255,255,255,0.07);
    border-radius: 8px;
    padding: 3mm 3.5mm;
    text-align: center;
    text-decoration: none;
    color: inherit;
    display: block;
}}
.cover-stat-num {{
    font-family: var(--font-heading);
    font-size: 15px;
    font-weight: 900;
    color: var(--accent);
    line-height: 1.1;
}}
.cover-stat-lbl {{
    font-size: 8px;
    font-weight: 700;
    color: var(--text-pure);
    margin: 0.8mm 0 0.3mm;
}}
.cover-stat-sub {{
    font-size: 6.8px;
    color: var(--text-dim);
    font-family: var(--font-mono);
}}
.cover-contact-bar {{
    background: var(--card-surface);
    border: 1px solid rgba(255,186,73,0.25);
    border-radius: 8px;
    padding: 3mm 4mm;
    display: grid;
    grid-template-columns: 1fr 1fr 1fr 1.2fr;
    gap: 2mm;
    font-size: 7.8px;
}}
.cover-c-item strong {{
    display: block;
    color: var(--accent);
    font-family: var(--font-mono);
    font-size: 7.2px;
    text-transform: uppercase;
    margin-bottom: 0.5mm;
}}
.cover-c-item a, .cover-c-link {{
    color: var(--text-primary);
    word-break: break-all;
    text-decoration: none;
}}

/* ─── PAGE 2 STYLES ───────────────────────────────── */
.summary-box {{
    background: var(--card-bg);
    border-left: 3px solid var(--accent);
    border-radius: 0 8px 8px 0;
    padding: 3mm 4.2mm;
    margin-bottom: 2.8mm;
    font-size: 9px;
    line-height: 1.5;
    color: #e2e8f0;
}}
.summary-box p {{ margin-bottom: 1.2mm; }}
.summary-box p:last-child {{ margin-bottom: 0; }}

.pillars-grid {{
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 2.5mm;
    margin-bottom: 2.8mm;
}}
.pillar-card {{
    background: var(--card-bg);
    border: 1px solid var(--border);
    border-radius: 7px;
    padding: 2.5mm 3mm;
}}
.pillar-header {{
    display: flex;
    align-items: center;
    gap: 2mm;
    margin-bottom: 1mm;
}}
.pillar-num {{
    font-family: var(--font-mono);
    font-size: 8.5px;
    font-weight: 800;
    color: var(--accent);
    background: var(--accent-glow);
    padding: 1px 4.5px;
    border-radius: 4px;
}}
.pillar-title {{
    font-size: 9.5px;
    font-weight: 800;
    color: var(--text-pure);
}}
.pillar-desc {{
    font-size: 8px;
    line-height: 1.38;
    color: var(--text-muted);
}}

.clients-grid {{
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 1.8mm;
    margin-bottom: 2.8mm;
}}
.client-card {{
    background: var(--card-bg);
    border: 1px solid var(--border);
    border-radius: 6px;
    padding: 2mm 2.8mm;
}}
.client-name {{
    font-size: 8.5px;
    font-weight: 700;
    color: var(--text-pure);
}}
.client-focus {{
    font-size: 7px;
    color: var(--text-muted);
    font-family: var(--font-mono);
}}
.client-flag {{
    font-size: 7.2px;
    color: var(--accent);
    font-weight: 700;
}}
.client-card-link {{
    display: flex;
    justify-content: space-between;
    align-items: center;
    width: 100%;
    text-decoration: none;
    color: inherit;
}}

.tech-taxonomy {{
    background: var(--card-bg);
    border: 1px solid var(--border);
    border-radius: 7px;
    padding: 2.2mm 3.2mm;
}}
.tech-tax-row {{
    display: flex;
    align-items: baseline;
    margin-bottom: 1mm;
}}
.tech-tax-row:last-child {{ margin-bottom: 0; }}
.tech-tax-lbl {{
    width: 28mm;
    font-family: var(--font-mono);
    font-size: 7px;
    font-weight: 700;
    color: var(--accent);
    text-transform: uppercase;
    flex-shrink: 0;
}}
.tech-tax-chips {{
    display: flex;
    flex-wrap: wrap;
    gap: 1.2mm;
}}

/* ─── PROJECTS DOSSIER (PAGES 3–8) ───────────────── */
.project-dossier-list {{
    display: flex;
    flex-direction: column;
    gap: 3mm;
    flex: 1;
}}
.project-dossier-list-p8 {{
    display: flex;
    flex-direction: column;
    gap: 2mm;
    flex: 1;
}}
.proj-card {{
    background: var(--card-bg);
    border: 1px solid var(--border);
    border-radius: 7px;
    padding: 2.8mm 3.8mm;
}}
.project-dossier-list-p8 .proj-card {{
    padding: 2.2mm 3.2mm;
}}
.proj-card-head {{
    display: flex;
    justify-content: space-between;
    align-items: baseline;
    margin-bottom: 0.8mm;
}}
.proj-card-title {{
    font-size: 10.2px;
    font-weight: 800;
    color: var(--text-pure);
}}
.proj-card-title a {{
    color: var(--text-pure);
    text-decoration: none;
}}
.proj-card-meta {{
    display: flex;
    gap: 1.8mm;
    align-items: center;
}}
.proj-date {{
    font-family: var(--font-mono);
    font-size: 7.6px;
    font-weight: 700;
    color: var(--accent);
}}
.proj-badge {{
    font-family: var(--font-mono);
    font-size: 6.8px;
    font-weight: 700;
    padding: 1px 4.5px;
    border-radius: 99px;
    background: rgba(56,189,248,0.12);
    border: 1px solid rgba(56,189,248,0.3);
    color: var(--cyan);
}}
.proj-org {{
    font-size: 8.5px;
    font-weight: 600;
    color: var(--text-primary);
    margin-bottom: 0.8mm;
}}
.proj-tags {{
    font-family: var(--font-mono);
    font-size: 6.8px;
    font-weight: 600;
    color: var(--accent);
    margin-bottom: 1.5mm;
    text-transform: uppercase;
    letter-spacing: 0.3px;
}}
.proj-bullets {{
    list-style: none;
    padding-left: 0;
    margin: 0;
}}
.proj-bullets li {{
    position: relative;
    padding-left: 3.5mm;
    font-size: 8px;
    line-height: 1.45;
    color: #cbd5e1;
    margin-bottom: 0.9mm;
}}
.project-dossier-list-p8 .proj-bullets li {{
    font-size: 7.7px;
    line-height: 1.38;
    margin-bottom: 0.5mm;
}}
.proj-bullets li:last-child {{ margin-bottom: 0; }}
.proj-bullets li::before {{
    content: '›';
    position: absolute;
    left: 0;
    color: var(--accent);
    font-weight: 800;
    font-size: 9.5px;
}}
.proj-bullets li strong {{
    color: var(--text-pure);
    font-weight: 700;
}}
.proj-bullets li code {{
    background: rgba(255,255,255,0.08);
    padding: 0.5px 3px;
    border-radius: 3px;
    color: var(--accent);
    font-family: var(--font-mono);
    font-size: 0.9em;
}}

/* ─── PAGE 9: ACADEMIC RESEARCH ──────────────────── */
.wos-profile-card {{
    background: var(--card-bg);
    border: 1px solid var(--border-accent);
    border-radius: 7px;
    padding: 3mm 4mm;
    margin-bottom: 3mm;
    display: flex;
    justify-content: space-between;
    align-items: center;
}}
.wos-info h3 {{
    font-size: 10.5px;
    font-weight: 800;
    color: var(--text-pure);
    margin-bottom: 0.5mm;
}}
.wos-info p {{ font-size: 7.8px; color: var(--text-muted); }}
.wos-ids {{ display: flex; gap: 2mm; }}
.wos-chip-link {{
    display: inline-flex;
    align-items: center;
    gap: 3px;
    font-family: var(--font-mono);
    font-size: 7.2px;
    font-weight: 700;
    padding: 1.5px 5px;
    border-radius: 4px;
    background: rgba(255,186,73,0.12);
    border: 1px solid rgba(255,186,73,0.35);
    color: var(--accent);
    text-decoration: none;
}}
.reviewer-grid {{
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 2.2mm;
    margin-bottom: 3.5mm;
}}
.review-item {{
    background: var(--card-bg);
    border: 1px solid var(--border);
    border-radius: 6px;
    padding: 2.2mm 2.8mm;
}}
.review-journal {{
    font-size: 8px;
    font-weight: 700;
    color: var(--text-pure);
    margin-bottom: 0.5mm;
}}
.review-journal a {{ color: var(--text-pure); text-decoration: none; }}
.review-cert-no {{
    font-family: var(--font-mono);
    font-size: 6.6px;
    color: var(--accent);
    margin-bottom: 0.8mm;
}}
.review-paper-title {{
    font-size: 7.2px;
    color: var(--text-muted);
    line-height: 1.35;
}}
.papers-list {{ display: flex; flex-direction: column; gap: 1.8mm; }}
.paper-row {{
    background: var(--card-bg);
    border: 1px solid var(--border);
    border-radius: 6px;
    padding: 2mm 3mm;
    display: flex;
    justify-content: space-between;
    align-items: center;
    gap: 2.5mm;
}}
.paper-row-left {{ flex: 1; }}
.paper-title {{
    font-size: 8.2px;
    font-weight: 700;
    color: var(--text-pure);
    margin-bottom: 0.5mm;
}}
.paper-meta {{
    font-size: 7px;
    color: var(--text-dim);
    font-family: var(--font-mono);
}}
.paper-meta a {{ color: var(--accent); text-decoration: underline; }}
.paper-badge {{
    font-family: var(--font-mono);
    font-size: 6.8px;
    font-weight: 700;
    padding: 1.2px 5mm;
    border-radius: 99px;
    text-transform: uppercase;
    white-space: nowrap;
}}

/* ─── PAGE 10: EDUCATION & CLOSING ───────────────── */
.edu-block-grid {{
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 2.8mm;
    margin-bottom: 3mm;
}}
.edu-card {{
    background: var(--card-bg);
    border: 1px solid var(--border);
    border-radius: 7px;
    padding: 2.8mm 3.5mm;
}}
.edu-degree {{
    font-size: 9.8px;
    font-weight: 800;
    color: var(--text-pure);
    margin-bottom: 0.5mm;
}}
.edu-school {{
    font-size: 7.6px;
    color: var(--accent);
    margin-bottom: 1.2mm;
    font-weight: 600;
}}
.edu-badges-row {{
    display: flex;
    gap: 1.2mm;
    margin-bottom: 1.5mm;
    flex-wrap: wrap;
}}
.edu-desc {{
    font-size: 7.6px;
    color: var(--text-muted);
    line-height: 1.4;
}}
.awards-grid {{
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 2.5mm;
    margin-bottom: 3mm;
}}
.award-box {{
    background: var(--card-bg);
    border: 1px solid var(--border);
    border-radius: 6px;
    padding: 2.2mm 2.8mm;
}}
.award-tag {{
    font-family: var(--font-mono);
    font-size: 6.6px;
    font-weight: 700;
    color: var(--accent);
    margin-bottom: 0.6mm;
}}
.award-name {{
    font-size: 8.4px;
    font-weight: 800;
    color: var(--text-pure);
    margin-bottom: 0.8mm;
}}
.award-org {{
    font-size: 7.2px;
    color: var(--text-dim);
    line-height: 1.35;
}}
.certs-grid-p10 {{
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 2.5mm;
    margin-bottom: 3.5mm;
}}
.cert-col {{
    background: var(--card-bg);
    border: 1px solid var(--border);
    border-radius: 6px;
    padding: 2.5mm 3mm;
}}
.cert-col-title {{
    font-family: var(--font-mono);
    font-size: 7.4px;
    font-weight: 800;
    color: var(--accent);
    margin-bottom: 1.5mm;
    text-transform: uppercase;
}}
.cert-item-link {{
    font-size: 7.2px;
    color: var(--text-secondary);
    display: block;
    margin-bottom: 1.2mm;
    text-decoration: none;
}}
.closing-dossier {{
    background: radial-gradient(circle at 50% 50%, #171525 0%, #0d0c14 100%);
    border: 1px solid var(--border-accent);
    border-radius: 8px;
    padding: 3.5mm 5mm;
    text-align: center;
    margin-top: auto;
}}
.closing-dossier h3 {{
    font-family: var(--font-heading);
    font-size: 12px;
    font-weight: 900;
    color: var(--text-pure);
    margin-bottom: 1mm;
}}
.closing-dossier p {{
    font-size: 8.4px;
    color: var(--text-muted);
    max-width: 140mm;
    margin: 0 auto 2.2mm;
}}
.closing-links {{
    display: flex;
    justify-content: center;
    gap: 2.5mm;
    font-family: var(--font-mono);
    font-size: 7.8px;
}}
.closing-link {{
    color: var(--accent);
    background: rgba(255,186,73,0.1);
    border: 1px solid rgba(255,186,73,0.3);
    padding: 2.2px 7px;
    border-radius: 4px;
    text-decoration: none;
    display: inline-flex;
    align-items: center;
    gap: 4px;
}}

/* Global link styles */
a {{ color: inherit; text-decoration: none; }}
</style>
</head>
<body>

<!-- PAGE 1: COVER -->
<div class="pdf-page cover-page">
    <div class="cover-top">
        <div class="cover-brand">AT.</div>
        <div class="cover-badge">Available for Engagements · Forward Deployed AI Engineer</div>
    </div>
    <div class="cover-hero">
        <div class="cover-avatar-wrap">
            <img class="cover-avatar" src="data:image/jpeg;base64,{prof_b64}" alt="Ahsan Tariq">
        </div>
        <h1 class="cover-name">Ahsan Tariq</h1>
        <div class="cover-role">AI Engineer · Forward Deployed Engineer</div>
        <div class="cover-quote">
            "Designing and deploying scalable, maintainable production architectures — bridging autonomous multi-agent swarms, machine learning, deep learning, reinforcement learning, and zero-trust cryptographic runtimes."
        </div>
    </div>
    <div class="cover-stats-grid">
        <a href="https://leetcode.com/u/ahsantariq7/" target="_blank" class="cover-stat-card">
            <div class="cover-stat-num">81</div>
            <div class="cover-stat-lbl">LeetCode DSA</div>
            <div class="cover-stat-sub">Algorithms &amp; Problem Solving</div>
        </a>
        <a href="https://www.kaggle.com/engrahsantariq" target="_blank" class="cover-stat-card">
            <div class="cover-stat-num">Expert</div>
            <div class="cover-stat-lbl">Kaggle ML Rank</div>
            <div class="cover-stat-sub">Top Solved ML Solutions</div>
        </a>
        <a href="https://pypi.org/user/ahsantariq7/" target="_blank" class="cover-stat-card">
            <div class="cover-stat-num">11,500+</div>
            <div class="cover-stat-lbl">PyPI &amp; npm Downloads</div>
            <div class="cover-stat-sub">Production Open-Source SDKs</div>
        </a>
        <a href="https://www.webofscience.com/wos/author/record/OMK-7734-2025" target="_blank" class="cover-stat-card">
            <div class="cover-stat-num">5+ Journals</div>
            <div class="cover-stat-lbl">Academic Peer Reviewer</div>
            <div class="cover-stat-sub">1 Book · WoS Verified</div>
        </a>
        <a href="https://orcid.org/0009-0005-0673-8369" target="_blank" class="cover-stat-card">
            <div class="cover-stat-num">6 Papers</div>
            <div class="cover-stat-lbl">Research &amp; Preprints</div>
            <div class="cover-stat-sub">JISRC · Zenodo DOI</div>
        </a>
        <a href="https://github.com/tariqdreamstech" target="_blank" class="cover-stat-card">
            <div class="cover-stat-num">23 Roles</div>
            <div class="cover-stat-lbl">Production Deployments</div>
            <div class="cover-stat-sub">B2B Enterprise &amp; B2C Platforms</div>
        </a>
    </div>
    <div class="cover-contact-bar">
        <div class="cover-c-item">
            <strong>Direct Email</strong>
            <a href="mailto:ahsantariq0724@gmail.com" class="cover-c-link">ahsantariq0724@gmail.com</a>
        </div>
        <div class="cover-c-item">
            <strong>LinkedIn</strong>
            <a href="https://www.linkedin.com/in/ahsan-tariq-comp-engr/" target="_blank" class="cover-c-link">linkedin.com/in/ahsan-tariq-comp-engr</a>
        </div>
        <div class="cover-c-item">
            <strong>GitHub / Org</strong>
            <a href="https://github.com/ahsantariq7" target="_blank" class="cover-c-link">ahsantariq7</a> · <a href="https://github.com/tariqdreamstech" target="_blank" class="cover-c-link">tariqdreamstech</a>
        </div>
        <div class="cover-c-item">
            <strong>WoS / ORCID</strong>
            <a href="https://www.webofscience.com/wos/author/record/OMK-7734-2025" target="_blank" class="cover-c-link">OMK-7734-2025</a> · <a href="https://orcid.org/0009-0005-0673-8369" target="_blank" class="cover-c-link">0009-0005-0673-8369</a>
        </div>
    </div>
</div>

<!-- PAGE 2: EXECUTIVE SUMMARY & CLIENTS -->
<div class="pdf-page">
    <div class="doc-header">
        <div class="doc-header-left">AHSAN TARIQ <span>/</span> FORWARD DEPLOYED AI ENGINEER · SUMMARY &amp; CLIENTS</div>
        <div class="doc-header-right">DOSSIER 2026 · SECTION 01</div>
    </div>
    <div class="page-title-block">
        <span class="page-tag">Engineering Discipline &amp; Global Impact</span>
        <h2 class="page-title">Forward Deployed Engineering &amp; Architecture</h2>
        <p class="page-subtitle">Proven track record deploying complex zero-to-production AI and distributed systems for international enterprise clients across US, UK, and Europe.</p>
    </div>
    <div class="summary-box">
        <p><strong>Forward Deployed AI Engineer &amp; Systems Architect.</strong> Dedicated to hands-on, high-velocity zero-to-production engineering — transforming complex distributed problems into resilient, fault-tolerant software built for real-world impact. Proven execution across <strong>Enterprise B2B client architectures</strong> (multi-tenant ERP portals, real-time NetSuite synchronization, fleet telematics, and automated merchant lifecycle engines) and <strong>consumer-facing B2C applications</strong> (real-time avatar intelligence, automated video-to-shorts creators, and cross-platform mobile apps).</p>
        <p>Deep engineering foundation bridging <strong>Autonomous Robotics &amp; Embedded Systems (ROS/ROS2, sensor fusion, Byzantine-resilient perception)</strong> with modern <strong>Machine Learning (ML), Deep Learning (DL), Reinforcement Learning (RL), and Generative AI / LLMOps</strong>. Expert in orchestrating multi-agent state machines via LangGraph, training PyTorch deep models &amp; RL policy optimization (DQN, PPO), and deploying hybrid dense/sparse RAG pipelines (Pinecone, MongoDB Atlas).</p>
    </div>
    <div class="pillars-grid">
        <div class="pillar-card">
            <div class="pillar-header"><span class="pillar-num">01</span><span class="pillar-title">ML, Deep Learning &amp; RL</span></div>
            <p class="pillar-desc">PyTorch &amp; TensorFlow, Deep Q-Networks (DQN), Policy Gradients / PPO, reward modeling, Vision Transformers (ViT), CNNs, Scikit-Learn, and feature engineering.</p>
        </div>
        <div class="pillar-card">
            <div class="pillar-header"><span class="pillar-num">02</span><span class="pillar-title">Multi-Agent Swarms &amp; LLMOps</span></div>
            <p class="pillar-desc">State machine graphs with LangGraph, Claude 3.5 Sonnet, Gemini 2.5 Flash. Multi-tier prompt routing, context compression, and deterministic tool validation.</p>
        </div>
        <div class="pillar-card">
            <div class="pillar-header"><span class="pillar-num">03</span><span class="pillar-title">Cloud &amp; Systems Architecture</span></div>
            <p class="pillar-desc">GCP Cloud Run multi-tenant backends, FastAPI (Python 3.12), NetSuite SuiteQL streaming mirrors, Celery Beat schedulers, and Cloud SQL PostgreSQL 18.</p>
        </div>
        <div class="pillar-card">
            <div class="pillar-header"><span class="pillar-num">04</span><span class="pillar-title">Robotics &amp; Zero-Trust Secrets</span></div>
            <p class="pillar-desc">ROS/ROS2 perception pipelines, MediaPipe 468-point mesh, Zero-Shot CLIP, pure ASGI auto-decryption, AES-GCM / ChaCha20, and repo-bound cryptographic vaults.</p>
        </div>
    </div>
    <div>
        <div style="font-family: var(--font-heading); font-size: 10.5px; font-weight: 800; color: var(--text-pure); margin-bottom: 1.8mm;">International Clients &amp; Enterprise Organizations</div>
        <div class="clients-grid">
            <div class="client-card"><a href="https://github.com/tariqdreamstech" target="_blank" class="client-card-link"><div><div class="client-name">Ambica International ↗</div><div class="client-focus">Cloud &amp; NetSuite ERP Portal</div></div><div class="client-flag">USA 🇺🇸</div></a></div>
            <div class="client-card"><a href="https://github.com/tariqdreamstech" target="_blank" class="client-card-link"><div><div class="client-name">Savvy Programmers ↗</div><div class="client-focus">AI Screening &amp; CSR Workflows</div></div><div class="client-flag">USA 🇺🇸</div></a></div>
            <div class="client-card"><a href="https://github.com/tariqdreamstech" target="_blank" class="client-card-link"><div><div class="client-name">InstaMailAI ↗</div><div class="client-focus">Vector DB &amp; Email Intelligence</div></div><div class="client-flag">USA 🇺🇸</div></a></div>
            <div class="client-card"><a href="https://github.com/tariqdreamstech" target="_blank" class="client-card-link"><div><div class="client-name">Artilence ↗</div><div class="client-focus">Multi-Tenant Agent Backends</div></div><div class="client-flag">USA 🇺🇸</div></a></div>
            <div class="client-card"><a href="https://github.com/tariqdreamstech" target="_blank" class="client-card-link"><div><div class="client-name">Transact Ultd ↗</div><div class="client-focus">Iris CRM &amp; Merchant Onboarding</div></div><div class="client-flag">USA 🇺🇸</div></a></div>
            <div class="client-card"><a href="https://github.com/tariqdreamstech" target="_blank" class="client-card-link"><div><div class="client-name">hddisenos ↗</div><div class="client-focus">Advanced N8N Automations</div></div><div class="client-flag">VEN 🇻🇪</div></a></div>
            <div class="client-card"><a href="https://github.com/tariqdreamstech" target="_blank" class="client-card-link"><div><div class="client-name">QPharma ↗</div><div class="client-focus">ETL &amp; Analytics Architecture</div></div><div class="client-flag">USA 🇺🇸</div></a></div>
            <div class="client-card"><a href="https://github.com/tariqdreamstech" target="_blank" class="client-card-link"><div><div class="client-name">2456.ai ↗</div><div class="client-focus">AI Workflow Platform Backend</div></div><div class="client-flag">USA 🇺🇸</div></a></div>
            <div class="client-card"><a href="https://github.com/tariqdreamstech" target="_blank" class="client-card-link"><div><div class="client-name">Seanz Law Firm ↗</div><div class="client-focus">Legal Interview Intelligence</div></div><div class="client-flag">USA 🇺🇸</div></a></div>
        </div>
    </div>
    <div class="tech-taxonomy">
        <div class="tech-tax-row">
            <div class="tech-tax-lbl">ML, DL &amp; RL:</div>
            <div class="tech-tax-chips">
                <span class="chip chip-purple">Machine Learning</span>
                <span class="chip chip-purple">Deep Learning</span>
                <span class="chip chip-purple">Reinforcement Learning</span>
                <span class="chip chip-purple">PyTorch</span>
                <span class="chip chip-purple">TensorFlow</span>
                <span class="chip chip-purple">DQN / PPO</span>
                <span class="chip">Scikit-Learn</span>
                <span class="chip">Autoencoders</span>
                <span class="chip">CNNs &amp; ViT</span>
                <span class="chip">XGBoost</span>
            </div>
        </div>
        <div class="tech-tax-row">
            <div class="tech-tax-lbl">AI &amp; Multi-Agent:</div>
            <div class="tech-tax-chips">
                <span class="chip chip-cyan">LangGraph Swarms</span>
                <span class="chip chip-cyan">Claude 3.5 Sonnet</span>
                <span class="chip chip-cyan">Gemini 2.5 Flash</span>
                <span class="chip">Pinecone</span>
                <span class="chip">MongoDB Atlas Vector</span>
                <span class="chip">Agentic RAG</span>
                <span class="chip">Explicit Context Caching</span>
            </div>
        </div>
        <div class="tech-tax-row">
            <div class="tech-tax-lbl">Languages &amp; Core:</div>
            <div class="tech-tax-chips">
                <span class="chip chip-accent">Python 3.12</span>
                <span class="chip">FastAPI</span>
                <span class="chip">SQL</span>
                <span class="chip">TypeScript</span>
                <span class="chip">C / C++</span>
                <span class="chip">Bash / BAT</span>
                <span class="chip">AsyncIO</span>
                <span class="chip">ROS / ROS2</span>
            </div>
        </div>
        <div class="tech-tax-row">
            <div class="tech-tax-lbl">Cloud &amp; Infra:</div>
            <div class="tech-tax-chips">
                <span class="chip chip-emerald">GCP Cloud Run</span>
                <span class="chip chip-emerald">Docker Multi-Stage</span>
                <span class="chip">Postgres 18</span>
                <span class="chip">Redis</span>
                <span class="chip">Celery Beat</span>
                <span class="chip">Nginx</span>
                <span class="chip">N8N Enterprise</span>
                <span class="chip">Zero-Trust Vaults</span>
            </div>
        </div>
    </div>
    <div class="doc-footer">
        <div class="doc-footer-left">Ahsan Tariq · <strong>AI Engineer · Forward Deployed Engineer</strong> · <a href="mailto:ahsantariq0724@gmail.com" class="doc-footer-link">ahsantariq0724@gmail.com</a></div>
        <div class="doc-footer-right">PAGE 02 OF {TOTAL_PAGES}</div>
    </div>
</div>
"""

# Pages 3–8: Projects with authentic bullets
page_titles = [
    (3, "FLAGSHIP ENTERPRISE & FINTECH SYSTEMS", "High-Impact FinTech & Enterprise Deployments"),
    (4, "CANDIDATE INTELLIGENCE, SALES AI & MEDIA ENGINES", "Screening Automations, LLM Caching & Autonomous Media"),
    (5, "CUSTOMER SUCCESS, CONTENT AI & MERCHANT ONBOARDING", "Multi-Agent QA, Answer-First SEO & Payment Systems"),
    (6, "DIGITAL OPS TRANSFORMATION & MULTILINGUAL PLATFORMS", "Workflow Modernization, Computer Vision & Zero-Touch Ops"),
    (7, "PROPOSAL GENERATION, VECTOR INTELLIGENCE & CRMS", "LangGraph Streaming, Vector DBs & Enterprise Integrations"),
    (8, "LEGAL TECH, MULTI-TENANT SAAS & DATA ENGINEERING", "Bilingual Legal AI, SaaS Backends & Serverless ETL")
]

for idx, p_group in enumerate(projects_data):
    p_num, sec_title, sec_sub = page_titles[idx]
    list_class = "project-dossier-list-p8" if p_num == 8 else "project-dossier-list"
    html += f"""
<div class="pdf-page">
    <div class="doc-header">
        <div class="doc-header-left">AHSAN TARIQ <span>/</span> {sec_title}</div>
        <div class="doc-header-right">DOSSIER 2026 · SECTION 02</div>
    </div>
    <div class="page-title-block">
        <span class="page-tag">Production Projects &amp; Deployments</span>
        <h2 class="page-title">{sec_sub}</h2>
    </div>
    <div class="{list_class}">
"""
    for proj in p_group:
        bullets_html = "".join([f"<li>{b}</li>" for b in proj['bullets']])
        html += f"""
        <div class="proj-card">
            <div class="proj-card-head">
                <div class="proj-card-title"><a href="{proj['url']}" target="_blank">#{proj['num']}. {h(proj['title'])} <span style="font-size:8px;color:var(--accent);">↗</span></a></div>
                <div class="proj-card-meta">
                    <span class="proj-date">{h(proj['date'])}</span>
                    <span class="proj-badge">{h(proj['badge'])}</span>
                </div>
            </div>
            <div class="proj-org">{h(proj['org'])}</div>
            <div class="proj-tags">{h(proj['tags'])}</div>
            <ul class="proj-bullets">{bullets_html}</ul>
        </div>
"""
    html += f"""
    </div>
    <div class="doc-footer">
        <div class="doc-footer-left">Ahsan Tariq · <strong>AI Engineer · Forward Deployed Engineer</strong> · <a href="mailto:ahsantariq0724@gmail.com" class="doc-footer-link">ahsantariq0724@gmail.com</a></div>
        <div class="doc-footer-right">PAGE {p_num:02d} OF {TOTAL_PAGES}</div>
    </div>
</div>
"""

# Page 9: Academic Research
html += f"""
<div class="pdf-page">
    <div class="doc-header">
        <div class="doc-header-left">AHSAN TARIQ <span>/</span> ACADEMIC RESEARCH &amp; PEER REVIEWER CREDENTIALS</div>
        <div class="doc-header-right">DOSSIER 2026 · SECTION 03</div>
    </div>
    <div class="page-title-block">
        <span class="page-tag">Web of Science Verified Researcher</span>
        <h2 class="page-title">Academic Publications &amp; Peer Review Appointments</h2>
        <p class="page-subtitle">Scholarly contributions in Network Intrusion Detection, Zero-Trust Cryptography, Federated Learning, and Computer Vision defect localization.</p>
    </div>
    <div class="wos-profile-card">
        <div class="wos-info">
            <h3>Verified Academic Peer Reviewer Profile</h3>
            <p>5+ Verified International Journal Peer Reviews &amp; 1 Edited Academic Book · Web of Science &amp; Publons Indexed</p>
        </div>
        <div class="wos-ids">
            <a href="https://www.webofscience.com/wos/author/record/OMK-7734-2025" target="_blank" class="wos-chip-link">WoS: OMK-7734-2025 ↗</a>
            <a href="https://orcid.org/0009-0005-0673-8369" target="_blank" class="wos-chip-link">ORCID: 0009-0005-0673-8369 ↗</a>
        </div>
    </div>
    <div class="reviewer-grid">
        <div class="review-item">
            <div class="review-journal"><a href="https://www.webofscience.com/wos/author/record/OMK-7734-2025" target="_blank">Journal of Engineering Research and Reports ↗</a></div>
            <div class="review-cert-no">Cert No: PRJERR95781EMC · 2026 – 2027</div>
            <div class="review-paper-title">Reviewed: "Secure Secret Platform Migration with Application Continuity in Cloud-Native Systems" (WoS ID: 34272761)</div>
        </div>
        <div class="review-item">
            <div class="review-journal"><a href="https://www.webofscience.com/wos/author/record/OMK-7734-2025" target="_blank">Asian Journal of Economics, Business &amp; Accounting ↗</a></div>
            <div class="review-cert-no">Cert No: PRAJEBAFBE5E3MC · 2026 – 2027</div>
            <div class="review-paper-title">Reviewed: "Automation of Storage Systems and Warehouse Performance in an Emerging Economy" (WoS ID: 33978061)</div>
        </div>
        <div class="review-item">
            <div class="review-journal"><a href="https://www.webofscience.com/wos/author/record/OMK-7734-2025" target="_blank">Asian Journal of Agricultural Extension &amp; Sociology ↗</a></div>
            <div class="review-cert-no">Cert No: PRAJAEES145241AHS · 2025 – 2026</div>
            <div class="review-paper-title">Reviewed: "Identify the Perceived Constraints in the Use of Green Products" (WoS ID: 29505416)</div>
        </div>
    </div>
    <div>
        <div style="font-family: var(--font-heading); font-size: 10.5px; font-weight: 800; color: var(--text-pure); margin-bottom: 1.8mm;">Scholarly Papers, Preprints &amp; Package Publications</div>
        <div class="papers-list">
            <div class="paper-row"><div class="paper-row-left"><div class="paper-title">1. Ranbval Secret Manager: Replacing Plaintext .env Files with Encrypted, Repository-Bound, and Zero-Knowledge Security</div><div class="paper-meta">Ahsan Tariq (Corresponding Author) · Submitted to JISRC (2026) · <a href="https://pypi.org/project/ranbval-sdk/" target="_blank">PyPI</a> &amp; <a href="https://www.npmjs.com/package/ranbval-sdk" target="_blank">npm</a> SDKs (11,500+ DLs)</div></div><span class="paper-badge chip-emerald">SUBMITTED (JISRC)</span></div>
            <div class="paper-row"><div class="paper-row-left"><div class="paper-title">2. ANOVA F-Test Feature Selection for Machine Learning-Based Network Intrusion Detection on the UNSW-NB15 Dataset</div><div class="paper-meta">Ahsan Tariq (Primary Author) · Capstone FYDP funded by Ignite National Technology Fund · <a href="https://doi.org/10.5281/zenodo.12688032" target="_blank">Zenodo DOI ↗</a></div></div><span class="paper-badge chip-accent">FUNDED FYDP</span></div>
            <div class="paper-row"><div class="paper-row-left"><div class="paper-title">3. Trust as a Gate, Not a Weight: Robust Federated Aggregation for Safety-Critical Perception under Natural Heterogeneity</div><div class="paper-meta">Ahsan Tariq (Lead Author) · Submitted to JISRC · Byzantine-Resilient Autonomous Perception</div></div><span class="paper-badge chip-emerald">SUBMITTED (JISRC)</span></div>
            <div class="paper-row"><div class="paper-row-left"><div class="paper-title">4. Three Paradigms, One Benchmark: A Negative-Result Study of Zero-Shot CLIP, Supervised FPN–Attention and Autoencoders on MVTec AD</div><div class="paper-meta">Ahsan Tariq · Industrial Anomaly Detection &amp; Defect Localisation · <a href="https://doi.org/10.5281/zenodo.12688032" target="_blank">Zenodo DOI ↗</a></div></div><span class="paper-badge chip-purple">ZENODO PREPRINT</span></div>
            <div class="paper-row"><div class="paper-row-left"><div class="paper-title">5. Fuzzy Rough Nearest Neighbours Approaches for Emotion Detection in Tweets &amp; PyPI Package (emotion-analysis)</div><div class="paper-meta">Ahsan Tariq · NLP Emotion Classification on SemEval Benchmark · <a href="https://pypi.org/project/emotion-analysis/" target="_blank">emotion-analysis (2,100+ DLs) ↗</a></div></div><span class="paper-badge chip-cyan">PUBLISHED PKG</span></div>
            <div class="paper-row"><div class="paper-row-left"><div class="paper-title">6. ISGC: A Python Package For Summarizing University Student Examination Performance</div><div class="paper-meta">Ahsan Tariq (Corresponding Author) · <a href="https://doi.org/10.5281/zenodo.12688032" target="_blank">Zenodo DOI: 10.5281/zenodo.12688032 ↗</a> · <a href="https://pypi.org/project/isgc/" target="_blank">isgc (1,725+ Downloads) ↗</a></div></div><span class="paper-badge chip-cyan">PUBLISHED (ZENODO)</span></div>
        </div>
    </div>
    <div class="doc-footer">
        <div class="doc-footer-left">Ahsan Tariq · <strong>AI Engineer · Forward Deployed Engineer</strong> · <a href="mailto:ahsantariq0724@gmail.com" class="doc-footer-link">ahsantariq0724@gmail.com</a></div>
        <div class="doc-footer-right">PAGE 09 OF {TOTAL_PAGES}</div>
    </div>
</div>

<!-- PAGE 10: EDUCATION, CREDENTIALS & CLOSING -->
<div class="pdf-page">
    <div class="doc-header">
        <div class="doc-header-left">AHSAN TARIQ <span>/</span> CREDENTIALS, HONORS &amp; EXECUTIVE CONTACT</div>
        <div class="doc-header-right">DOSSIER 2026 · SECTION 04</div>
    </div>
    <div class="page-title-block">
        <span class="page-tag">Academic Pedigree &amp; Industry Accreditations</span>
        <h2 class="page-title">Higher Education, Grants &amp; Verified Certifications</h2>
    </div>
    <div class="edu-block-grid">
        <div class="edu-card">
            <div class="edu-degree">M.S. in Computer Systems Engineering</div>
            <div class="edu-school">The Islamia University of Bahawalpur, Pakistan · Session 2026 – 2028</div>
            <div class="edu-badges-row"><span class="chip chip-purple">In Progress</span><span class="chip">Distributed Systems Focus</span><span class="chip">Zero-Trust Cryptography</span></div>
            <p class="edu-desc">Postgraduate research focusing on Distributed Microservice Runtimes, Advanced Machine Learning, Encrypted Zero-Trust Infrastructures, and Autonomous Multi-Agent Robotics.</p>
        </div>
        <div class="edu-card">
            <div class="edu-degree">B.S. in Computer Systems Engineering</div>
            <div class="edu-school">The Islamia University of Bahawalpur, Pakistan · Graduated 2020 – 2024</div>
            <div class="edu-badges-row"><span class="chip chip-emerald">CGPA: 3.40 / 4.00 (79.16%)</span><span class="chip">141 Credit Hours</span><span class="chip">42 Courses</span></div>
            <p class="edu-desc">Comprehensive 4-year engineering curriculum. Awarded Ignite National Technology Fund Grant for Capstone FYDP on ML-driven Network Intrusion Detection Systems (NIDS).</p>
        </div>
    </div>
    <div class="awards-grid">
        <div class="award-box">
            <div class="award-tag">INTERNATIONAL GRANT · 2026</div>
            <a href="https://nlnet.nl/codesupply/eligibility" target="_blank" style="color:inherit;text-decoration:none;"><div class="award-name">NLnet Foundation Research Grant ↗</div></a>
            <div class="award-org">NLnet Foundation (Netherlands) · NGI Zero-Trust. In two-round review for Ranbval Secret Manager self-hostable control plane.</div>
        </div>
        <div class="award-box">
            <div class="award-tag">NATIONAL RESEARCH GRANT · 2024</div>
            <a href="https://ignite.org.pk/" target="_blank" style="color:inherit;text-decoration:none;"><div class="award-name">Ignite National Technology Fund ↗</div></a>
            <div class="award-org">Ministry of IT &amp; Telecom, Govt. of Pakistan. Competitively selected and funded for Capstone ML-based Network Intrusion Detection.</div>
        </div>
        <div class="award-box">
            <div class="award-tag">ACADEMIC MERIT AWARD</div>
            <div class="award-name">PMYP Laptop Scheme Selection</div>
            <div class="award-org">Prime Minister's Youth Programme. Awarded high-performance workstation under national competitive merit standing for academic excellence.</div>
        </div>
    </div>
    <div class="certs-grid-p10">
        <div class="cert-col">
            <div class="cert-col-title">Machine Learning &amp; AI</div>
            <a href="https://www.kaggle.com/learn/certification/engrahsantariq/feature-engineering" target="_blank" class="cert-item-link">Feature Engineering (Kaggle Learn) ↗</a>
            <a href="https://www.kaggle.com/learn/certification/engrahsantariq/intermediate-machine-learning" target="_blank" class="cert-item-link">Intermediate ML (Kaggle Learn) ↗</a>
            <a href="https://www.kaggle.com/learn/certification/engrahsantariq/intro-to-machine-learning" target="_blank" class="cert-item-link">Intro to Machine Learning (Kaggle Learn) ↗</a>
        </div>
        <div class="cert-col">
            <div class="cert-col-title">Data Analytics &amp; BI</div>
            <a href="https://www.freecodecamp.org/certification/ahsantariq0724/data-analysis-with-python-v7" target="_blank" class="cert-item-link">Data Analysis with Python (freeCodeCamp) ↗</a>
            <a href="https://drive.google.com/file/d/1jgeW-fB1xhlVXRipIRsGPDylvBQh6Gkj/view?usp=sharing" target="_blank" class="cert-item-link">Data Mining &amp; BI (NAVTTC) ↗</a>
            <a href="https://www.kaggle.com/learn/certification/engrahsantariq/data-visualization" target="_blank" class="cert-item-link">Data Visualization (Kaggle Learn) ↗</a>
        </div>
        <div class="cert-col">
            <div class="cert-col-title">Databases &amp; Infrastructure</div>
            <a href="https://www.kaggle.com/learn/certification/engrahsantariq/intro-to-sql" target="_blank" class="cert-item-link">Intro to SQL &amp; Advanced SQL (Kaggle Learn) ↗</a>
            <a href="https://github.com/tariqdreamstech" target="_blank" class="cert-item-link">GCP Cloud Run &amp; Docker Multi-Stage ↗</a>
            <a href="https://github.com/tariqdreamstech" target="_blank" class="cert-item-link">N8N Enterprise Automation Specialist ↗</a>
        </div>
    </div>
    <div class="closing-dossier">
        <h3>Let's Build the Next Extraordinary System Together</h3>
        <p>Available for forward deployed engineering engagements, enterprise AI systems architecture, and technical consulting worldwide.</p>
        <div class="closing-links">
            <a href="mailto:ahsantariq0724@gmail.com" class="closing-link">📧 ahsantariq0724@gmail.com</a>
            <a href="https://www.linkedin.com/in/ahsan-tariq-comp-engr/" target="_blank" class="closing-link">🔗 linkedin.com/in/ahsan-tariq-comp-engr</a>
            <a href="https://github.com/ahsantariq7" target="_blank" class="closing-link">💻 github.com/ahsantariq7</a>
            <a href="https://github.com/tariqdreamstech" target="_blank" class="closing-link">🌐 tariqdreamstech</a>
        </div>
    </div>
    <div class="doc-footer">
        <div class="doc-footer-left">Ahsan Tariq · <strong>AI Engineer · Forward Deployed Engineer</strong> · <a href="mailto:ahsantariq0724@gmail.com" class="doc-footer-link">ahsantariq0724@gmail.com</a></div>
        <div class="doc-footer-right">PAGE 10 OF {TOTAL_PAGES}</div>
    </div>
</div>

</body>
</html>
"""

with open('portfolio-pdf.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Generated portfolio-pdf.html successfully. Size:", len(html), "bytes")
