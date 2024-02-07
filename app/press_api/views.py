'''
1. `Case`: 데이터베이스에서 조건에 따라 다른 값을 반환하는 함수입니다. 예를 들어, 성별이 "남성"인 경우에는 "M", 그렇지 않은 경우에는 "F"를 반환할 수 있습니다.

2. `F`: 데이터베이스 필드의 값을 가져오고 업데이트하는데 사용되는 함수입니다. 다른 필드의 값을 가져와서 계산하거나 업데이트할 때 유용합니다.

3. `Sum`: 데이터베이스에서 특정 필드의 값을 모두 합산하는 함수입니다. 주로 그룹화된 쿼리나 특정 조건을 만족하는 레코드들의 값을 합산할 때 사용됩니다.

4. `Value`: 특정 값을 나타내는 객체를 생성하는 함수입니다. 이 객체는 데이터베이스 쿼리에서 특정 값을 지정할 때 사용됩니다.

5. `When`: Case 문에서 각 조건에 대한 조건절을 지정하는 함수입니다. Case 문에서 사용되며, 각 조건에 대한 조건식과 그에 해당하는 값을 지정합니다.
'''
from django.db.models import Case, F, Sum, Value, When
# Coalesce 함수는 여러 개의 인자 중에서 첫 번째로 NULL이 아닌 값을 반환하는 함수
from django.db.models.functions import Coalesce

# RESTful API를 만들기 위한 일반적인 클래스 기반 뷰를 제공
'''ListAPIView: 리스트 형식의 리소스를 나타내는 뷰를 제공합니다. 이 뷰를 사용하면 데이터베이스 쿼리 결과를 시리얼라이저를 통해 JSON 형식으로 반환할 수 있습니다.

RetrieveAPIView: 단일 리소스를 나타내는 뷰를 제공합니다. 이 뷰를 사용하여 데이터베이스에서 단일 객체를 가져와 JSON 형식으로 반환할 수 있습니다.

CreateAPIView: 새로운 리소스를 생성하는 뷰를 제공합니다. 이 뷰를 사용하여 POST 요청을 통해 새로운 객체를 생성하고 데이터베이스에 저장할 수 있습니다.

UpdateAPIView: 기존의 리소스를 업데이트하는 뷰를 제공합니다. 이 뷰를 사용하여 PUT 또는 PATCH 요청을 통해 객체를 업데이트할 수 있습니다.

DestroyAPIView: 기존의 리소스를 삭제하는 뷰를 제공합니다. 이 뷰를 사용하여 DELETE 요청을 통해 객체를 삭제할 수 있습니다.

ListCreateAPIView: 리스트 및 생성 기능을 모두 제공하는 뷰를 제공합니다. 이 뷰를 사용하여 리스트 조회와 새로운 객체 생성 기능을 한 번에 제공할 수 있습니다.'''
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
# Response 클래스를 사용하여 데이터를 포함한 응답을 생성하였습니다. 이 응답은 클라이언트에게 JSON 형식으로 반환
from rest_framework.response import Response
from rest_framework.views import APIView

from press.models import Age, Category, Gender, Journalist, Press, models
from press_api.pagination import PostPageNumberPagination
from press_api.serializer import (
    AgeRankingByCategorySerializer,
    CategorySerializer,
    GenderSerializer,
    JournalistSerializer,
    PressAgeSerializer,
    PressGenderSerializer,
    PressSerializer,
    PressSubscriberAgeSerializer,
    SectionSerializer,
)

from .queryset import (
    category_query_set,
    journalist_query_set,
    press_query_set,
    secion_query_set,
)

class CategoryRanking(generics.ListCreateAPIView):
    # CategorySerializer를 사용하여 직렬화합니다
    serializer_class = CategorySerializer
    # 페이지네이션에는 PageNumberPagination을 사용합니다
    pagination_class = PageNumberPagination
    # 요청에서 쿼리 매개변수를 가져오거나 기본값을 설정합니다
    def get_queryset(self):
        # 'sort' 요청이 없다면 'id'을 기본값으로 정렬 설정
        # 이는 API에서 결과를 어떻게 정렬할지를 클라이언트가 지정할 수 있도록 하는 일반적인 패턴
        sort = self.request.GET.get("sort", "id")
        # 'number' 매개변수를 가져오거나 1000000으로 기본값 설정
        number = self.request.GET.get("number", 1000000)
        # 'number'를 정수로 변환합니다
        number = int(number)
        # 'sort'가 'id'가 아니면 내림차순으로 설정하기 위해 '-'를 추가합니다
        if sort != "id":
            sort = "-" + sort
        # 지정된 정렬로 데이터베이스를 쿼리하고 결과의 수를 제한합니다
        qs = category_query_set.order_by(sort)[:number]
        return qs

# 단일 카테고리에 대한 조회, 업데이트, 삭제를 처리하는 뷰를 정의
class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = category_query_set
    serializer_class = CategorySerializer
    lookup_field = "category_name"


class CategoryPressRanking(generics.ListAPIView):
    serializer_class = PressSerializer
    pagination_class = PageNumberPagination

    def get_queryset(self):
        sort = self.request.GET.get("sort", "id")
        number = self.request.GET.get("number", 10)
        number = int(number)
        if sort != "id":
            sort = "-" + sort
        qs = press_query_set
        qs = qs.filter(category__category_name=self.kwargs["category_name"]).order_by(
            sort
        )[:number]
        return qs


class CategoryJournalistRanking(generics.ListAPIView):
    serializer_class = JournalistSerializer
    pagination_class = PageNumberPagination

    def get_queryset(self):
        sort = self.request.GET.get("sort", "id")
        number = self.request.GET.get("number", 1000000)
        number = int(number)
        if sort != "id":
            sort = "-" + sort
        qs = journalist_query_set
        qs = qs.filter(
            press__category__category_name=self.kwargs["category_name"]
        ).order_by(sort)[:number]
        return qs


class PressRanking(generics.ListCreateAPIView):
    serializer_class = PressSerializer
    pagination_class = PageNumberPagination

    def get_queryset(self):
        sort = self.request.GET.get("sort", "id")
        number = self.request.GET.get("number", 1000000)
        number = int(number)
        if sort != "id":
            sort = "-" + sort
        qs = press_query_set.order_by(sort)[:number]
        return qs


class PressDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = press_query_set
    serializer_class = PressSerializer
    lookup_field = "press_name"


class PressJournallistRanking(generics.ListAPIView):
    serializer_class = JournalistSerializer
    pagination_class = PageNumberPagination

    def get_queryset(self):
        sort = self.request.GET.get("sort", "id")
        number = self.request.GET.get("number", 1000000)
        number = int(number)
        if sort != "id":
            sort = "-" + sort
        qs = journalist_query_set
        qs = qs.filter(press__press_name=self.kwargs["press_name"]).order_by(sort)[
            :number
        ]
        return qs


class SectionRanking(generics.ListCreateAPIView):
    serializer_class = SectionSerializer
    pagination_class = PageNumberPagination

    def get_queryset(self):
        sort = self.request.GET.get("sort", "id")
        number = self.request.GET.get("number", 1000000)
        number = int(number)
        if sort != "id":
            sort = "-" + sort
        qs = secion_query_set.order_by(sort)[:number]
        return qs


class SectionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = secion_query_set
    serializer_class = SectionSerializer
    lookup_field = "section_name"


class SectionJournallistRanking(generics.ListAPIView):
    serializer_class = JournalistSerializer
    pagination_class = PageNumberPagination

    def get_queryset(self):
        sort = self.request.GET.get("sort", "id")
        number = self.request.GET.get("number", 1000000)
        number = int(number)
        if sort != "id":
            sort = "-" + sort
        qs = journalist_query_set
        qs = qs.filter(
            journalistsection__section__section_name=self.kwargs["section_name"]
        ).order_by(sort)[:number]
        return qs


class JournalistRanking(generics.ListCreateAPIView):
    serializer_class = JournalistSerializer
    pagination_class = PageNumberPagination

    def get_queryset(self):
        sort = self.request.GET.get("sort", "id")
        number = self.request.GET.get("number", 1000000)
        number = int(number)
        if sort != "id":
            sort = "-" + sort
        qs = journalist_query_set.order_by(sort)[:number]
        return qs


class JournalistDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = journalist_query_set
    serializer_class = JournalistSerializer
    lookup_field = "journalist_id"


class SubscriberAgeList(generics.ListCreateAPIView):
    queryset = Age.objects.all()
    serializer_class = PressSubscriberAgeSerializer
    pagination_class = PostPageNumberPagination


class SubscriberAgeDetail(generics.ListAPIView):
    queryset = Age.objects.all()
    serializer_class = PressSubscriberAgeSerializer
    pagination_class = PostPageNumberPagination
    lookup_field = "journalist_id"

    def get_queryset(self):
        journalist_id = self.kwargs["journalist_id"]
        queryset = Age.objects.filter(journalist_id=journalist_id)
        return queryset


class SubscribersAgeByPressName(generics.ListAPIView):
    serializer_class = PressSubscriberAgeSerializer
    pagination_class = PostPageNumberPagination

    def get_queryset(self):
        press_name = self.kwargs["press_name"]  # URL에서 press_name을 가져옴
        queryset = Age.objects.filter(journalist__press__press_name=press_name)
        return queryset


class AgePressRanking(generics.ListAPIView):
    serializer_class = AgeRankingByCategorySerializer
    pagination_class = PostPageNumberPagination

    def get_queryset(self):
        age_ranges = [10, 20, 30, 40, 50, 60]
        result = []

        for age_range in age_ranges:
            age_group = f"{age_range}대"
            press_ranking = []

            for press in Press.objects.all():
                press_name = press.press_name
                age_subscriber_count = self.get_age_subscriber_count(press, age_range)

                press_ranking.append(
                    {"press_name": press_name, "count": age_subscriber_count}
                )

            press_ranking = sorted(
                press_ranking, key=lambda x: x["count"], reverse=True
            )
            press_ranking = press_ranking[:5]
            result.append({"age_group": age_group, "press_ranking": press_ranking})

        return result

    def get_age_subscriber_count(self, press, age_range):
        age_subscriber_count = (
            Press.objects.filter(id=press.id)
            .annotate(
                age_subscriber_count=Coalesce(
                    Sum(
                        Case(
                            When(
                                journalist__age__age=age_range,
                                then=F("journalist__subscriber_count")
                                * F("journalist__age__percentage")
                                / 100,
                            ),
                            default=Value(0),
                            output_field=models.IntegerField(),
                        )
                    ),
                    Value(0),
                )
            )
            .values_list("age_subscriber_count", flat=True)
            .first()
        )

        return age_subscriber_count

    def list(self, request):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class CategoryWiseAgePressRanking(APIView):
    paginatoin_class = PostPageNumberPagination

    def get(self, request):
        age = request.query_params.get("age")

        if age is not None:
            age_ranges = [int(age)]
        else:
            age_ranges = [10, 20, 30, 40, 50, 60]

        result = []

        for age_range in age_ranges:
            age_group = f"{age_range}대"
            age_ranking = []

            for category in Category.objects.all():
                category_name = category.category_name
                age_press_ranking = (
                    Press.objects.annotate(
                        age_subscriber_count=Coalesce(
                            Sum(
                                Case(
                                    When(
                                        journalist__age__age=age_range,
                                        then=F("journalist__subscriber_count")
                                        * F("journalist__age__percentage")
                                        / 100,
                                    ),
                                    default=Value(0),
                                    output_field=models.IntegerField(),
                                )
                            ),
                            Value(0),
                        )
                    )
                    .filter(category=category)
                    .order_by("-age_subscriber_count")[:5]
                )

                category_ranking = {
                    "category_name": category_name,
                    "press_ranking": [
                        {
                            "press_name": press.press_name,
                            "count": press.age_subscriber_count,
                        }
                        for press in age_press_ranking
                    ],
                }

                age_ranking.append(category_ranking)

            age_group_ranking = {"age_group": age_group, "categories": age_ranking}
            result.append(age_group_ranking)

        return Response(result)


class TotalAgeByPress(generics.RetrieveAPIView):
    serializer_class = PressAgeSerializer

    def get_queryset(self):
        press_name = self.kwargs.get("press_name").upper()
        return Age.objects.filter(journalist__press__press_name=press_name)

    def retrieve(self, request, *args, **kwargs):
        press_name = self.kwargs.get("press_name").upper()
        queryset = self.get_queryset()
        age_ranges = [10, 20, 30, 40, 50, 60]
        result = []
        result.append({"press_name": press_name})

        for age_range in age_ranges:
            age_group = f"{age_range}대"
            total_subscribers = queryset.filter(
                journalist__age__age=age_range
            ).aggregate(
                total=Sum(
                    (
                        F("journalist__subscriber_count")
                        * F("journalist__age__percentage")
                    )
                    / (100 * 6)
                )
            )[
                "total"
            ]
            result.append(
                {"age_group": age_group, "total_subscribers": total_subscribers}
            )

        return Response(result)


class MalePressRanking(generics.ListAPIView):
    queryset = Press.objects.all()
    serializer_class = PressGenderSerializer

    def get_queryset(self):
        queryset = Press.objects.annotate(
            male_subscriber_count=Sum(
                F("journalist__subscriber_count")
                * F("journalist__gender__percentage")
                / 100,
                output_field=models.IntegerField(),
                filter=models.Q(journalist__gender__gender="M"),
            )
        ).order_by("-male_subscriber_count")[:10]

        return queryset


class FemalePressRanking(generics.ListAPIView):
    queryset = Press.objects.all()
    serializer_class = PressGenderSerializer

    def get_queryset(self):
        queryset = Press.objects.annotate(
            male_subscriber_count=Sum(
                F("journalist__subscriber_count")
                * F("journalist__gender__percentage")
                / 100,
                output_field=models.IntegerField(),
                filter=models.Q(journalist__gender__gender="F"),
            )
        ).order_by("-male_subscriber_count")[:10]
        return queryset


class JournalistGenderDetail(generics.ListAPIView):
    queryset = Journalist.objects.all()
    serializer_class = GenderSerializer

    def get_queryset(self):
        journalist_id = self.kwargs.get("journalist_id")
        queryset = Gender.objects.filter(journalist_id=journalist_id)
        return queryset
