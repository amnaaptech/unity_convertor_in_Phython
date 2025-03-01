import streamlit as st
st.markdown(
 """
  <style>
body{
    background-color: #1e1e2f;
    color: white;
}
.stApp{
    background:linear-gradient(to top, #ebbba7 0%, #cfc7f8 100%);
    padding: 30px;
    border-radius: 15px;
    box-shadow: 0px 10px 30px rgba(0 ,0 ,0, 0.3) ;
}
h1 {
    text-aling:center;
    font-size: 36px;
    color: white;
}
.stButton>button{
    background:linear-gradient(45deg, #9796f0,#fbc7d4);
    color: white;
    font-size: 18px;
    paddingL: 10px 20px;
    border-radius: 10px;
    transitoin:0.3s;
    box-shadow: 0px 5px 15px (#E7E9BB);
}
.stButton>button:hover{
    background: #FBC7D4;
    border-color: black;
    transform: scale(1.05);
    color: black;
}
.result-box{
    font-size:20px;
    font-weight:bold;
    text-align:center;
    background: rgba(255,255,255,0.1);
    padding: 20px;
    border-radius: 10px;
    margin-top:10px;
    box-shadow: 0px 5px 15px rgba(0 ,201 ,225, 0.3) ;
}
.footer{
    text-align:center;
    margin-top:50px;
    font-size: 14px;
    color: black;
}
  </style>
 """,
 unsafe_allow_html=True
)

#titel and description
st.markdown("<h1>Unit Convertor</h1>", unsafe_allow_html=True)
st.write("Esily Conver Between different units of lenght, weight and temprature.")

#sidebar menu
conversion_type = st.sidebar.selectbox("Choose Conversion Type",["Lenght","Weight","Temprature"])
values = st.number_input("Enter the value to convert",value=0.0, min_value=0.0,step=0.1)
col1,col2 = st.columns(2)

#for define types
if conversion_type == "Lenght":
    with col1:
        from_unit = st.selectbox("From",["Meters","Kilograms","Centimeters","Millimeters","Feet","Inches","Yards","Miles"])
    with col2:
        to_unit = st.selectbox("To",["Meters","Kilograms","Centimeters","Millimeters","Feet","Inches","Yards","Miles"])
elif conversion_type == "Weight":
    with col1:
        from_unit = st.selectbox("From",["Kilograms","Grams","Milligrams","Pounds","Ounces"])
    with col2:
        to_unit = st.selectbox("To",["Kilograms","Grams","Milligrams","Pounds","Ounces"])
elif conversion_type == "Temprature":
    with col1:
        from_unit = st.selectbox("From",["Celsius","Fahrenheit","Kelvin"])
    with col2:
        to_unit = st.selectbox("To",["Celsius","Fahrenheit","Kelvin"])

#converted funtctions lenght
def lenght_convert(from_unit,to_unit,values):
    lenght_units = {
        "Meters":1,
        "Kilograms":0.001,
        "Centimeters":100,
        "Millimeters":1000,
        "Feet":3.28,
        "Inches":39.37,
        "Yards":1.09636,
        "Miles":0.000621371,
    }
    return (values / lenght_units[from_unit]) * lenght_units[to_unit]

#converted funtctions Weight
def weight_convert(from_unit,to_unit,values):
    weight_units = {
        "Kilograms":1,
        "Grams":1000,
        "Milligrams":1000000,
        "Pounds":2.20462,
        "Ounces":35.274,
    }
    return (values / weight_units[from_unit]) * weight_units[to_unit]

#converted funtctions Temprature
def temprature_convert(from_unit,to_unit,values):
    if from_unit == "Celsius":
        return (values * 9/5) + 32 if to_unit == "Fahrenheit" else values + 273.15 if to_unit == "Kelvin" else values
    elif from_unit == "Fahrenheit":
        return (values - 32) * 5/9 if to_unit == "Celsius" else (values - 32) * 5/9 + 273.15 if to_unit == "Kelvin" else values
    elif from_unit == "Kelvin":
        return values - 273.15 if to_unit == "Celsius" else (values - 273.15) * 9/5 + 32 if to_unit == "Fahrenheit" else values
    else:
        return values

        #button for conversion
if st.button("🔄 Convert"):
    if conversion_type == "Lenght":
        result = lenght_convert(from_unit,to_unit,values)
    elif conversion_type == "Weight":
        result = weight_convert(from_unit,to_unit,values)
    elif conversion_type == "Temprature":
        result = temprature_convert(from_unit,to_unit,values)

    #display result
    st.markdown(f"<div class='result-box'>{values}{from_unit}={result:.4f} {to_unit}</div>",unsafe_allow_html=True)

    st.markdown(f"<div class='footer'>Created by Amna Adnan </div>",unsafe_allow_html=True)

