import streamlit as st

st.set_page_config(page_title="Vijay War", page_icon="⚔️")

st.title("🇮🇳 विजय वार – देसी हिंदी AI सहायक 🤖")
st.markdown("**ChatGPT जैसा लेकिन फुल देसी और हिंदी में!**")
st.markdown("✉️ Contact: Vv301999@gmail.com | GitHub: [@vijayVishwakarma383](https://github.com/vijayVishwakarma383)")

prompt = st.text_input("👇 अपना सवाल लिखिए (रील, मोटिवेशन, प्यार, हैकिंग, शायरी):")

if prompt:
    if "रील" in prompt:
        st.success("🎬 Script ➤ 'जब खामोशियाँ बोलने लगे, समझ लो कुछ बड़ा होने वाला है...'")
    elif "मोटिवेशन" in prompt:
        st.success("🔥 'कोशिश करने वालों की कभी हार नहीं होती!' – चलो उठो, आगे बढ़ो!")
    elif "प्यार" in prompt:
        st.success("❤️ 'सच्चा प्यार वही है जो हर आँसू में साथ निभाए, ना कि सिर्फ मुस्कुराहट में।'")
    elif "हैकिंग" in prompt:
        st.success("💻 Ethical hacking सीखने के लिए visit करें: [CyberSecureVijayIndia.in](https://example.com) (जल्द लॉन्च होगा)")
    elif "शायरी" in prompt:
        st.success("📝 'ज़िन्दगी एक किताब है,\nहर दिन एक नया पन्ना...\nजो समझ गया वही विजेता बना!'")
    else:
        st.info("🤖 माफ कीजिए! अभी मैं केवल रील, मोटिवेशन, प्यार, शायरी, हैकिंग पर जवाब दे सकता हूँ।")

st.markdown("---")
st.markdown("💬 बनवाया गया @Vijay_Vishwakarma_07 द्वारा")

