import streamlit as st
import pandas as pd

def main():
    st.title("Excel File Uploader and Downloader")

    # File uploader widget
    uploaded_file = st.file_uploader("Choose an Excel file", type=["xlsx", "xls"])

    if uploaded_file is not None:
        st.subheader("Uploaded Excel Data")

        # Read the Excel file
        df = pd.read_excel(uploaded_file)

        # Display the DataFrame
        st.write(df)

        st.download_button(
            "Press to Download",
            df.to_csv(index=False).encode('utf-8'),
            "file.csv",
            "text/csv",
            key='download-csv'
            )


if __name__ == "__main__":
    main()

