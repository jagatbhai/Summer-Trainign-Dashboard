# dashboard_modules/leaderboard_tab.py

import streamlit as st
import plotly.express as px


def show_leaderboard_tab(master_df):

    st.title(
        "🏆 Leaderboard"
    )

    st.markdown("---")

    # ======================================
    # TOP 20 CHART
    # ======================================

    st.subheader(
        "Top 20 Students"
    )

    top20 = (

        master_df

        .sort_values(

            by="Rank"

        )

        .head(

            20

        )

    )

    fig = px.bar(

        top20,

        x="Overall_Percentage",

        y="Name",

        orientation="h",

        color="Grade",

        text="Overall_Percentage",

        title="Top 20 Students"

    )

    fig.update_traces(

        texttemplate='%{text:.1f}',

        textposition='outside'

    )

    st.plotly_chart(

        fig,

        use_container_width=True

    )

    st.markdown("---")

    # ======================================
    # TOP 10 TABLE
    # ======================================

    st.subheader(
        "🥇 Top 10 Students"
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

    st.dataframe(

        top10[

            [

                "Rank",

                "Name",

                "Overall_Percentage",

                "Final_Percentile",

                "Grade"

            ]

        ],

        use_container_width=True

    )

    st.markdown("---")

    # ======================================
    # SEARCH BY RANK
    # ======================================

    st.subheader(
        "🔍 Search by Rank"
    )

    rank = st.number_input(

        "Enter Rank",

        min_value=1,

        step=1

    )

    result = master_df[

        master_df["Rank"]

        == rank

    ]

    if len(result) > 0:

        st.dataframe(

            result[

                [

                    "Name",

                    "Email",

                    "Rank",

                    "Overall_Percentage",

                    "Grade"

                ]

            ],

            use_container_width=True

        )

    st.markdown("---")

    # ======================================
    # COMPLETE LEADERBOARD
    # ======================================

    st.subheader(
        "📋 Complete Leaderboard"
    )

    leaderboard_df = (

        master_df

        [

            [

                "Rank",

                "Name",

                "Overall_Percentage",

                "Final_Percentile",

                "Grade"

            ]

        ]

        .sort_values(

            by="Rank"

        )

    )

    st.dataframe(

        leaderboard_df,

        use_container_width=True

    )