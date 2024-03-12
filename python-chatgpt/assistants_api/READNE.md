
### Assistants API with Code interpreter & Retrieval Tool 기반 Image(Pliot) 제작 서비스
이 코드는 OpenAI의 GPT-4와 연동하여 CSV 파일에서 데이터를 추출하고, 이를 바탕으로 상위 10개 기업의 매출을 시각화하는 프로세스를 자동화하는 예제입니다. 이 코드는 데이터 분석 및 시각화 작업을 자동화하며, 특히 대용량 데이터 처리와 복잡한 쿼리에 대응하는 어플리케이션 개발에 유용합니다.

- 코드 해석기(Code Interpreter)를 사용하면 Assistants API를 사용하여 샌드박스 실행 환경에서 Python 코드를 작성하고 실행할 수 있습니다.
- 이 도구는 다양한 데이터와 포맷의 파일을 처리할 수 있으며, 데이터와 그래프 이미지가 포함된 파일을 생성할 수 있습니다.
- https://platform.openai.com/docs/assistants/tools/supported-files

***

**1. 동작 과정**
<p align="center">
	<img alt="image" src="https://github.com/i-am-shuan/learn-openai/assets/161431602/a059336a-c99f-49ba-b9a9-0fef44b20d23" width="80%" height="80%">
</p>

- 1단계: 환경 설정과 클라이언트 초기화
  - 먼저, OPENAI_API_KEY 환경 변수를 설정하여 API 키를 제공합니다. 이는 OpenAI 서비스에 접근하기 위한 인증 키입니다.
OpenAI() 클라이언트 객체를 생성하여 OpenAI API와의 연결을 초기화합니다.

- 2단계: 참조 파일 업로드
  - client.files.create 메서드를 사용하여 'sample/fortune_1000_revenue_2022.csv' 파일을 OpenAI 서버에 업로드합니다. 이 파일은 분석 대상인 포춘 1000 기업의 2022년 매출 데이터를 포함하고 있습니다.
  - 업로드된 파일의 ID를 출력합니다. 이 ID는 후속 단계에서 파일을 참조하는 데 사용됩니다.

- 3단계: 어시스턴트 생성
  - client.beta.assistants.create 메서드를 통해 새로운 어시스턴트를 생성합니다. 이 어시스턴트는 CSV 파일로부터 데이터를 추출하고, 사용자 쿼리에 최적으로 응답하기 위한 지시사항을 포함합니다.
생성된 어시스턴트는 코드 해석(code_interpreter) 및 데이터 검색(retrieval) 도구를 사용할 수 있으며, 업로드한 파일 ID를 참조합니다.

- 4단계: 스레드 생성 및 메시지 전송
  - client.beta.threads.create 메서드로 새로운 스레드를 생성합니다.
생성된 스레드에 메시지를 전송하여, 업로드된 파일을 사용한 상위 10개 기업의 매출 시각화를 요청합니다.

- 5단계: 실행 명령 및 상태 확인
  - client.beta.threads.runs.create 메서드를 호출하여, 어시스턴트에게 특정 지시사항을 실행하도록 요청합니다.
  - 실행 상태를 주기적으로 확인하여, 작업이 완료될 때까지 대기합니다. 상태가 'completed'가 되면, 다음 단계로 진행합니다.

- 6단계: 결과 메시지 검색
  - client.beta.threads.messages.list 메서드를 사용하여 스레드에서 생성된 메시지를 검색합니다. 이를 통해 어시스턴트가 수행한 데이터 처리 및 시각화 작업의 결과를 확인할 수 있습니다.

- 7단계: 시각화 파일 저장
  - 마지막 단계에서는 어시스턴트가 생성한 매출 시각화 이미지 파일을 로컬 시스템에 저장합니다. client.files.content 메서드를 사용하여 파일의 내용을 검색하고, 이를 바이트 형식으로 로컬 파일에 작성합니다.


***

**2. 실행 결과**
<p align="center">
	<img alt="image" src="https://github.com/i-am-shuan/learn-openai/assets/161431602/4a68e104-6716-406a-875d-38d3d96512b3" width="80%" height="80%">
</p>

***

