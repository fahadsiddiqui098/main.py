import streamlit as st

# --- Page Configuration ---
st.set_page_config(page_title="Property Manager", layout="centered")

# --- Sidebar: Theme Toggle ---
st.sidebar.title("🎛️ Settings")
theme_mode = st.sidebar.radio("🌓 Theme", ["Light", "Dark"], horizontal=True)

# --- Custom Theme Styles ---
if theme_mode == "Dark":
    st.markdown("""
        <style>
        .main {
            background-color: #1e1e1e;
            color: #ffffff;
        }
        div[data-testid="stSidebar"] {
            background-color: #2c2c2c;
        }
        </style>
    """, unsafe_allow_html=True)
else:
    st.markdown("""
        <style>
        .main {
            background-color: #ffffff;
            color: #000000;
        }
        div[data-testid="stSidebar"] {
            background-color: #f0f2f6;
        }
        </style>
    """, unsafe_allow_html=True)

# --- App Title ---
st.title("🏡 Property Listing Manager")
st.markdown("Add and manage your real estate listings easily.")

# --- Initialize session state for properties ---
if "properties" not in st.session_state:
    st.session_state.properties = []

# --- Form to Add Property ---
with st.form("add_property_form"):
    st.subheader("➕ Add a New Property")
    
    name = st.text_input("📍 Property Location", placeholder="e.g., DHA Lahore")
    property_type = st.selectbox("🏷️ Type", ["House", "Plot", "Apartment"])

    col1, col2 = st.columns(2)
    with col1:
        size = st.text_input("📐 Size", placeholder="e.g., 10 Marla")
    with col2:
        price = st.text_input("💰 Price (PKR)", placeholder="e.g., 35000000")

    submitted = st.form_submit_button("✅ Add Property")

# --- Handle Submit ---
if submitted:
    if name and size and price:
        st.session_state.properties.append({
            "name": name,
            "type": property_type,
            "size": size,
            "price": price
        })
        print(f"Property added: {name} - {property_type} - {size} - PKR {price}")
        st.success(f"✅ Property '{name}' added successfully!")
    else:
        st.warning("⚠️ Please fill in all the fields.")

# --- Divider ---
st.markdown("---")

# --- Display Property List ---
if st.session_state.properties:
    st.subheader("📋 Property Listings")
    for i, prop in enumerate(reversed(st.session_state.properties), start=1):
        with st.expander(f"{i}. {prop['name']} ({prop['type']})", expanded=False):
            st.markdown(f"📍 **Location:** {prop['name']}")
            st.markdown(f"🏷️ **Type:** {prop['type']}")
            st.markdown(f"📐 **Size:** {prop['size']}")
            st.markdown(f"💰 **Price:** ₨ {prop['price']}")
else:
    st.info("No properties added yet. Use the form above to add some.")


