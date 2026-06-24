# dashboard_modules/module_analysis_tab.py

import streamlit as st
import plotly.express as px
import pandas as pd


def show_module_analysis_tab(master_df):

    st.title(
        "📚 Module Analysis"
    )

    st.markdown("---")

    # ====================================
    # Find module percentage columns
    # ====================================

    module_cols = [

        col

        for col in master_df.columns

        if col.startswith("Module")

        and col.endswith("_Pct")

    ]

    # ====================================
    # Average Performance
    # ====================================

    module_avg = pd.DataFrame(

        {

            "Module": [

                col.replace(

                    "_Pct",

                    ""

                )

                for col in module_cols

            ],

            "Average Percentage": [

                master_df[col]

                .mean()

                for col in module_cols

            ]

        }

    )

    st.subheader(
        "Average Module Performance"
    )

    fig = px.bar(

        module_avg,

        x="Average Percentage",

        y="Module",

        orientation="h",

        text="Average Percentage",

        color="Average Percentage"

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

    # ====================================
    # Highest Scores
    # ====================================

    highest_df = pd.DataFrame(

        {

            "Module": [

                col.replace(

                    "_Pct",

                    ""

                )

                for col in module_cols

            ],

            "Highest Score": [

                master_df[col]

                .max()

                for col in module_cols

            ]

        }

    )

    st.subheader(
        "Highest Score in Each Module"
    )

    fig = px.bar(

        highest_df,

        x="Highest Score",

        y="Module",

        orientation="h",

        color="Highest Score",

        text="Highest Score"

    )

    st.plotly_chart(

        fig,

        use_container_width=True

    )

    st.markdown("---")

    # ====================================
    # Lowest Scores
    # ====================================

    lowest_df = pd.DataFrame(

        {

            "Module": [

                col.replace(

                    "_Pct",

                    ""

                )

                for col in module_cols

            ],

            "Lowest Score": [

                master_df[col]

                .min()

                for col in module_cols

            ]

        }

    )

    st.subheader(
        "Lowest Score in Each Module"
    )

    fig = px.bar(

        lowest_df,

        x="Lowest Score",

        y="Module",

        orientation="h",

        color="Lowest Score",

        text="Lowest Score"

    )

    st.plotly_chart(

        fig,

        use_container_width=True

    )

    st.markdown("---")

    # ====================================
    # Summary Table
    # ====================================

    summary_df = pd.DataFrame(

        {

            "Module": [

                col.replace(

                    "_Pct",

                    ""

                )

                for col in module_cols

            ],

            "Average": [

                round(

                    master_df[col]

                    .mean(),

                    2

                )

                for col in module_cols

            ],

            "Maximum": [

                round(

                    master_df[col]

                    .max(),

                    2

                )

                for col in module_cols

            ],

            "Minimum": [

                round(

                    master_df[col]

                    .min(),

                    2

                )

                for col in module_cols

            ]

        }

    )

    st.subheader(
        "Module Summary"
    )

    st.dataframe(

        summary_df,

        use_container_width=True

    )