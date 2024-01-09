# Library imports
import streamlit as st
import tiledbvcf
import pandas as pd

# Page Headers
st.header("Lineberger Comprehensive Cancer Center")
st.subheader("UNC-Chapel Hill")
st.subheader("VCF Dataset Explorer")
st.markdown(''' <p><b>Developed by:</b> Vibhor Gupta <br/> <b>Supervised by:</b> Saianand Balu''',
            unsafe_allow_html=True)
st.divider()

# Explore Tiledbvcf dataset
uri = {paht_to_tiledbvcf_dataset}


def tiledbvcfds(path_to_dataset):
    ds = tiledbvcf.Dataset(path_to_dataset, "r")
    dfs = [ds.read()]
    while not ds.read_completed():  # If dataset is large, then to read the full dataset
        dfs.append(ds.continue_read())
    df = pd.concat(dfs)
    return df


df = tiledbvcfds(uri)

# Reading and displaying the metadata file
st.markdown('''<h3>Metadata File</h3>''', unsafe_allow_html=True)
metadata = pd.read_csv({path_to_csv_file})
st.write("Few records from the file")
st.dataframe(metadata.head())

# Sidebar Code
with st.sidebar:
    st.subheader("Filters", divider='grey')
    metadata_query = st.selectbox("Select the Tumour Region", key="metadata_query", index=None,
                                  options=metadata["region"].unique())
    query1 = st.text_input("Enter query to be searched in vcf dataset", value=None)
    field1 = st.selectbox("Field to be searched", key="field1", index=None, options=df.columns)
    query2 = None
    check = False
    if query1 is None and field1 is None:
        pass
    else:
        check = st.toggle("Use the resulting sample set to look for another query")
        if check == True:
            query2 = st.text_input("Enter another query to be searched", value=None)
            field2 = st.selectbox("Field to be searched", key="field2", index=None, options=df.columns)

# Displaying report from filtered metadata based on region
st.markdown('''<h5>Report:</h5>''', unsafe_allow_html=True)
st.markdown(f'''- The metadata file has {metadata.shape[0]} records''', unsafe_allow_html=True)
if metadata_query == None:
    unique_samples = None
else:
    unique_samples = metadata[metadata["region"] == metadata_query]["sample"].unique()
    st.markdown(
        f'''- The file has {unique_samples.shape[0]} unique samples corresponding to {metadata_query} region ''')

if unique_samples is None:
    temp_df = df
else:
    temp_df = df[df["sample_name"].isin(unique_samples)]

try:
    temp1 = temp_df[temp_df[field1].str.contains(query1)]
    rows1 = temp1.shape[0]
    samples1 = temp1["sample_name"].unique().shape[0]
    st.markdown(f'''- The dataset has {rows1} rows for query 1 corresponding to {samples1} unique samples''',
                unsafe_allow_html=True)
except:
    st.error("Enter both query and field to be searched to proceed further")

if check == True:
    try:
        temp2 = temp_df[temp_df[field2].str.contains(query2)]
        rows2 = temp2.shape[0]
        samples2 = temp2["sample_name"].unique().shape[0]
        samples3 = pd.merge(pd.DataFrame(temp1["sample_name"].unique()), pd.DataFrame(temp2["sample_name"].unique()), on=0).shape[
            0]
        st.markdown(f'''- The dataset has {rows2} rows for query 2 corresponding to {samples2} unique samples''',
                    unsafe_allow_html=True)
        st.markdown(f'''- Both the datasets have {samples2} unique samples in common''',
                    unsafe_allow_html=True)

    except:
        st.error("Enter both query and field to be searched to proceed further")
