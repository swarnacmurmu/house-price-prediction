import streamlit as st
import pandas as pd
import joblib

model = joblib.load("model/house_price_model.pkl")
model_columns = joblib.load("model/model_columns.pkl")

st.set_page_config(
    page_title="House Price Predictor",
    page_icon="🏠",
    layout="wide"
)

st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #0f172a, #111827);
}

.main-title {
    text-align: center;
    font-size: 46px;
    font-weight: 800;
    color: #38bdf8;
    margin-bottom: 5px;
}

.sub-title {
    text-align: center;
    font-size: 18px;
    color: #cbd5e1;
    margin-bottom: 40px;
}

.card {
    background-color: #f8fafc;
    padding: 28px;
    border-radius: 18px;
    color: #111827;
    box-shadow: 0px 8px 25px rgba(0,0,0,0.25);
    border-left: 7px solid #38bdf8;
}

.price-card {
    background: linear-gradient(135deg, #dbeafe, #eff6ff);
    padding: 35px;
    border-radius: 18px;
    text-align: center;
    color: #0f172a;
    box-shadow: 0px 8px 25px rgba(0,0,0,0.25);
}

.price {
    font-size: 42px;
    font-weight: 800;
    color: #0369a1;
}

.feature-line {
    font-size: 18px;
    margin-bottom: 18px;
}

.section-heading {
    color: white;
    font-size: 30px;
    font-weight: 700;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-title">🏠 House Price Prediction App</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">Predict estimated house prices using Machine Learning</div>', unsafe_allow_html=True)

with st.sidebar:
    st.header("🏡 Enter House Details")

    overall_qual = st.slider("Overall Quality", 1, 10, 6)
    gr_liv_area = st.number_input("Above Ground Living Area", 300, 6000, 1800)
    garage_cars = st.slider("Garage Cars", 0, 5, 2)
    garage_area = st.number_input("Garage Area", 0, 1500, 500)
    total_bsmt_sf = st.number_input("Total Basement Area", 0, 3000, 900)
    first_flr_sf = st.number_input("First Floor Area", 300, 4000, 1200)
    full_bath = st.slider("Full Bathrooms", 0, 4, 2)
    year_built = st.number_input("Year Built", 1800, 2026, 2005)
    year_remod_add = st.number_input("Year Remodeled", 1800, 2026, 2010)

input_data = pd.DataFrame(0, index=[0], columns=model_columns)

input_data["OverallQual"] = overall_qual
input_data["GrLivArea"] = gr_liv_area
input_data["GarageCars"] = garage_cars
input_data["GarageArea"] = garage_area
input_data["TotalBsmtSF"] = total_bsmt_sf
input_data["1stFlrSF"] = first_flr_sf
input_data["FullBath"] = full_bath
input_data["YearBuilt"] = year_built
input_data["YearRemodAdd"] = year_remod_add

prediction_usd = model.predict(input_data)[0]

usd_to_inr = 85
prediction_inr = prediction_usd * usd_to_inr

col1, col2 = st.columns([1.1, 0.9], gap="large")

with col1:
    st.markdown('<div class="section-heading">📌 Selected House Features</div>', unsafe_allow_html=True)
    st.write("")

    st.markdown(f"""
    <div class="card">
        <div class="feature-line">🏡 <b>Overall Quality:</b> {overall_qual} / 10</div>
        <div class="feature-line">📐 <b>Living Area:</b> {gr_liv_area} sq ft</div>
        <div class="feature-line">🚗 <b>Garage Cars:</b> {garage_cars}</div>
        <div class="feature-line">🅿️ <b>Garage Area:</b> {garage_area} sq ft</div>
        <div class="feature-line">🏠 <b>Basement Area:</b> {total_bsmt_sf} sq ft</div>
        <div class="feature-line">🧱 <b>First Floor Area:</b> {first_flr_sf} sq ft</div>
        <div class="feature-line">🛁 <b>Bathrooms:</b> {full_bath}</div>
        <div class="feature-line">📅 <b>Year Built:</b> {year_built}</div>
        <div class="feature-line">🔨 <b>Year Remodeled:</b> {year_remod_add}</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown('<div class="section-heading">💰 Prediction Result</div>', unsafe_allow_html=True)
    st.write("")

    if st.button("🔮 Predict House Price", use_container_width=True):
        st.markdown(f"""
        <div class="price-card">
            <h2>Estimated Price</h2>
            <div class="price">₹ {prediction_inr:,.0f}</div>
            <p>Based on the selected house features</p>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.info("Click the button to generate prediction.")