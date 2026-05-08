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
    margin-bottom: 16px;
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
    lot_area = st.number_input("Lot Area", 1000, 50000, 8000)
    overall_cond = st.slider("Overall Condition", 1, 10, 5)
    tot_rms_abv_grd = st.slider("Total Rooms Above Ground", 2, 15, 6)

    neighborhood = st.selectbox(
        "Neighborhood",
        [
            "CollgCr", "Veenker", "Crawfor", "NoRidge", "Mitchel",
            "Somerst", "NWAmes", "OldTown", "BrkSide", "Sawyer",
            "NridgHt", "NAmes", "SawyerW", "IDOTRR", "MeadowV",
            "Edwards", "Timber", "Gilbert", "StoneBr", "ClearCr",
            "NPkVill", "Blmngtn", "BrDale", "SWISU", "Blueste"
        ]
    )

    house_style = st.selectbox(
        "House Style",
        [
            "1Story", "2Story", "1.5Fin", "SLvl", "SFoyer",
            "1.5Unf", "2.5Unf", "2.5Fin"
        ]
    )

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
input_data["LotArea"] = lot_area
input_data["OverallCond"] = overall_cond
input_data["TotRmsAbvGrd"] = tot_rms_abv_grd

neighborhood_col = "Neighborhood_" + neighborhood
if neighborhood_col in input_data.columns:
    input_data[neighborhood_col] = 1

house_style_col = "HouseStyle_" + house_style
if house_style_col in input_data.columns:
    input_data[house_style_col] = 1

col1, col2 = st.columns([1.1, 0.9], gap="large")

with col1:
    st.markdown('<div class="section-heading">📌 Selected House Features</div>', unsafe_allow_html=True)
    st.write("")

    features_html = f"""
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
<div class="feature-line">🌳 <b>Lot Area:</b> {lot_area} sq ft</div>
<div class="feature-line">⭐ <b>Overall Condition:</b> {overall_cond} / 10</div>
<div class="feature-line">🚪 <b>Total Rooms:</b> {tot_rms_abv_grd}</div>
<div class="feature-line">📍 <b>Neighborhood:</b> {neighborhood}</div>
<div class="feature-line">🏘️ <b>House Style:</b> {house_style}</div>
</div>
"""
    st.markdown(features_html, unsafe_allow_html=True)

with col2:
    st.markdown('<div class="section-heading">💰 Prediction Result</div>', unsafe_allow_html=True)
    st.write("")

    if st.button("🔮 Predict House Price", use_container_width=True):
        prediction_usd = model.predict(input_data)[0]
        usd_to_inr = 85
        prediction_inr = prediction_usd * usd_to_inr

        price_html = f"""
<div class="price-card">
<h2>Estimated Price</h2>
<div class="price">₹ {prediction_inr:,.0f}</div>
<p style="font-size:18px; margin-top:10px;">Approx. USD Price: ${prediction_usd:,.2f}</p>
<p style="margin-top:15px;">Based on the selected house features</p>
<p style="font-size:13px; color:#374151; margin-top:18px; line-height:1.6;">
Note: This model was trained on the Ames Housing dataset. INR value is converted from USD using an approximate exchange rate.
</p>
</div>
"""
        st.markdown(price_html, unsafe_allow_html=True)

        st.write("")
        st.markdown('<div class="section-heading">📈 Prediction Impact Analysis</div>', unsafe_allow_html=True)
        st.write("")

        impact_points = []

        if overall_qual >= 8:
            impact_points.append("⭐ High overall quality significantly increased the estimated house price.")
        elif overall_qual <= 4:
            impact_points.append("⭐ Lower overall quality reduced the estimated house price.")

        if gr_liv_area >= 2500:
            impact_points.append("📐 Large living area positively impacted the prediction.")
        elif gr_liv_area <= 1200:
            impact_points.append("📐 Smaller living area reduced the predicted value.")

        if garage_cars >= 3:
            impact_points.append("🚗 Large garage capacity contributed to a higher valuation.")
        elif garage_cars == 0:
            impact_points.append("🚗 Absence of garage space negatively affected the prediction.")

        if year_built >= 2015:
            impact_points.append("📅 Recently built property increased the house value.")
        elif year_built <= 1980:
            impact_points.append("📅 Older construction slightly reduced the estimated value.")

        premium_neighborhoods = ["NridgHt", "StoneBr", "NoRidge"]
        if neighborhood in premium_neighborhoods:
            impact_points.append("📍 Premium neighborhood selection boosted the prediction.")

        if tot_rms_abv_grd >= 10:
            impact_points.append("🚪 Higher number of rooms increased estimated price.")

        if total_bsmt_sf >= 1500:
            impact_points.append("🏠 Large basement area positively influenced prediction.")

        if not impact_points:
            impact_points.append("ℹ️ The selected features represent a moderate house profile with balanced price impact.")

        analysis_html = """
<div class="card">
"""
        for point in impact_points:
            analysis_html += f'<div class="feature-line">• {point}</div>'

        analysis_html += """
</div>
"""
        st.markdown(analysis_html, unsafe_allow_html=True)

    else:
        st.info("Click the button to generate prediction.")

st.write("---")

st.markdown('<div class="section-heading">📊 Model Comparison</div>', unsafe_allow_html=True)
st.write("")

comparison_df = pd.read_csv("model/model_comparison.csv")

comparison_df["MAE"] = comparison_df["MAE"].round(2)
comparison_df["RMSE"] = comparison_df["RMSE"].round(2)
comparison_df["R2 Score"] = comparison_df["R2 Score"].round(4)

cards = st.columns(4)

for i, row in comparison_df.iterrows():
    with cards[i]:
        model_card = f"""
<div style="background: linear-gradient(135deg, #dbeafe, #eff6ff); padding:22px; border-radius:18px; color:#0f172a; box-shadow:0px 8px 25px rgba(0,0,0,0.25); min-height:230px; border-top:6px solid #38bdf8;">
<h3 style="text-align:center; color:#0369a1;">{row['Model']}</h3>
<hr>
<p><b>MAE:</b><br>{row['MAE']:,.2f}</p>
<p><b>RMSE:</b><br>{row['RMSE']:,.2f}</p>
<p><b>R² Score:</b><br>{row['R2 Score']:.4f}</p>
</div>
"""
        st.markdown(model_card, unsafe_allow_html=True)

st.markdown("""
<p style="color:#cbd5e1; font-size:15px; margin-top:25px;">
Lower MAE and RMSE indicate better performance, while higher R² score indicates better model fit.
</p>
""", unsafe_allow_html=True)

st.write("---")

st.markdown('<div class="section-heading">📈 Feature Importance</div>', unsafe_allow_html=True)
st.write("")

st.image(
    "model/feature_importance.png",
    caption="Top 15 features affecting house price prediction",
    use_container_width=True
)

st.markdown("""
<p style="color:#cbd5e1; font-size:15px; margin-top:15px;">
Feature importance helps explain which input variables contributed most to the model's predictions.
</p>
""", unsafe_allow_html=True)