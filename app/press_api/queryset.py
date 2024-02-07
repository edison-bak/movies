from django.db import models
from django.db.models import F, Sum

from press.models import Category, Journalist, Press, Section

# Django ORM을 사용하여 데이터베이스에서 카테고리별로 남성 구독자 수를 계산하는 쿼리를 작성하는 부분
# 그전에 다 분석할텐데 장고내에서 sql이 필요한경우가 있을까?

# 카테고리에 대해 남성 구독자 수, .... 를 계산하여 male_subscriber 필드로 어노테이션을 추가하는 쿼리를 작성
# 기존의 모델이나 테이블에 새로운 필드를 추가하는 것이 아니라, 쿼리를 실행할 때만 필요한 계산된 값을 가상의 
# 필드로 추가하는 것입니다. 이렇게 추가된 가상의 필드는 실제로 데이터베이스에 저장되지 않습니다.
category_query_set = Category.objects.annotate(
    male_subscriber=Sum(
        F("press__journalist__subscriber_count")
        * F("press__journalist__gender__percentage")
        / (100 * 6),
        filter=models.Q(press__journalist__gender__gender="M"),
    ),
    female_subscriber=Sum(
        F("press__journalist__subscriber_count")
        * F("press__journalist__gender__percentage")
        / (100 * 6),
        filter=models.Q(press__journalist__gender__gender="F"),
    ),
    teen_subscriber=Sum(
        F("press__journalist__subscriber_count")
        * F("press__journalist__age__percentage")
        / (100 * 2),
        filter=models.Q(press__journalist__age__age="10"),
    ),
    twenty_subscriber=Sum(
        F("press__journalist__subscriber_count")
        * F("press__journalist__age__percentage")
        / (100 * 2),
        filter=models.Q(press__journalist__age__age="20"),
    ),
    thirty_subscriber=Sum(
        F("press__journalist__subscriber_count")
        * F("press__journalist__age__percentage")
        / (100 * 2),
        filter=models.Q(press__journalist__age__age="30"),
    ),
    forty_subscriber=Sum(
        F("press__journalist__subscriber_count")
        * F("press__journalist__age__percentage")
        / (100 * 2),
        filter=models.Q(press__journalist__age__age="40"),
    ),
    fifty_subscriber=Sum(
        F("press__journalist__subscriber_count")
        * F("press__journalist__age__percentage")
        / (100 * 2),
        filter=models.Q(press__journalist__age__age="50"),
    ),
    sixty_subscriber=Sum(
        F("press__journalist__subscriber_count")
        * F("press__journalist__age__percentage")
        / (100 * 2),
        filter=models.Q(press__journalist__age__age="60"),
    ),
    subscriber_count=Sum("press__journalist__subscriber_count") / 12,
    cheer_count=Sum("press__journalist__cheer_count") / 12,
)


press_query_set = Press.objects.annotate(
    male_subscriber=Sum(
        F("journalist__subscriber_count")
        * F("journalist__gender__percentage")
        / (100 * 6),
        filter=models.Q(journalist__gender__gender="M"),
    ),
    female_subscriber=Sum(
        F("journalist__subscriber_count")
        * F("journalist__gender__percentage")
        / (100 * 6),
        filter=models.Q(journalist__gender__gender="F"),
    ),
    teen_subscriber=Sum(
        F("journalist__subscriber_count")
        * F("journalist__age__percentage")
        / (100 * 2),
        filter=models.Q(journalist__age__age="10"),
    ),
    twenty_subscriber=Sum(
        F("journalist__subscriber_count")
        * F("journalist__age__percentage")
        / (100 * 2),
        filter=models.Q(journalist__age__age="20"),
    ),
    thirty_subscriber=Sum(
        F("journalist__subscriber_count")
        * F("journalist__age__percentage")
        / (100 * 2),
        filter=models.Q(journalist__age__age="30"),
    ),
    forty_subscriber=Sum(
        F("journalist__subscriber_count")
        * F("journalist__age__percentage")
        / (100 * 2),
        filter=models.Q(journalist__age__age="40"),
    ),
    fifty_subscriber=Sum(
        F("journalist__subscriber_count")
        * F("journalist__age__percentage")
        / (100 * 2),
        filter=models.Q(journalist__age__age="50"),
    ),
    sixty_subscriber=Sum(
        F("journalist__subscriber_count")
        * F("journalist__age__percentage")
        / (100 * 2),
        filter=models.Q(journalist__age__age="60"),
    ),
    subscriber_count=Sum("journalist__subscriber_count") / 12,
    cheer_count=Sum("journalist__cheer_count") / 12,
)

secion_query_set = Section.objects.annotate(
    male_subscriber=Sum(
        F("journalistsection__journalist__subscriber_count")
        * F("journalistsection__journalist__gender__percentage")
        / (100 * 6),
        filter=models.Q(journalistsection__journalist__gender__gender="M"),
    ),
    female_subscriber=Sum(
        F("journalistsection__journalist__subscriber_count")
        * F("journalistsection__journalist__gender__percentage")
        / (100 * 6),
        filter=models.Q(journalistsection__journalist__gender__gender="F"),
    ),
    teen_subscriber=Sum(
        F("journalistsection__journalist__subscriber_count")
        * F("journalistsection__journalist__age__percentage")
        / (100 * 2),
        filter=models.Q(journalistsection__journalist__age__age="10"),
    ),
    twenty_subscriber=Sum(
        F("journalistsection__journalist__subscriber_count")
        * F("journalistsection__journalist__age__percentage")
        / (100 * 2),
        filter=models.Q(journalistsection__journalist__age__age="20"),
    ),
    thirty_subscriber=Sum(
        F("journalistsection__journalist__subscriber_count")
        * F("journalistsection__journalist__age__percentage")
        / (100 * 2),
        filter=models.Q(journalistsection__journalist__age__age="30"),
    ),
    forty_subscriber=Sum(
        F("journalistsection__journalist__subscriber_count")
        * F("journalistsection__journalist__age__percentage")
        / (100 * 2),
        filter=models.Q(journalistsection__journalist__age__age="40"),
    ),
    fifty_subscriber=Sum(
        F("journalistsection__journalist__subscriber_count")
        * F("journalistsection__journalist__age__percentage")
        / (100 * 2),
        filter=models.Q(journalistsection__journalist__age__age="50"),
    ),
    sixty_subscriber=Sum(
        F("journalistsection__journalist__subscriber_count")
        * F("journalistsection__journalist__age__percentage")
        / (100 * 2),
        filter=models.Q(journalistsection__journalist__age__age="60"),
    ),
    subscriber_count=Sum("journalistsection__journalist__subscriber_count") / 12,
    cheer_count=Sum("journalistsection__journalist__cheer_count") / 12,
)


journalist_query_set = Journalist.objects.annotate(
    male_subscriber=Sum(
        F("subscriber_count") * F("gender__percentage") / (100 * 6),
        filter=models.Q(gender__gender="M"),
    ),
    female_subscriber=Sum(
        F("subscriber_count") * F("gender__percentage") / (100 * 6),
        filter=models.Q(gender__gender="F"),
    ),
    teen_subscriber=Sum(
        F("subscriber_count") * F("age__percentage") / (100 * 2),
        filter=models.Q(age__age="10"),
    ),
    twenty_subscriber=Sum(
        F("subscriber_count") * F("age__percentage") / (100 * 2),
        filter=models.Q(age__age="20"),
    ),
    thirty_subscriber=Sum(
        F("subscriber_count") * F("age__percentage") / (100 * 2),
        filter=models.Q(age__age="30"),
    ),
    forty_subscriber=Sum(
        F("subscriber_count") * F("age__percentage") / (100 * 2),
        filter=models.Q(age__age="40"),
    ),
    fifty_subscriber=Sum(
        F("subscriber_count") * F("age__percentage") / (100 * 2),
        filter=models.Q(age__age="50"),
    ),
    sixty_subscriber=Sum(
        F("subscriber_count") * F("age__percentage") / (100 * 2),
        filter=models.Q(age__age="60"),
    ),
)
