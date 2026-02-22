import streamlit as st
import requests

API_BASE = "http://api:8000"


st.set_page_config(page_title="Admin Dashboard", page_icon="🧑‍💼")

st.title("Support Admin Dashboard")

status_filter = st.selectbox(
    "Filter tickets by status",
    ["", "NEW", "IN_PROCESS", "RESOLVED"]
)

params = {"status": status_filter} if status_filter else {}
response = requests.get(f"{API_BASE}/admin/tickets", params=params)

if response.status_code == 200:
    tickets = response.json()

    if not tickets:
        st.info("No tickets found.")
    else:
        for t in tickets:
            st.subheader(t["ticket_id"])
            st.write("Category:", t["category"])
            st.write("Priority:", t["priority"])
            st.write("Status:", t["status"])
            st.write("Channel:", t["channel"])
            st.write("Summary:", t["summary"])
            st.write("Created At:", t["created_at"])

            new_status = st.selectbox(
                "Update status",
                ["NEW", "IN_PROCESS", "RESOLVED"],
                index=["NEW", "IN_PROCESS", "RESOLVED"].index(t["status"]),
                key=t["ticket_id"]
            )

            if st.button("Update", key=f"btn_{t['ticket_id']}"):
                update_resp = requests.patch(
                    f"{API_BASE}/admin/ticketupdate",
                    json={
                        "ticket_id": t["ticket_id"],
                        "status": new_status
                    }
                )

                if update_resp.status_code == 200:
                    st.success("Status updated")
                else:
                    st.error("Update failed")

            st.divider()
else:
    st.error("Failed to fetch tickets")
