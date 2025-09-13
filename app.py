import streamlit as st
import joblib
import os

# Check if model file exists
MODEL_PATH = "e_tongue_model.pkl"

if not os.path.exists(MODEL_PATH):
    st.error("❌ Model file not found! Please upload e_tongue_model.pkl to the repo.")
else:
    # Load the model
    model = joblib.load(MODEL_PATH)
    st.success("✅ Model loaded successfully!")

    # Example UI
    st.title("AI E-Tongue Quality Assessment")

    ph = st.number_input("Enter pH value", min_value=0.0, max_value=14.0, step=0.1)
    turbidity = st.number_input("Enter Turbidity (NTU)", min_value=0.0, step=0.1)
    conductivity = st.number_input("Enter Conductivity (µS/cm)", min_value=0.0, step=0.1)

    if st.button("Predict Quality"):
        features = [[ph, turbidity, conductivity]]
        prediction = model.predict(features)
        st.write("🔮 Prediction:", prediction)
