# 사용자 가이드

이 가이드는 Vargur API SDK를 사용하여 플러그인을 만드는 과정을 안내합니다.

## 플러그인 만들기

플러그인을 만들려면 다음 단계를 따르세요:

1. 플러그인용 새 Python 파일을 만듭니다.
2. Vargur SDK에서 필요한 구성 요소를 가져옵니다:

```python
from vargur_sdk import Plugin, router, task
```

3. `Plugin`을 상속받는 클래스를 만듭니다:

```python
class MyPlugin(Plugin):
    def __init__(self):
        super().__init__()
```

4. `router` 데코레이터를 사용하여 엔드포인트를 추가합니다:

```python
@router.get("/my-endpoint")
async def my_endpoint():
    return {"message": "플러그인에서 안녕하세요!"}
```

5. `task` 데코레이터를 사용하여 백그라운드 작업을 추가합니다:

```python
@task
async def my_background_task(self):
    while True:
        # 백그라운드 작업 로직을 여기에 작성하세요
        await asyncio.sleep(60)  # 1분마다 실행
```

## 캐시 사용하기

SDK는 내장 캐싱 시스템을 제공합니다. 사용 방법은 다음과 같습니다:

```python
from vargur_sdk import cache

# 캐시에 값 설정하기
await cache.set("my_key", "my_value", expire=3600)  # 1시간 후 만료

# 캐시에서 값 가져오기
value = await cache.get("my_key")

# 캐시에서 값 삭제하기
await cache.delete("my_key")
```

## 데이터베이스 작업하기

SDK는 데이터베이스 통합을 제공합니다. 기본 예제는 다음과 같습니다:

```python
from vargur_sdk import get_db
from sqlalchemy.future import select
from your_models import YourModel

@router.get("/db-example")
async def db_example():
    async with get_db() as session:
        result = await session.execute(select(YourModel))
        items = result.scalars().all()
        return {"items": items}
```

더 고급 사용법은 [API 레퍼런스](api-reference.md)를 참조하세요.