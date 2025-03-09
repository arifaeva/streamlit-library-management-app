import streamlit as st
from libs import Library, Member

st.title("Library Management System")

if "library" not in st.session_state:
    st.session_state.library = Library("My Library")
# 2 baris kode di atas menunjukkan state selama session berjalan
# state di dalam streamlit hanya boleh ada 1
# kita bisa mengakses state dengan menggunakan keyword-nya

# Kode menyatakan bahwa jika "library" tidak ada di dalam session_state, maka dia akan
# create one. Tapi kalau sudah ada maka secara otomatis dia akan me-return yang ada di 
# dalam state.

# Jika tidak menggunakan 2 baris kode di atas, maka data akan terus di-refresh

page = st.sidebar.selectbox("Menu", ["Add Member", "Manage Membership", "View Members"])

if page == "Add Member":
    st.write("### Add Member")
    name = st.text_input("Name")
    button = st.button("Add Member")

    if button:
        new_member = Member(name)
        st.session_state.library.register_member(new_member)
        st.rerun()

elif page == "Manage Membership":
    st.write("### Manage Membership Cek Edit Push")

    for index, member in enumerate(st.session_state.library.members):
        status = "Active" if member.is_active else "Inactive"
        st.write(f"{member.name} - {status}")
        deactivate_btn = st.button("Deactivate", key=f"deactivate_{index}")

        if deactivate_btn:
            member.deactivate()
            st.rerun()

elif page == "View Members":
    if not st.session_state.library.members:
        st.write("No current active members")
    else: 
        active_members = st.session_state.library.get_active_members()
        for member in active_members:
            st.write(member.name)


print(st.session_state.library.members)