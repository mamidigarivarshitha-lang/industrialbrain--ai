import streamlit as st
from modules.rag_engine import ask_question
from modules.knowledge_graph import build_graph
import networkx as nx
import matplotlib.pyplot as plt
from modules.rca_agent import analyze_failure
from modules.compliance_checker_v2 import check_compliance

st.set_page_config(
    page_title="IndustrialBrain AI",
    layout="wide"
)

st.title("🏭 IndustrialBrain AI")

st.subheader(
    "Unified Asset & Operations Intelligence Platform"
)

tab1, tab2, tab3, tab4, tab5 = st.tabs(
    [
        "📄 Documents",
        "🤖 AI Assistant",
        "🔗 Knowledge Graph",
        "⚙ RCA Agent",
        "📋 Compliance"
    ]
)

with tab1:
    st.header("Upload Industrial Documents")

    uploaded_files = st.file_uploader(
        "Upload Files",
        accept_multiple_files=True,
        type=["txt"]
    )

    if uploaded_files:
        for uploaded_file in uploaded_files:

            content = uploaded_file.read().decode("utf-8")

            file_path = f"data/raw/{uploaded_file.name}"

            with open(file_path, "w", encoding="utf-8") as f:
                f.write(content)

        st.success("Files uploaded and saved successfully!")

        # Optional: show uploaded file names
        st.subheader("Uploaded Files")
        for file in uploaded_files:
            st.write(file.name)

with tab2:

    st.header("Industrial AI Assistant")

    question = st.text_input(
        "Ask a question about plant documents"
    )

    if st.button("Ask AI"):

        answer = ask_question(question)

        st.success(answer)

with tab3:

    st.header("Knowledge Graph")

    G = build_graph()

    fig, ax = plt.subplots(
        figsize=(8,5)
    )

    pos = nx.spring_layout(G)

    nx.draw(
        G,
        pos,
        with_labels=True,
        node_size=3000,
        ax=ax
    )

    st.pyplot(fig)

with tab4:

    st.header("Root Cause Analysis Agent")

    issue = st.text_area(
        "Describe Equipment Failure"
    )

    if st.button("Analyze Failure"):

        result = analyze_failure(issue)

        st.success(result)
        
with tab5:

    st.header("📋 Compliance Checker")

    if st.button("Run Compliance Check"):

        score, results = check_compliance()

        # 🔥 Dashboard style metrics
        col1, col2, col3 = st.columns(3)

        col1.metric("Assets Monitored", "12")
        col2.metric("Alerts", "3")
        col3.metric("Compliance", f"{score}%")

        st.divider()

        # 📊 Progress bar
        st.progress(score / 100)

        st.metric(
            label="Compliance Score",
            value=f"{score}%"
        )

        # 🎯 Status message
        if score == 100:
            st.success("✅ Fully Compliant System")
        elif score >= 75:
            st.warning("⚠️ Minor Compliance Gaps")
        else:
            st.error("❌ Non-Compliant System")

        # 📅 Next inspection
        st.info("📅 Next Inspection: 15 July 2026")

        st.divider()

        # 📋 Results section
        st.subheader("Compliance Checks")

        for item in results:
            st.write(item)