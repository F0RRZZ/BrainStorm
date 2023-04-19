import django.core.exceptions
import django.test

import tags.models


class TagsTests(django.test.TestCase):
    def tearDown(self):
        tags.models.Tag.objects.all().delete()

    def test_create(self):
        tags_count = tags.models.Tag.objects.count()
        tag = tags.models.Tag(
            name='tag',
            description='tag',
            slug='tag',
        )
        tag.full_clean()
        tag.save()
        self.assertEqual(tags_count + 1, tags.models.Tag.objects.count())

    def test_name_repeat_validator(self):
        first_tag = tags.models.Tag(
            name='tag1',
            description='tag',
            slug='tag1',
        )
        first_tag.full_clean()
        first_tag.save()
        second_tag = tags.models.Tag(
            name='tag2',
            description='tag',
            slug='tag2',
        )
        second_tag.full_clean()
        second_tag.save()

    def test_negative_name_repeat_validator(self):
        with self.assertRaises(django.core.exceptions.ValidationError):
            first_tag = tags.models.Tag(
                name='tag',
                description='tag',
                slug='tag',
            )
            first_tag.full_clean()
            first_tag.save()
            second_tag = tags.models.Tag(
                name='tag',
                description='tag',
                slug='tag',
            )
            second_tag.full_clean()
            second_tag.save()
