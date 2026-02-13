"""
OMS Expert Reference Bot
AI-powered clinical reference for oral and maxillofacial surgery.
Every answer cites verifiable sources.
"""

import streamlit as st
from anthropic import Anthropic
from pathlib import Path
import datetime
import json

# --- Configuration ---
MODEL = "claude-sonnet-4-5-20250929"
MAX_TOKENS = 4096
KNOWLEDGE_BASE_PATH = Path(__file__).parent / "knowledge_base.txt"
LOG_PATH = Path(__file__).parent / "query_log.jsonl"

# --- Page Setup ---
st.set_page_config(
    page_title="OMS Expert Reference",
    page_icon="\U0001FA7A",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- Load Knowledge Base ---
@st.cache_data
def load_knowledge_base():
    if KNOWLEDGE_BASE_PATH.exists():
        return KNOWLEDGE_BASE_PATH.read_text(encoding="utf-8")
    return "Knowledge base not yet built. Run build_knowledge_base.py first."

knowledge_base = load_knowledge_base()

# --- System Prompt ---
SYSTEM_PROMPT = f"""You are the OMS Expert Reference Bot, an AI clinical reference for a practicing oral and maxillofacial surgeon in the United States.

CORE RULES:
1. EVERY response must cite specific sources: AAOMS ParCare section numbers, CPT/CDT/ICD-10 codes, journal references (JOMS, IJOMS, OOO), FDA clearance numbers, or textbook chapters.
2. If you are not confident in an answer, say so explicitly and suggest where to find the information (e.g., "Check AAOMS ParCare Section 3 for updated guidelines" or "Verify current CPT code with the AMA CPT manual").
3. For coding questions, always distinguish between CDT (dental) and CPT (medical) codes and note when cross-coding to medical insurance is appropriate.
4. Never provide information you cannot trace to a source. Unsourced clinical claims are unacceptable.
5. Use precise medical terminology appropriate for a board-certified OMS surgeon.
6. For drug dosages and protocols, always note that the surgeon should verify against current formulary and institutional protocols.
7. Flag when content may be subject to annual updates (CPT codes, fee schedules, guidelines).

KNOWLEDGE DOMAINS:
- Clinical surgery: All 11 AAOMS ParCare areas (dentoalveolar, implants, orthognathic, trauma, pathology, TMJ, craniofacial, cosmetic, sleep apnea, anesthesia, infections)
- Surgical technology: Robotic systems (Yomi, da Vinci, Hugo RAS), navigation (Brainlab, Stryker, KLS Martin), 3D printing/VSP, AI diagnostics
- Practice operations: CPT/CDT coding, ICD-10, cross-coding, Medicare/Medicaid, EHR systems, compliance, financials
- Pharmacology: Analgesics, antibiotics, sedation agents, hemostatics, biologics
- Professional: ABOMS certification/MOC, medicolegal, telemedicine

RESPONSE FORMAT:
- Lead with the direct answer
- Follow with supporting evidence and source citations
- Include relevant CPT/CDT codes when applicable
- Note any caveats, contraindications, or areas of active debate
- End complex answers with "Sources:" listing specific references

KNOWLEDGE BASE:
{knowledge_base}
"""

# --- Sidebar ---
with st.sidebar:
    st.markdown(
        """
        <div style="text-align:center; padding: 1em 0;">
            <h2 style="margin:0; color: #1B3A5C;">OMS Expert Reference</h2>
            <p style="color: #495057; font-size: 0.85rem; margin-top: 0.3em;">
                Evidence-based. Source-cited.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.divider()

    st.markdown("**Clinical Topics**")
    topics = [
        "Surgical Anatomy",
        "Imaging & Diagnosis",
        "Anesthesia & Sedation",
        "Pharmacology",
        "Dentoalveolar Surgery",
        "Dental Implants",
        "Oral Pathology & Oncology",
        "Facial Trauma",
        "Orthognathic Surgery",
        "TMJ Surgery",
        "Craniofacial & Cleft",
        "Cosmetic Surgery",
        "Sleep Apnea (OSA)",
        "Robotic Surgery",
        "Navigation & Digital",
        "3D Printing & VSP",
        "Billing & Coding",
        "Practice Management",
        "Telemedicine",
        "Emerging Frontiers",
    ]
    for topic in topics:
        st.markdown(f"<span style='font-size:0.8rem; color:#495057;'>- {topic}</span>", unsafe_allow_html=True)

    st.divider()

    # API Key
    api_key = None
    if hasattr(st, "secrets") and "ANTHROPIC_API_KEY" in st.secrets:
        api_key = st.secrets["ANTHROPIC_API_KEY"]
    else:
        import os
        api_key = os.environ.get("ANTHROPIC_API_KEY")

    if not api_key:
        api_key = st.text_input("Anthropic API Key", type="password", help="Required for AI responses")

    st.divider()
    if st.button("Clear History", use_container_width=True):
        st.session_state.messages = []
        st.rerun()

# --- Session State ---
if "messages" not in st.session_state:
    st.session_state.messages = []

# --- Main Content ---
if not st.session_state.messages:
    st.markdown(
        """
        <div style="text-align:center; padding: 2em 0 1em;">
            <h3 style="color: #1B3A5C;">Ask any clinical, coding, or practice question.</h3>
            <p style="color: #868E96; font-size: 0.85rem;">Every answer will cite its source.</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    col1, col2, col3 = st.columns(3)
    with col1:
        st.info("What are the CPT codes for open treatment of a mandibular angle fracture?")
    with col2:
        st.info("When should I bill medical vs. dental insurance for third molar extractions?")
    with col3:
        st.info("What is the current evidence for the Yomi robotic implant system?")

# --- Chat Display ---
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# --- Chat Input ---
if prompt := st.chat_input("Ask a clinical, coding, or practice question..."):
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("user"):
        st.markdown(prompt)

    if not api_key:
        with st.chat_message("assistant"):
            st.error("Please provide an Anthropic API key in the sidebar.")
    else:
        with st.chat_message("assistant"):
            with st.spinner("Searching knowledge base..."):
                try:
                    client = Anthropic(api_key=api_key)
                    api_messages = [
                        {"role": m["role"], "content": m["content"]}
                        for m in st.session_state.messages
                    ]
                    response = client.messages.create(
                        model=MODEL,
                        max_tokens=MAX_TOKENS,
                        system=SYSTEM_PROMPT,
                        messages=api_messages,
                    )
                    assistant_message = response.content[0].text
                    st.markdown(assistant_message)
                    st.session_state.messages.append(
                        {"role": "assistant", "content": assistant_message}
                    )

                    # Log query for analytics
                    log_entry = {
                        "timestamp": datetime.datetime.now().isoformat(),
                        "question": prompt,
                        "response_length": len(assistant_message),
                        "model": MODEL,
                    }
                    with open(LOG_PATH, "a") as f:
                        f.write(json.dumps(log_entry) + "\n")

                except Exception as e:
                    st.error(f"Error: {str(e)}")
