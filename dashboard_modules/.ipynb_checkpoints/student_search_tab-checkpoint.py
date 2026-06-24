# dashboard_modules/student_search_tab.py

import streamlit as st
import plotly.express as px


def show_student_search_tab(master_df):

    st.title(
        "🔍 Student Search"
    )

    st.markdown("---")

    # ======================================
    # Search Box
    # ======================================

    student_name = st.text_input(

        "Enter Student Name"

    )

    if student_name:

        result = master_df[

            master_df["Name"]

            .str.contains(

                student_name,

                case=False,

                na=False

            )

        ]

        if len(result) == 0:

            st.error(

                "No student found."

            )

        else:

            st.success(

                f"{len(result)} student(s) found."

            )

            st.dataframe(

                result,

                use_container_width=True

            )

            # ======================================
            # Detailed Student View
            # ======================================

            student = result.iloc[0]

            st.markdown("---")

            st.subheader(
                "Student Details"
            )

            col1, col2, col3, col4 = st.columns(4)

            with col1:

                st.metric(

                    "Rank",

                    int(

                        student["Rank"]

                    )

                )

            with col2:

                st.metric(

                    "Grade",

                    student["Grade"]

                )

            with col3:

                st.metric(

                    "Percentage",

                    round(

                        student["Overall_Percentage"],

                        2

                    )

                )

            with col4:

                st.metric(

                    "Percentile",

                    round(

                        student["Final_Percentile"],

                        2

                    )

                )

            st.markdown("---")

            # ======================================
            # Module Performance
            # ======================================

            module_cols = [

                col

                for col in master_df.columns

                if col.startswith("Module")

                and col.endswith("_Pct")

            ]

            module_names = [

                col.replace(

                    "_Pct",

                    ""

                )

                for col in module_cols

            ]

            module_scores = [

                student[col]

                for col in module_cols

            ]

            module_df = {

                "Module": module_names,

                "Score": module_scores

            }

            st.subheader(

                "Module-wise Performance"

            )

            fig = px.bar(

                module_df,

                x="Score",

                y="Module",

                orientation="h",

                text="Score",

                color="Score"

            )

            fig.update_traces(

                texttemplate="%{text:.1f}",

                textposition="outside"

            )

            st.plotly_chart(

                fig,

                use_container_width=True

            )

            st.markdown("---")

            # ======================================
            # Day-wise Scores
            # ======================================

            day_cols = [

                col

                for col in master_df.columns

                if col.startswith("Day")

                and col.endswith("_Pct")

            ]

            if len(day_cols) > 0:

                day_df = {

                    "Day": day_cols,

                    "Score": [

                        student[col]

                        for col in day_cols

                    ]

                }

                st.subheader(

                    "Day-wise Performance"

                )

                fig = px.line(

                    day_df,

                    x="Day",

                    y="Score",

                    markers=True

                )

                st.plotly_chart(

                    fig,

                    use_container_width=True

                )