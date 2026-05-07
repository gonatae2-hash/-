# 나사 검출 프로젝트

## 프로젝트 개요
카메라로 나사를 촬영하여 종류를 분류하고 Arduino LED로 결과를 출력하는 시스템

## 전체 흐름
카메라 → Teachable Machine (나사 종류 분류) → ROS 노드 → Arduino LED 제어

## 사용 기술
- Teachable Machine
- Google Colab
- ROS
- Arduino

## 진행 상황
### 04-24
- Roboflow + 직접 촬영 이미지로 나사 라벨링
- YOLOv8로 나사 검출 구현 (Colab)
- VSCode에서 불량 감지 시도 → 실패
- 방향 전환: 나사 종류 분류 시스템으로 변경

### 앞으로 할 것
- Teachable Machine으로 나사 종류 라벨링 및 모델 학습
- ROS 노드 구성
- Arduino LED 연동
