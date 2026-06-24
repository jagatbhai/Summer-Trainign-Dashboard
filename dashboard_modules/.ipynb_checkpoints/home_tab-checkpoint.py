# containing:

# KPI cards
# Total Students
# Average Percentage
# Highest Percentage
# Lowest Percentage
# Charts
# Grade Distribution Pie Chart
# Top 10 Bar Chart
# Overall Percentage Histogram

# dashboard_modules/home_tab.py

import streamlit as st
import plotly.express as px


def show_home_tab(master_df):

    # ====================================
    # TITLE
    # ====================================

    st.title(
        "📊 ML & Agentic AI Training Dashboard"
    )

    st.markdown("---")

    # ====================================
    # KPI CARDS
    # ====================================

    col1, col2, col3, col4 = st.columns(4)

    with col1:

        st.metric(

            "Total Students",

            len(master_df)

        )

    with col2:

        st.metric(

            "Average Percentage",

            round(

                master_df["Overall_Percentage"]

                .mean(),

                2

            )

        )

    with col3:

        st.metric(

            "Highest Percentage",

            round(

                master_df["Overall_Percentage"]

                .max(),

                2

            )

        )

    with col4:

        st.metric(

            "Lowest Percentage",

            round(

                master_df["Overall_Percentage"]

                .min(),

                2

            )

        )

    st.markdown("---")

    # ====================================
    # TOP 10 STUDENTS
    # ====================================

    col1, col2 = st.columns(2)

    with col1:

        st.subheader(
            "🏆 Top 10 Students"
        )

        top10 = (

            master_df

            .sort_values(

                by="Rank"

            )

            .head(

                10

            )

        )

        fig = px.bar(

            top10,

            x="Overall_Percentage",

            y="Name",

            orientation="h",

            text="Overall_Percentage",

            title="Top 10 Students"

        )

        fig.update_traces(

            texttemplate='%{text:.1f}',

            textposition='outside'

        )

        st.plotly_chart(

            fig,

            use_container_width=True

        )

    # ====================================
    # GRADE DISTRIBUTION
    # ====================================

    with col2:

        st.subheader(
            "🎓 Grade Distribution"
        )

        grade_dist = (

            master_df["Grade"]

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

            hole=0.4,

            title="Grade Distribution"

        )

        st.plotly_chart(

            fig,

            use_container_width=True

        )

    st.markdown("---")

    # ====================================
    # HISTOGRAM
    # ====================================

    st.subheader(
        "📈 Overall Percentage Distribution"
    )

    fig = px.histogram(

        master_df,

        x="Overall_Percentage",

        nbins=20,

        title="Overall Percentage Distribution"

    )

    st.plotly_chart(

        fig,

        use_container_width=True

    )

    # ====================================
    # QUICK LEADERBOARD
    # ====================================

    st.subheader(
        "🥇 Top 10 Leaderboard"
    )

    st.dataframe(

        top10[

            [

                "Rank",

                "Name",

                "Overall_Percentage",

                "Grade"

            ]

        ],

        use_container_width=True

    )