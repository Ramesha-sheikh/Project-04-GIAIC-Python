# Project: Streamlit Web App - Country Information Cards
# Yeh Streamlit web app kisi bhi country ki basic information show karega.

# Required Libraries:
# Is project ke liye `streamlit` aur `requests` install karni hogi.
# Install karne ke liye terminal me yeh command chalayein:
# pip install streamlit requests

import streamlit as st
import requests

def get_country_info(country):
    """Diye gaye country ka information fetch karne ke liye API request bhejta hai."""
    url = f"https://restcountries.com/v3.1/name/{country}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()[0]  # Pehla result lete hain
        info = {
            "Country": data.get("name", {}).get("common", "N/A"),
            "Capital": data.get("capital", ["N/A"])[0],
            "Region": data.get("region", "N/A"),
            "Population": data.get("population", "N/A"),
            "Currency": list(data.get("currencies", {}).keys())[0] if "currencies" in data else "N/A",
            "Flag": data.get("flags", {}).get("png", "")
        }
        return info
    else:
        return None

def main():
    st.title("🌍 Country Information Cards")
    st.write("Kisi bhi country ka naam likhiye aur uski maloomat dekhiye!")
    
    country = st.text_input("Enter Country Name:")
    
    if st.button("Search"):
        if country:
            info = get_country_info(country)
            if info:
                st.subheader(f"Information about {info['Country']}")
                st.write(f"**Capital:** {info['Capital']}")
                st.write(f"**Region:** {info['Region']}")
                st.write(f"**Population:** {info['Population']}")
                st.write(f"**Currency:** {info['Currency']}")
                if info["Flag"]:
                    st.image(info["Flag"], caption=f"Flag of {info['Country']}")
            else:
                st.error("Koi maloomat nahi mili, dobara check karein!")
        else:
            st.warning("Please enter a country name.")

if __name__ == "__main__":
    main()
