# Whisper 오디오 변환 프로젝트

## 📌 소개
이 프로젝트는 OpenAI의 **Whisper** 모델을 활용하여 오디오 파일을 텍스트로 변환하고, 번역 및 요약하는 기능을 제공합니다. 다양한 형식(SRT, 텍스트, 번역 등)으로 변환이 가능하며, GPT-3.5를 사용하여 내용을 요약할 수도 있습니다.

## 🚀 주요 기능

### 1. 오디오를 텍스트로 변환 (`text.py`)
```bash
python text.py
```
- `sample.wav` 파일을 Whisper 모델을 사용하여 텍스트로 변환
- 결과를 출력

### 2. 오디오를 SRT(자막)로 변환 (`srt.py`)
```bash
python srt.py
```
- `sample.wav` 파일을 변환하여 SRT 형식의 자막 출력

### 3. 오디오를 번역 (`translate.py`)
```bash
python translate.py
```
- 기본적으로 영어로 변환
- 필요 시 한국어 번역 및 요약 기능 포함

### 4. 오디오 내용을 요약 (`main.py`)
```bash
python main.py
```
- `sample.wav` 오디오 내용을 Whisper 모델로 텍스트 변환
- 변환된 텍스트를 GPT 모델을 사용하여 3줄 요약
- 사용된 토큰 수 출력

## 📂 프로젝트 구조
```
whisper/
│── main.py          # 텍스트 변환 후 요약
│── srt.py           # SRT(자막) 변환
│── text.py          # 텍스트 변환
│── translate.py     # 번역 기능 포함
│── sample.wav       # 테스트용 오디오 파일
```
※ sample.wav을/를 필요한 음성 파일로 대체해야 원하는 결과 나옵니다!

## 💻 설치 및 실행 방법
### 1. 필수 라이브러리 설치
```bash
pip install openai
```

### 2. OpenAI API 키 설정
환경 변수에 OpenAI API 키를 설정해야 합니다.
```bash
export OPENAI_API_KEY="your-api-key"
```

### 3. 프로그램 실행
위의 주요 기능별 실행 방법을 참고하여 원하는 기능을 실행하면 됩니다.

## 📢 참고 사항
- OpenAI의 Whisper 모델을 사용하기 때문에 **OpenAI API 키**가 필요합니다.
- `sample.wav` 파일을 원하는 오디오 파일로 변경하여 사용 가능합니다.

## 📜 라이선스
이 프로젝트는 MIT 라이선스를 따릅니다.

