from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=255, unique=True)


class Source(models.Model):
    NAME_CHOICES = (
        ("Indeed", "Indeed"),
        ("LinkedIn", "LinkedIn"),
        ("Monster", "Monster"),
    )
    name = models.CharField(max_length=255, choices=NAME_CHOICES)
    from_api = models.BooleanField()


class Position(models.Model):
    TITLE_CHOICES = (
        ("Software Engineer", "Software Engineer"),
        ("Full Stack Engineer", "Full Stack Engineer"),
        ("Front End Engineer", "Front End Engineer"),
        ("Back End Engineer", "Back End Engineer"),
    )
    title = models.CharField(max_length=255, choices=TITLE_CHOICES, unique=True)

    def search_str(self):
        return self.title.replace(" ", "+")


class Post(models.Model):
    title = models.CharField(max_length=255)
    company = models.ForeignKey("Company", to_field="name", on_delete=models.CASCADE)
    description = models.TextField()
    location = models.CharField(max_length=255, null=True)
    is_sponsored = models.BooleanField()
    date_posted = models.DateField(null=True)
    date_added_db = models.DateField(auto_now_add=True)
    source = models.ForeignKey("Source", on_delete=models.CASCADE)
    link = models.TextField()
    position = models.ForeignKey("Position", on_delete=models.SET_NULL, null=True)

    class Meta:
        unique_together = (
            "company",
            "title",
            "date_posted",
        )

    @property
    def experience(self):
        substring_list = ["intern", "internship"]
        if any(substring in self.title.lower() for substring in substring_list):
            return "Internship"
        else:
            return "Full-Time"

    @property
    def sponsored(self):
        if not self.date_posted or not self.location:
            return True
        else:
            return False
