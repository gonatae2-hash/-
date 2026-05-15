# 나사 검출 프로젝트

## 프로젝트 개요
카메라로 나사를 촬영하여 종류를 분류하고 Arduino LED로 결과를 출력하는 시스템

## 전체 흐름
카메라 노드 (영상 송출)

→ 검출 노드 (YOLO(나사 검출) + teachable machine(나사 종류 분류)) 

→ 결과 노드 (openCV(실시간 화면 표시 - 종류 + 개수 + LED 색) + Arduino (LED 제어))

## 사용 기술
- Teachable Machine
- Google Colab
- ROS
- Arduino
- openCV

## 진행 상황
### 04-24
- Roboflow + 직접 촬영 이미지로 나사 라벨링
- YOLOv8로 나사 검출 구현 (Colab)
- VSCode에서 불량 감지 시도 → 실패
- 방향 전환: 나사 불량 검출 -> 나사 종류 분류

### 05-08
- 나사 불량 검출 -> 나사 종류 분류 목표변경
- roboflow 데이터셋을 통한 YOLOv8 모델로 나사 검출
- teachable machine을 통해 종류별 나사 라벨링 (나사 종류별 검출 정확도가 떨어짐 - 밝기에 따른 추가 라벨링 필요)
- Arduino LED 연동 (나사 종류별 Led ON)

### 05-15
- openCV를 통한 실시간 화면 표시(종류 + 개수 + LED 색)
- ros 노드 연결(카메라, 검출, 결과)

### 05-20 진행 계획
- 밝기에 따른 teachable machine 라벨링 추가
- 현재(05-15) vmware 카메라 연결 실패 문제 해결
