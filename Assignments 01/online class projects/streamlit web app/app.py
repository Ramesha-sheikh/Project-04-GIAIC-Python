import streamlit as st  # 🚀 Ignore type checking for Streamlit
import pandas as pd  # 📊 Ignore type checking for Pandas
import os  # 📁 Import OS module for file operations
from io import BytesIO  # 🔄 Ignore type checking for BytesIO

# 🌟 Set page configuration
st.set_page_config(page_title="Data Sweeper", layout="wide")
# 🏆 Display title
st.title("✨ Data Sweeper ✨")
st.write("🔄 Transform your file between CSV and Excel format with built-in data cleaning and visualization. 📂📊")

# 📤 File uploader to upload CSV or Excel files
upload_files = st.file_uploader("📂 Upload your files (CSV or Excel):", type=["csv", "xlsx"], accept_multiple_files=True)

if upload_files:
    for file in upload_files:
        file_ext = os.path.splitext(file.name)[-1].lower()  # 📝 Get file extension
        
        # 📑 Read file based on its extension
        if file_ext == ".csv":
            df = pd.read_csv(file)
        elif file_ext == ".xlsx":
            df = pd.read_excel(file)    
        else:
            st.error(f"❌ Unsupported file type: {file_ext}")
            continue
        
        # 📜 Display file name and size
        st.write(f"📄 File Name: {file.name}")
        file.seek(0, os.SEEK_END)  # 📏 Get file size
        file_size_kb = file.tell() / 1024
        file.seek(0)  # 🔄 Reset file pointer
        st.write(f"📏 File Size: {file_size_kb:.2f} KB")

        # 🔍 Show preview of the DataFrame
        st.write("📊 Preview of the DataFrame:")
        st.dataframe(df.head())
        
        # 🛠️ Data Cleaning Options
        st.subheader("🧹 Data Cleaning Options")
        if st.checkbox(f"🧼 Clean Data for {file.name}"):
            col1, col2 = st.columns(2)
            
            with col1:
                if st.button(f"🗑️ Remove Duplicates from {file.name}"):
                    df.drop_duplicates(inplace=True)
                    st.write("✅ Duplicates removed!")

            with col2:
                if st.button(f"🔄 Fill Missing Values for {file.name}"):
                    numeric_cols = df.select_dtypes(include=['number']).columns
                    df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())
                    st.write("✅ Missing values filled!")
                    
            # 🔀 Select columns to keep
            st.subheader("🎯 Select columns to convert")
            colums = st.multiselect(f"📌 Choose columns for {file.name}", df.columns, default=df.columns)
            df = df[colums]  # ✅ Corrected variable name from 'columns' to 'colums'

        # 📈 Data Visualization
        st.subheader("📊 Data Visualization")
        if st.checkbox(f"📉 Show visualization for {file.name}"):
            st.bar_chart(df.select_dtypes(include=['number']).iloc[:, :2])
                    
        # 🔄 Conversion Options
        st.subheader("🔃 Conversion Options")
        conversion_type = st.radio("📥 Choose conversion type:", ("CSV", "Excel"))
        if st.button(f"🔄 Convert {file.name}"):
            buffer = BytesIO()  # ✅ Corrected initialization of BytesIO()
            
            if conversion_type == "CSV":
                df.to_csv(buffer, index=False)
                file_name = file.name.replace(file_ext, ".csv")  # ✅ Corrected filename replacement
                mime_type = "text/csv"
            elif conversion_type == "Excel":
                df.to_excel(buffer, index=False)
                file_name = file.name.replace(file_ext, ".xlsx")  # ✅ Corrected 'file.ext' to 'file_ext'
                mime_type = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            
            buffer.seek(0)  # ✅ Ensure buffer is reset before downloading

            st.download_button(
                label=f"📥 Download {file.name} as {conversion_type}",
                data=buffer,
                file_name=file_name,
                mime=mime_type
            )

# 🎉 Show success message when all processes are completed
st.success("✅ All file processes completed! 🎊")
