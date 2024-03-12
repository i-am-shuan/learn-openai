
### Assistants API with Code interpreter & Retrieval Tool을 가지고 Image를 만들기
- 코드 해석기(Code Interpreter)를 사용하면 Assistants API를 사용하여 샌드박스 실행 환경에서 Python 코드를 작성하고 실행할 수 있습니다.
- 이 도구는 다양한 데이터와 포맷의 파일을 처리할 수 있으며, 데이터와 그래프 이미지가 포함된 파일을 생성할 수 있습니다.
- https://platform.openai.com/docs/assistants/tools/supported-files

***

**1. 동작 과정**
- code_interpreter: CSV 파일에서 데이터를 추출하고, 데이터를 가공한 후 시각화에 활용
- retrieval: CSV 파일 내에서 2022년 포춘 1000 기업의 수익 정보를 찾는데 활용

<p align="center">
	<img alt="image" src="https://github.com/i-am-shuan/learn-openai/assets/161431602/a059336a-c99f-49ba-b9a9-0fef44b20d23" width="80%" height="80%">
</p>

***

**2. 실행 결과**
<p align="center">
	<img alt="image" src="https://github.com/i-am-shuan/learn-openai/assets/161431602/4a68e104-6716-406a-875d-38d3d96512b3" width="80%" height="80%">
</p>

***

