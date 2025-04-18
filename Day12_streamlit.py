import streamlit as st 

st.set_page_config(page_title="Tasks Manager")
st.title('Ứng dụng quản lý công việc:')

task = st.text_input('Nhập tên công việc', placeholder = 'Vui lòng nhập tên công việc...')

priority = st.slider("Chọn mức độ ưu tiên:", step = 1, min_value = 0, max_value = 5)

status = st.selectbox(
    "Chọn trạng thái:",
    ("Chưa làm", "Đang làm", "Hoàn thành"),
    index = None,
    placeholder = "Vui lòng chọn trạng thái...",
)

if "tasks" not in st.session_state:
    st.session_state.tasks = []

if st.button("Thêm công việc"):
    st.session_state.tasks.append((task, priority, status))


st.header("Danh sách công việc:")

for idx, (task, priority, status) in enumerate(st.session_state.tasks, start=1):
    col1, col2 = st.columns(2)
    with col1:
        st.write(f"{idx}. {task} - Ưu tiên: {priority} - Trạng thái: {status}")
    with col2:
        if st.button("❌", key = f"del_{idx}"):
            del st.session_state.tasks[idx-1]
            st.rerun()

if st.button("Xóa danh sách"):
    st.session_state.tasks = []
    st.rerun()