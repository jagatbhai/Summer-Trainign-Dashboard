# dashboard_modules/reports_tab.py

import os
import streamlit as st

REPORT_FOLDER = "Reports"


def show_reports_tab():

    st.title(
        "📑 Report Explorer"
    )

    st.markdown("---")

    report_files = [

        "Master_Report.xlsx",

        "Summary_Report.xlsx",

        "score_summary.xlsx",

        "final_rankings.xlsx",

        "Top_10_Report.xlsx",

        "Grade_Distribution_Report.xlsx",

        "Attendance_Report.xlsx",

        "Low_Performer_Report.xlsx",

        "Module_Analysis_Report.xlsx",

        "module_summary.xlsx",

        "batch_summary.pdf"

    ]

    for report_file in report_files:

        file_path = os.path.join(

            REPORT_FOLDER,

            report_file

        )

        col1, col2 = st.columns(

            [4,1]

        )

        with col1:

            st.write(

                "📄",

                report_file

            )

        with col2:

            if os.path.exists(

                file_path

            ):

                with open(

                    file_path,

                    "rb"

                ) as file:

                    st.download_button(

                        label="Download",

                        data=file,

                        file_name=report_file,

                        key=report_file

                    )

            else:

                st.error(

                    "Not Found"

                )

    st.markdown("---")

    # ====================================
    # Gradecards
    # ====================================

    st.subheader(

        "🎓 Grade Cards"

    )

    gradecard_folder = "GradeCards"

    if os.path.exists(

        gradecard_folder

    ):

        pdf_files = [

            file

            for file in os.listdir(

                gradecard_folder

            )

            if file.endswith(

                ".pdf"

            )

        ]

        selected_pdf = st.selectbox(

            "Select Student Grade Card",

            pdf_files

        )

        pdf_path = os.path.join(

            gradecard_folder,

            selected_pdf

        )

        with open(

            pdf_path,

            "rb"

        ) as file:

            st.download_button(

                label="Download Grade Card",

                data=file,

                file_name=selected_pdf,

                key="gradecard"

            )

    else:

        st.warning(

            "GradeCard folder not found."

        )
