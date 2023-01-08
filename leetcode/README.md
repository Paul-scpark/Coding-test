# SQL 코딩 테스트 Tips 정리

## 쿼리 실행 작동 순서 (참고)
- `FROM`: 조회 테이블을 확인하기
- `WHERE`: 데이터 추출에 대한 조건 확인하기
- `GROUP BY`: 묶을 컬럼에 대한 조건 확인하기
- `HAVING`: 묶은 컬럼에 대한 추가적인 조건 확인하기
- `SELECT`: 데이터 추출하기
- `ORDER BY`: 데이터 정렬 순서 확인하기

## 기초 구조

1. `SELECT, FROM, WHERE`: DB_NAME 데이터베이스로부터 WHERE 절 조건에 해당하는 모든 Columns을 출력
- `ORDER BY`: 출력하는 것의 순서를 정렬할 수 있음. Default는 `ASC` 이고, `DESC`로 작성하여 내림차순 정렬 가능
- `DISTINCT`: 중복된 데이터를 제거하여 Unique 한 결과를 조회 가능
- `AND`, `OR`: 쿼리의 조건 상에 복수의 조건을 넣을 경우, 일반 코드에서 작성하듯 `AND`와 `OR`로 조건 추가 가능
- `MIN`, `MAX`: 특정 값의 최댓값과 최솟값을 조회 가능
- `COUNT`: 조건에 해당하는 개수 결과 조회 가능
- `!=`, `<>`: 조건 상에서 같지 않다는 조건을 쓰고 싶을 때, 이 두 키워드를 사용할 수 있음
- `LIMIT <NUMBER>`, `LIMIT <NUMBER1> <NUMBER2>`, `LIMIT <NUMBER1> OFFSET <NUMBER2>`: 
  - `LIMIT` 뒤에 오는 숫자가 한 개이면, 그 숫자만큼 출력
  - `LIMIT` 뒤에 오는 숫자가 두 개이면, 첫 숫짜에 해당하는 행부터 두 번째 숫짜의 결과를 출력
- `BETWEEN <COL_NAME> BETWEEN <VALUE1> AND <VALUE2>`:
  - COL_NAME 컬럼에 대해 VALUE1 이상이면서 VALUE2 이하인 결과 출력
  - 반드시 앞에 오는 값 (VALUE1)이 뒤에 오는 값 (VALUE2) 보다 작아야 함
```
SELECT * FROM <DB_NAME>
WHERE <CONDITION1> AND <CONDITION2>
ORDER BY <COL_NAME1>, <COL_NAME2> DESC         # 복수의 Columns에 대해 정렬 가능
LIMIT 3, 2                                     # 3번째 행부터 2개의 결과만 출력
```

2. `GROUP BY, HAVING`: DB_NAME 데이터베이스로부터 COL_NAME으로 묶은 후, HAVING 절 조건에 해당하는 모든 Columns 출력
- `GROUP BY`가 포함된 쿼리에서는 조건절을 `WHERE`를 쓰지 않고, `HAVING`으로 작성. 
- 반드시 `GROUP BY` 뒤에 `HAVING` 절이 나와야 함 (순서가 중요)
```
SELECT * FROM <DB_NAME>
GROUP BY <COL_NAME>
HAVING <CONDITION>
```

3. `JOIN`: DB_NAME1과 DB_NAME2 데이터를 중복된 KEY_COL에 대해 JOIN 하는 결과 출력
```
SELECT * FROM <DB_NAME1> A
JOIN <DB_NAME2> B
USING(<KEY_COL>)                               # ON A.KEY_COL = B.KEY_COL과 동일
```

## 특수한 문법
1. 순위 매기기 (RANK, DENSE_RANK, ROW_NUMBER)
- `RANK()`: 공동 순위만큼 건너 뛰어서 결과 출력 (1, 2, 2, 4)
- `DENSE_RANK()`: 공동 순위를 건너 뛰지 않고 결과 출력 (1, 2, 2, 3)
- `ROW_NUMBER()`: 공동 순위를 무시하고 결과 출력 (1, 2, 3, 4)

2. 날짜 데이터 확인하기 (SUBDATE, DATEDIFF)
- `SUBDATE(DATE_COL_NAME, NUMBER)`: DATE_COL_NAME 칼럼 값에 대해 NUMBER 만큼 과거의 날짜를 출력
- `DATEDIFF(DATE_COL_NAME1, DATE_COL_NAME2)`: DATE_COL_NAME1과 DATE_COL_NAME2의 날짜의 차이를 출력

3. NULL 관련 함수 (IS NULL, IS NOT NULL, IFNULL)
- `IFNULL(COL_NAME, "No name")`: COL_NAME 칼럼의 값이 NULL 이라면, "No name"을 출력
- `IS NULL`, `IS NOT NULL`: NULL이거나, 아니거나 하는 조건을 추가할 때는 `=`이 아닌 `IS` 키워드를 사용해야 함
