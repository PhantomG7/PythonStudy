Festa.io 의 이벤트 목록 정렬하기 v2.0
===================================

# 문제 설명

- 해나라는 Festa.io 에 그동안 다녀왔던 목록을 재정렬 하는데는 성공했다. 하지만 이것을 깃헙 레포지토리에 관리하던 중 조금 더 자동화 할 수 있지 않을까 하는 생각에 도달했다.
- 이번엔 추가 기능으로 이벤트 이름에 해당하는 폴더와 markdown 파일을 일부 자동으로 생성하는 프로그램을 작성하고자 한다.
 
# 요구 사항

- 날짜, 행사이름, 주최자 순으로 출력되어있는 문자열을 입력 받았을 때, 연도별로 폴더를 만들고 해당 이벤트 이름에 맞는 markdown 파일을 생성하는 파이썬 프로그램 코드를 작성한다.
- 행사 이름에 포함된 특수문자는 전부 생략한다.
- 행사 이름의 띄어쓰기는 전부 '_' 로 대치한다.
- markdown 파일 안에도 기본 템플릿대로 생성한다.

- 입력되는 포맷은 아래와 같다.
```
행사 일시
행사명
주최자 명
... 반복
```

- 생성할 폴더와 파일의 경로와 이름은 아래와 같다.
```
.
├── 연도1
│   ├── 행사1일시
│   │   └── 행사명1.md
│   ├── 행사2일시
│   │   └── 행사명2.md
│   └──  ⋮
└── 연도2
    ├── 행사1일시
    │   └── 행사명1.md
    └──  ⋮
```

- 생성한 markdown 파일은 아래의 내용을 가지고 있어야 한다.
```
### 행사명

![행사사진]()

- **⏰ 일시** : 행사 일시 (포맷은 YYYY. mm. dd (w) )
- **💁 주최** : 주최자 명
- **📝 장소** : 
- **📝 총평** : 
- **🔗 링크** : 
```

# 예제 입력

```
2019년 12월 21일 오후 1:00
Android Dev Summit 2019 extended Seoul!
GDG Korea Android
2018년 06월 10일 오전 11:00
Google I/O Extended 2018 Seoul
GDG Korea
```

# 예제 출력

## 파일 경로 
```
.
├── 2018
│   └──0610
│        └── Google_IO_Extended_2018_Seoul.md
└── 2019
    └──1221
         └── Android_Dev_Summit_2019_extended_Seoul.md
```

## .md 파일 예시

- ./2019/Android_Dev_Summit_2019_extended_Seoul.md 
```
### Android Dev Summit 2019 extended Seoul

![행사사진]()

- **⏰ 일시** : 2019. 12. 21 (토)
- **💁 주최** : GDG Korea Android
- **📝 장소** : 
- **📝 총평** : 
- **🔗 링크** : 
```

- ./2018/Google_IO_Extended_2018_Seoul.md

```
### Google I/O Extended 2018 Seoul

![행사사진]()

- **⏰ 일시** : 2018. 06. 10 (토)
- **💁 주최** : GDG Korea
- **📝 장소** : 
- **📝 총평** : 
- **🔗 링크** : 
```


# 풀이

- 소스 코드 : [FestaListSortingv2.py](FestaListSortingv2.py)
- 내가 원하는 정확한 포맷으로 파일을 전부 생성해주었다! 기쁘다!
- 간단하지만 파일 입출력과 정규식, 날짜 포맷변경을 만져볼 수 있었다.

# 적용

- https://github.com/HaenaraShin/Dev-Conference-Review/commit/abc08cc8a4b6def75d29f3f8984be5ceea274db9