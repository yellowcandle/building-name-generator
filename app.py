import streamlit as st
import random

st.set_page_config(page_title="唐樓命名攻略", page_icon="🏢", layout="wide")

st.title("唐樓命名攻略 (上世紀適用)")

st.markdown("""
            原 post: https://www.threads.net/@hkcornerhouses/post/DASXHABSXVa
            """)

# Define the character sets
first_characters = {
    "時間": ["永", "恆"],
    "地方": ["海", "東"],
    "數量": ["富", "盛", "同", "萬", "廣", "長"],
    "意頭": ["寶", "順", "好", "榮"],
    "其他": ["金", "新"]
}

last_characters = ["昌", "運", "利", "安", "勝", "發", "成", "豐", "益", "源", "裕", "基"]
suffix = ["大廈", "大樓", "樓"]

# Create checkboxes for category selection
st.subheader("選擇字頭類別")
selected_categories = {}
for category in first_characters.keys():
    selected_categories[category] = st.checkbox(category, value=True)

# Generate button
if st.button("隨機生成大廈名稱"):
    # Filter selected categories
    available_categories = [cat for cat, selected in selected_categories.items() if selected]
    
    if not available_categories:
        st.error("請至少選擇一個字頭類別")
    else:
        # Randomly select a category and a character from that category
        chosen_category = random.choice(available_categories)
        first_char = random.choice(first_characters[chosen_category])
        last_char = random.choice(last_characters)
        suffix_char = random.choice(suffix)
        building_name = f"{first_char}{last_char}{suffix_char}"
        st.success(f"生成的大廈名稱: {building_name}")
        st.info(f"使用的字頭類別: {chosen_category}")

# Add some information about the naming strategy
st.markdown("---")
st.subheader("命名策略說明")
st.markdown("""
- 字頭: 根據選擇的類別隨機選擇，包括時間、地方、數量、意頭和其他。
- 字尾: 從常用的吉祥字中隨機選擇。
- 大廈: 名稱最後加上「大廈」、「大樓」或「樓」。
""")

# Add the image
st.markdown("---")
st.subheader("參考圖片")
st.image("461008388_1761486387931403_1695198223138866317_n.jpg", caption="唐樓命名攻略圖", use_column_width=True)

# Add credits
st.markdown("---")
st.caption("圖片來源: HKU Digital Repository 「聯和大廈」售樓書")