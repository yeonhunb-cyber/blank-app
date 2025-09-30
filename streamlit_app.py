import streamlit as st


# Streamlit 요소 예시 페이지
import streamlit as st

st.title("🎈 Streamlit 요소 예시")  # 페이지 제목
st.caption("이 페이지는 Streamlit에서 사용할 수 있는 다양한 요소의 예시와 각주를 보여줍니다.")

# 텍스트 관련 요소
st.header("1. 텍스트 관련 요소")
st.subheader("st.text, st.markdown, st.latex, st.code")
st.text("이것은 일반 텍스트입니다.")  # 일반 텍스트
st.markdown("**이것은 마크다운 텍스트입니다.** _기울임, 링크, 리스트 등 지원_ ")  # 마크다운
st.latex(r"E=mc^2")  # LaTeX 수식
st.code("print('Hello, Streamlit!')", language="python")  # 코드 블록
st.caption("각주: st.text, st.markdown, st.latex, st.code는 다양한 텍스트 표현을 지원합니다.")

# 입력 위젯
st.header("2. 입력 위젯")
name = st.text_input("이름을 입력하세요")  # 텍스트 입력
age = st.number_input("나이", min_value=0, max_value=120, value=25)  # 숫자 입력
agree = st.checkbox("동의합니다")  # 체크박스
color = st.radio("좋아하는 색상은?", ("빨강", "파랑", "초록"))  # 라디오 버튼
option = st.selectbox("직업을 선택하세요", ("학생", "직장인", "기타"))  # 셀렉트박스
multi = st.multiselect("취미를 선택하세요", ["독서", "운동", "게임", "음악감상"])  # 다중 선택
date = st.date_input("날짜를 선택하세요")  # 날짜 입력
time = st.time_input("시간을 선택하세요")  # 시간 입력
st.caption("각주: 입력 위젯은 사용자로부터 다양한 형태의 데이터를 받을 수 있습니다.")

# 버튼
st.header("3. 버튼")
if st.button("클릭하세요"):
    st.success("버튼이 클릭되었습니다!")
st.caption("각주: st.button은 클릭 시 동작을 트리거합니다.")

# 슬라이더
st.header("4. 슬라이더")
value = st.slider("값을 선택하세요", 0, 100, 50)
st.caption("각주: st.slider는 범위 내에서 값을 선택할 수 있습니다.")

# 파일 업로드
st.header("5. 파일 업로드")
uploaded_file = st.file_uploader("파일을 업로드하세요")
if uploaded_file is not None:
    st.write("파일명:", uploaded_file.name)
st.caption("각주: st.file_uploader로 파일을 업로드할 수 있습니다.")

# 이미지, 오디오, 비디오
st.header("6. 미디어 요소")
st.image("https://placekitten.com/200/300", caption="고양이 이미지 예시")
st.audio(
    "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3",
    format="audio/mp3"
)
st.video("https://www.w3schools.com/html/mov_bbb.mp4")
st.caption("각주: st.image, st.audio, st.video로 다양한 미디어를 표시할 수 있습니다.")

# 진행바와 상태 표시
st.header("7. 진행바와 상태 표시")
import time
progress = st.progress(0)
for i in range(1, 11):
    time.sleep(0.05)
    progress.progress(i * 10)
st.spinner("로딩 중...")
st.balloons()
st.caption("각주: st.progress, st.spinner, st.balloons 등으로 상태를 시각화할 수 있습니다.")

# 데이터프레임과 표
st.header("8. 데이터 표시")
import pandas as pd
import numpy as np
df = pd.DataFrame(
    np.random.randn(5, 3),
    columns=["A", "B", "C"]
)
st.dataframe(df)
st.table(df.head(3))
st.caption("각주: st.dataframe, st.table로 표 형태의 데이터를 표시할 수 있습니다.")

# 차트
st.header("9. 차트")
st.line_chart(df)
st.bar_chart(df)
st.area_chart(df)
st.caption("각주: st.line_chart, st.bar_chart, st.area_chart로 간단한 시각화를 할 수 있습니다.")

# 사이드바
st.sidebar.title("사이드바 예시")
st.sidebar.write("여기는 사이드바입니다.")
st.sidebar.button("사이드바 버튼")
st.caption("각주: st.sidebar를 사용하면 보조 UI를 만들 수 있습니다.")
