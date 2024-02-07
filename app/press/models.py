from django.db import models


class Category(models.Model):
    category_name = models.CharField(max_length=20, unique=True)


class Press(models.Model):
    press_name = models.CharField(max_length=50, unique=True)
    # join 과 같은 효과
    category = models.ForeignKey(
        Category,
        # CASCADE 옵션은 연결된 객체가 삭제될 때 이를 참조하는 모든 객체도 함께 삭제
        on_delete=models.CASCADE,
        # 연결된 모델에서 참조할 필드를 지정
        to_field="category_name",
        # 데이터베이스 테이블에서 사용될 칼럼의 이름을 지정
        db_column="category_name",
        # 만약 category에서 역으로 참조 할때 사용되는 이름
        related_name="press",
    )


class Journalist(models.Model):
    journalist_id = models.IntegerField(unique=True)
    name = models.CharField(max_length=20)
    subscriber_count = models.IntegerField(default=0)
    article_count = models.IntegerField(default=0)
    cheer_count = models.IntegerField(default=0)
    press = models.ForeignKey(
        Press,
        on_delete=models.CASCADE,
        to_field="press_name",
        db_column="press_name",
        related_name="journalist",
    )


class Gender(models.Model):
    gender = models.CharField(max_length=1)
    percentage = models.IntegerField(default=0)
    journalist = models.ForeignKey(
        Journalist,
        on_delete=models.CASCADE,
        to_field="journalist_id",
        db_column="journalist_id",
        related_name="gender",
    )


class Age(models.Model):
    age = models.IntegerField(default=0)
    percentage = models.IntegerField(default=0)
    journalist = models.ForeignKey(
        Journalist,
        on_delete=models.CASCADE,
        to_field="journalist_id",
        db_column="journalist_id",
        related_name="age",
    )


class Section(models.Model):
    section_name = models.CharField(max_length=10, unique=True)


class JournalistSection(models.Model):
    journalist = models.ForeignKey(
        Journalist,
        on_delete=models.CASCADE,
        to_field="journalist_id",
        db_column="journalist_id",
        related_name="journalistsection",
    )
    section = models.ForeignKey(
        Section,
        on_delete=models.CASCADE,
        to_field="section_name",
        db_column="section_name",
        related_name="journalistsection",
    )
    # journalist와 section 두 필드의 조합이 유일해야 한다는 것을 나타냅니다. 
    # 즉, 하나의 기자가 하나의 섹션에 여러 번 속할 수 없으며, 하나의 섹션에 여러 기자가 속할 수 없습니다.
    class Meta:
        unique_together = (("journalist", "section"),)
