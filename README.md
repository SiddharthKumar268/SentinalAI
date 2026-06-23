# 🛡️ SentinelAI

## A Full-Lifecycle Automotive Intelligence Platform

**Cognitive Risk Prevention • Incident Intelligence • Human Recovery**

> InnoVent-27 Hackathon | Tata Technologies  
> Category: AI at the Edge Solutions for Automotive  
> Platform Type: 100% Software-Based | Zero Hardware Dependencies

---

## 🧠 What is SentinelAI?

SentinelAI is **not** a crash detector. It is a complete human experience platform wrapped around the worst moment of a driver's life.

While every other automotive AI solution focuses narrowly on the collision event itself, SentinelAI addresses the **full lifecycle**:

| Phase | Focus | Modules |
|-------|-------|---------|
| 🔴 **Pre-Accident** | Preventable cognitive & contextual risks | Cognitive Load Profiler, Route Risk Scorer, Pre-Trip Readiness, Social Drive Intelligence |
| 🟡 **During Accident** | Critical documentation & response | Crash Context Recorder, Witness Statement AI |
| 🟢 **Post-Accident** | Legal, financial & psychological recovery | Legal Document AI, Insurance Negotiation Agent, Psychological Recovery Coach |

---

## 📊 The Problem

- **1.5 lakh+** road accident deaths annually in India
- **30–90 days** average insurance claim settlement time
- **30–40%** of survivors develop PTSD, driving anxiety, or adjustment disorder
- **Zero** existing products address all three failure points

---

## 🏗️ Architecture

```
SentinelAI/
├── mcp-servers/              # MCP Server implementations
│   ├── cognitive-profiler/   # Module 1: Cognitive Load Profiler
│   ├── route-risk/           # Module 2: Route Risk Scorer
│   ├── crash-recorder/       # Module 5: Crash Context Recorder
│   ├── witness-ai/           # Module 6: Witness Statement AI
│   ├── legal-doc/            # Module 7: Legal Document AI
│   └── recovery-coach/       # Module 9: Psychological Recovery Coach
├── shared/                   # Shared utilities and types
├── mcp-config.json           # MCP client configuration
├── requirements.txt          # Python dependencies
├── package.json              # Node.js dependencies
└── .env.example              # Environment variables template
```

---

## 🚀 Quick Start

### Prerequisites
- Python 3.10+
- Node.js 18+
- API Keys: Claude (Anthropic), OpenWeatherMap, Google Maps Platform

### Installation

```bash
# Clone the repository
git clone https://github.com/YOUR_USERNAME/SentinelAI.git
cd SentinelAI

# Install Python dependencies
pip install -r requirements.txt

# Install Node.js dependencies
npm install

# Configure environment
cp .env.example .env
# Edit .env with your API keys
```

### Running MCP Servers

```bash
# Start the Cognitive Profiler MCP server
python mcp-servers/cognitive-profiler/server.py

# Start the Route Risk Scorer MCP server
python mcp-servers/route-risk/server.py

# Start the Crash Context Recorder MCP server
python mcp-servers/crash-recorder/server.py
```

---

## 🔧 Technology Stack

| Module | Core Technology | Data Source |
|--------|----------------|-------------|
| Cognitive Load Profiler | Claude API, Web Speech API | Driver voice/text input |
| Route Risk Scorer | Python, OSMnx, XGBoost | OpenStreetMap, NCRB, OpenWeatherMap |
| Pre-Trip Readiness | Claude API, Embeddings | Driver check-in history |
| Social Drive Intelligence | Supabase Realtime | Anonymised fleet signals |
| Crash Context Recorder | Claude API, Maps API | Device GPS, weather data |
| Witness Statement AI | Claude API, Speech API | Live voice input |
| Legal Document AI | Claude API, docx generation | Incident record, MVA knowledge base |
| Insurance Negotiation | Claude API, Agentic flow | Claim data, IRDAI guidelines |
| Recovery Coach | Claude API, n8n scheduling | PHQ-9, PCL-5 instruments |

---

## 🛡️ Privacy & Security

- All signals are **anonymised at source**
- Cryptographic hashing (SHA-256) for incident records
- Row-level encryption for sensitive health data
- Data minimisation: check-in responses processed in-memory
- User owns all their data with full export capability

---

## 📄 License

MIT License — see [LICENSE](LICENSE) for details.

---

## 🤝 Contributing

Contributions are welcome! Please read our contributing guidelines before submitting a PR.

---

<p align="center">
  <strong>SentinelAI</strong> — Because safety doesn't end at the collision.
</p>
