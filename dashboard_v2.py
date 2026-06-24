import streamlit as st
import pandas as pd

from dashboard_modules.home_tab import show_home_tab
from dashboard_modules.leaderboard_tab import show_leaderboard_tab
from dashboard_modules.analytics_tab import show_analytics_tab
from dashboard_modules.module_analysis_tab import show_module_analysis_tab
from dashboard_modules.low_performer_tab import show_low_performer_tab
from dashboard_modules.student_search_tab import show_student_search_tab
from dashboard_modules.reports_tab import show_reports_tab

# ==========================================
# PAGE CONFIG
# ==========================================

st.set_page_config(
    page_title="ML & Agentic AI Dashboard",
    page_icon="📊",
    layout="wide"
)

MASTER_FILE = "Reports/Master_Report.xlsx"

master_df = pd.read_excel(MASTER_FILE)

menu = st.sidebar.radio(
    "Navigation",
    [
        "Home",
        "Leaderboard",
        "Analytics",
        "Module Analysis",
        "Low Performers",
        "Student Search",
        "Reports"
    ]
)

# dashboard_v2.py



from dashboard_modules.home_tab import show_home_tab

# ==========================================
# PAGE CONFIG
# ==========================================

st.set_page_config(

    page_title="ML & Agentic AI Dashboard",

    page_icon="📊",

    layout="wide"

)

# ==========================================
# LOAD DATA
# ==========================================


    MASTER_FILE = "Reports/Master_Report.xlsx"


master_df = pd.read_excel(

    MASTER_FILE

)

# # ==========================================
# # SIDEBAR
# # ==========================================

# st.sidebar.title(

#     "ML & Agentic AI"

# )

# menu = st.sidebar.radio(

#     "Navigation",

#     [

#         "Home"

#     ]

# )

# ==========================================
# HOME TAB
# ==========================================

if menu == "Home":

    show_home_tab(
        master_df
    )

elif menu == "Leaderboard":

    show_leaderboard_tab(
        master_df
    )

elif menu == "Analytics":

    show_analytics_tab(
        master_df
    )
elif menu == "Module Analysis":

    show_module_analysis_tab(

        master_df

    )
elif menu == "Low Performers":

    show_low_performer_tab(

        master_df

    )
elif menu == "Student Search":

    show_student_search_tab(

        master_df

    )
elif menu == "Reports":

    show_reports_tab()