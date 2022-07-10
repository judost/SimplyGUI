# SimplyGUI
Python Tkinter로 구현하는 간단한 GUI

### 1.1 exe 만들기 (터미널에서 입력)
    pip install pyinstaller  
    pyinstaller -w --uac-admin --icon=my path main.py # -w --uac-admin : 관리자 권한 / --icon=your path / main.py : your Py script Name

### 1.2 상대 경로 바로가기 만들기
##### 1. txt 만들기
##### 2 . 아래 내용 복붙
    cd .\your folder path\
    start "" ".\main.exe"
