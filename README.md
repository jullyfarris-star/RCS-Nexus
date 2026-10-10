# RCS-Nexus: Reactive Control System & Context Optimization Framework

RCS-Nexus is an open-source, production-ready system architecture and modular framework designed for orchestrating multi-agent AI ecosystems and optimizing large language model (LLM) context windows.

By utilizing a decentralized **7-layer Reactive Control System (RCS)** topology alongside automated memory defragmentation routines, RCS-Nexus prevents state explosion and significantly lowers token costs in long-running autonomous workflows.

## 🔑 Core Features

- **Decentralized Multi-Agent Orchestration:** Asynchronous pipeline dividing tasks into specialized operational nodes (Temporal, Spatial, Sensory, and Processing streams).
- **Hierarchical Memory Management:** Segregates incoming data into short-term execution buffers and a persistent semantic graph structure.
- **Signal Translation Bridge:** High-throughput translation layer that normalizes raw telemetry, positional variables, and unstructured real-time inputs into formal vector tokens.
- **Context Defragmentation (Sleep Routine):** Automated background cycles that halt external state consumption to analyze memory graphs, consolidate historical records into abstract schemas, and flush execution buffers.

---

## 📐 System Architecture

The ecosystem relies on an asynchronous event-driven layout structured as follows:

```text
RCS-Nexus/
├── rcs_core/
│   ├── agents/
│   │   ├── temporal.py        # Timeline management & epoch validation
│   │   ├── spatial.py         # Relational coordinate calculations
│   │   ├── sensory.py         # Raw ingest & telemetric capture
│   │   └── processing.py      # Local decision engines & state evaluations
│   ├── memory/
│   │   ├── graph_manager.py   # Semantic knowledge graph graph construction
│   │   └── buffer_cleaner.py  # Context defragmentation & sleep executor
│   └── translators/
│       └── signal_bridge.py   # Structural JSON serialization
```

### The Data Flow Topology

```text
[Raw External Data] ──> (Sensory Node) ──> [Signal Bridge]
│
▼
[Temporal Log] <─── [Orchestrator Matrix] ───> [Spatial Coordinate Node]
│
▼
[Processing / Decision]
│
┌───────────────────────┴───────────────────────┐
▼ ▼
[Short-Term Buffer] [Memory Graph Manager]
│ ▲
└─────────────> (Sleep Routine Cycle) ──────────┘
[Defragment & Compress]
```

---

## 🛠️ Deep Dive: The Defragmentation (Sleep) Cycle

In long-lived autonomous applications, direct state accumulation results in contextual drift and linear token cost escalation. RCS-Nexus solves this via an isolated system routing called the **Sleep Cycle**:

1. **Isolation:** The main orchestrator temporarily buffers external incoming telemetry.
2. **Analysis:** The `buffer_cleaner` parses the active Short-Term Buffer to generate entity-relation clusters.
3. **Consolidation:** Intersecting data nodes are pushed to the underlying Knowledge Graph. Redundant structural noise is pruned.
4. **Abstract Compression:** Historical operational logs are condensed into static "state definitions", significantly lessening context weight for subsequent evaluations.
5. **Flush:** The ephemeral processing workspace is wiped, returning the active execution frame to base usage levels.

---

## 🚀 Quick Start

### Prerequisites

- Python 3.10 or higher
- Virtual environment manager (`venv` or `conda`)

### Installation

Clone the repository and install the framework dependencies:

```bash
git clone https://github.com/jullyfarris-star/RCS-Nexus.git
cd RCS-Nexus
python -m venv venv
source venv/bin/activate # On Windows use: venv\Scripts\activate
pip install -r requirements.txt
```

### Basic Usage Example

```python
from rcs_core.orchestrator import NexusOrchestrator

# Initialize the central matrix orchestrator
orchestrator = NexusOrchestrator(config_path="config.json")

# Ingest an external raw signal stream
raw_signal = {"timestamp": 1791641340, "vector_type": "spatial_node", "payload": {"x": 40.0, "y": 1.85}}
orchestrator.process_signal(raw_signal)

# Explicitly trigger the defragmentation (sleep) routine to optimize context
orchestrator.trigger_sleep_cycle()
```
