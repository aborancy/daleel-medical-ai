import streamlit as st
import pytesseract
from PIL import Image
import io

st.set_page_config(page_title="دليل طبي - مساعد تشخيص ذكي", page_icon="🧠")

st.title("🧠 دليل طبي - مساعد تشخيص ذكي")
st.write("أدخل الأعراض أو ارفع صورة التحليل وسأقوم بتحليلها مبدئيًا 👨‍⚕️")

option = st.radio("اختار نوع الإدخال:", ["أعراض نصية", "رفع صورة تحليل"])

if option == "أعراض نصية":
    symptoms = st.text_area("اكتب الأعراض بالتفصيل:")
    if st.button("تحليل مبدئي"):
        st.write("تحليل مبدئي بناء على الأعراض:")
        if "حمى" in symptoms or "حرارة" in symptoms:
            st.warning("قد يكون هناك التهاب حاد. يُنصح بعمل تحاليل دم كاملة.")
        elif "صداع" in symptoms:
            st.info("الصداع قد يشير لعدة أسباب مثل التوتر أو الأنيميا أو مشاكل عصبية.")
        else:
            st.write("الأعراض تحتاج تقييم طبي شامل.")

elif option == "رفع صورة تحليل":
    uploaded_file = st.file_uploader("ارفع صورة التحليل (PNG أو JPG)", type=["png", "jpg", "jpeg"])
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="صورة التحليل المرفوعة", use_column_width=True)
        st.write("جاري قراءة التحليل...")
        text = pytesseract.image_to_string(image, lang="eng")
        st.write("النتائج المستخرجة من الصورة:")
        st.text(text)
        st.write("تحليل مبدئي (تجريبي):")
        if "Hemoglobin" in text and "10" in text:
            st.warning("الهيموجلوبين منخفض → احتمال أنيميا.")
        elif "CRP" in text and "50" in text:
            st.warning("CRP مرتفع → احتمال التهاب.")
        else:
            st.write("النتائج تحتاج مراجعة طبية أكثر دقة.")
