
import time
import streamlit as st

st.title("⏱️ เกมเติมศัพท์จับเวลา")

# ----------------------------------------------------
# 1. ตั้งค่าเริ่มต้น
# ----------------------------------------------------
if "start" not in st.session_state:
    st.session_state.start = None

if "is_ended" not in st.session_state:
    st.session_state.is_ended = False

if "ans1" not in st.session_state:
    st.session_state.ans1 = ""

if "ans2" not in st.session_state:
    st.session_state.ans2 = ""

if "ans3" not in st.session_state:
    st.session_state.ans3 = ""

if "ans4" not in st.session_state:
    st.session_state.ans4 = ""


# ----------------------------------------------------
# 2. ฟังก์ชันเริ่มเกมใหม่
# ----------------------------------------------------
def reset_game():
    st.session_state.start = time.time()
    st.session_state.is_ended = False

    st.session_state.ans1 = ""
    st.session_state.ans2 = ""
    st.session_state.ans3 = ""
    st.session_state.ans4 = ""


# ----------------------------------------------------
# 3. ฟังก์ชันตรวจคำตอบและแสดงผล
# ----------------------------------------------------
@st.dialog("📊 สรุปผลการเล่นเกม")
def show_result_dialog(ans1, ans2, ans3, ans4):

    score = 0

    # แปลงคำตอบเป็นตัวพิมพ์เล็ก
    u_ans1 = ans1.strip().lower()
    u_ans2 = ans2.strip().lower()
    u_ans3 = ans3.strip().lower()
    u_ans4 = ans4.strip().lower()

    # ------------------------------------------------
    # ข้อ 1
    # ------------------------------------------------
    if u_ans1 == "apple":
        st.success("✅ ข้อ 1: ถูกต้อง")
        score += 1
    else:
        st.error(f"❌ ข้อ 1: ผิด (คุณตอบ '{u_ans1}')")
        st.info("💡 คำตอบที่ถูกต้องคือ: apple")

    # ------------------------------------------------
    # ข้อ 2
    # ------------------------------------------------
    if u_ans2 == "fish":
        st.success("✅ ข้อ 2: ถูกต้อง")
        score += 1
    else:
        st.error(f"❌ ข้อ 2: ผิด (คุณตอบ '{u_ans2}')")
        st.info("💡 คำตอบที่ถูกต้องคือ: fish")

    # ------------------------------------------------
    # ข้อ 3
    # ------------------------------------------------
    if u_ans3 == "banana":
        st.success("✅ ข้อ 3: ถูกต้อง")
        score += 1
    else:
        st.error(f"❌ ข้อ 3: ผิด (คุณตอบ '{u_ans3}')")
        st.info("💡 คำตอบที่ถูกต้องคือ: banana")

    # ------------------------------------------------
    # ข้อ 4
    # ------------------------------------------------
    if u_ans4 == "coconut":
        st.success("✅ ข้อ 4: ถูกต้อง")
        score += 1
    else:
        st.error(f"❌ ข้อ 4: ผิด (คุณตอบ '{u_ans4}')")
        st.info("💡 คำตอบที่ถูกต้องคือ: coconut")

    # ------------------------------------------------
    # สรุปคะแนน
    # ------------------------------------------------
    st.divider()

    st.subheader(f"🏆 คะแนนของคุณ: {score}/4")

    if score == 4:
        st.success("🎉 You win!")
        st.balloons()
    else:
        st.error("💀 You lose!")


# ----------------------------------------------------
# 4. ปุ่มเริ่มเกม
# ----------------------------------------------------
st.button(
    "🎮 เริ่มเล่นเกม",
    on_click=reset_game
)


# ----------------------------------------------------
# 5. ตัวจับเวลา 30 วินาที
# ----------------------------------------------------
if (
    st.session_state.start is not None
    and not st.session_state.is_ended
):

    elapsed_time = time.time() - st.session_state.start
    time_left = int(30 - elapsed_time)

    if time_left > 0:

        st.error(f"⏳ เหลือเวลา: {time_left} วินาที")

        # อัปเดตหน้าจอทุก 1 วินาที
        time.sleep(1)
        st.rerun()

    else:

        st.session_state.is_ended = True
        st.rerun()


st.divider()


# ----------------------------------------------------
# 6. ช่องกรอกคำตอบ
# ----------------------------------------------------
st.text_input(
    "ข้อ 1: An `a _ _ l e` a day keeps the doctor away. 🍎",
    key="ans1",
)

st.text_input(
    "ข้อ 2: Cats love to eat `f _ s h`. 🐟",
    key="ans2",
)

st.text_input(
    "ข้อ 3: Slip on a `b a _ a n _`. 🍌",
    key="ans3",
)

st.text_input(
    "ข้อ 4: Lovely bunch of `_ o c _ _ u t`. 🥥",
    key="ans4",
)


# ----------------------------------------------------
# 7. ปุ่มส่งคำตอบ
# ----------------------------------------------------
if (
    st.session_state.start is not None
    and not st.session_state.is_ended
):

    if st.button("📥 ส่งคำตอบ"):

        st.session_state.is_ended = True
        st.rerun()


# ----------------------------------------------------
# 8. แสดงผลคะแนน
# ----------------------------------------------------
if st.session_state.is_ended:

    show_result_dialog(
        st.session_state.ans1,
        st.session_state.ans2,
        st.session_state.ans3,
        st.session_state.ans4,
    )


# ----------------------------------------------------
# 9. เครดิต
# ----------------------------------------------------
st.divider()

st.write("นายอดิเทพ วงษา เลขที่ 17 ม.4/7")
