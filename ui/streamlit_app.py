import streamlit as st, subprocess, json, os
st.title('Data Quality Agent — UI')
uploaded = st.file_uploader('Upload CSV', type=['csv'])
if uploaded:
    path = os.path.join('data','input', uploaded.name)
    with open(path,'wb') as f: f.write(uploaded.getbuffer())
    st.success('Saved to ' + path)
if st.button('Run pipeline'):
    proc = subprocess.Popen(['python','app.py'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    for line in proc.stdout:
        st.text(line.strip())
    proc.wait()
    st.success('Pipeline finished')
    report_path = os.path.join('data','output','report.json')
    if os.path.exists(report_path):
        st.json(json.load(open(report_path)))
