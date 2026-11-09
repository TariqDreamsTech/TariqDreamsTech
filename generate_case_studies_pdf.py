import base64
import os

with open('prof.jpeg', 'rb') as f:
    prof_b64 = base64.b64encode(f.read()).decode('utf-8')

BASE_URL = "https://ahsantariq.ranbval.com"

# 24 Detailed Case Studies (23 from portfolio + Volvexer platform)
# Paired 2 per page across 12 project pages = 24 projects
case_studies = [
    # ─── TRACK 1: HEALTHCARE & ENTERPRISE OPERATIONS ───────────
    {
        "num": "01",
        "title": "Ambica International (Dovetail) — Healthcare Logistics & Enterprise ERP",
        "category": "Healthcare Enterprise · ERP & Live Telematics",
        "client": "Ambica International · United States (Remote)",
        "timeline": "2025 – 2026",
        "slug": "ambica-dovetail",
        "badge": "Live Production",
        "badge_color": "#10b981",
        "metrics": [
            {"val": "$141.3M", "lbl": "Active Cargo Mirrored"},
            {"val": "102 Trucks", "lbl": "Live Cartrack GPS"},
            {"val": "< 60s", "lbl": "DocuSign Approvals"},
            {"val": "3-Sec", "lbl": "Live P&L Ticking"}
        ],
        "problem": "Hospitals and pharmacies were relying on paper clipboards, phone calls, and manual spreadsheet entries to track critical medicine shipments. Managers had zero live visibility into delivery trucks, purchase orders took days to manually key into NetSuite, and signing vendor contracts required printing physical paper.",
        "solution": "Built a 100% digital, autonomous operations portal hosted on Google Cloud Run. Connected live GPS sensors from 102 delivery vehicles, built a sub-second data bridge that syncs NetSuite inventory and invoices every 3 seconds, and integrated automated DocuSign workflows so executives can approve supplier contracts from their phones in under 60 seconds.",
        "impact": "Eliminated lost shipments completely, automated tracking across 51,462 invoices and 35,935 purchase orders, reduced vendor contract turnaround from 3 days to under 1 minute, and gave executive leadership a live 3-second profit & loss dashboard with zero manual bookkeeping."
    },
    {
        "num": "02",
        "title": "Petroski Physiotherapy — Clinic Marketing & Patient Intake Governance",
        "category": "Healthcare Governance · Clinical Workflow",
        "client": "Petroski Physio Clinic · Sports Rehabilitation (USA)",
        "timeline": "2025",
        "slug": "petroski-physio",
        "badge": "Clinical Automation",
        "badge_color": "#10b981",
        "metrics": [
            {"val": "100%", "lbl": "HIPAA Privacy Shield"},
            {"val": "24-Hour", "lbl": "Automated Trigger"},
            {"val": "1-Click", "lbl": "Slack Approval"},
            {"val": "0 Interruptions", "lbl": "During Patient Care"}
        ],
        "problem": "Sports physical therapists were constantly being interrupted during patient therapy sessions by clinic marketers asking: 'Can we film this injured athlete for Instagram/TikTok?' This created HIPAA privacy risks, annoyed busy therapists, and resulted in missed marketing opportunities when therapists forgot to follow up.",
        "solution": "Designed an automated 'Two-Board' governance system. Clinical medical records are kept completely separated from marketing. Exactly 24 hours after a patient's evaluation, the therapist automatically receives a friendly Slack message asking: 'Can we film this athlete?' with simple 'Yes' and 'No' buttons. Clicking 'Yes' instantly and safely updates the marketing team's board.",
        "impact": "Completely eliminated office interruptions during patient treatment, guaranteed 100% HIPAA medical privacy compliance with zero patient data leaks, and automatically archives patients once their physical therapy program concludes."
    },

    # ─── TRACK 2: FINANCIAL AUTOMATION & MULTI-LEDGER ACCOUNTING ─
    {
        "num": "03",
        "title": "Volvexer — Global Multi-Ledger Accounting & Tax Reconciliation",
        "category": "Global FinTech · Multi-Jurisdiction Ledgers",
        "client": "Volvexer · Financial Services (USA, UK, Australia, Pakistan)",
        "timeline": "2024 – Present",
        "custom_url": "https://www.volvexer.com/",
        "slug": "",
        "badge": "Enterprise Platform",
        "badge_color": "#ffba49",
        "metrics": [
            {"val": "75%", "lbl": "Faster Month-End Close"},
            {"val": "4 Countries", "lbl": "Tax Rules Integrated"},
            {"val": "0 Re-typing", "lbl": "Manual Data Entry"},
            {"val": "100%", "lbl": "Audit-Ready Trail"}
        ],
        "problem": "Multinational companies operating across the US, UK, Australia, and Pakistan were wasting hundreds of hours every month manually re-entering bank transactions, converting currencies, and matching invoices between different accounting software like QuickBooks, Xero, NetSuite, and Zoho Books.",
        "solution": "Co-founded and engineered an automated financial platform that synchronizes bank transactions, automatically converts international exchange rates, reads messy receipts with AI, and prepares tax reconciliation reports tailored to US (GAAP/IRS), UK (HMRC), and Australian tax rules without manual entry.",
        "impact": "Reduced month-end financial closing time by 75%, eliminated duplicate payments, and established an encrypted, tamper-proof audit trail that satisfies international corporate tax audits."
    },
    {
        "num": "04",
        "title": "Terry Properties — AI Accounting Automation & QuickBooks / Buildium Sync",
        "category": "Real Estate FinTech · Invoice Reconciliation",
        "client": "Terry Real Estate Management · United States (Remote)",
        "timeline": "2024 – 2025",
        "slug": "terry-accounting",
        "badge": "Production System",
        "badge_color": "#10b981",
        "metrics": [
            {"val": "25+ Hours", "lbl": "Saved Every Week"},
            {"val": "99.4%", "lbl": "AI Invoice Extraction"},
            {"val": "0 Duplicate", "lbl": "Contractor Payments"},
            {"val": "2-Way", "lbl": "Real-Time Sync"}
        ],
        "problem": "Property managers were spending 25+ hours every week manually opening hundreds of vendor bills from messy email attachments and WhatsApp photos, and manually typing invoice numbers, amounts, and dates into both QuickBooks Online and Buildium. Several maintenance contractors were accidentally paid twice.",
        "solution": "Engineered an AI accountant that automatically reads photos or PDF invoices, verifies whether the bill has already been paid or entered, extracts the contractor name and general ledger code, and syncs the expense record accurately across both QuickBooks and Buildium simultaneously.",
        "impact": "Saved property management staff 25+ hours of tedious manual typing every single week, completely eradicated duplicate contractor payments, and gave property owners instant financial clarity on every repair bill."
    },

    # ─── TRACK 3: AUTONOMOUS VOICE SPECIALISTS & PHONE AI ────────
    {
        "num": "05",
        "title": "Transact ULTD — Sub-Second Voice AI & Automated Merchant Lifecycle",
        "category": "FinTech Sales · Real-Time Voice Specialist",
        "client": "Transact ULTD · Payment Technology (USA)",
        "timeline": "2025 – 2026",
        "slug": "transact-ultd",
        "badge": "Voice AI · Live",
        "badge_color": "#f59e0b",
        "metrics": [
            {"val": "< 60 Sec", "lbl": "Lead Response Time"},
            {"val": "< 600ms", "lbl": "Conversational Delay"},
            {"val": "0 Hold Times", "lbl": "24/7 Availability"},
            {"val": "5 Experts", "lbl": "Live Transfer Mesh"}
        ],
        "problem": "Credit card processing companies lose over 60% of interested business leads when sales calls go to voicemail or callers are placed on hold. Busy merchant owners hang up immediately if an automated phone system sounds robotic, stutters, or delays before replying.",
        "solution": "Engineered a lightning-fast AI phone specialist that calls incoming merchant leads in under 60 seconds. It talks smoothly like a knowledgeable consultant, explains fee savings on credit cards, parses merchant statements, and transfers live callers smoothly to human closing specialists when complex questions arise.",
        "impact": "Cut inbound lead response time from hours to under 60 seconds, boosted sales appointment booking rates, and created a 24/7 automated qualification funnel that never puts a customer on hold."
    },
    {
        "num": "06",
        "title": "Django Voice Agent — Autonomous Phone AI & Meeting Action Summarizer",
        "category": "Autonomous Voice AI · Calendar Automation",
        "client": "Enterprise Sales Infrastructure · Commercial Deployment",
        "timeline": "2025 – 2026",
        "slug": "django-voice-agent",
        "badge": "Autonomous Agent",
        "badge_color": "#38bdf8",
        "metrics": [
            {"val": "100%", "lbl": "Hands-Free Booking"},
            {"val": "0 Note-Taking", "lbl": "Automated Transcripts"},
            {"val": "< 2 Min", "lbl": "Slack Action Delivery"},
            {"val": "3 Platforms", "lbl": "Google / Zoom / Teams"}
        ],
        "problem": "Sales teams lose valuable selling hours dialing cold phone numbers, emailing calendar links back and forth across different time zones, and taking manual meeting notes during client consultations.",
        "solution": "Built an autonomous phone assistant combining Twilio, Deepgram, and Claude. The agent speaks naturally, answers objections, checks team calendar availability, and reserves appointments on Google Meet or Zoom. When the meeting concludes, the AI automatically transcribes the recording and delivers concise next steps directly into Slack.",
        "impact": "Eliminated back-and-forth calendar scheduling emails entirely, removed the burden of manual note-taking, and ensured sales managers receive instant action-item summaries within 2 minutes of every call."
    },

    # ─── TRACK 4: INTERACTIVE AI, DIGITAL TWINS & RESERVATIONS ──
    {
        "num": "07",
        "title": "Qira AI — Real-Time Avatar Intelligence & Multilingual Digital Twins",
        "category": "Consumer AI · Digital Twin Video Synthesis",
        "client": "Qira AI · United States & Global",
        "timeline": "2024 – 2025",
        "slug": "qira-ai",
        "badge": "Consumer Platform",
        "badge_color": "#ec4899",
        "metrics": [
            {"val": "1 Photo", "lbl": "Avatar Creation"},
            {"val": "< 800ms", "lbl": "Real-Time Video Sync"},
            {"val": "Multi-Lang", "lbl": "Live Speech Translation"},
            {"val": "24/7", "lbl": "Autonomous Twin Mode"}
        ],
        "problem": "Content creators, influencers, and busy professionals want to stay connected with their fans and friends, but it is physically impossible to respond to thousands of video calls, chats, and direct messages around the clock.",
        "solution": "Built an entertainment platform where users create a speaking 3D digital clone from just one selfie and short voice sample. Friends can video call, text, and play games with the digital twin, which speaks authentically in the user's real voice, translates conversations across multiple languages, and interacts autonomously when the real user is asleep or busy.",
        "impact": "Delivered lifelike real-time video chat with sub-800ms latency, enabled creators to scale their personal presence to thousands of fans simultaneously, and opened an entirely new category of interactive social entertainment."
    },
    {
        "num": "08",
        "title": "Ballyhass Adventure Park — Autonomous Booking Assistant & Availability",
        "category": "Hospitality & Leisure · Live Reservations",
        "client": "Ballyhass Outdoor Adventure · Ireland / Europe",
        "timeline": "2024 – 2025",
        "slug": "ballyhass-booking",
        "badge": "Commercial Chatbot",
        "badge_color": "#f59e0b",
        "metrics": [
            {"val": "0.4 Sec", "lbl": "Availability Lookup"},
            {"val": "1-Click", "lbl": "Ticket Reservation"},
            {"val": "2 Lakes", "lbl": "Multi-Venue Polling"},
            {"val": "24/7", "lbl": "Automated Helpdesk"}
        ],
        "problem": "Families planning weekend trips to a large outdoor lake park struggled to find open time slots across different sports like wakeboarding, ziplines, and aquaparks. The customer support phone line was constantly jammed with callers asking simple questions about ticket availability.",
        "solution": "Built a friendly booking assistant that understands everyday conversational questions like: 'Are there spots for 4 people next Friday afternoon at Mallow?' It checks live ticket availability in 0.4 seconds across all activity venues and provides direct buttons for visitors to book their preferred slot in one click.",
        "impact": "Reduced customer support phone calls by over 50%, eliminated booking friction, and allowed thousands of visitors to reserve adventure passes effortlessly 24 hours a day."
    },

    # ─── TRACK 5: SALES INTELLIGENCE & PRIVATE AUTOMATION CLOUD ─
    {
        "num": "09",
        "title": "Prospect Intelligence Engine — Sales AI with Google Context Caching",
        "category": "Sales Enablement · LLM Server Caching",
        "client": "Enterprise Sales Intelligence · Contract Engagement",
        "timeline": "2025 – 2026",
        "slug": "prospect-intelligence",
        "badge": "Enterprise AI",
        "badge_color": "#38bdf8",
        "metrics": [
            {"val": "90%", "lbl": "AI Bill Slashed"},
            {"val": "< 1 Sec", "lbl": "Query Response Time"},
            {"val": "100k Words", "lbl": "Instant Context Memory"},
            {"val": "10 Min -> 0", "lbl": "Pre-Call Prep Time"}
        ],
        "problem": "Sales representatives wasted 10 to 15 minutes before every call digging through old call recordings, LinkedIn profiles, and company PDFs to answer buyer questions. Asking conventional AI to re-read 100,000 words on every question was too slow (10+ seconds) and cost a small fortune in API fees.",
        "solution": "Engineered an AI sales assistant utilizing Google Gemini's advanced server caching. The system loads the client's complete historical profile into server memory once; future buyer questions are answered in less than 1 second while bypassing 90% of the normal AI computing charges.",
        "impact": "Slashed monthly AI infrastructure bills by over 90%, cut answer latency from 10 seconds to under 800 milliseconds, and equipped sales reps with instant, accurate prospect knowledge during high-stakes sales conversations."
    },
    {
        "num": "10",
        "title": "hddisenos — Self-Hosted Automation Cloud & Multi-CRM Synchronization",
        "category": "Private Cloud DevOps · Multi-CRM Workflows",
        "client": "hddisenos Creative & Industrial Agency · International",
        "timeline": "2025",
        "slug": "hddisenos-automation",
        "badge": "Self-Hosted Cloud",
        "badge_color": "#10b981",
        "metrics": [
            {"val": "60%", "lbl": "Manual Work Cut"},
            {"val": "$0 / Month", "lbl": "Recurring Tool Fees"},
            {"val": "57 Automated", "lbl": "Business Workflows"},
            {"val": "2 Major CRMs", "lbl": "HubSpot & Zoho Sync"}
        ],
        "problem": "Commercial automation platforms (like Zapier or Make) charge for every single click, workflow trigger, and data transfer. As the agency scaled, software bills ballooned into thousands of dollars each month, while team members still had to manually sync leads between HubSpot and Zoho CRM.",
        "solution": "Built a private, self-hosted automation cloud on dedicated servers. It powers 57 business operations—including turning customer pet photos into AI watercolor art, automatically posting car inventory to Facebook Marketplace for auto dealerships, and synchronizing customer records across HubSpot and Zoho with zero third-party software subscriptions.",
        "impact": "Cut manual administrative office work by 60%, eliminated thousands of dollars in monthly SaaS subscription fees forever, and delivered 100% data ownership and privacy on dedicated servers."
    },

    # ─── TRACK 6: HOLLYWOOD TELEMATICS & LEGAL WORKFLOWS ─────────
    {
        "num": "11",
        "title": "CoreImmersive — Hollywood Call Sheet Parsing & Set Telematics",
        "category": "Film Production AI · Logistics & Telematics",
        "client": "CoreImmersive Productions · Hollywood / Los Angeles (Remote)",
        "timeline": "2024 – 2025",
        "slug": "coreimmersive-film",
        "badge": "Media Production AI",
        "badge_color": "#ec4899",
        "metrics": [
            {"val": "99.2%", "lbl": "PDF Call Sheet Accuracy"},
            {"val": "90 Min", "lbl": "Advance Rain Warning"},
            {"val": "$0 Union", "lbl": "Meal Penalty Fines"},
            {"val": "100% Real-Time", "lbl": "Director Dashboards"}
        ],
        "problem": "Filming a movie or television series is high-stakes logistical chaos: hundreds of actors, camera crews, and catering trucks operate off complicated 20-page PDF 'Call Sheets' emailed late at night. Production assistants spent hours manually copying schedules, missing rainstorms, and triggering expensive union meal penalty fines.",
        "solution": "Built an intelligent production management platform. The AI scans dense multi-page schedule PDFs in seconds, organizes arrival times and shooting locations for every actor, tracks union meal break countdowns, and monitors weather radar to warn directors 90 minutes before rain hits outdoor filming sets.",
        "impact": "Eliminated expensive union delay penalties, automated call sheet distribution to cast and crew, protected filming equipment from sudden weather damage, and gave Hollywood directors a live progress dashboard on set."
    },
    {
        "num": "12",
        "title": "Sean Z & Associates — Multilingual AI Legal Intake Architecture",
        "category": "Legal Technology · Multilingual Case Prep",
        "client": "Sean Z & Associates · Law Practice (USA)",
        "timeline": "2024",
        "slug": "seanz-law-firm",
        "badge": "Legal AI Assistant",
        "badge_color": "#f59e0b",
        "metrics": [
            {"val": "2 Languages", "lbl": "English & Spanish"},
            {"val": "100%", "lbl": "Attorney-Client Privilege"},
            {"val": "70% Faster", "lbl": "Case File Preparation"},
            {"val": "24/7", "lbl": "Client Intake on WhatsApp"}
        ],
        "problem": "Immigration lawyers spend endless hours conducting repetitive initial screening interviews in English and Spanish over the phone. Potential clients who contacted the firm after business hours were lost to competitor law firms before staff could respond.",
        "solution": "Built an intelligent legal intake assistant accessible via WhatsApp and phone. The AI interviews potential clients in their native language, asks relevant questions about family history and visa requirements, structures the facts into a clean case dossier, and alerts attorneys immediately while ensuring all data remains confidential.",
        "impact": "Cut case file preparation time by 70%, captured after-hours client leads that were previously lost, and freed attorneys from repetitive paperwork so they could focus on courtroom advocacy."
    },

    # ─── TRACK 7: MULTI-CLOUD ORCHESTRATION & VECTOR SEARCH ──────
    {
        "num": "13",
        "title": "Jericho AI — Autonomous GenAI Ops & Multi-Cloud Cost Orchestrator",
        "category": "DevOps & Cloud Computing · Multi-Cloud FinOps",
        "client": "Jericho AI · Florida, United States",
        "timeline": "2024 – 2025",
        "slug": "jericho-ai-multicloud",
        "badge": "Multi-Cloud Platform",
        "badge_color": "#38bdf8",
        "metrics": [
            {"val": "5 Clouds", "lbl": "AWS, Azure, GCP, IBM, OCI"},
            {"val": "35%+", "lbl": "Cloud Waste Reduction"},
            {"val": "0 Downtime", "lbl": "Automated Scaling"},
            {"val": "24/7 AI", "lbl": "Autonomous Server Swarm"}
        ],
        "problem": "Enterprises run software across multiple cloud providers (AWS, Azure, Google Cloud, IBM, and Oracle). Because every platform has different dashboards and billing rules, companies waste thousands of dollars every month on idle, over-provisioned servers and cloud bandwidth.",
        "solution": "Engineered a unified multi-cloud orchestration platform powered by autonomous AI agents. The agents continuously monitor server loads across all five cloud providers, identify unused computing power, and automatically restructure workloads in real time to stop waste without causing service interruptions.",
        "impact": "Cut unnecessary cloud spending by over 35%, automated infrastructure optimization across multi-cloud environments, and gave engineering leadership a single unified dashboard to govern all company cloud assets."
    },
    {
        "num": "14",
        "title": "InstaMailAI — Scalable Vector Database & Semantic RAG Email Engine",
        "category": "Vector Databases · Semantic Search & RAG",
        "client": "InstaMailAI · United States (Remote)",
        "timeline": "2025",
        "slug": "instamail-ai",
        "badge": "Vector Search RAG",
        "badge_color": "#10b981",
        "metrics": [
            {"val": "< 50ms", "lbl": "Vector Search Speed"},
            {"val": "80%", "lbl": "Faster Email Drafting"},
            {"val": "0 Hallucinations", "lbl": "Context-Grounded Replies"},
            {"val": "Millions", "lbl": "Indexed Email Threads"}
        ],
        "problem": "Traditional email search requires users to remember the exact keyword used months ago. When corporate teams handle thousands of customer emails, finding past context or drafting accurate, customized replies takes minutes per email, slowing down customer service.",
        "solution": "Built a scalable vector search engine using MongoDB Atlas Vector Search and OpenAI embeddings. The system indexes millions of email messages into mathematical representations of meaning; users can find past discussions instantly using everyday concept searches, and the AI drafts context-aware responses automatically.",
        "impact": "Accelerated email drafting speed by 80%, allowed teams to find past client agreements in less than 50 milliseconds, and eliminated customer service delays across high-volume email workflows."
    },

    # ─── TRACK 8: AI PLATFORMS & CLINICAL DATA LAKES ─────────────
    {
        "num": "15",
        "title": "2456.ai — Autonomous AI Tool Discovery & Scalable Microservices",
        "category": "AI SaaS Architecture · Microservices",
        "client": "2456.ai · United States (Remote)",
        "timeline": "2023 – 2024",
        "slug": "2456-ai-platform",
        "badge": "SaaS Platform",
        "badge_color": "#38bdf8",
        "metrics": [
            {"val": "Thousands", "lbl": "AI Tools Indexed"},
            {"val": "< 1 Sec", "lbl": "Model Routing Latency"},
            {"val": "100%", "lbl": "Automated Stripe Billing"},
            {"val": "Zero-Lag", "lbl": "Concurrent Search"}
        ],
        "problem": "With thousands of new AI tools launching every week, businesses and professionals struggle to identify which AI model actually solves their specific problem, leading to wasted subscription fees and confusion.",
        "solution": "Built an intelligent AI platform that automatically catalogs AI tools, analyzes their performance capabilities, and routes user questions to the optimal tool with sub-second response times, integrated vector recommendations, and automated tiered Stripe subscription billing.",
        "impact": "Created an effortless AI discovery hub that routes queries in under 1 second, automated recurring customer billing, and handled high concurrent user search traffic without server slowdowns."
    },
    {
        "num": "16",
        "title": "QPharma Global — Cloud Data Lake & Cold-Chain Telemetry Pipeline",
        "category": "Big Data Engineering · Cloud Data Lake",
        "client": "QPharma Global · United States (Remote)",
        "timeline": "2022",
        "slug": "qpharma-data-platform",
        "badge": "Enterprise Data Lake",
        "badge_color": "#10b981",
        "metrics": [
            {"val": "70%", "lbl": "Faster Data Reporting"},
            {"val": "Millions", "lbl": "Records Cleansed"},
            {"val": "100%", "lbl": "Cold-Chain Integrity"},
            {"val": "Sub-Second", "lbl": "Athena SQL Queries"}
        ],
        "problem": "Pharmaceutical companies must guarantee that temperature-sensitive vaccines and medicines never spoil during international transportation. Manually processing gigabytes of sensor temperature logs and pharmacy sales spreadsheets took days, delaying critical regulatory compliance reports.",
        "solution": "Built a serverless cloud data lake on Amazon Web Services (AWS Glue, S3, and Lambda). The pipeline automatically ingests, cleans, and partitions millions of shipment logs, alerting quality managers instantly if medicine temperature limits were breached.",
        "impact": "Cut data processing and compliance reporting time by 70%, prevented damaged pharmaceutical batches from reaching pharmacy shelves, and delivered sub-second audit queries for federal regulators."
    },

    # ─── TRACK 9: CRYPTOGRAPHIC VAULTS & COLLABORATIVE ECOSYSTEMS 
    {
        "num": "17",
        "title": "Ranbval Core & Secret Manager — Zero-Knowledge Cryptographic Vault",
        "category": "Cryptographic Security · Zero-Trust Architecture",
        "client": "Ranbval Security Platform · Global Enterprise SaaS",
        "timeline": "2025 – Present",
        "slug": "ranbval-core",
        "badge": "NLnet Grant Award",
        "badge_color": "#38bdf8",
        "metrics": [
            {"val": "< 2ms", "lbl": "Key Decryption Speed"},
            {"val": "11,500+", "lbl": "SDK Downloads Globally"},
            {"val": "NLnet EU", "lbl": "Research Grant Winner"},
            {"val": "0 Leaks", "lbl": "Tamper-Proof Killswitch"}
        ],
        "problem": "Over 80% of corporate data breaches occur because software engineers leave database passwords, customer encryption keys, and API tokens stored in plain text configuration files on servers or in GitHub repositories.",
        "solution": "Built an ultra-secure digital vault that encrypts confidential credentials using military-grade cryptography (AES-256 and ChaCha20). Keys are verified offline in less than 2 milliseconds, and if unauthorized tampering is detected, the system shuts down access instantly. Awarded an EU NLnet Foundation research grant.",
        "impact": "Protected production servers from credential theft, published open-source verification libraries on PyPI and npm with over 11,500 global downloads, and achieved verified sub-2ms decryption latency."
    },
    {
        "num": "18",
        "title": "Ranbval Social Super-System — 16-Pillar Collaborative Platform",
        "category": "Unified SaaS · Single Secure Root",
        "client": "Ranbval Platform · Lead Systems Architect",
        "timeline": "2024 – Present",
        "slug": "ranbval-social",
        "badge": "Proprietary Platform",
        "badge_color": "#ec4899",
        "metrics": [
            {"val": "16 Apps", "lbl": "Unified Under 1 Login"},
            {"val": "< 50ms", "lbl": "Real-Time Chat Latency"},
            {"val": "100%", "lbl": "Single Secure Web Root"},
            {"val": "10 Apps", "lbl": "Replaced by Ranbval"}
        ],
        "problem": "Modern business teams waste productive hours jumping between 10 separate apps for team messaging, task management, file storage, video meetings, and AI helpers—paying separate subscriptions for each and scattering data everywhere.",
        "solution": "Architected an all-in-one collaborative ecosystem operating on a single secure web address (ranbval.com). Combines instant team chat, automated AI assistants, encrypted file vaults, interactive project boards, and group calls under one login protected by vault-first security.",
        "impact": "Eliminated the chaos and cost of subscribing to 10 disconnected software tools, unified team communication in under 50 milliseconds, and delivered total data privacy under a single secure umbrella."
    },

    # ─── TRACK 10: OMNICHANNEL CLIENT MEMORY & DEFECT VISION ─────
    {
        "num": "19",
        "title": "Ranbval Conversations — Centralized Client Memory & Omnichannel Hub",
        "category": "Omnichannel CRM · Customer Memory",
        "client": "Ranbval Platform · Lead Systems Architect",
        "timeline": "2024 – Present",
        "slug": "ranbval-conversations",
        "badge": "Proprietary Platform",
        "badge_color": "#ffba49",
        "metrics": [
            {"val": "1 Inbox", "lbl": "WhatsApp, Email, LinkedIn"},
            {"val": "100%", "lbl": "Historical Context Memory"},
            {"val": "0 Repetitions", "lbl": "No Repeated Questions"},
            {"val": "Instant", "lbl": "Unified Client Profile"}
        ],
        "problem": "When customers contact a business across different channels (email on Monday, WhatsApp on Wednesday, LinkedIn on Friday), support reps lose track of past conversations, frustrating clients who are forced to repeat themselves.",
        "solution": "Built a unified client communication hub where incoming messages from WhatsApp, email, LinkedIn, and websites flow into a single smart inbox. The AI remembers every customer's previous requests and purchases, instantly briefing the team before they answer.",
        "impact": "Ensured no customer inquiry is ever forgotten, eliminated customer frustration from repeating past issues, and boosted customer satisfaction scores across multi-channel sales teams."
    },
    {
        "num": "20",
        "title": "Industrial Defect Localization — Zero-Shot vs Few-Shot Vision Benchmark",
        "category": "Computer Vision · Industrial Quality Control",
        "client": "Peer-Reviewed Deep Learning Research · Sole Author: Ahsan Tariq",
        "timeline": "2025 – 2026",
        "slug": "mvtec-defect-benchmark",
        "badge": "Academic Research",
        "badge_color": "#a855f7",
        "metrics": [
            {"val": "15 Categories", "lbl": "Industrial Objects & Textures"},
            {"val": "5,354", "lbl": "High-Res Factory Images"},
            {"val": "0 Prior Defect", "lbl": "Photos Required to Test"},
            {"val": "Published", "lbl": "Peer-Reviewed Study"}
        ],
        "problem": "Factory production lines lose millions when computer vision cameras fail to spot microscopic defects in manufactured products (cracked metal tiles, torn fabrics, loose screws), or when traditional AI models demand thousands of sample photos of defects before they can learn to spot them.",
        "solution": "Conducted comprehensive peer-reviewed computer vision research evaluating three modern AI paradigms across 15 industrial manufacturing categories (5,354 high-resolution images). Proved which visual foundation models accurately pinpoint microscopic manufacturing flaws with zero prior training photos.",
        "impact": "Demonstrated how manufacturing plants can deploy visual AI quality control immediately without wasting months collecting rare defect samples, establishing empirical benchmarks for automated zero-defect manufacturing."
    },

    # ─── TRACK 11: PEER-REVIEWED AI SECURITY & HIGH-SPEED FIREWALLS 
    {
        "num": "21",
        "title": "Robust Federated Learning — Defense Against Byzantine Model Poisoning",
        "category": "Decentralized AI · Cybersecurity Defense",
        "client": "Peer-Reviewed Research · Sole Author: Ahsan Tariq",
        "timeline": "2025 – 2026",
        "slug": "robust-federated-perception",
        "badge": "Academic Research",
        "badge_color": "#38bdf8",
        "metrics": [
            {"val": "99.1%", "lbl": "Attack Rejection Rate"},
            {"val": "0 Private Data", "lbl": "Transferred or Leaked"},
            {"val": "Byzantine", "lbl": "Poisoning Shield"},
            {"val": "Published", "lbl": "Peer-Reviewed Study"}
        ],
        "problem": "Hospitals or fleets of autonomous vehicles need to train shared AI models together without exposing sensitive patient medical records or vehicle GPS coordinates to central servers. However, if a rogue or hacked device submits corrupted data, it can poison and crash the shared AI brain.",
        "solution": "Engineered a mathematical 'Trust Gate' algorithm that inspects AI model updates from every participant before accepting them into the global network. It detects subtle mathematical misalignments, instantly blocking and rejecting malicious updates without needing to look at private raw data.",
        "impact": "Maintained 99.1% AI model accuracy even under coordinated cyber sabotage where standard federated learning failed completely, paving the way for safe, privacy-preserving AI collaboration across hospitals and connected vehicles."
    },
    {
        "num": "22",
        "title": "High-Throughput Network Intrusion Detection — ANOVA F-Test NIDS",
        "category": "Cybersecurity & Machine Learning · Real-Time Defense",
        "client": "Peer-Reviewed Research · Sole Author: Ahsan Tariq",
        "timeline": "2025 – 2026",
        "slug": "unsw-intrusion-detection",
        "badge": "Academic Research",
        "badge_color": "#10b981",
        "metrics": [
            {"val": "98.67%", "lbl": "Cyber Threat Accuracy"},
            {"val": "69.4%", "lbl": "Network Clutter Removed"},
            {"val": "< 1ms", "lbl": "Threat Detection Latency"},
            {"val": "82,332", "lbl": "Network Flow Records Tested"}
        ],
        "problem": "Modern enterprise networks face thousands of sophisticated hacking attempts, malware intrusions, and denial-of-service attacks every hour. Traditional AI firewalls get overwhelmed trying to analyze dozens of complex network attributes for every single packet, causing network lag or letting stealthy attacks slip through.",
        "solution": "Engineered a fast, lightweight cybersecurity defense pipeline using ANOVA statistical mathematics. It strips away 70% of network data clutter, focusing exclusively on the 15 most critical threat signals to identify cyber attacks with 98.67% accuracy in less than a millisecond.",
        "impact": "Achieved state-of-the-art 98.67% threat detection accuracy on the modern UNSW-NB15 cybersecurity dataset, outperforming slower and more expensive deep learning firewalls while maintaining lightning-fast network speeds."
    },

    # ─── TRACK 12: FIELD ROBOTICS SLAM & AERIAL UAV AUTONOMY ─────
    {
        "num": "23",
        "title": "Clearpath Husky A200 UGV — Autonomous 4x4 SLAM & Dijkstra Navigation",
        "category": "Field Robotics · Autonomous Navigation & SLAM",
        "client": "Field Robotics & Autonomous Systems · Clearpath Robotics",
        "timeline": "2025 – 2026",
        "slug": "husky-slam-navigation",
        "badge": "Field Robotics",
        "badge_color": "#f59e0b",
        "metrics": [
            {"val": "20mm", "lbl": "Laser Map Resolution"},
            {"val": "100%", "lbl": "Autonomous Obstacle Avoidance"},
            {"val": "0 Human", "lbl": "Remote Control Required"},
            {"val": "1.07m", "lbl": "Calibrated Wheelbase"}
        ],
        "problem": "Operating heavy-duty industrial vehicles in hazardous, unmapped environments (like mining tunnels, search-and-rescue disaster sites, or construction areas) is dangerous for human drivers, while remote-controlled vehicles lose signal and crash into obstacles.",
        "solution": "Engineered a complete autonomous navigation brain on a rugged Clearpath Husky 4x4 outdoor robot in ROS and Gazebo. The robot scans its surroundings with laser sensors, builds an accurate digital 2D floorplan in real time, and calculates the safest obstacle-free driving route autonomously.",
        "impact": "Enabled unmanned rugged ground robots to navigate dangerous, unmapped territory safely without human drivers, accurately building 20mm resolution terrain maps while navigating around sudden obstacles."
    },
    {
        "num": "24",
        "title": "Hector Quadrotor UAV & Smart Wheelchair — Flight Dynamics & Autonav",
        "category": "Aerial Drone & Assistive Mobility · 3D Flight Control",
        "client": "Autonomous Drone & Hospital Mobility · ROS & Gazebo 3D",
        "timeline": "2025 – 2026",
        "slug": "hector-quadrotor-uav",
        "badge": "Aerial & Ground Robotics",
        "badge_color": "#38bdf8",
        "metrics": [
            {"val": "< 5cm", "lbl": "Drone Altitude Hover Error"},
            {"val": "100 Hz", "lbl": "PID Flight Feedback"},
            {"val": "100%", "lbl": "Doorway Passage Safety"},
            {"val": "0 Collisions", "lbl": "In Hospital Corridors"}
        ],
        "problem": "1) Drones in tight indoor spaces drift, shake, and crash due to air turbulence and wall reflections without GPS. 2) Wheelchair-bound hospital patients struggle to navigate narrow clinic corridors, constantly scraping door frames and walls.",
        "solution": "Engineered two high-precision autonomous navigation systems: 1) An autonomous quadrotor drone equipped with a 100 Hz cascade PID flight controller that takes off, hovers steadily in mid-air with sub-5cm altitude error, and flies through 3D waypoints. 2) A self-driving smart wheelchair that uses laser scanners to center itself through narrow hospital doorways with zero collisions.",
        "impact": "Delivered sub-5cm flight stability for autonomous indoor drones without GPS, and gave hospital patients a crash-proof autonomous wheelchair that navigates narrow clinic hallways safely."
    }
]

TOTAL_PAGES = 1 + (len(case_studies) // 2) + 1  # Cover + 12 project pages + 1 closing summary = 14 pages

html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Ahsan Tariq — Case Studies & Business Impact Dossier</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Outfit:wght@400;500;600;700;800&family=Plus+Jakarta+Sans:wght@400;500;600;700&family=JetBrains+Mono:wght@500;600;700&display=swap" rel="stylesheet">
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
    --bg: #07090e;
    --card: #0d111a;
    --accent: #ffba49;
    --cyan: #38bdf8;
    --emerald: #10b981;
    --coral: #f43f5e;
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

/* Top Header & Bottom Footer */
.doc-header {{
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding-bottom: 5px;
    border-bottom: 1px solid rgba(255, 255, 255, 0.08);
    margin-bottom: 8px;
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
.doc-footer {{
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding-top: 5px;
    border-top: 1px solid rgba(255, 255, 255, 0.08);
    margin-top: 8px;
    font-size: 7.2px;
    color: var(--text-dim);
    font-family: var(--font-mono);
}}
.doc-footer a {{
    color: var(--cyan);
    text-decoration: none;
}}

/* Page Title Block */
.page-title-block {{
    margin-bottom: 8px;
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

/* Case Study Cards (2 per page) */
.cs-cards-wrapper {{
    display: flex;
    flex-direction: column;
    gap: 8px;
    flex-grow: 1;
}}
.cs-card {{
    background: var(--card);
    border: 1px solid var(--border);
    border-radius: 8px;
    padding: 10px 12px;
    display: flex;
    flex-direction: column;
    gap: 5px;
    border-left: 4px solid var(--accent);
}}
.cs-card-header {{
    display: flex;
    justify-content: space-between;
    align-items: flex-start;
}}
.cs-num-title {{
    display: flex;
    align-items: center;
    gap: 6px;
}}
.cs-num {{
    font-family: var(--font-mono);
    font-size: 10px;
    font-weight: 800;
    color: var(--accent);
    background: rgba(255, 186, 73, 0.1);
    padding: 2px 5px;
    border-radius: 4px;
}}
.cs-title {{
    font-family: var(--font-heading);
    font-size: 11px;
    font-weight: 700;
    color: #ffffff;
}}
.cs-badge {{
    font-size: 7px;
    font-weight: 700;
    padding: 2px 6px;
    border-radius: 4px;
    text-transform: uppercase;
    white-space: nowrap;
}}
.cs-meta {{
    font-size: 7.2px;
    color: var(--text-dim);
    display: flex;
    gap: 12px;
}}
.cs-meta strong {{
    color: var(--text-secondary);
}}

/* 3 Core Impact Callout Boxes */
.impact-breakdown-grid {{
    display: flex;
    flex-direction: column;
    gap: 4px;
    margin: 3px 0;
}}
.impact-box {{
    border-radius: 5px;
    padding: 5px 8px;
}}
.impact-box.problem {{
    background: rgba(244, 63, 94, 0.05);
    border: 1px solid rgba(244, 63, 94, 0.25);
}}
.impact-box.problem .impact-box-lbl {{
    color: #fb7185;
}}
.impact-box.solution {{
    background: rgba(56, 189, 248, 0.05);
    border: 1px solid rgba(56, 189, 248, 0.25);
}}
.impact-box.solution .impact-box-lbl {{
    color: #38bdf8;
}}
.impact-box.results {{
    background: rgba(16, 185, 129, 0.06);
    border: 1px solid rgba(16, 185, 129, 0.25);
}}
.impact-box.results .impact-box-lbl {{
    color: #34d399;
}}
.impact-box-lbl {{
    font-size: 6.8px;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.6px;
    margin-bottom: 2px;
    display: flex;
    align-items: center;
    gap: 4px;
}}
.impact-box p {{
    font-size: 7.8px;
    color: #f1f5f9;
    line-height: 1.4;
}}

/* Key Metric Badges */
.metrics-row {{
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 5px;
    margin: 3px 0;
}}
.metric-pill {{
    background: rgba(255, 255, 255, 0.03);
    border: 1px solid var(--border);
    border-radius: 4px;
    padding: 4px 6px;
    text-align: center;
}}
.metric-val {{
    font-family: var(--font-heading);
    font-size: 9.5px;
    font-weight: 800;
    color: var(--accent);
    line-height: 1.1;
}}
.metric-lbl {{
    font-size: 6.2px;
    color: var(--text-dim);
    margin-top: 1px;
    text-transform: uppercase;
    font-weight: 600;
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
    margin-top: 2px;
    box-shadow: 0 2px 8px rgba(255, 186, 73, 0.3);
}}

/* Cover Page */
.cover-hero {{
    display: flex;
    flex-direction: column;
    align-items: center;
    text-align: center;
    padding: 12mm 0 6mm;
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
    grid-template-columns: repeat(4, 1fr);
    gap: 8px;
    width: 100%;
    margin-bottom: 16px;
}}
.cover-stat-card {{
    background: var(--card);
    border: 1px solid var(--border);
    border-radius: 6px;
    padding: 9px 8px;
    text-align: center;
}}
.cover-stat-val {{
    font-family: var(--font-heading);
    font-size: 16px;
    font-weight: 800;
    color: var(--accent);
    line-height: 1.1;
}}
.cover-stat-lbl {{
    font-size: 7px;
    color: var(--text-muted);
    margin-top: 3px;
    font-weight: 600;
    text-transform: uppercase;
}}
.cover-guide-box {{
    background: rgba(56, 189, 248, 0.06);
    border: 1px solid rgba(56, 189, 248, 0.25);
    border-radius: 8px;
    padding: 10px 14px;
    width: 100%;
    text-align: left;
}}
.cover-guide-title {{
    font-family: var(--font-heading);
    font-size: 9.5px;
    font-weight: 700;
    color: var(--cyan);
    margin-bottom: 3px;
}}
.cover-guide-box p {{
    font-size: 7.8px;
    color: #e2e8f0;
    line-height: 1.45;
}}

/* Closing Page (Page 14) */
.closing-page-container {{
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    text-align: center;
    padding: 15mm 10mm;
    gap: 15px;
}}
.closing-hero-box {{
    background: var(--card);
    border: 1px solid var(--border);
    border-radius: 10px;
    padding: 16px 20px;
    width: 100%;
    max-width: 170mm;
    border-top: 4px solid var(--accent);
}}
.closing-hero-box h2 {{
    font-family: var(--font-heading);
    font-size: 18px;
    font-weight: 800;
    color: #ffffff;
    margin-bottom: 6px;
}}
.closing-hero-box p {{
    font-size: 8.5px;
    color: var(--text-secondary);
    line-height: 1.5;
    margin-bottom: 12px;
}}
.summary-grid-3 {{
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 10px;
    width: 100%;
    max-width: 170mm;
}}
.summary-card {{
    background: var(--card);
    border: 1px solid var(--border);
    border-radius: 6px;
    padding: 10px 8px;
    text-align: center;
}}
.summary-card h4 {{
    font-family: var(--font-heading);
    font-size: 10px;
    font-weight: 700;
    color: var(--accent);
    margin-bottom: 3px;
}}
.summary-card p {{
    font-size: 7.4px;
    color: var(--text-muted);
    line-height: 1.35;
}}
.contact-pill-row {{
    display: flex;
    justify-content: center;
    gap: 12px;
    margin-top: 8px;
}}
.contact-big-btn {{
    display: inline-flex;
    align-items: center;
    gap: 6px;
    background: #0b0f19;
    border: 1px solid var(--border);
    padding: 6px 14px;
    border-radius: 6px;
    color: #ffffff;
    font-size: 8px;
    font-weight: 700;
    text-decoration: none;
}}
</style>
</head>
<body>
"""

# ─── PAGE 1: COVER PAGE ─────────────────────────────────────────
html += f"""
<div class="pdf-page">
    <div class="doc-header">
        <div><span class="doc-header-brand">AHSAN TARIQ</span> · CASE STUDIES COMPENDIUM</div>
        <div>BUSINESS PROBLEMS SOLVED &amp; REAL-WORLD IMPACT</div>
        <div><a href="{BASE_URL}/case-studies/" target="_blank">{BASE_URL}/case-studies/</a></div>
    </div>

    <div class="cover-hero">
        <img src="data:image/jpeg;base64,{prof_b64}" class="cover-avatar" alt="Ahsan Tariq">
        <h1 class="cover-name">Ahsan Tariq</h1>
        <div class="cover-role-badge">
            AI/ML Engineer <span>|</span> Forward Deployed Engineer <span>|</span> Systems Architect
        </div>
        <p class="cover-summary">
            A non-technical, executive business impact compendium detailing <strong>24 production systems and architectural case studies</strong> engineered across the United States, United Kingdom, and Europe. Structured specifically for founders, CEOs, and non-developers to clearly explain <strong>what painful problems existed</strong>, <strong>how they were solved with AI &amp; automation</strong>, and <strong>what measurable business results were delivered</strong>.
        </p>

        <div class="cover-links">
            <a href="{BASE_URL}/case-studies/" target="_blank" class="cover-link-pill accent">📁 Case Studies Hub: ahsantariq.ranbval.com/case-studies/ ↗</a>
            <a href="{BASE_URL}" target="_blank" class="cover-link-pill">🌐 Main Portfolio ↗</a>
            <a href="mailto:ahsantariq0724@gmail.com" class="cover-link-pill">📧 ahsantariq0724@gmail.com</a>
            <a href="https://www.linkedin.com/in/ahsan-tariq-comp-engr/" target="_blank" class="cover-link-pill">🔗 LinkedIn Profile ↗</a>
        </div>

        <div class="cover-stats-grid">
            <div class="cover-stat-card">
                <div class="cover-stat-val">24</div>
                <div class="cover-stat-lbl">In-Depth Case Studies</div>
            </div>
            <div class="cover-stat-card">
                <div class="cover-stat-val">60% – 90%</div>
                <div class="cover-stat-lbl">Manual Effort Slashed</div>
            </div>
            <div class="cover-stat-card">
                <div class="cover-stat-val">$141M+</div>
                <div class="cover-stat-lbl">Active Operations Mirrored</div>
            </div>
            <div class="cover-stat-card">
                <div class="cover-stat-val">&lt; 60s</div>
                <div class="cover-stat-lbl">Lead Voice Turnaround</div>
            </div>
        </div>

        <div class="cover-guide-box">
            <div class="cover-guide-title">📖 How This Case Studies Guide Is Structured for Non-Developers:</div>
            <p>
                Every project in this document follows a three-part business framework:
                <br>• <strong>1. The Painful Problem Faced:</strong> What manual bottleneck, lost revenue, or operational chaos the client suffered before.
                <br>• <strong>2. The Smart Solution Built:</strong> In plain English, how the software or AI system was designed to fix the root problem.
                <br>• <strong>3. The Real-World Business Results:</strong> Concrete hours saved, dollars cut, error rates eliminated, and direct links to live case studies.
            </p>
        </div>
    </div>

    <div class="doc-footer">
        <div>Ahsan Tariq · Executive Case Studies Compendium</div>
        <div>PAGE 01 OF {TOTAL_PAGES:02d}</div>
    </div>
</div>
"""

# ─── PAGES 2 to 13: 2 CASE STUDIES PER PAGE (TOTAL 24) ──────────
current_page = 2
for i in range(0, len(case_studies), 2):
    pair = case_studies[i:i+2]
    first_cs = pair[0]

    html += f"""
<div class="pdf-page">
    <div class="doc-header">
        <div><span class="doc-header-brand">AHSAN TARIQ</span> · CASE STUDIES DOSSIER</div>
        <div>REAL-WORLD PROBLEMS SOLVED &amp; BUSINESS IMPACT · PAGE {current_page:02d}</div>
        <div><a href="{BASE_URL}/case-studies/" target="_blank">ALL CASE STUDIES ↗</a></div>
    </div>

    <div>
        <div class="page-title-block">
            <span class="page-title-badge">Impact Deep Dives</span>
            <h2>{first_cs["category"].split(' · ')[0]} Case Studies</h2>
            <p>Non-technical problem breakdowns and measurable operational results delivered for international business clients.</p>
        </div>

        <div class="cs-cards-wrapper">
    """

    for cs in pair:
        cs_url = cs.get("custom_url") if cs.get("custom_url") else f"{BASE_URL}/case-studies/{cs['slug']}/"
        badge_style = f"background: {cs['badge_color']}20; border: 1px solid {cs['badge_color']}50; color: {cs['badge_color']};"

        html += f"""
            <div class="cs-card" style="border-left-color: {cs['badge_color']};">
                <div class="cs-card-header">
                    <div class="cs-num-title">
                        <span class="cs-num">#{cs["num"]}</span>
                        <span class="cs-title">{cs["title"]}</span>
                    </div>
                    <span class="cs-badge" style="{badge_style}">{cs["badge"]}</span>
                </div>

                <div class="cs-meta">
                    <div><strong>Client / Organization:</strong> {cs["client"]}</div>
                    <div><strong>Timeline:</strong> {cs["timeline"]}</div>
                    <div><strong>Domain:</strong> {cs["category"]}</div>
                </div>

                <div class="impact-breakdown-grid">
                    <div class="impact-box problem">
                        <div class="impact-box-lbl">⚠️ The Painful Problem Faced</div>
                        <p>{cs["problem"]}</p>
                    </div>

                    <div class="impact-box solution">
                        <div class="impact-box-lbl">💡 The Smart Solution Built</div>
                        <p>{cs["solution"]}</p>
                    </div>

                    <div class="impact-box results">
                        <div class="impact-box-lbl">🚀 The Real-World Business Results Delivered</div>
                        <p>{cs["impact"]}</p>
                    </div>
                </div>

                <div class="metrics-row">
        """
        for m in cs["metrics"]:
            html += f"""
                    <div class="metric-pill">
                        <div class="metric-val">{m["val"]}</div>
                        <div class="metric-lbl">{m["lbl"]}</div>
                    </div>
            """

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
        <div>Ahsan Tariq · <strong>Case Studies &amp; Business Impact Dossier</strong> · <a href="{BASE_URL}/case-studies/" target="_blank">{BASE_URL}/case-studies/</a></div>
        <div>PAGE {current_page:02d} OF {TOTAL_PAGES:02d}</div>
    </div>
</div>
    """
    current_page += 1

# ─── PAGE 14: CLOSING BUSINESS SUMMARY & ENGAGEMENT DOSSIER ─────
html += f"""
<div class="pdf-page">
    <div class="doc-header">
        <div><span class="doc-header-brand">AHSAN TARIQ</span> · EXECUTIVE DOSSIER</div>
        <div>ENGAGEMENT DOSSIER &amp; NEXT STEPS</div>
        <div><a href="{BASE_URL}" target="_blank">{BASE_URL}</a></div>
    </div>

    <div class="closing-page-container">
        <div class="closing-hero-box">
            <h2>Ready to Eliminate Manual Bottlenecks &amp; Scale with AI?</h2>
            <p>
                Whether you need an autonomous phone assistant to capture customer leads, an automated accounting system to eliminate double-payments, or a multi-cloud architecture that slashes your server bills—I engineer production systems designed to pay for themselves through immediate operational savings.
            </p>
            <div class="contact-pill-row">
                <a href="mailto:ahsantariq0724@gmail.com" class="contact-big-btn">📧 ahsantariq0724@gmail.com</a>
                <a href="{BASE_URL}" target="_blank" class="contact-big-btn" style="border-color: var(--accent); color: var(--accent);">🌐 ahsantariq.ranbval.com ↗</a>
                <a href="https://www.linkedin.com/in/ahsan-tariq-comp-engr/" target="_blank" class="contact-big-btn">🔗 LinkedIn Profile ↗</a>
            </div>
        </div>

        <div class="summary-grid-3">
            <div class="summary-card">
                <h4>Forward Deployed Engineering</h4>
                <p>Direct hands-on integration into your team, bridging high-level business requirements into production software in weeks, not quarters.</p>
            </div>
            <div class="summary-card">
                <h4>Zero-Jargon Transparency</h4>
                <p>Clear, direct communication. You always know what is being built, how it works, and exactly what business impact it generates.</p>
            </div>
            <div class="summary-card">
                <h4>Disciplined Zero-to-Production</h4>
                <p>Enterprise reliability, cryptographic security, sub-second latency, and multi-tenant scaling tested against real-world traffic.</p>
            </div>
        </div>
    </div>

    <div class="doc-footer">
        <div>Ahsan Tariq · Executive Case Studies Compendium</div>
        <div>PAGE {TOTAL_PAGES:02d} OF {TOTAL_PAGES:02d}</div>
    </div>
</div>
</body>
</html>
"""

with open('case-studies-pdf.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Generated case-studies-pdf.html successfully. Size:", len(html), "characters.")
