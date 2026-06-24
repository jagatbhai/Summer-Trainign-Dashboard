# dashboard_modules/analytics_tab.py

import streamlit as st
import plotly.express as px
import pandas as pd


def show_analytics_tab(master_df):

    st.title(
        "📈 Analytics"
    )

    st.markdown("---")

    # =====================================
    # HISTOGRAM
    # =====================================

    st.subheader(
        "Overall Percentage Distribution"
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

    st.markdown("---")

    # =====================================
    # GRADE DISTRIBUTION
    # =====================================

    col1, col2 = st.columns(2)

    with col1:

        st.subheader(
            "Grade Distribution"
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

    # =====================================
    # GRADE-WISE AVERAGE
    # =====================================

    with col2:

        st.subheader(
            "Grade-wise Average Percentage"
        )

        grade_avg = (

            master_df

            .groupby(

                "Grade"

            )["Overall_Percentage"]

            .mean()

            .reset_index()

        )

        fig = px.bar(

            grade_avg,

            x="Grade",

            y="Overall_Percentage",

            color="Grade",

            text="Overall_Percentage",

            title="Grade-wise Average Percentage"

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

    # =====================================
    # SCATTER PLOT
    # =====================================

    st.subheader(
        "Overall Percentage vs Final Percentile"
    )

    fig = px.scatter(

        master_df,

        x="Overall_Percentage",

        y="Final_Percentile",

        color="Grade",

        hover_data=[

            "Name",

            "Rank"

        ],

        title="Overall Percentage vs Final Percentile"

    )

    st.plotly_chart(

        fig,

        use_container_width=True

    )

    st.markdown("---")

    # =====================================
    # BOX PLOT
    # =====================================

    st.subheader(
        "Box Plot for Outlier Detection"
    )

    fig = px.box(

        master_df,

        y="Overall_Percentage",

        points="all",

        title="Overall Percentage Box Plot"

    )

    st.plotly_chart(

        fig,

        use_container_width=True

    )

    st.markdown("---")

    # =====================================
    # SUMMARY STATISTICS
    # =====================================

    st.subheader(
        "Summary Statistics"
    )

    summary_df = pd.DataFrame(

        {

            "Metric": [

                "Mean",

                "Median",

                "Standard Deviation",

                "Minimum",

                "Maximum"

            ],

            "Value": [

                round(

                    master_df["Overall_Percentage"]

                    .mean(),

                    2

                ),

                round(

                    master_df["Overall_Percentage"]

                    .median(),

                    2

                ),

                round(

                    master_df["Overall_Percentage"]

                    .std(),

                    2

                ),

                round(

                    master_df["Overall_Percentage"]

                    .min(),

                    2

                ),

                round(

                    master_df["Overall_Percentage"]

                    .max(),

                    2

                )

            ]

        }

    )

    st.dataframe(

        summary_df,

        use_container_width=True

    )