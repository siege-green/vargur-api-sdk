# Vargur API SDK 환영합니다

Vargur API SDK는 Vargur 플랫폼용 플러그인을 개발하기 위한 강력한 도구입니다. 이 문서는 SDK 사용법과 자체 플러그인 생성 과정을 안내합니다.

## 빠른 시작

Vargur API SDK를 시작하려면 다음 단계를 따르세요:

1. SDK 설치: `pip install vargur-sdk`
2. 코드에 필요한 구성 요소 가져오기:

```python
from vargur_sdk import Plugin, router, task
```

3. 플러그인 클래스 만들기:

```python
class MyPlugin(Plugin):
    def __init__(self):
        super().__init__()

    @task
    async def my_background_task(self):
        # 백그라운드 작업 로직을 여기에 작성하세요
        pass

@router.get("/my-endpoint")
async def my_endpoint():
    # 엔드포인트 로직을 여기에 작성하세요
    return {"message": "플러그인에서 안녕하세요!"}
```

4. Vargur 애플리케이션에서 플러그인 사용하기

더 자세한 정보는 [사용자 가이드](user-guide.md)와 [API 레퍼런스](api-reference.md)를 참조하세요.

## 기능

- 사용하기 쉬운 플러그인 시스템
- 백그라운드 작업 지원
- 내장 캐싱 및 이벤트 시스템
- 데이터베이스 통합
- 다국어 지원

## 지원

문제가 발생하거나 질문이 있으면 [GitHub Issues](https://github.com/vargur/vargur-sdk/issues) 페이지를 확인하거나 지원 팀에 문의하세요.