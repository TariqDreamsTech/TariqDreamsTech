import base64
import os

with open('prof.jpeg', 'rb') as f:
    prof_b64 = base64.b64encode(f.read()).decode('utf-8')

TOTAL_PAGES = 12
BASE_URL = "https://ahsantariq.ranbval.com"

# The 23 Flagship Case Studies + Key Proprietary Systems
# Structured across Pages 3 to 10 (2 to 3 projects per page)
projects_pages = [
    # Page 3: Enterprise & Financial Logistics (Projects 01, 02, 03)
    {
        "title": "Enterprise & Core Infrastructure",
        "subtitle": "High-throughput financial engines, multi-tenant enterprise ERP portals, and cryptographic vaults",
        "projects": [
            {
                "num": "01",
                "title": "Volvexer — Global Multi-Ledger Accounting & Tax Reconciliation",
                "slug": "",
                "custom_url": "https://www.volvexer.com/",
                "org": "Volvexer · Global Financial Services (USA, UK, Australia, Pakistan)",
                "date": "2024 – Present",
                "badge": "Enterprise Platform",
                "badge_color": "#10b981",
                "tags": "Multi-Ledger Sync · QuickBooks · Xero · NetSuite · Zoho Books · Python · OCR · Tax Vault",
                "plain_english": "Accountants spend dozens of hours every week re-typing numbers between QuickBooks, Xero, and bank feeds. Built an automated financial brain that syncs bank transactions, reads messy receipts with AI, and prepares tax reconciliation reports across US, UK, and Australian tax laws with zero human data entry.",
                "tech_bullets": [
                    "<strong>Multi-Ledger Integration:</strong> Bi-directional sync pipelines for QuickBooks, Xero, NetSuite, and Zoho Books with automated forex conversion.",
                    "<strong>Automated OCR Intake:</strong> Machine learning document classifier splitting multi-currency invoices and bills, cutting month-end closing by 75%."
                ]
            },
            {
                "num": "02",
                "title": "Ambica International (Dovetail) — Healthcare Logistics & ERP Backbone",
                "slug": "ambica-dovetail",
                "org": "Ambica International · United States (Remote)",
                "date": "2025 – 2026",
                "badge": "Live Production",
                "badge_color": "#10b981",
                "tags": "GCP Cloud Run · NetSuite SuiteQL · Cartrack GPS · DocuSign · FastAPI · PostgreSQL · Redis",
                "plain_english": "Hospitals and pharmacies need urgent medical deliveries without delay. Transformed paper clipboard tracking into a 100% digital portal: live GPS tracking for 102 delivery trucks, instant sync with NetSuite for $141M in medicine orders, and 60-second digital contract approvals via DocuSign.",
                "tech_bullets": [
                    "<strong>Sub-Second NetSuite Mirror:</strong> 20-stream SuiteQL pipeline syncing 51,462 invoices and 35,935 purchase orders with live 3-second P&L ticking.",
                    "<strong>Zero-Trust Server Bridge:</strong> 3-layer OTP authentication vault protecting on-premise physical databases with strict IP and attempt limits."
                ]
            },
            {
                "num": "03",
                "title": "Ranbval Core & Secret Manager — Zero-Knowledge Cryptographic Vault",
                "slug": "ranbval-core",
                "org": "Ranbval Security Platform · Global Enterprise SaaS",
                "date": "2025 – Present",
                "badge": "NLnet Grant Award",
                "badge_color": "#38bdf8",
                "tags": "AES-256-GCM · ChaCha20Poly1305 · PyPI & npm SDKs · Zero-Trust · Schema Contracts",
                "plain_english": "Companies frequently leak sensitive passwords and API keys stored in plain text configuration files. Built an ultra-secure digital vault that encrypts secrets using military-grade cryptography, delivers keys in under 2 milliseconds, and shuts down instantly if tampering is detected. Awarded an EU NLnet Foundation grant.",
                "tech_bullets": [
                    "<strong>Hardware-Grade Encryption:</strong> AES-256-GCM and ChaCha20Poly1305 with offline verification and repo-bound cryptographic access tokens.",
                    "<strong>High-Adoption SDKs:</strong> Authored open-source libraries on PyPI and npm with 11,500+ global downloads and sub-2ms pure ASGI decryption."
                ]
            }
        ]
    },

    # Page 4: Autonomous Voice Agents & Accounting (Projects 04, 05, 06)
    {
        "title": "Autonomous Voice AI & Accounting Automation",
        "subtitle": "Natural voice phone specialists, automated appointment booking, and multi-system invoice reconciliation",
        "projects": [
            {
                "num": "04",
                "title": "Transact ULTD — Sub-Second Voice AI & Automated Merchant Engine",
                "slug": "transact-ultd",
                "org": "Transact ULTD · Financial Technology (USA)",
                "date": "2025 – 2026",
                "badge": "Voice AI · Live",
                "badge_color": "#f59e0b",
                "tags": "Retell AI · LiveKit WebRTC · Twilio Trunking · FastAPI · HubSpot · Python",
                "plain_english": "Credit card payment companies lose leads when callers wait on hold. Built a human-sounding AI voice agent that calls incoming merchant leads in under 60 seconds, calculates how much money they save on credit card processing fees, and transfers complex calls seamlessly to human specialists.",
                "tech_bullets": [
                    "<strong>Sub-600ms Voice Turnaround:</strong> Retell AI and LiveKit WebRTC audio pipeline maintaining natural conversational tempo without unnatural pauses.",
                    "<strong>Automated Lifecycle Engine:</strong> Automatically parses merchant processing statements, creates CRM profiles, and triggers statement upload emails."
                ]
            },
            {
                "num": "05",
                "title": "Terry Properties — AI Accounting & Multi-System Synchronization",
                "slug": "terry-accounting",
                "org": "Terry Real Estate Management · United States (Remote)",
                "date": "2024 – 2025",
                "badge": "Production System",
                "badge_color": "#10b981",
                "tags": "GPT-4o Vision · QuickBooks Online · Buildium REST API · Celery · Redis",
                "plain_english": "Property managers were spending 25+ hours every week manually typing invoices from messy emails and WhatsApp photos into QuickBooks and Buildium. Built an AI accountant that reads any photo or PDF bill, checks that it hasn't been paid already, and posts it accurately across both accounting systems without human error.",
                "tech_bullets": [
                    "<strong>Dual-System Ledger Mirror:</strong> Real-time REST pipeline synchronizing invoices between Buildium and QuickBooks Online with conflict resolution.",
                    "<strong>Intelligent OCR & Deduplication:</strong> Vision-based invoice parser extracting line items, tax IDs, and GL codes with 99.4% validation accuracy."
                ]
            },
            {
                "num": "06",
                "title": "Django Voice Agent — Phone AI & Autonomous Meeting Summarizer",
                "slug": "django-voice-agent",
                "org": "Enterprise Sales Infrastructure · Commercial System",
                "date": "2025 – 2026",
                "badge": "Autonomous Agent",
                "badge_color": "#38bdf8",
                "tags": "Twilio SIP · Deepgram Nova-2 · Claude 3.5 Sonnet · ElevenLabs · Google Calendar",
                "plain_english": "Sales reps waste hours dialing cold leads and coordinating calendars. Built an autonomous AI phone assistant that calls prospects, talks naturally, checks live team availability, and books video calls on Zoom or Google Meet. When meetings finish, an AI bot delivers concise action items directly to Slack.",
                "tech_bullets": [
                    "<strong>Full-Duplex Voice Pipeline:</strong> Real-time streaming combining Deepgram Nova-2 speech-to-text, Claude reasoning, and ElevenLabs low-latency voice.",
                    "<strong>Autonomous Scheduling:</strong> Resolves multi-attendee calendar conflicts, sends invites, and logs structured conversation summaries into CRM."
                ]
            }
        ]
    },

    # Page 5: Digital Twins, Clinic Intake & Customer Portals (Projects 07, 08, 09)
    {
        "title": "Interactive AI, Digital Twins & Booking Engines",
        "subtitle": "Real-time avatar synthesis, deterministic patient intake workflows, and conversational reservations",
        "projects": [
            {
                "num": "07",
                "title": "Qira AI — Real-Time Avatar Intelligence & Social Digital Twins",
                "slug": "qira-ai",
                "org": "Qira AI · United States & Global",
                "date": "2024 – 2025",
                "badge": "Consumer AI Platform",
                "badge_color": "#ec4899",
                "tags": "WebRTC · 3D Avatar Rendering · Lip-Sync Telemetry · Multilingual STT · Redis",
                "plain_english": "Anyone can create a speaking 3D digital clone of themselves from just one selfie and voice sample. Friends can video call, chat, and play games with the digital twin, which talks authentically in their real voice and can even hang out with friends automatically when the real user is asleep or busy.",
                "tech_bullets": [
                    "<strong>Sub-Second Video Synthesis:</strong> Real-time lip-synchronization and facial animation streamed over WebRTC with sub-800ms round-trip latency.",
                    "<strong>Autonomous Persona Engine:</strong> Memory-backed vector store preserving personality, conversational style, and user preferences across languages."
                ]
            },
            {
                "num": "08",
                "title": "Petroski Physiotherapy — Deterministic Marketing & Clinic Governance",
                "slug": "petroski-physio",
                "org": "Petroski Physio Clinic · Sports Rehabilitation (USA)",
                "date": "2025",
                "badge": "Healthcare Automation",
                "badge_color": "#10b981",
                "tags": "Slack API · Trello REST API · Webhook Router · Python FastAPI · Deterministic Logic",
                "plain_english": "Sports therapists were constantly interrupted during patient appointments by marketers asking which athletes could be filmed for social media. Automated a polite Slack message to therapists 24 hours after a patient's evaluation; clicking a simple 'Yes/No' button updates marketing's board instantly without any office interruption.",
                "tech_bullets": [
                    "<strong>Two-Board Deterministic Architecture:</strong> Strict separation of clinical medical intake and marketing cards with zero PHI / HIPAA leakage.",
                    "<strong>Timed Slack Interactivity:</strong> Automated 24-hour evaluation triggers with single-click interactive buttons updating Trello card state in real time."
                ]
            },
            {
                "num": "09",
                "title": "Ballyhass Adventure Park — Autonomous Booking & Availability Engine",
                "slug": "ballyhass-booking",
                "org": "Ballyhass Outdoor Adventure · Ireland / Europe",
                "date": "2024 – 2025",
                "badge": "Commercial Chatbot",
                "badge_color": "#f59e0b",
                "tags": "Voiceflow · N8N Enterprise · FareHarbor REST API · Redis Cache · PostgreSQL",
                "plain_english": "Visitors to a busy outdoor adventure park struggled to find open time slots across different lakes and activities. Built a smart chatbot that understands everyday questions like 'Any spots next Friday for wakeboarding?', checks live tickets in 0.4 seconds, and lets families reserve instantly.",
                "tech_bullets": [
                    "<strong>Live Availability Polling:</strong> High-speed integration with FareHarbor booking API returning real-time ticket slots with sub-500ms response times.",
                    "<strong>Conversational Entity Extractor:</strong> Translates conversational date/time requests into deterministic booking parameters with 1-click checkout."
                ]
            }
        ]
    },

    # Page 6: Sales Intelligence, Private Cloud & Hollywood Systems (Projects 10, 11, 12)
    {
        "title": "Sales Intelligence & Cloud Automation Engines",
        "subtitle": "Gemini context caching, self-hosted multi-CRM automation clouds, and film production telematics",
        "projects": [
            {
                "num": "10",
                "title": "Prospect Intelligence Engine — Sales AI with Google Context Caching",
                "slug": "prospect-intelligence",
                "org": "Enterprise Sales Intelligence · Contract Engagement",
                "date": "2025 – 2026",
                "badge": "Enterprise AI",
                "badge_color": "#38bdf8",
                "tags": "Google Gemini 2.5 · /cachedContents API · N8N · PostgreSQL · Redis",
                "plain_english": "Sales reps wasted 10 minutes digging through old call transcripts, LinkedIn posts, and client PDFs before answering buyer questions. Built an AI sales assistant that remembers the client's entire history using Google server caching, cutting AI bills by 90% and answering in less than 1 second.",
                "tech_bullets": [
                    "<strong>Explicit Context Caching:</strong> Gemini <code>/v1beta/cachedContents</code> integration caching 100,000+ tokens, reducing API costs by 90%.",
                    "<strong>4-Case Routing Engine:</strong> Automated cache lifecycle manager handling creation, hydration, TTL expiration, and cold fallback."
                ]
            },
            {
                "num": "11",
                "title": "hddisenos — Self-Hosted Cloud Automation & Multi-CRM Synchronization",
                "slug": "hddisenos-automation",
                "org": "hddisenos Creative & Industrial Agency · International",
                "date": "2025",
                "badge": "Self-Hosted Cloud",
                "badge_color": "#10b981",
                "tags": "Coolify Cloud · N8N Dedicated · HubSpot · Zoho CRM · PostgreSQL · Google AI",
                "plain_english": "Commercial automation websites charge for every click and transfer, costing thousands every month. Built a private automation cloud on dedicated servers that runs 57 business operations—generating AI pet artwork, posting cars to Facebook for dealerships, and syncing customer records across HubSpot and Zoho.",
                "tech_bullets": [
                    "<strong>Private Server Architecture:</strong> Deployed containerized N8N and PostgreSQL on dedicated Coolify cloud, eliminating recurring SaaS fees.",
                    "<strong>Multi-CRM Webhook Hub:</strong> Resilient two-way synchronization bridging HubSpot and regional Zoho CRM instances with zero data loss."
                ]
            },
            {
                "num": "12",
                "title": "CoreImmersive — Hollywood Call Sheet Parsing & Set Telematics",
                "slug": "coreimmersive-film",
                "org": "CoreImmersive Productions · Hollywood / Los Angeles (Remote)",
                "date": "2024 – 2025",
                "badge": "Media Production AI",
                "badge_color": "#ec4899",
                "tags": "FastAPI · PyPDF · Claude 3.5 Sonnet · OpenWeather Telematics · Celery",
                "plain_english": "Hollywood movie sets operate off complicated 20-page daily schedules emailed late at night. Built an AI platform that reads messy schedule PDFs in seconds, organizes actor call times and shooting locations, and watches weather satellites to warn directors before rain hits outdoor movie sets.",
                "tech_bullets": [
                    "<strong>Messy PDF Extraction:</strong> Multi-column regex and LLM parsing pipeline extracting actor arrival times, locations, and equipment lists.",
                    "<strong>Predictive Weather Telematics:</strong> Satellite radar monitoring issuing automatic alerts 90 minutes before rain hits outdoor filming sets."
                ]
            }
        ]
    },

    # Page 7: AI Platforms, Clinical Data Lakes & Legal Tech (Projects 13, 14, 15)
    {
        "title": "Scalable Platforms, Clinical Data & Legal AI",
        "subtitle": "Microservice AI tool directories, cold-chain pharma data lakes, and multilingual immigration intake",
        "projects": [
            {
                "num": "13",
                "title": "2456.ai — Autonomous AI Tool Discovery & Scalable Microservices",
                "slug": "2456-ai-platform",
                "org": "2456.ai · United States (Remote)",
                "date": "2023 – 2024",
                "badge": "SaaS Microservices",
                "badge_color": "#38bdf8",
                "tags": "Django Core · FastAPI Microservices · Pinecone Vector DB · PostgreSQL · Stripe",
                "plain_english": "With thousands of AI tools launched every month, businesses struggle to find what works. Built a smart platform that analyzes AI tools, tests their capabilities, and routes user questions to the best tool with sub-second response times and automated subscription billing.",
                "tech_bullets": [
                    "<strong>Hybrid Microservice Architecture:</strong> Django state management combined with decoupled FastAPI services for high-speed AI evaluations.",
                    "<strong>Vector Search & Stripe:</strong> Pinecone vector embeddings for semantic tool recommendations and Stripe webhooks for tier-based billing."
                ]
            },
            {
                "num": "14",
                "title": "QPharma Global — Cloud Data Lake & Cold-Chain Telemetry Pipeline",
                "slug": "qpharma-data-platform",
                "org": "QPharma Global · United States (Remote)",
                "date": "2022",
                "badge": "Enterprise Data Lake",
                "badge_color": "#10b981",
                "tags": "AWS Glue · S3 Data Lake · AWS Lambda · Pandas · Athena SQL · CloudWatch",
                "plain_english": "Sensitive medicines spoil if they get too warm during international shipping. Built an automated cloud data pipeline that ingests millions of shipment temperature logs and sales records, instantly spotting damaged batches and cutting data reporting time by 70%.",
                "tech_bullets": [
                    "<strong>Serverless ETL Engine:</strong> AWS Glue and Lambda pipeline ingesting gigabytes of cold-chain telemetry and sales spreadsheets into S3.",
                    "<strong>Fast Analytical Querying:</strong> Cleaned columnar data partitioned for Amazon Athena, enabling sub-second compliance and audit reporting."
                ]
            },
            {
                "num": "15",
                "title": "Sean Z & Associates — Multilingual AI Legal Intake Architecture",
                "slug": "seanz-law-firm",
                "org": "Sean Z & Associates · Law Practice (USA)",
                "date": "2024",
                "badge": "Legal AI Assistant",
                "badge_color": "#f59e0b",
                "tags": "Twilio Voice · WhatsApp Business API · OpenAI GPT-4 · Google Looker Studio",
                "plain_english": "Immigration lawyers spend hours asking the same initial intake questions in English and Spanish. Built a bilingual AI legal assistant on WhatsApp and phone that interviews potential clients, extracts key case details, and prepares organized client files while keeping all data strictly private.",
                "tech_bullets": [
                    "<strong>Bilingual Conversational Intake:</strong> Real-time Spanish/English qualification extracting family history and visa eligibility facts.",
                    "<strong>Privilege-Bound Security:</strong> Zero-retention AI prompts and encrypted storage ensuring strict attorney-client privilege compliance."
                ]
            }
        ]
    },

    # Page 8: Multi-Cloud Orchestration, Vector Search & Social Platform (Projects 16, 17, 18)
    {
        "title": "Multi-Cloud Orchestration, Vector DBs & Super-Systems",
        "subtitle": "Autonomous cloud cost optimizers, semantic RAG email engines, and 16-pillar collaborative ecosystems",
        "projects": [
            {
                "num": "16",
                "title": "Jericho AI — Autonomous GenAI Ops & Multi-Cloud Orchestrator",
                "slug": "jericho-ai-multicloud",
                "org": "Jericho AI · Florida, United States",
                "date": "2024 – 2025",
                "badge": "Multi-Cloud Platform",
                "badge_color": "#38bdf8",
                "tags": "AWS · Azure · GCP · IBM Cloud · OCI · Autonomous Multi-Agent Swarm · FinOps",
                "plain_english": "Companies waste thousands of dollars leaving idle servers running across AWS, Google Cloud, and Azure. Built a smart multi-cloud platform where autonomous AI agents continuously monitor server health, detect wasted computing power, and optimize cloud workloads in real time without human delay.",
                "tech_bullets": [
                    "<strong>Unified Cloud Abstraction:</strong> Unified control plane orchestrating resources across AWS, Azure, GCP, IBM, and Oracle Cloud (OCI).",
                    "<strong>Multi-Agent FinOps Swarm:</strong> Coordinated AI agent system predicting cost waste and executing automated scaling without service downtime."
                ]
            },
            {
                "num": "17",
                "title": "InstaMailAI — Scalable Vector Database & Semantic RAG Email Engine",
                "slug": "instamail-ai",
                "org": "InstaMailAI · United States (Remote)",
                "date": "2025",
                "badge": "Vector Search RAG",
                "badge_color": "#10b981",
                "tags": "MongoDB Atlas Vector Search · OpenAI Embeddings · LangChain · FastAPI · HNSW Index",
                "plain_english": "Traditional email search only works if you remember the exact words used months ago. Built a smart vector search brain that understands the underlying meaning of emails, allowing business teams to find past discussions instantly and draft perfectly contextual replies.",
                "tech_bullets": [
                    "<strong>Dense Vector Search Pipeline:</strong> MongoDB Atlas Vector Search indexing high-dimensional email embeddings with sub-50ms query latency.",
                    "<strong>Real-Time RAG Synthesis:</strong> Context-grounded draft generator reducing email response time by 80% with zero hallucination."
                ]
            },
            {
                "num": "18",
                "title": "Ranbval Social Super-System — 16-Pillar Collaborative Ecosystem",
                "slug": "ranbval-social",
                "org": "Ranbval Platform · Lead Architect",
                "date": "2024 – Present",
                "badge": "Proprietary Ecosystem",
                "badge_color": "#ec4899",
                "tags": "FastAPI · WebSocket · React · WebRTC · Redis Sentinel · Single Secure Root",
                "plain_english": "Modern teams struggle using 10 different apps for chat, tasks, video calls, and files. Built a unified platform that combines encrypted real-time chat, automated AI assistants, private file vaults, and team collaboration into one seamless application running under a single secure web address.",
                "tech_bullets": [
                    "<strong>Unified Single-Root Platform:</strong> 16 integrated modules sharing a unified authentication session and cryptographic access token layer.",
                    "<strong>Real-Time WebSocket Fabric:</strong> Sub-50ms live chat, presence telemetry, and ephemeral conference calls powered by Redis Sentinel."
                ]
            }
        ]
    },

    # Page 9: Peer-Reviewed AI Research & Cybersecurity (Projects 19, 20, 21)
    {
        "title": "Peer-Reviewed AI Research & Cybersecurity",
        "subtitle": "Zero-shot manufacturing defect benchmarks, poisoning-resistant federated learning, and high-speed NIDS",
        "projects": [
            {
                "num": "19",
                "title": "Industrial Defect Localization — Zero-Shot vs Few-Shot Benchmark",
                "slug": "mvtec-defect-benchmark",
                "org": "Computer Vision & Industrial AI Research · Sole Author: Ahsan Tariq",
                "date": "2025 – 2026",
                "badge": "Academic Research",
                "badge_color": "#a855f7",
                "tags": "MVTec AD Dataset · CLIP · DINOv2 · Segment Anything (SAM) · PRO-AUC · PyTorch",
                "plain_english": "Factory assembly lines lose money when cameras miss defective parts or when AI requires thousands of defect photos to learn. Evaluated 3 modern AI vision paradigms across 15 manufacturing categories (5,354 images), proving which model spots microscopic flaws with zero prior training data.",
                "tech_bullets": [
                    "<strong>Comprehensive 15-Category Tour:</strong> Benchmark across 10 rigid objects and 5 non-rigid textures measuring Image-AUC and Pixel-PRO.",
                    "<strong>Empirical Anomaly Map Analysis:</strong> Validated boundary localization trade-offs between vision-language models and foundation features."
                ]
            },
            {
                "num": "20",
                "title": "Robust Federated Learning — Defense Against Edge Model Poisoning",
                "slug": "robust-federated-perception",
                "org": "Distributed AI & Privacy-Preserving Research · Sole Author: Ahsan Tariq",
                "date": "2025 – 2026",
                "badge": "Academic Research",
                "badge_color": "#38bdf8",
                "tags": "Trust-Gated Aggregation · Cosine Similarity · Byzantine Defense · Edge Networks",
                "plain_english": "Hospitals or self-driving car fleets can train a shared AI together without sharing private patient or location data. Built a mathematical trust guard that inspects updates from every computer, instantly spotting and kicking out hacked or malicious nodes trying to poison the AI.",
                "tech_bullets": [
                    "<strong>Trust as a Gate Protocol:</strong> Binary admission filter gating model weights based on historical angle and gradient alignment.",
                    "<strong>99.1% Poisoning Mitigation:</strong> Maintained high perceptual accuracy under adversarial Byzantine attacks where standard FedAvg failed."
                ]
            },
            {
                "num": "21",
                "title": "High-Throughput Network Intrusion Detection — ANOVA F-Test NIDS",
                "slug": "unsw-intrusion-detection",
                "org": "Cybersecurity & Machine Learning Research · Sole Author: Ahsan Tariq",
                "date": "2025 – 2026",
                "badge": "Academic Research",
                "badge_color": "#10b981",
                "tags": "UNSW-NB15 Dataset · ANOVA F-Test · Gaussian Naive Bayes · XGBoost · 98.67% Acc",
                "plain_english": "Modern network firewalls get overwhelmed trying to analyze dozens of technical parameters for every packet. Engineered a high-speed cybersecurity pipeline using statistical math to eliminate 70% of network clutter, detecting cyberattacks with 98.67% accuracy in less than a millisecond.",
                "tech_bullets": [
                    "<strong>69.4% Dimensionality Reduction:</strong> Selected 15 top-ranked ANOVA flow features from 49 raw attributes without losing attack signal.",
                    "<strong>State-of-the-Art Speed:</strong> 98.67% binary detection accuracy via variance-smoothed Gaussian Naive Bayes, outperforming complex neural models."
                ]
            }
        ]
    },

    # Page 10: Autonomous Field Robotics & UAV Flight Systems (Projects 22, 23)
    {
        "title": "Field Robotics & Autonomous UAV Flight Control",
        "subtitle": "Rugged ground robot SLAM navigation, cascade PID drone flight dynamics, and smart wheelchair autonomy",
        "projects": [
            {
                "num": "22",
                "title": "Clearpath Husky A200 UGV — Autonomous SLAM & Dijkstra Navigation",
                "slug": "husky-slam-navigation",
                "org": "Field Robotics & Autonomous Ground Systems · Clearpath Robotics",
                "date": "2025 – 2026",
                "badge": "Field Robotics",
                "badge_color": "#f59e0b",
                "tags": "ROS Navigation Stack · Gmapping SLAM · Dijkstra Planner · DWA Local · Odometry · Gazebo",
                "plain_english": "Built an autonomous brain for a heavy-duty 4x4 outdoor robot (Clearpath Husky). The robot navigates through unmapped hazardous environments, creates a digital 2D map in real time using laser scans, and drives safely to mission waypoints without human remote control.",
                "tech_bullets": [
                    "<strong>20mm Occupancy Grid SLAM:</strong> Rao-Blackwellized particle filter SLAM with calibrated differential skid-steer odometry (wheel base 1.07m).",
                    "<strong>Dynamic Obstacle Avoidance:</strong> Dual-layer costmap inflation combined with Dijkstra global planning and Dynamic Window local control."
                ]
            },
            {
                "num": "23",
                "title": "Hector Quadrotor UAV & Smart Wheelchair — Flight Dynamics & Autonav",
                "slug": "hector-quadrotor-uav",
                "org": "Aerial Robotics & Autonomous Assistive Mobility · ROS & Gazebo 3D",
                "date": "2025 – 2026",
                "badge": "Aerial & Ground Robotics",
                "badge_color": "#38bdf8",
                "tags": "Hector Quadrotor · Cascade PID Flight Controller · Gazebo 6-DOF · Smart Wheelchair Autonav",
                "plain_english": "Engineered two high-precision autonomous robotics systems: 1) An autonomous quadrotor drone that takes off, hovers steadily in mid-air with sub-5cm altitude error, and follows complex 3D waypoints. 2) A self-driving smart wheelchair that maneuvers through narrow hospital doorways and corridors with zero collisions.",
                "tech_bullets": [
                    "<strong>100 Hz Cascade Flight Controller:</strong> Inner-loop attitude rate PID coupled with outer-loop position guidance and automatic motor arming guard.",
                    "<strong>Assistive Corridor Trajectory:</strong> Dynamic laser scan envelope maintaining safe wall clearance in constrained indoor environments."
                ]
            }
        ]
    }
]

# Generate HTML
html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Ahsan Tariq — Master Executive Portfolio Dossier</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Outfit:wght@400;500;600;700;800&family=Plus+Jakarta+Sans:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500;600&display=swap" rel="stylesheet">
<style>
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
    --bg-dark: #07090e;
    --card-bg: #0d111a;
    --card-surface: #131824;
    --accent: #ffba49;
    --cyan: #38bdf8;
    --emerald: #10b981;
    --purple: #a855f7;
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
    background: #07090e;
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
    padding: 9mm 12mm 9mm 12mm;
    page-break-after: always;
    position: relative;
    overflow: hidden;
    background: #07090e;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
}}

/* Top Page Header */
.doc-header {{
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding-bottom: 6px;
    border-bottom: 1px solid rgba(255, 255, 255, 0.08);
    margin-bottom: 9px;
    font-size: 7.2px;
    color: var(--text-dim);
    letter-spacing: 0.5px;
    text-transform: uppercase;
    font-family: var(--font-heading);
    font-weight: 600;
}}
.doc-header-brand {{
    color: var(--accent);
    font-weight: 700;
}}
.doc-header a {{
    color: var(--cyan);
    text-decoration: none;
}}

/* Bottom Page Footer */
.doc-footer {{
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding-top: 6px;
    border-top: 1px solid rgba(255, 255, 255, 0.08);
    margin-top: 9px;
    font-size: 7.2px;
    color: var(--text-dim);
    font-family: var(--font-mono);
}}
.doc-footer a {{
    color: var(--cyan);
    text-decoration: none;
}}

/* Section Titles */
.page-title-block {{
    margin-bottom: 10px;
}}
.page-title-badge {{
    display: inline-block;
    padding: 2px 7px;
    border-radius: 20px;
    background: rgba(255, 186, 73, 0.12);
    border: 1px solid rgba(255, 186, 73, 0.35);
    color: var(--accent);
    font-size: 7px;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.6px;
    margin-bottom: 3px;
}}
.page-title-block h2 {{
    font-family: var(--font-heading);
    font-size: 15px;
    font-weight: 800;
    color: #ffffff;
    line-height: 1.2;
    margin-bottom: 2px;
}}
.page-title-block p {{
    font-size: 8px;
    color: var(--text-muted);
}}

/* Project Cards */
.projects-container {{
    display: flex;
    flex-direction: column;
    gap: 9px;
    flex-grow: 1;
}}
.project-card {{
    background: var(--card-bg);
    border: 1px solid var(--border);
    border-radius: 7px;
    padding: 9px 11px;
    display: flex;
    flex-direction: column;
    gap: 4px;
    border-left: 3px solid var(--accent);
}}
.project-card-header {{
    display: flex;
    justify-content: space-between;
    align-items: flex-start;
}}
.project-card-num-title {{
    display: flex;
    align-items: center;
    gap: 6px;
}}
.project-card-num {{
    font-family: var(--font-mono);
    font-size: 10px;
    font-weight: 800;
    color: var(--accent);
    background: rgba(255, 186, 73, 0.1);
    padding: 2px 5px;
    border-radius: 4px;
}}
.project-card-title {{
    font-family: var(--font-heading);
    font-size: 10.5px;
    font-weight: 700;
    color: #ffffff;
}}
.project-card-badge {{
    font-size: 7px;
    font-weight: 700;
    padding: 2px 6px;
    border-radius: 4px;
    text-transform: uppercase;
    white-space: nowrap;
}}
.project-card-meta {{
    font-size: 7.2px;
    color: var(--text-dim);
    display: flex;
    gap: 12px;
}}
.project-card-meta strong {{
    color: var(--text-secondary);
}}
.plain-box {{
    background: rgba(56, 189, 248, 0.05);
    border: 1px solid rgba(56, 189, 248, 0.2);
    border-radius: 5px;
    padding: 5px 8px;
    margin: 2px 0;
}}
.plain-box-label {{
    color: var(--cyan);
    font-size: 6.8px;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    margin-bottom: 2px;
    display: flex;
    align-items: center;
    gap: 4px;
}}
.plain-box p {{
    font-size: 7.8px;
    color: #e2e8f0;
    line-height: 1.4;
}}
.tech-bullets-list {{
    list-style: none;
    display: flex;
    flex-direction: column;
    gap: 2px;
    margin-top: 2px;
}}
.tech-bullets-list li {{
    font-size: 7.4px;
    color: var(--text-secondary);
    line-height: 1.35;
    padding-left: 10px;
    position: relative;
}}
.tech-bullets-list li::before {{
    content: '▪';
    position: absolute;
    left: 1px;
    color: var(--accent);
    font-size: 9px;
}}
.tech-tags-bar {{
    display: flex;
    flex-wrap: wrap;
    gap: 3px;
    margin-top: 3px;
}}
.tech-tag-pill {{
    font-size: 6.8px;
    background: rgba(255, 255, 255, 0.04);
    border: 1px solid var(--border);
    padding: 1px 5px;
    border-radius: 3px;
    color: #94a3b8;
    font-family: var(--font-mono);
}}
.cs-link-btn {{
    display: inline-flex;
    align-items: center;
    gap: 4px;
    font-size: 7.2px;
    font-weight: 700;
    color: #0b0f19;
    background: linear-gradient(135deg, #ffba49 0%, #ff8e3c 100%);
    padding: 3px 8px;
    border-radius: 4px;
    text-decoration: none;
    align-self: flex-start;
    margin-top: 3px;
    box-shadow: 0 2px 8px rgba(255, 186, 73, 0.3);
}}

/* Page 1: Cover Page */
.cover-hero {{
    display: flex;
    flex-direction: column;
    align-items: center;
    text-align: center;
    padding: 12mm 0 8mm;
}}
.cover-avatar {{
    width: 90px;
    height: 90px;
    border-radius: 50%;
    border: 3px solid var(--accent);
    box-shadow: 0 0 30px rgba(255, 186, 73, 0.35);
    margin-bottom: 12px;
    object-fit: cover;
}}
.cover-name {{
    font-family: var(--font-heading);
    font-size: 26px;
    font-weight: 800;
    color: #ffffff;
    letter-spacing: -0.5px;
    margin-bottom: 4px;
}}
.cover-role-badge {{
    font-family: var(--font-heading);
    font-size: 11px;
    font-weight: 700;
    color: var(--accent);
    margin-bottom: 10px;
    letter-spacing: 0.5px;
}}
.cover-role-badge span {{
    color: rgba(255, 255, 255, 0.4);
    margin: 0 5px;
}}
.cover-summary {{
    max-width: 170mm;
    font-size: 8.8px;
    color: var(--text-secondary);
    line-height: 1.55;
    margin-bottom: 14px;
}}
.cover-links {{
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    gap: 10px;
    margin-bottom: 16px;
}}
.cover-link-pill {{
    display: inline-flex;
    align-items: center;
    gap: 4px;
    background: rgba(255, 255, 255, 0.04);
    border: 1px solid var(--border);
    padding: 4px 10px;
    border-radius: 20px;
    color: var(--text-primary);
    font-size: 7.6px;
    font-weight: 600;
    text-decoration: none;
}}
.cover-link-pill.accent {{
    border-color: rgba(255, 186, 73, 0.4);
    color: var(--accent);
    background: rgba(255, 186, 73, 0.08);
}}
.cover-stats-grid {{
    display: grid;
    grid-template-columns: repeat(5, 1fr);
    gap: 7px;
    width: 100%;
    margin-bottom: 16px;
}}
.cover-stat-card {{
    background: var(--card-bg);
    border: 1px solid var(--border);
    border-radius: 6px;
    padding: 8px 6px;
    text-align: center;
}}
.cover-stat-val {{
    font-family: var(--font-heading);
    font-size: 15px;
    font-weight: 800;
    color: var(--accent);
    line-height: 1.1;
}}
.cover-stat-lbl {{
    font-size: 6.8px;
    color: var(--text-muted);
    margin-top: 2px;
    font-weight: 600;
    text-transform: uppercase;
}}
.cover-toc {{
    background: rgba(255, 255, 255, 0.02);
    border: 1px solid var(--border);
    border-radius: 7px;
    padding: 10px 14px;
    width: 100%;
}}
.cover-toc-title {{
    font-family: var(--font-heading);
    font-size: 9px;
    font-weight: 700;
    color: var(--accent);
    text-transform: uppercase;
    letter-spacing: 0.8px;
    margin-bottom: 6px;
}}
.cover-toc-grid {{
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 4px 14px;
    font-size: 7.4px;
}}
.cover-toc-item {{
    display: flex;
    justify-content: space-between;
    color: var(--text-secondary);
    border-bottom: 1px dashed rgba(255, 255, 255, 0.08);
    padding-bottom: 2px;
}}
.cover-toc-item strong {{
    color: #ffffff;
}}
.cover-toc-item span {{
    color: var(--accent);
    font-family: var(--font-mono);
}}

/* Page 2: Non-Technical Capability Overview */
.overview-pillars-grid {{
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 10px;
    margin-bottom: 12px;
}}
.pillar-card {{
    background: var(--card-bg);
    border: 1px solid var(--border);
    border-radius: 7px;
    padding: 10px 12px;
    border-top: 3px solid var(--accent);
}}
.pillar-icon-title {{
    display: flex;
    align-items: center;
    gap: 6px;
    margin-bottom: 4px;
}}
.pillar-icon {{
    font-size: 14px;
}}
.pillar-card h3 {{
    font-family: var(--font-heading);
    font-size: 11px;
    font-weight: 700;
    color: #ffffff;
}}
.pillar-card p {{
    font-size: 7.8px;
    color: var(--text-secondary);
    line-height: 1.45;
    margin-bottom: 6px;
}}
.pillar-metrics {{
    display: flex;
    flex-wrap: wrap;
    gap: 4px;
}}
.pillar-metric-tag {{
    font-size: 6.8px;
    background: rgba(255, 255, 255, 0.04);
    border: 1px solid var(--border);
    padding: 2px 6px;
    border-radius: 4px;
    color: var(--accent);
    font-weight: 600;
}}
.value-proposition-box {{
    background: rgba(16, 185, 129, 0.06);
    border: 1px solid rgba(16, 185, 129, 0.25);
    border-radius: 7px;
    padding: 9px 12px;
    margin-bottom: 10px;
}}
.value-proposition-box h4 {{
    font-family: var(--font-heading);
    font-size: 9.5px;
    font-weight: 700;
    color: var(--emerald);
    margin-bottom: 3px;
}}
.value-proposition-box p {{
    font-size: 7.8px;
    color: #e2e8f0;
    line-height: 1.45;
}}
.client-footprint-grid {{
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 7px;
}}
.client-footprint-item {{
    background: var(--card-bg);
    border: 1px solid var(--border);
    border-radius: 5px;
    padding: 6px 8px;
    text-align: center;
}}
.client-footprint-item strong {{
    display: block;
    color: #ffffff;
    font-size: 8px;
}}
.client-footprint-item span {{
    font-size: 6.8px;
    color: var(--text-dim);
}}

/* Page 11: Proprietary Products */
.products-full-grid {{
    display: flex;
    flex-direction: column;
    gap: 10px;
}}
.prod-feature-box {{
    background: var(--card-bg);
    border: 1px solid var(--border);
    border-radius: 8px;
    padding: 11px 13px;
    border-left: 4px solid var(--accent);
}}
.prod-feature-header {{
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 5px;
}}
.prod-feature-header h3 {{
    font-family: var(--font-heading);
    font-size: 13px;
    font-weight: 800;
    color: #ffffff;
}}
.prod-badge {{
    font-size: 7px;
    font-weight: 700;
    padding: 2px 6px;
    border-radius: 4px;
    background: rgba(255, 186, 73, 0.15);
    border: 1px solid rgba(255, 186, 73, 0.35);
    color: var(--accent);
    text-transform: uppercase;
}}
.prod-feature-desc {{
    font-size: 8px;
    color: var(--text-secondary);
    line-height: 1.5;
    margin-bottom: 7px;
}}
.prod-grid-3 {{
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 7px;
    margin-top: 6px;
}}
.prod-grid-item {{
    background: rgba(255, 255, 255, 0.02);
    border: 1px solid var(--border);
    border-radius: 5px;
    padding: 6px 8px;
}}
.prod-grid-item h5 {{
    font-family: var(--font-heading);
    font-size: 8px;
    font-weight: 700;
    color: var(--cyan);
    margin-bottom: 2px;
}}
.prod-grid-item p {{
    font-size: 7.2px;
    color: var(--text-muted);
    line-height: 1.35;
}}

/* Page 12: Publications & Credentials */
.papers-list {{
    display: flex;
    flex-direction: column;
    gap: 6px;
    margin-bottom: 10px;
}}
.paper-item {{
    background: var(--card-bg);
    border: 1px solid var(--border);
    border-radius: 5px;
    padding: 7px 9px;
    border-left: 3px solid var(--cyan);
}}
.paper-title {{
    font-family: var(--font-heading);
    font-size: 8.8px;
    font-weight: 700;
    color: #ffffff;
    line-height: 1.25;
    margin-bottom: 2px;
}}
.paper-meta {{
    font-size: 7px;
    color: var(--text-dim);
    margin-bottom: 2px;
}}
.paper-doi {{
    font-family: var(--font-mono);
    font-size: 6.8px;
    color: var(--accent);
    text-decoration: none;
}}
.reviewer-box {{
    background: rgba(168, 85, 247, 0.05);
    border: 1px solid rgba(168, 85, 247, 0.25);
    border-radius: 6px;
    padding: 8px 11px;
    margin-bottom: 10px;
}}
.reviewer-box h4 {{
    font-family: var(--font-heading);
    font-size: 9px;
    font-weight: 700;
    color: var(--purple);
    margin-bottom: 4px;
}}
.reviewer-journals-grid {{
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 4px 8px;
    font-size: 7.2px;
    color: var(--text-secondary);
}}
.contact-dossier-card {{
    background: linear-gradient(135deg, rgba(255, 186, 73, 0.1) 0%, rgba(56, 189, 248, 0.1) 100%);
    border: 1px solid var(--border-accent);
    border-radius: 7px;
    padding: 10px 14px;
    text-align: center;
}}
.contact-dossier-card h3 {{
    font-family: var(--font-heading);
    font-size: 12px;
    font-weight: 800;
    color: #ffffff;
    margin-bottom: 3px;
}}
.contact-dossier-card p {{
    font-size: 7.8px;
    color: var(--text-secondary);
    margin-bottom: 8px;
}}
.contact-links-row {{
    display: flex;
    justify-content: center;
    gap: 12px;
}}
.contact-link-pill {{
    display: inline-flex;
    align-items: center;
    gap: 4px;
    background: #0b0f19;
    border: 1px solid var(--border);
    padding: 4px 9px;
    border-radius: 4px;
    color: #ffffff;
    font-size: 7.4px;
    font-weight: 600;
    text-decoration: none;
}}
.contact-link-pill:hover {{
    border-color: var(--accent);
    color: var(--accent);
}}
</style>
</head>
<body>
"""

# PAGE 1: COVER
html += f"""
<div class="pdf-page">
    <div class="doc-header">
        <div><span class="doc-header-brand">AHSAN TARIQ</span> · EXECUTIVE DOSSIER</div>
        <div>CONFIDENTIAL · REVISED NOVEMBER 2026</div>
        <div><a href="{BASE_URL}" target="_blank">{BASE_URL}</a></div>
    </div>

    <div class="cover-hero">
        <img src="data:image/jpeg;base64,{prof_b64}" class="cover-avatar" alt="Ahsan Tariq">
        <h1 class="cover-name">Ahsan Tariq</h1>
        <div class="cover-role-badge">
            AI/ML Engineer <span>|</span> Forward Deployed Engineer
        </div>
        <p class="cover-summary">
            Senior AI Systems Architect and Forward Deployed Engineer with an established track record of designing, building, and deploying <strong>23+ production systems</strong> across the United States, United Kingdom, and Europe. Specializing in autonomous multi-agent pipelines, multi-cloud GenAI ops, vector databases, zero-trust cryptographic vaults, and peer-reviewed deep learning research.
        </p>

        <div class="cover-links">
            <a href="{BASE_URL}" target="_blank" class="cover-link-pill accent">🌐 Live Portfolio: ahsantariq.ranbval.com ↗</a>
            <a href="{BASE_URL}/case-studies/" target="_blank" class="cover-link-pill accent">📁 Case Studies Hub (23 Projects) ↗</a>
            <a href="mailto:ahsantariq0724@gmail.com" class="cover-link-pill">📧 ahsantariq0724@gmail.com</a>
            <a href="https://www.linkedin.com/in/ahsan-tariq-comp-engr/" target="_blank" class="cover-link-pill">🔗 LinkedIn Profile ↗</a>
            <a href="https://github.com/ahsantariq7" target="_blank" class="cover-link-pill">💻 GitHub: ahsantariq7 ↗</a>
        </div>

        <div class="cover-stats-grid">
            <div class="cover-stat-card">
                <div class="cover-stat-val">23+</div>
                <div class="cover-stat-lbl">Production Systems</div>
            </div>
            <div class="cover-stat-card">
                <div class="cover-stat-val">$141M+</div>
                <div class="cover-stat-lbl">Active Pipeline Sync</div>
            </div>
            <div class="cover-stat-card">
                <div class="cover-stat-val">6</div>
                <div class="cover-stat-lbl">Published Papers</div>
            </div>
            <div class="cover-stat-card">
                <div class="cover-stat-val">11,500+</div>
                <div class="cover-stat-lbl">Open-Source Downloads</div>
            </div>
            <div class="cover-stat-card">
                <div class="cover-stat-val">81</div>
                <div class="cover-stat-lbl">Logic Puzzles Solved</div>
            </div>
        </div>

        <div class="cover-toc">
            <div class="cover-toc-title">Table of Contents &amp; Executive Roadmap</div>
            <div class="cover-toc-grid">
                <div class="cover-toc-item"><strong>01. Executive Overview &amp; Plain English Capability Guide</strong> <span>PAGE 02</span></div>
                <div class="cover-toc-item"><strong>02. Enterprise Systems, Logistics &amp; Cryptographic Vaults</strong> <span>PAGE 03</span></div>
                <div class="cover-toc-item"><strong>03. Autonomous Voice AI, Phone Agents &amp; Smart Booking</strong> <span>PAGE 04</span></div>
                <div class="cover-toc-item"><strong>04. Interactive Digital Twins, Clinic Intake &amp; Reservations</strong> <span>PAGE 05</span></div>
                <div class="cover-toc-item"><strong>05. Sales Intelligence, Private Automation &amp; Hollywood Set AI</strong> <span>PAGE 06</span></div>
                <div class="cover-toc-item"><strong>06. Scalable Platforms, Clinical Data Lakes &amp; Legal Tech</strong> <span>PAGE 07</span></div>
                <div class="cover-toc-item"><strong>07. Multi-Cloud Orchestration, Vector DBs &amp; Super-Systems</strong> <span>PAGE 08</span></div>
                <div class="cover-toc-item"><strong>08. Peer-Reviewed AI Research &amp; High-Throughput Cybersecurity</strong> <span>PAGE 09</span></div>
                <div class="cover-toc-item"><strong>09. Field Robotics SLAM Navigation &amp; UAV Flight Dynamics</strong> <span>PAGE 10</span></div>
                <div class="cover-toc-item"><strong>10. Proprietary Products (Ranbval Ecosystem &amp; Volvexer)</strong> <span>PAGE 11</span></div>
                <div class="cover-toc-item"><strong>11. Scientific Publications, Peer Reviewer &amp; Contact Dossier</strong> <span>PAGE 12</span></div>
                <div class="cover-toc-item"><strong>Case Studies Directory (Clickable URLs for All 23 Projects)</strong> <span>ALL PAGES</span></div>
            </div>
        </div>
    </div>

    <div class="doc-footer">
        <div>Ahsan Tariq · Master Executive Portfolio Dossier</div>
        <div>PAGE 01 OF {TOTAL_PAGES}</div>
    </div>
</div>
"""

# PAGE 2: NON-TECHNICAL CAPABILITY GUIDE
html += f"""
<div class="pdf-page">
    <div class="doc-header">
        <div><span class="doc-header-brand">AHSAN TARIQ</span> · EXECUTIVE DOSSIER</div>
        <div>CAPABILITY GUIDE FOR FOUNDERS &amp; EXECUTIVES</div>
        <div><a href="{BASE_URL}" target="_blank">{BASE_URL}</a></div>
    </div>

    <div>
        <div class="page-title-block">
            <span class="page-title-badge">Executive Overview</span>
            <h2>What I Build &amp; The Real-World Problems I Solve</h2>
            <p>A crystal-clear guide written in plain everyday English for founders, executives, non-technical managers, and recruiters.</p>
        </div>

        <div class="value-proposition-box">
            <h4>💡 The Engineering Philosophy: Zero Manual Clutter, 100% Reliable Automation</h4>
            <p>
                Modern businesses lose hundreds of hours each month copying data between software, taking meeting notes by hand, chasing unpaid invoices, and fielding repetitive phone calls. I design and build automated software brains that take over repetitive office work, connect disconnected apps, and ensure systems run 24/7 with zero human errors and sub-second response times.
            </p>
        </div>

        <div class="overview-pillars-grid">
            <div class="pillar-card">
                <div class="pillar-icon-title">
                    <span class="pillar-icon">🤖</span>
                    <h3>1. Autonomous AI Agents &amp; Voice Specialists</h3>
                </div>
                <p>
                    I build AI phone agents and chatbots that speak naturally like human experts. They answer incoming customer calls in under 60 seconds, resolve client questions, check live calendars, book appointments on Zoom/Google Meet, and deliver concise action-item summaries directly into team Slack channels.
                </p>
                <div class="pillar-metrics">
                    <span class="pillar-metric-tag">&lt; 600ms Voice Turnaround</span>
                    <span class="pillar-metric-tag">Zero Call Drops</span>
                    <span class="pillar-metric-tag">Automated Calendar Booking</span>
                </div>
            </div>

            <div class="pillar-card">
                <div class="pillar-icon-title">
                    <span class="pillar-icon">⚡</span>
                    <h3>2. Business Automation &amp; Multi-Ledger Accounting</h3>
                </div>
                <p>
                    I eliminate repetitive paperwork. My accounting engines read receipts and vendor bills automatically, verify they haven't been paid before, and sync them seamlessly across QuickBooks, Xero, Buildium, and NetSuite without humans having to type a single number.
                </p>
                <div class="pillar-metrics">
                    <span class="pillar-metric-tag">75% Faster Closing</span>
                    <span class="pillar-metric-tag">Zero Double-Payments</span>
                    <span class="pillar-metric-tag">Multi-Currency Ready</span>
                </div>
            </div>

            <div class="pillar-card">
                <div class="pillar-icon-title">
                    <span class="pillar-icon">🔒</span>
                    <h3>3. Military-Grade Cloud &amp; Cryptographic Security</h3>
                </div>
                <p>
                    I protect sensitive corporate data. Instead of keeping confidential passwords and keys in vulnerable text files, I engineer encrypted vaults with sub-2ms verification. My systems manage multi-cloud networks across AWS, Azure, and Google Cloud to automatically stop waste and lower server bills.
                </p>
                <div class="pillar-metrics">
                    <span class="pillar-metric-tag">NLnet EU Research Grant</span>
                    <span class="pillar-metric-tag">11,500+ SDK Downloads</span>
                    <span class="pillar-metric-tag">Multi-Cloud FinOps</span>
                </div>
            </div>

            <div class="pillar-card">
                <div class="pillar-icon-title">
                    <span class="pillar-icon">🔬</span>
                    <h3>4. Deep Learning Research &amp; Field Robotics</h3>
                </div>
                <p>
                    I conduct original peer-reviewed AI research and build self-navigating robotics. From autonomous 4x4 ground vehicles that map uncharted hazard areas using laser scans, to indoor drones with sub-5cm hovering accuracy and factory vision AI that spots product defects with zero prior training data.
                </p>
                <div class="pillar-metrics">
                    <span class="pillar-metric-tag">6 Published Papers</span>
                    <span class="pillar-metric-tag">Sub-5cm Hover Accuracy</span>
                    <span class="pillar-metric-tag">98.67% Cyber Threat Accuracy</span>
                </div>
            </div>
        </div>

        <div class="page-title-block" style="margin-top: 10px; margin-bottom: 6px;">
            <span class="page-title-badge">Global Footprint</span>
            <h2>Trusted Across International Markets</h2>
        </div>

        <div class="client-footprint-grid">
            <div class="client-footprint-item">
                <strong>🇺🇸 United States</strong>
                <span>Healthcare ERP, Real Estate Accounting, Legal Intake &amp; FinTech</span>
            </div>
            <div class="client-footprint-item">
                <strong>🇬🇧 United Kingdom</strong>
                <span>Multi-Ledger Tax Reconciliations &amp; Corporate Portals</span>
            </div>
            <div class="client-footprint-item">
                <strong>🇪🇺 European Union</strong>
                <span>NLnet NGI Zero-Trust Grant &amp; Tourism Booking Engines</span>
            </div>
            <div class="client-footprint-item">
                <strong>🇦🇺 Australia &amp; PK</strong>
                <span>Multi-Jurisdictional Financial Vaults &amp; AI Microservices</span>
            </div>
        </div>
    </div>

    <div class="doc-footer">
        <div>Ahsan Tariq · Master Executive Portfolio Dossier</div>
        <div>PAGE 02 OF {TOTAL_PAGES}</div>
    </div>
</div>
"""

# PAGES 3 to 10: THE 23 CASE STUDIES
page_num = 3
for section in projects_pages:
    html += f"""
<div class="pdf-page">
    <div class="doc-header">
        <div><span class="doc-header-brand">AHSAN TARIQ</span> · EXECUTIVE DOSSIER</div>
        <div>ARCHITECTURAL CASE STUDIES · PAGE {page_num:02d}</div>
        <div><a href="{BASE_URL}/case-studies/" target="_blank">CASE STUDIES HUB ↗</a></div>
    </div>

    <div>
        <div class="page-title-block">
            <span class="page-title-badge">Section {page_num-2:02d}</span>
            <h2>{section["title"]}</h2>
            <p>{section["subtitle"]}</p>
        </div>

        <div class="projects-container">
    """

    for p in section["projects"]:
        cs_url = p["custom_url"] if p.get("custom_url") else f"{BASE_URL}/case-studies/{p['slug']}/"
        badge_style = f"background: {p['badge_color']}20; border: 1px solid {p['badge_color']}50; color: {p['badge_color']};"

        html += f"""
            <div class="project-card" style="border-left-color: {p['badge_color']};">
                <div class="project-card-header">
                    <div class="project-card-num-title">
                        <span class="project-card-num">#{p["num"]}</span>
                        <span class="project-card-title">{p["title"]}</span>
                    </div>
                    <span class="project-card-badge" style="{badge_style}">{p["badge"]}</span>
                </div>

                <div class="project-card-meta">
                    <div><strong>Client / Org:</strong> {p["org"]}</div>
                    <div><strong>Timeline:</strong> {p["date"]}</div>
                </div>

                <div class="plain-box">
                    <div class="plain-box-label"><i class="fas fa-lightbulb"></i> In Plain English: Problem Solved &amp; Business Results</div>
                    <p>{p["plain_english"]}</p>
                </div>

                <ul class="tech-bullets-list">
        """
        for b in p["tech_bullets"]:
            html += f"<li>{b}</li>\n"

        html += f"""
                </ul>

                <div class="tech-tags-bar">
        """
        for t in p["tags"].split(" · "):
            html += f'<span class="tech-tag-pill">{t}</span>'

        html += f"""
                </div>

                <a href="{cs_url}" target="_blank" class="cs-link-btn">
                    Read Full Architectural Case Study: {cs_url.replace('https://', '')} ↗
                </a>
            </div>
        """

    html += f"""
        </div>
    </div>

    <div class="doc-footer">
        <div>Ahsan Tariq · <strong>AI/ML Engineer | Forward Deployed Engineer</strong> · <a href="{BASE_URL}/case-studies/" target="_blank">{BASE_URL}/case-studies/</a></div>
        <div>PAGE {page_num:02d} OF {TOTAL_PAGES}</div>
    </div>
</div>
    """
    page_num += 1

# PAGE 11: PROPRIETARY PRODUCTS (RANBVAL & VOLVEXER)
html += f"""
<div class="pdf-page">
    <div class="doc-header">
        <div><span class="doc-header-brand">AHSAN TARIQ</span> · EXECUTIVE DOSSIER</div>
        <div>PROPRIETARY SAAS &amp; ECOSYSTEMS</div>
        <div><a href="https://ranbval.com" target="_blank">ranbval.com ↗</a></div>
    </div>

    <div>
        <div class="page-title-block">
            <span class="page-title-badge">Proprietary Products</span>
            <h2>SaaS Platforms I Architected, Built &amp; Own</h2>
            <p>Beyond client engagements, I design and operate proprietary software ecosystems built for extreme scale, security, and financial reliability.</p>
        </div>

        <div class="products-full-grid">
            <div class="prod-feature-box" style="border-left-color: #ffba49;">
                <div class="prod-feature-header">
                    <h3>1. Ranbval — The 16-Pillar Collaborative Platform</h3>
                    <span class="prod-badge">Lead Architect · Live</span>
                </div>
                <p class="prod-feature-desc">
                    Ranbval (<a href="https://ranbval.com" target="_blank" style="color: var(--accent); font-weight:700;">ranbval.com</a>) is an all-in-one collaborative ecosystem engineered under a single secure root. It replaces dozens of disconnected subscription tools with unified team chat, AI digital assistants, encrypted file vaults, dynamic task boards, and social connection spaces—all protected by zero-trust cryptographic access.
                </p>
                <div class="prod-grid-3">
                    <div class="prod-grid-item">
                        <h5>Vault-First Architecture</h5>
                        <p>Zero-knowledge cryptographic access ensuring user passwords and files are inaccessible to unauthorized parties.</p>
                    </div>
                    <div class="prod-grid-item">
                        <h5>Sub-50ms WebSocket Mesh</h5>
                        <p>Live chat, real-time presence indicators, and instant group notifications powered by Redis Sentinel.</p>
                    </div>
                    <div class="prod-grid-item">
                        <h5>16 Unified Applications</h5>
                        <p>Chat, Video Conferencing, File Vault, Task Management, AI Workspaces, and Social Feed under 1 login.</p>
                    </div>
                </div>
                <div style="margin-top: 6px;">
                    <a href="{BASE_URL}/case-studies/ranbval-social/" target="_blank" class="cs-link-btn">Read Ranbval Platform Case Study ↗</a>
                    <a href="{BASE_URL}/case-studies/ranbval-core/" target="_blank" class="cs-link-btn" style="background: rgba(255,255,255,0.08); color:#ffffff; margin-left: 6px;">Read Ranbval Security Case Study ↗</a>
                </div>
            </div>

            <div class="prod-feature-box" style="border-left-color: #10b981;">
                <div class="prod-feature-header">
                    <h3>2. Volvexer — Automated Global Multi-Ledger Accounting</h3>
                    <span class="prod-badge" style="background: rgba(16,185,129,0.15); border-color: rgba(16,185,129,0.35); color:#10b981;">Lead Systems Architect</span>
                </div>
                <p class="prod-feature-desc">
                    Volvexer (<a href="https://www.volvexer.com/" target="_blank" style="color: var(--emerald); font-weight:700;">volvexer.com</a>) is an automated accounting service engineered for multinational businesses operating across the United States, United Kingdom, Australia, and Pakistan. It bridges disparate ledgers, automates monthly tax reconciliations, and runs high-accuracy OCR invoice extraction.
                </p>
                <div class="prod-grid-3">
                    <div class="prod-grid-item">
                        <h5>4 Global Jurisdictions</h5>
                        <p>Pre-configured tax and GAAP/IFRS reconciliation compliance rules for US, UK, AUS, and Pakistani law.</p>
                    </div>
                    <div class="prod-grid-item">
                        <h5>Bi-Directional ERP Sync</h5>
                        <p>Connects live with QuickBooks Online, Xero, NetSuite, and Zoho Books with automated forex conversion.</p>
                    </div>
                    <div class="prod-grid-item">
                        <h5>Zero-Leak Document Vault</h5>
                        <p>Encrypted multi-tenant document repository ensuring zero audit discrepancies and SOC 2 readiness.</p>
                    </div>
                </div>
                <div style="margin-top: 6px;">
                    <a href="https://www.volvexer.com/" target="_blank" class="cs-link-btn" style="background: #10b981; color: #000;">Visit Volvexer Platform: volvexer.com ↗</a>
                </div>
            </div>

            <div class="prod-feature-box" style="border-left-color: #38bdf8;">
                <div class="prod-feature-header">
                    <h3>3. Open-Source Ecosystem &amp; Package Footprint</h3>
                    <span class="prod-badge" style="background: rgba(56,189,248,0.15); border-color: rgba(56,189,248,0.35); color:#38bdf8;">Global Developer Tooling</span>
                </div>
                <p class="prod-feature-desc">
                    Active creator and maintainer of developer libraries on PyPI (Python) and npm (Node.js) with <strong>11,500+ global downloads</strong>. Tools include cryptographic secrets verification, high-performance ASGI decryptors, and automated context-caching connectors.
                </p>
                <div class="prod-grid-3">
                    <div class="prod-grid-item">
                        <h5>PyPI: ranbval-client</h5>
                        <p>Pure ASGI automatic environment secret decryption library for high-speed FastAPI runtimes.</p>
                    </div>
                    <div class="prod-grid-item">
                        <h5>npm: @ranbval/vault</h5>
                        <p>Production Node.js / TypeScript client for zero-latency cryptographic token verification.</p>
                    </div>
                    <div class="prod-grid-item">
                        <h5>GitHub Repositories</h5>
                        <p>Verified open-source machine learning pipelines, NIDS algorithms, and ROS navigation stacks.</p>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <div class="doc-footer">
        <div>Ahsan Tariq · Master Executive Portfolio Dossier</div>
        <div>PAGE 11 OF {TOTAL_PAGES}</div>
    </div>
</div>
"""

# PAGE 12: PUBLICATIONS, REVIEWER CREDENTIALS & CONTACT DOSSIER
html += f"""
<div class="pdf-page">
    <div class="doc-header">
        <div><span class="doc-header-brand">AHSAN TARIQ</span> · EXECUTIVE DOSSIER</div>
        <div>PUBLICATIONS, REVIEWER APPOINTMENTS &amp; ENGAGEMENTS</div>
        <div><a href="{BASE_URL}" target="_blank">{BASE_URL}</a></div>
    </div>

    <div>
        <div class="page-title-block">
            <span class="page-title-badge">Academic &amp; Professional Validation</span>
            <h2>Scientific Publications &amp; Peer Reviewer Appointments</h2>
            <p>Demonstrated peer-reviewed contributions to machine learning, cybersecurity, computer vision, and autonomous robotics.</p>
        </div>

        <div class="papers-list">
            <div class="paper-item">
                <div class="paper-title">1. Three Paradigms, One Benchmark: A Diagnostic Grand Tour of Zero-Shot vs Few-Shot Anomaly Localization on MVTec AD</div>
                <div class="paper-meta">Sole Author: <strong>Ahsan Tariq</strong> · Journal of Independent Studies and Research - Computing (JISR-C) · 2026</div>
                <a href="{BASE_URL}/case-studies/mvtec-defect-benchmark/" target="_blank" class="paper-doi">Read Case Study: {BASE_URL}/case-studies/mvtec-defect-benchmark/ ↗</a>
            </div>

            <div class="paper-item">
                <div class="paper-title">2. Trust as a Gate, Not a Weight: Robust Perception-Aware Federated Learning Under Byzantine Attacks</div>
                <div class="paper-meta">Sole Author: <strong>Ahsan Tariq</strong> · Journal of Independent Studies and Research - Computing (JISR-C) · 2026</div>
                <a href="{BASE_URL}/case-studies/robust-federated-perception/" target="_blank" class="paper-doi">Read Case Study: {BASE_URL}/case-studies/robust-federated-perception/ ↗</a>
            </div>

            <div class="paper-item">
                <div class="paper-title">3. ANOVA F-Test Feature Selection for Machine Learning-Based Network Intrusion Detection on the UNSW-NB15 Dataset</div>
                <div class="paper-meta">Sole Author: <strong>Ahsan Tariq</strong> · Journal of Independent Studies and Research - Computing (JISR-C) · 2026</div>
                <a href="{BASE_URL}/case-studies/unsw-intrusion-detection/" target="_blank" class="paper-doi">Read Case Study: {BASE_URL}/case-studies/unsw-intrusion-detection/ ↗</a>
            </div>

            <div class="paper-item">
                <div class="paper-title">4. Deep Learning Architectures for Robust Medical Imaging Diagnostic Localization</div>
                <div class="paper-meta">Lead Author: <strong>Ahsan Tariq</strong> · Peer-Reviewed Medical AI Research · 2024</div>
                <span class="paper-doi">Verified Publication Record</span>
            </div>

            <div class="paper-item">
                <div class="paper-title">5. Autonomous Mobile Robot Navigation and Dynamic Obstacle Avoidance via Deep Reinforcement Learning</div>
                <div class="paper-meta">Author: <strong>Ahsan Tariq</strong> · Robotics &amp; Autonomous Systems Proceedings · 2024</div>
                <span class="paper-doi">Verified Robotics Research</span>
            </div>

            <div class="paper-item">
                <div class="paper-title">6. Cryptographic Access Control and Zero-Trust Secrets Distribution for Microservice Swarms</div>
                <div class="paper-meta">Author: <strong>Ahsan Tariq</strong> · Security &amp; Distributed Systems Technical Report · 2025</div>
                <span class="paper-doi">NLnet Grant Research Documentation</span>
            </div>
        </div>

        <div class="reviewer-box">
            <h4>International Scientific Peer Reviewer Appointments</h4>
            <div class="reviewer-journals-grid">
                <div>▪ IEEE Transactions on Industrial Informatics</div>
                <div>▪ Elsevier Journal of Network &amp; Computer Apps</div>
                <div>▪ Springer Neural Computing &amp; Applications</div>
                <div>▪ Wiley Security &amp; Communication Networks</div>
                <div>▪ IGI Global Book Chapter Review Board</div>
                <div>▪ Verified Publons / Clarivate Reviewer ID</div>
            </div>
        </div>

        <div class="contact-dossier-card">
            <h3>Let's Build the Next Extraordinary Production System Together</h3>
            <p>Available for Forward Deployed Engineering engagements, Enterprise AI Systems Architecture, and Technical Advisory worldwide.</p>
            <div class="contact-links-row">
                <a href="mailto:ahsantariq0724@gmail.com" class="contact-link-pill">📧 ahsantariq0724@gmail.com</a>
                <a href="{BASE_URL}" target="_blank" class="contact-link-pill" style="border-color: var(--accent); color: var(--accent);">🌐 ahsantariq.ranbval.com ↗</a>
                <a href="https://www.linkedin.com/in/ahsan-tariq-comp-engr/" target="_blank" class="contact-link-pill">🔗 LinkedIn Profile ↗</a>
                <a href="https://github.com/ahsantariq7" target="_blank" class="contact-link-pill">💻 GitHub: ahsantariq7 ↗</a>
            </div>
        </div>
    </div>

    <div class="doc-footer">
        <div>Ahsan Tariq · <strong>AI/ML Engineer | Forward Deployed Engineer</strong> · <a href="{BASE_URL}" target="_blank">{BASE_URL}</a></div>
        <div>PAGE 12 OF {TOTAL_PAGES}</div>
    </div>
</div>
</body>
</html>
"""

with open('portfolio-pdf.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Generated portfolio-pdf.html successfully. Characters:", len(html))
