# dashboard_modules/low_performer_tab.py

import streamlit as st
import plotly.express as px


def show_low_performer_tab(master_df):

    st.title(
        "⚠ Low Performers Analysis"
    )

    st.markdown("---")

    # ====================================
    # Threshold Selector
    # ====================================

    threshold = st.slider(

        "Select Threshold Percentage",

        min_value=0,

        max_value=100,

        value=50

    )

    # ====================================
    # Filter Students
    # ====================================

    low_df = (

        master_df[

            master_df["Overall_Percentage"]

            < threshold

        ]

        .sort_values(

            by="Overall_Percentage"

        )

    )

    # ====================================
    # KPI Cards
    # ====================================

    col1, col2, col3 = st.columns(3)

    with col1:

        st.metric(

            "Threshold",

            f"{threshold}%"

        )

    with col2:

        st.metric(

            "Low Performers",

            len(low_df)

        )

    with col3:

        st.metric(

            "Total Students",

            len(master_df)

        )

    st.markdown("---")

    # ====================================
    # Horizontal Bar Chart
    # ====================================

    st.subheader(
        "Low Performers Chart"
    )

    if len(low_df) > 0:

        fig = px.bar(

            low_df,

            x="Overall_Percentage",

            y="Name",

            orientation="h",

            color="Grade",

            text="Overall_Percentage",

            title=f"Students Below {threshold}%"

        )

        fig.update_traces(

            texttemplate='%{text:.1f}',

            textposition='outside'

        )

        st.plotly_chart(

            fig,

            use_container_width=True

        )

    else:

        st.success(

            "No students below threshold."

        )

    st.markdown("---")

    # ====================================
    # Low Performer Table
    # ====================================

    st.subheader(
        "Low Performer Details"
    )

    if len(low_df) > 0:

        st.dataframe(

            low_df[

                [

                    "Rank",

                    "Name",

                    "Email",

                    "Overall_Percentage",

                    "Final_Percentile",

                    "Grade"

                ]

            ],

            use_container_width=True

        )

    st.markdown("---")

    # ====================================
    # Grade Distribution
    # ====================================

    if len(low_df) > 0:

        st.subheader(
            "Grade Distribution among Low Performers"
        )

        grade_dist = (

            low_df["Grade"]

            .value_counts()

            .reset_index()

        )

        grade_dist.columns = [

            "Grade",

            "Count"

        ]

        fig = px.pie(

            grade_dist,

            names="Grade",

            values="Count",

            hole=0.4

        )

        st.plotly_chart(

            fig,

            use_container_width=True

        )

    st.markdown("---")

    # ====================================
    # Download CSV
    # ====================================

    csv = low_df.to_csv(

        index=False

    )

    st.download_button(

        label="⬇ Download Low Performer Report",

        data=csv,

        file_name="Low_Performer_Report.csv",

        mime="text/csv"

    )